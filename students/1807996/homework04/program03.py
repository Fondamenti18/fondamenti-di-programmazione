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

def tagnodo(alb,selettore):
    insieme=set()
    if selettore in alb.tag:
        insieme=insieme.union(set([alb]))
    for figlio in alb.content:
        if type(figlio)!=str:
            insieme=insieme.union(set(tagnodo(figlio,selettore)))
    return insieme

def attrid(alb):
    insieme=set()
    if alb.attr!=[] and 'id' in alb.attr.keys():
        attributo=[alb.attr['id']]
        insieme=insieme.union(set(attributo))
    for nodo in alb.content:
        if type(nodo)!=str:
            insieme=insieme.union(set(list(attrid(nodo))))
    return insieme
    
def attrclass(alb):
    insieme=set()
    if alb.attr!=[] and 'class' in alb.attr.keys():
        attributo=[alb.attr['class']]
        insieme=insieme.union(set(attributo))
    for nodo in alb.content:
        if type(nodo)!=str:
            insieme=insieme.union(set(list(attrclass(nodo))))
    return insieme

def controllo(selettore):
    selettore=selettore[2:len(selettore)-1]
    chiave=''
    for carattere in selettore:
        if carattere!='=':
            chiave+=carattere
        else: break
    controllo=selettore[len(chiave)+2:len(selettore)-1]
    return chiave,controllo

def attrvalues(alb,selettore,listval):
    chiaves=controllo(selettore)[0]
    valores=controllo(selettore)[1]
    if chiaves in alb.attr.keys():       
        if valores in alb.attr[chiaves]:
            listval+=[valores]
    return trovaval(alb,selettore,listval)
            
def  trovaval(alb,selettore,listval):
    for nodo in alb.content:
        if type(nodo)!=str:
            attrvalues(nodo,selettore,listval)
    return listval

def tagsempl(alb,selettore):
    alblist=[alb]
    selettori=selettore.split()
    lun=len(selettori)
    esito=[]
    cont=0
    complist(lun,alblist,esito,selettori)        
    return calcont(alblist,selettori,cont)

def calcont(alblist,selettori,cont):
    for el in alblist:
        if selettori[-1] in el.tag:
            cont+=1
    return cont

def complist(lun,alblist,esito,selettori):
    for x in range(lun):
        for nodo in alblist:
            esito+=list(tagnodo(nodo,selettori[x]))
            alblist.remove(nodo)
        alblist+=esito
        
def ctag(alb,selettore):
    selettori=selettore.split(' > ')
    alblist1=list(tagnodo(alb,selettori[0]))
    cont=0
    for el in alblist1:
        cont+=incont(selettori,el,cont)                   
    return cont

def incont(selettori,el,cont):
    for figlio in el.content:
        if selettori[1] in figlio.tag:
            cont+=1
    return cont
    
def attr(selettore,alb):
    selettore=selettore[1:len(selettore)]
    alblist=attrid(alb)
    cont=0
    for el in alblist:
        if selettore in el:
            cont+=1
    return cont

def clas(selettore,alb):
    selettore=selettore[1:len(selettore)]
    alblist=attrclass(alb)
    cont=0
    for el in alblist:
        if selettore in el:
            cont+=1
    return cont

def conta_nodi(fileIn, selettore):
    alb=fparse(fileIn)    
    if selettore[0] not in '.#@' and '>' not in selettore:
        return tagsempl(alb,selettore)
    
    if '>' in selettore:
        return ctag(alb,selettore)
    
    if selettore[0] == '#':
        return attr(selettore,alb)
    
    if selettore[0] == '.':
        return clas(selettore,alb)
    
    if selettore[0] == '@':
        alblist=[]
        alblist=attrvalues(alb,selettore,alblist)
        return len(alblist)
    
def elimina_nodi(fileIn, selettore,fileout):
    pag=fparse(fileIn)
    if selettore[0] not in '.#@' and '>' not in selettore:
        lista=[pag]
        selettori=selettore.split()
        lun=len(selettori)
        esito=[]
        for x in range(lun):
            for nodo in lista:
                esito+=list(tagnodo(nodo,selettori[x]))
                lista.remove(nodo)
            lista+=esito
        for el in lista:
            if selettori[-1]== el.tag:
                remove_by_tag(pag,selettore[-1])
    stringa=pag.to_string().split('\n')
    doc=open (fileout,'w', encoding='utf-8')
    for st in stringa:
        doc.writeline(st)

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    #Inserite qui il vostro codice
    pag=fparse(fileIn)
    if selettore[0] not in '.#@' and '>' not in selettore:
        lista=[pag]
        selettori=selettore.split()
        lun=len(selettori)
        esito=[]
        for x in range(lun):
            for nodo in lista:
                esito+=list(tagnodo(nodo,selettori[x]))
                lista.remove(nodo)
            lista+=esito
        for el in lista:
            if selettori[-1]== el.tag:
                modalb(pag,selettore[-1],chiave,valore)
        return pag.to_string()

def modalb(node,tag,chiave,valore):
    if node.istext(): 
        return 
    for child in node.content: 
        modalb( child,tag,chiave,valore) 
    newcont = [] 
    for child in node.content:
        if child.tag == tag: 
            child.attr[chiave]=valore
            newcont += child.content 
        else: newcont  += [child] 
    node.content = newcont

def trova_attr_nodo(nodo):
    lista=[]
    lista.append(nodo.attr)
    for figlio in nodo.content:
        if type(figlio)!=str:
            lista.append(trova_attr_nodo(figlio))
    return lista 
    
def remove_by_tag(node,tag): 
    if node.istext(): 
        return 
    for child in node.content: 
        remove_by_tag( child,tag) 
    newcont = [] 
    for child in node.content:
        if child.tag == tag: 
            if not child.istext(): 
                newcont += child.content 
        else: newcont  += [child] 
    node.content = newcont
