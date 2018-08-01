'''
Un documento HTML puo' essere rappresentato sotto forma di albero, come visto a lezione, che si chiama DOM (Document Object Model).

Un qualsiasi nodo di questo albero puo' essere individuato sulla base delle proprie caratteristiche:
    - tag                       un tag del tipo indicato
    - .classe                   una delle parole presenti nel valore dell'attributo "class"
    - #id                       il valore dell'attributo "id"
    - @[attributo="valore"]     valore di un attributo generico
ed in base alla sua relazione con i tag che lo contengono:
    - avo discendente           il tag 'avo' contiene un tag 'discendente' a qualsiasi profondita'
    - padre > figlio            il tag 'padre' contiene il tag 'figlio' nel livello immediatamente sotto

Un selettore CSS e' una successione di selettori di tag separati da spazio che serve ad individuare uno o piu' nodi all'interno del DOM.
Esempio:
    div .class1 > #main_window
        seleziona un qualsiasi tag che ha                                       id="main_window"
        e' il figlio di un tag che ha                                            class="... class1 ..."
        e si trova all'interno (a qualsiasi livello di distanza) di un tag      div
Esempio2:
    p  table > tr > td > a
	seleziona un link (<a ...> </a>)
	figlio di una casella (<td> ... </td>)
	figlia di una riga (<tr> ... </tr>)
	figlia di una tabella (<table> ... </table>)
	contenuta a qualsiasi livello in un paragrafo (<p> .... </p>)

NOTA: questa definizione del CSS e' una versione ridottissima che non segue lo standard completo. 
In particolare, non e' possibile usare piu' relazioni '>' consecutive o costruire selettori alternativi (in OR) e selettori in AND.

Le modifiche da attuare su un DOM possono essere di 3 tipi:
    - conteggio dei nodi che soddisfano il selettore CSS
    - eliminazione di tutti i tag individuati da un selettore CSS
    - modifica degli attributi di tutti i tag individuati da un selettore CSS

Realizzate le funzioni che esplorano e modificano l'albero:
    conta_nodi(       fileIn, selettore)				
    elimina_nodi(       fileIn, selettore, fileOut)				
    cambia_attributo(	fileIn, selettore, chiave, valore, fileOut)

ATTENZIONE: nei test verra' utilizzato un timout globale di 1*N secondi (se il grader fa N test)
'''

from  my_html import HTMLNode, fparse

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    doc=fparse(fileIn)
    l=[]
    sel=[]
    sel1=selettore.split()
    for i in range(0,len(sel1)):
        sel+=[sel1[i]]
        if i+1<=len(sel1)-1 and  sel1[i]!=">" and sel1[i+1]!=">":
            sel+=[" "]
        
    l=trova(doc,sel[0],l)
    if len(sel)==1:
        return len(l)
    somma=0
    for i in l:
        la=[]
        x,l,la=conta(i,sel,la)
        for i in la:
            if i.tag==sel[-1]:
                somma+=1
    return somma
        
def conta(nodo,sel,la):
    l=[]
    if nodo.tag=="_text_" or len(sel)==1:
        return nodo,l,la
    li=[y.tag for y in nodo.content]
    if sel[1]!=">":
        l=trova(nodo,sel[2],l)
        la=l[:]
        for i in l:
            nodo,l,la=conta(i,sel[2:],la)
    elif sel[2] in li:
        l=[x for x in nodo.content if x.tag==sel[2]]
        la=[x for x in nodo.content if x.tag==sel[2]]
        for i in l:
            nodo,l,la=conta(i,sel[2:],la)
    return nodo,l,la

def trova(nodo,sel,l):
    if nodo.tag=="_text_":
        return l
    if sel[0]=="." and "class" in nodo.attr:
        li=nodo.attr["class"].split()
        if sel[1:] in li:
            l+=[nodo]
    elif sel[0]=="#" and "id" in nodo.attr and nodo.attr["id"]==sel[1:]:
        l+=[nodo]
    elif sel[0]=="@":
        s=sel.split('=')
        if s[0][2:] in nodo.attr and nodo.attr[s[0][2:]]==s[1][1:-2]:
            l+=[nodo]
    elif nodo.tag==sel:
        l+=[nodo]
    for i in nodo.content:
        l=trova(i,sel,l)
    return l


def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    doc=fparse(fileIn)
    l=[]
    sel=[]
    y=[]
    z=[]
    h=[]
    sel1=selettore.split()
    for i in range(0,len(sel1)):
        sel+=[sel1[i]]
        if i+1<=len(sel1)-1 and  sel1[i]!=">" and sel1[i+1]!=">":
            sel+=[" "]
        
    l=trova(doc,sel[0],l)
    a=l[:]
    if len(sel)==1:
        return len(l)
    for i in l:
        la=[]
        x,l,la=conta(i,sel,la)
        if la!=[]:
            y+=la
            h+=[i]
    lista=[]
    lst=[]
    for i in y:
        lst,x=trova_sottoalbero(i,lst)
    lista+=lst
    lista+=y
    z,x=cancella_root(doc,y,z)
    for i in z:
        for j in y:
            i.content.remove(j)
    for i in lista:
        i.content=[]
        del i
    s=doc.to_string()
    f=open(fileOut,"w",encoding="utf8")
    f.write(s)
    f.close()

def trova_sottoalbero(nodo,lista):
    if nodo.tag=="_text_":
        return lista,nodo
    lista+=[nodo]
    for i in nodo.content:
        trova_sottoalbero(i,lista)
    return lista,nodo

def cancella_root(nodo,daRicercare,h):
    if nodo.tag=="_text_":
        return h,nodo
    for i in nodo.content:
        if i in daRicercare:
            h+=[nodo]
    for i in nodo.content:
        h,nodo=cancella_root(i,daRicercare,h)
    return h,nodo

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    doc=fparse(fileIn)
    l=[]
    sel=[]
    y=[]
    sel1=selettore.split()
    for i in range(0,len(sel1)):
        sel+=[sel1[i]]
        if i+1<=len(sel1)-1 and  sel1[i]!=">" and sel1[i+1]!=">":
            sel+=[" "]    
    l=trova(doc,sel[0],l)
    if len(sel)!=1:
        for i in l:
            la=[]
            x,l,la=conta(i,sel,la)
            y+=la
    else:
        y=l
    for i in y:
        i.attr[chiave]=valore
    s=doc.to_string()
    f=open(fileOut,"w",encoding="utf8")
    f.write(s)
    f.close()