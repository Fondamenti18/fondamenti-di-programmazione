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
from sys import setrecursionlimit

def restituisci( struttura, fileOut):
    with open(fileOut, mode='w') as f:
        f.write(struttura.to_string())
    return

def individuaSelettore(selettore):

    tag, classe, ide, valore, attributo=  '', '', '', '', ''

    if '.' in selettore:
        classe= selettore[1:]
    elif '#' in selettore:
        ide= selettore[1:]
    elif '@' in selettore:
        attributo, valore= (selettore[1:].strip('[]')).split('=')
        valore= valore.strip('''"''')
    else: tag= selettore
    
    return tag, classe, ide, valore, attributo

def isClasse(nodo, classe):
    if classe=='':
        return True
    try:
        return  classe in nodo.attr['class']
    except KeyError:
        return False
    
def isId(nodo, ide):
    if ide=='':
        return True
    try:
        return ide in nodo.attr['id'] 
    except KeyError:
        return False

def isTag(nodo, tag):
    return tag=='' or nodo.tag== tag

def isAttributo(nodo, attributo, valore):
    if attributo=='':
        return True
    try:
        return nodo.attr[attributo]== valore
    except KeyError:
        return False

def contatore (nodo, selettore, controllo=True):

        risultato= 0
        
        if selettore[0] == '>':
            return contatore (nodo, selettore[1:], False)
        
        tag, classe, ide, valore, attributo= individuaSelettore(selettore[0])

        if isClasse(nodo, classe) and isId(nodo, ide) and isTag(nodo, tag) and isAttributo(nodo, attributo, valore):
            if len(selettore)== 1:
                return 1
            else: selettore= selettore[1:]

        if controllo and not nodo.istext():
            for nuovoNodo in nodo.content:
                risultato+= contatore (nuovoNodo, selettore)

        return risultato                

def eliminatore (nodo, selettore, nodoPadre='', controllo=True):
    
        if selettore[0] == '>':
            return eliminatore (nodo, selettore[1:], nodoPadre, False)
        
        tag, classe, ide, valore, attributo= individuaSelettore(selettore[0])

        if isClasse(nodo, classe) and isId(nodo, ide) and isTag(nodo, tag) and isAttributo(nodo, attributo, valore):
            if len(selettore)== 1:
                while nodo in nodoPadre.content: 
                    nodoPadre.content.remove(nodo)
                return 
            else: selettore= selettore[1:]

        if controllo and not nodo.istext():
            for nuovoNodo in nodo.content:
                eliminatore (nuovoNodo, selettore, nodo)

        return 

def modificatore (nodo, selettore, chiave, valoree, controllo=True):
        
        if selettore[0] == '>':
            return eliminatore (nodo, selettore[1:], chiave, valoree, False)
        
        tag, classe, ide, valore, attributo= individuaSelettore(selettore[0])

        if isClasse(nodo, classe) and isId(nodo, ide) and isTag(nodo, tag) and isAttributo(nodo, attributo, valore):
            if len(selettore)== 1:
                nodo.attr[chiave]= valoree
                return 
            else: selettore= selettore[1:]

        if controllo and not nodo.istext():
            for nuovoNodo in nodo.content:
                modificatore (nuovoNodo, selettore, chiave, valoree)

        return 
    
def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    #setrecursionlimit(100000000)
    return contatore(fparse(fileIn), selettore.split())
    
def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    struttura= fparse(fileIn)
    eliminatore(struttura, selettore.split())
    restituisci(struttura, fileOut)
    return

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    struttura= fparse(fileIn)
    modificatore(struttura, selettore.split(), chiave, valore)
    restituisci(struttura, fileOut)
    return

    

