'''
Un documento HTML può essere rappresentato sotto forma di albero, come visto a lezione, che si chiama DOM (Document Object Model).

Un qualsiasi nodo di questo albero può essere individuato sulla base delle proprie caratteristiche:
    - tag                       un tag del tipo indicato
    - .classe                   una delle parole presenti nel valore dell'attributo "class"
    - #id                       il valore dell'attributo "id"
    - @[attributo="valore"]     valore di un attributo generico
ed in base alla sua relazione con i tag che lo contengono:
    - avo discendente           il tag 'avo' contiene un tag 'discendente' a qualsiasi profondità
    - padre > figlio            il tag 'padre' contiene il tag 'figlio' nel livello immediatamente sotto

Un selettore CSS è una successione di selettori di tag separati da spazio che serve ad individuare uno o più nodi all'interno del DOM.
Esempio:
    div .class1 > #main_window
        seleziona un qualsiasi tag che ha                                       id="main_window"
        è il figlio di un tag che ha                                            class="... class1 ..."
        e si trova all'interno (a qualsiasi livello di distanza) di un tag      div
Esempio2:
    p  table > tr > td > a
	seleziona un link (<a ...> </a>)
	figlio di una casella (<td> ... </td>)
	figlia di una riga (<tr> ... </tr>)
	figlia di una tabella (<table> ... </table>)
	contenuta a qualsiasi livello in un paragrafo (<p> .... </p>)

NOTA: questa definizione del CSS è una versione ridottissima che non segue lo standard completo. 
In particolare, non è possibile usare più relazioni '>' consecutive o costruire selettori alternativi (in OR) e selettori in AND.

Le modifiche da attuare su un DOM possono essere di 3 tipi:
    - conteggio dei nodi che soddisfano il selettore CSS
    - eliminazione di tutti i tag individuati da un selettore CSS
    - modifica degli attributi di tutti i tag individuati da un selettore CSS

Realizzate le funzioni che esplorano e modificano l'albero:
    conta_nodi(       fileIn, selettore)				
    elimina_nodi(       fileIn, selettore, fileOut)				
    cambia_attributo(	fileIn, selettore, chiave, valore, fileOut)

ATTENZIONE: nei test verrà utilizzato un timout globale di 1*N secondi (se il grader fa N test)
'''

from  my_html import HTMLNode, fparse

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    doc=fparse(fileIn)
    cont=0
    
    if selettore[0]=="#":
        cont=conta_id(doc,selettore)
    elif selettore[0]==".":
        cont=conta_classe(doc,selettore[1:])
    elif selettore[0]=="@":
        cont=conta_attributo(doc,selettore[2:selettore.find("=")],selettore[selettore.find("=")+2:selettore.find("]")-1])
    elif ">" in selettore:
        cont=conta_relazione(doc,selettore[:selettore.find(">")].strip(),selettore[selettore.find(">")+1:].strip())
    elif " " in selettore:
        if trova_avo(doc,selettore[:selettore.find(" ")].strip())>=1:
            cont=conta_avo(doc,selettore[selettore.find(" ")+1:].strip())
    else:
        cont=conta_tag(doc,selettore)
    
    return cont

def conta_tag(nodo,select):
    cont=0
    if nodo.tag==select:
        cont+=1
    if not nodo.istext():
        for figlio in nodo.content:
            cont+=conta_tag(figlio,select)
    return cont
    
def conta_id(nodo,select):
    cont=0
    if "id" in nodo.attr:
        if "#"+nodo.attr["id"]==select:
            cont+=1
    if not nodo.istext():
        for figlio in nodo.content:
            cont+=conta_id(figlio,select)
    return cont

def conta_classe(nodo,select):
    cont=0
    if "class" in nodo.attr:
        if select in nodo.attr["class"]:
            cont+=1
    if not nodo.istext():
        for figlio in nodo.content:
            cont+=conta_classe(figlio,select)
    return cont

def conta_attributo(nodo,attributo,valore):
    cont=0
    if attributo in nodo.attr:
        if nodo.attr[attributo]==valore:
            cont+=1
    if not nodo.istext():
        for figlio in nodo.content:
            cont+=conta_attributo(figlio,attributo,valore)
    return cont

def conta_relazione(nodo,padre,figlio):
    cont=0
    if nodo.tag==padre:
        for child in nodo.content:
            if child.tag==figlio:
                cont+=1
    if not nodo.istext():
        for child in nodo.content:
            cont+=conta_relazione(child,padre,figlio)
    return cont

def trova_avo(nodo,avo):
    cont=0
    if nodo.tag==avo:
        cont+=1
    if not nodo.istext():
        for figlio in nodo.content:
            cont+=trova_avo(figlio,avo)
    return cont

def conta_avo(nodo,desc):
    cont=0
    if nodo.tag==desc:
        cont+=1
    if not nodo.istext():
        for figlio in nodo.content:
            cont+=conta_avo(figlio,desc)
    return cont

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    doc=fparse(fileIn)
    
    if trova_avo(doc,selettore[:selettore.find(" ")].strip())>=1:
        elimina_avo(doc,selettore[selettore.find(" ")+1:].strip())
        
    f=open(fileOut,'w')
    f.write(doc.to_string())
    f.close()
    
def elimina_avo(nodo,desc):
    if nodo.istext(): return
    for figlio in nodo.content:
        elimina_avo(figlio,desc)
    newcontent=[]
    for figlio in nodo.content:
        if figlio.tag==desc:
            if not figlio.istext():
                newcontent+=figlio.content
        else:
            newcontent+=[figlio]
    nodo.content=newcontent

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    doc=fparse("page1-3.html")
    
    if trova_avo(doc,selettore[:selettore.find(" ")].strip())>=1:
        cambia_avo(doc,selettore[selettore.find(" ")+1:].strip(),chiave,valore)
        
    f=open(fileOut,'w')
    f.write(doc.to_string())
    f.close()

def cambia_avo(nodo,desc,chiave,valore):
    if nodo.tag==desc:
        nodo.attr[chiave]=valore
    if not nodo.istext():
        for figlio in nodo.content:
            cambia_avo(figlio,desc,chiave,valore)
            