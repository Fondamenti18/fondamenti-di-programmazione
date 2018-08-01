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

#def conta_nodi(fileIn, selettore):
 #   '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    #Inserite qui il vostro codice
def co_tagD(nodo, selettore ):
    #if selettore[0] == '#':
    li=[]
    if nodo.tag == selettore:
        li += [nodo]
    if nodo.tag!='_text_':
        for figlio in nodo.content:
            li += co_tagD(figlio, selettore)
    return li
def co_idD(nodo, selettore):
    li = []
    if 'id' in nodo.attr.keys():
        if nodo.attr['id'] == selettore[1:]:
            li += [nodo]#tot.update(nodo.attr)
    if nodo.tag!='_text_':
        for figlio in nodo.content:
            li += ( co_idD(figlio, selettore))
    return li
def co_classD(nodo, selettore):
    li = []
    if 'class' in nodo.attr.keys():
        if selettore[1:] in (nodo.attr['class']).split():
            li += [nodo]
    if nodo.tag!='_text_':
        for figlio in nodo.content:
            li += ( co_classD(figlio, selettore))
    return li
def co_genD(nodo, selettore):
    li = []
    pri = selettore[2:(selettore.index('='))]
    sec = selettore[(selettore.index('='))+2:-2]
    if pri in nodo.attr.keys():
        if sec in (nodo.attr[pri]).split():
            li += [nodo]
    if nodo.tag!='_text_':
        for figlio in nodo.content:
            li += ( co_genD(figlio, selettore))
    return li 
def co_tag(nodo, selettore ):
    #if selettore[0] == '#':
    li=[]
    if nodo.tag!='_text_':
        for figlio in nodo.content:
           if figlio.tag == selettore:
               li += [figlio]
    return li
def co_id(nodo, selettore):
    li = []
    for figlio in nodo.content:
         if figlio.tag!='_text_':
             if 'id' in figlio.attr.keys():
                 if figlio.attr['id'] == selettore[1:]:
                     li += [figlio]#tot.update(nodo.attr)
    return li
def co_class(nodo, selettore):
    li = []
    for figlio in nodo.content:
         if figlio.tag!='_text_':
             if 'class' in figlio.attr.keys():
                 if selettore[1:] in (figlio.attr['class']).split():
                     li += [figlio]
    return li
def co_gen(nodo, selettore):
    li = []
    pri = selettore[2:(selettore.index('='))]
    sec = selettore[(selettore.index('='))+2:-2]
    for figlio in nodo.content:
        if figlio.tag!='_text_':
            if pri in figlio.attr.keys():
                if sec in (figlio.attr[pri]).split():
                    li += [figlio]
    return li 


def quasiD(nodo, selettore):
    #nodo = fparse(fileIn)
    if selettore[0] == '#':
       a = co_idD(nodo, selettore)
    elif selettore[0] =='.':
        a = co_classD(nodo, selettore)
    elif selettore[0] == '@':
        a = co_genD(nodo, selettore)
    else:
        a = co_tagD(nodo, selettore)
    return a
def quasi(nodo, selettore):
    #nodo = fparse(fileIn)
    if selettore[0] == '#':
       a = co_id(nodo, selettore)
    elif selettore[0] =='.':
        a = co_class(nodo, selettore)
    elif selettore[0] == '@':
        a = co_gen(nodo, selettore)
    else:
        a = co_tag(nodo, selettore)
    return a
def conta_nodi(fileIn, selettore):
    a = []
    nodo = fparse(fileIn)
    selist = selettore.split(' ')
    #a = quasi(nodo, selist[0])
    try:
        if selist[1] != '>':
            for c in quasiD(nodo, selist[0]):
                a += quasiD(c, selist[1])
    except IndexError:
        a = quasiD(nodo, selist[0])
    try:
        if selist[1] == '>':
            for c in quasiD(nodo, selist[0]):
                a += quasi(c, selist[2])
    except IndexError:
        a = quasiD(nodo, selist[0])
    return len(a)

fileIn    = 'page1-3.html'
selettore = 'p > a'
print(conta_nodi(fileIn, selettore))



def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice

