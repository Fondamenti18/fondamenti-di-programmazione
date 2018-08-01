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

def trova_selettore(radice, selettore, ris, soloPrimiFigli = False):
    if radice.tag != '_text_':
        
        if selettore[0] == '.':
            nome_classe = selettore[1:]
            if 'class' in radice.attr:
                if nome_classe in radice.attr['class'].split():
                    ris.add(radice)

                    
        elif selettore[0] == '#':
            
            nome_id = selettore[1:]
            if 'id' in radice.attr:
                if radice.attr['id'] == nome_id:
                    ris.add(radice)

            
        elif selettore[0] == '@':
            split = selettore.split('=')
            attributo = split[0][2:] 
            valore = split[1][1:-2]
            if attributo in radice.attr:
                if radice.attr[attributo] == valore:
                    ris.add(radice)
                    
        split = selettore.split()
        if len(split) == 1: #tag da solo
            if radice.tag == selettore:
                ris.add(radice)
                 
        elif len(split) == 2: #avo discendente
            split = selettore.split()
            nodiPadre = set()
            nodiPadre = trova_selettore(radice, split[0],nodiPadre)

            for nodo in nodiPadre:
                trova_selettore(nodo, split[1], ris)

                    
        elif len(split) >= 3: #padre[0] >[1] figlio[2] > ....
            discendente = selettore.split('>')
            nodiPadre = set()
            nodiPadre = trova_selettore(radice,discendente[0].strip(),nodiPadre)#salva i possibili padri che rispettano il selettore
            if len(discendente) == 2: #se si tratta del caso base padre > figlio
                for nodo in nodiPadre:
                    for figlio in nodo.content:
                        trova_selettore(figlio, discendente[1].strip(), ris, True)
            else:            
                for nodo in nodiPadre:
                    for figlio in nodo.content:
                        trova_selettore(nodo, selettore[selettore.find('>')+2:], ris)
                        
                
        if not soloPrimiFigli:
            for figlio in radice.content:
                trova_selettore(figlio, selettore, ris)
            
    return ris


def elimina_nodo(radice, nodo):
    if radice.tag == '_text_': return
    for figlio in radice.content:
        if figlio == nodo: #Se il nodo da eliminare è il figlio
            elimina_figli(figlio)
            radice.content.remove(figlio)
        else:
            elimina_nodo(figlio, nodo)
            
def elimina_figli(nodo):
    if nodo.tag == '_text_': return
    for figlio in nodo.content:
        elimina_figli(figlio)
    del(figlio)
#--------------------------

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    #Inserite qui il vostro codice
    radice = fparse(fileIn)
    ris = set()
    ris = trova_selettore(radice, selettore, ris)
    return len(ris)

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice
    radice = fparse(fileIn)
    ris = set()
    ris = trova_selettore(radice, selettore, ris)
    for nodo in ris:
        elimina_nodo(radice, nodo)
    with open(fileOut,'w',encoding='utf-8') as f:
        f.write(radice.to_string())
        
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
    radice = fparse(fileIn)
    ris = set()
    ris = trova_selettore(radice, selettore, ris)
    for nodo in ris:
        nodo.attr[chiave] = valore

    with open(fileOut,'w',encoding='utf-8') as f:
        f.write(radice.to_string())

