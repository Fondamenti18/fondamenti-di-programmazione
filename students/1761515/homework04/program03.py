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
    #Inserite qui il vostro codice
    html = fparse(fileIn)
    l=[]
    lista = ["#","@","."]
    if selettore.startswith(lista[0]):
        return len(searchId(html,selettore,l))
    
    elif selettore.startswith(lista[1]):
        indice = selettore.index("=")
        chiave = selettore[2:indice]
        valore = selettore[indice+2: len(selettore)-2]
        return len(searchGenAttr(html,chiave,valore,l))
    
    elif selettore.startswith(lista[2]):
        return len(searchClass(html,selettore,l))
    
    elif ">" in selettore:
        tags = selettore.split(" > ")
        return len(padreFiglio(html,tags,l))
    
    elif " " in selettore:
        l2 = []
        c = 0
        tags = selettore.split(" ")
        nodi = searchNodo(html,tags[0],l)
        for x in nodi:
            l2 = avoDiscendente(x,tags,l2)
            c += len(l2)
        return c
    
    elif selettore[0] not in lista or ">" not in selettore or " " not in selettore:
        return len(searchTags(html,selettore,l))
    
        
def searchTags(html,selettore,l):
    if html.tag == selettore:
        l += [html.tag]
    for x in html.content:
        if not x.istext():
            searchTags(x,selettore,l)
    return l

            
def searchClass(html,selettore,l):
    ID = selettore[1:]
    d = html.attr
    for k in d.keys():
        if k == ID:
            l += ['ok']
    for x in html.content:
        if not x.istext():
            searchClass(x,selettore,l)
    return l

def searchId(html,selettore,l):
    ID = 'id'
    d = html.attr
    if len(d) > 0 and ID in d.keys():
        if d.get(ID) == selettore[1:]:
            l += ['ok']
    for x in html.content:
        if not x.istext():
            searchId(x,selettore,l)
    return l

def searchGenAttr(html,chiave,valore,l):
    d = html.attr
    for k,v in d.items():
        if k == chiave and v == valore:
            l+=['ok']
    for x in html.content:
        if not x.istext():
            searchGenAttr(x,chiave,valore,l)
    return l

def padreFiglio(html,tags,l):
    if html.tag == tags[0]:
        for x in html.content:
            if x.tag == tags[1]:
                l += ['ok']
    for x in html.content:
        if not x.istext():
            padreFiglio(x,tags,l)
    return l
    
def avoDiscendente(html,tags,l):
    if html.tag == tags[1]:
        l += ['ok']
    for x in html.content:
        if not x.istext():
            avoDiscendente(x,tags,l)
    return l

def searchNodo(html,nodo,l):
    if html.tag == nodo:
        l += [html]
    for x in html.content:
        if not x.istext():
            searchNodo(x,nodo,l)
    return l


def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
