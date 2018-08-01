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

import my_html

def interpreta(selettore):
    
    #Interpreta la richiesta del selettore controllandone il primo carattere.
    firstcar = selettore[0]
    
    if firstcar == '#': return 'id'
    if firstcar == '.': return 'classe'
    if selettore.isalpha(): return 'tag'

    
def conta(radice, selettore):
    
    #Se il selettore chiede un'id viene cercato come valore della chiave 'id'
    #nel dizionario degli attributi.
    if interpreta(selettore) == 'id':
        if 'id' in radice.attr:
            if radice.attr['id'] == selettore[1:]:
                return 1
            
    #Se il selettore chiede una classe viene cercato nel valore della chiave 'class'
    #nel dizionario degli attributi.
    if interpreta(selettore) == 'classe':
        if 'class' in radice.attr:
            if selettore[1:] in radice.attr['class']:
                return 1
            
    #Se il selettore chiede un tag viene cercato nel .tag del nodo.
    if interpreta(selettore) == 'tag':
        if radice.tag == selettore:
            return 1
        
    #la funzione viene richiamata ricorsivamente sui figli (se essi non sono di tipo _text_)
    #incrementando il contatore.
    count = 0
    for figlio in radice.content:
        if figlio.istext() == False:
            count += conta(figlio, selettore)
            #print('r')
            
    return count

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    
    radice = my_html.fparse(fileIn)
    
    return conta(radice, selettore)

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice