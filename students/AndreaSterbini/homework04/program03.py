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
    #Inserite qui il vostro codice
    DOM = fparse(fileIn)
    return len(trova_nodi(DOM, selettore))

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice
    DOM = fparse(fileIn)
    _elimina_nodi(DOM, selettore)
    with open(fileOut, mode="w") as f:
        f.write(DOM.to_string())

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
    DOM = fparse(fileIn)
    _cambia_attributo(DOM, selettore, chiave, valore)
    with open(fileOut, mode="w") as f:
        f.write(DOM.to_string())


def trova_nodi(DOM, selettore):
    '''Torna la lista di nodi dell'albero, che soddisfano il selettore CSS.'''
    sequenza = selettore.split()
    return search_CSS(DOM,sequenza)


def _elimina_nodi(DOM, selettore):
    da_eliminare = trova_nodi(DOM, selettore)
    for nodo in da_eliminare:
        elimina_nodo(DOM, nodo)


def _cambia_attributo(DOM, selettore, chiave, valore):
    da_modificare = trova_nodi(DOM, selettore)
    for nodo in da_modificare:
        if not nodo.istext():
            nodo.attr[chiave] = valore


def elimina_nodo(DOM, nodo):
    if DOM is nodo:
        return True
    elif DOM.istext():
        return False
    else:
        if nodo in DOM.content:
            DOM.content.remove(nodo)
            return True
        else:
            for figlio in DOM.content:
                if elimina_nodo(figlio, nodo):
                    return True
            return False


def search_CSS(DOM, sequenza, stop=False):
    '''Torna la sequenza di nodi che soddisfa il selettore.
    Se stop=True il primo selettore deve corrispondere a questo nodo, altrimenti viene cercato anche in profondità.
    Gestisce lo '>' che limita la profondità di ricerca del selettore seguente ai soli figli.
    '''
    #print( 'entering search_CSS ', DOM, sequenza)
    first, *rest = sequenza
    res = []

    if first == '>':
        # ricorsione con stop=True
        return search_CSS(DOM, rest, True)

    # it could match here, the we ignore stop
    if  match_CSS(DOM, first):
        if not rest:
            return [DOM]
        else:
            for tag in DOM.content:
                res += search_CSS(tag, rest, False)
    elif DOM.istext():
        pass
    elif not stop:
        # else if not stop we go looking down
        for tag in DOM.content:
            res += search_CSS(tag, sequenza, False)
    return res

def match_CSS(DOM, selettore):
    '''Torna true se il nodo corrisponde al selettore'''
    #print( 'entering match_CSS ', DOM, selettore)
    fc   = selettore[0]             # primo carattere
    rest = selettore[1:]            # resto del selettore
    if DOM.tag == '_text_':
        return False
    elif fc == '.':                 # se è .classe
        return 'class' in DOM.attr and rest in DOM.attr['class'].split()
    elif fc == '#':                 # se è #id
        return 'id' in DOM.attr    and DOM.attr['id'] == rest
    elif fc == '@':                 # se ha l'attributo dato col valore indicato
        rest = rest.strip('[]')     # via le parentesi
        k,v = rest.split('=')       # k="v"
        v = v.strip('\'"')          # si tolgono gli apici
        return k in DOM.attr       and DOM.attr[k] == v
    else:
        return selettore == DOM.tag


if __name__ == '__main__':
    import sys
    print(sys.argv)
    fn  = 'docs.python.org.html'
    css = '.btn'
    if len(sys.argv) > 1:
        css = sys.argv[1]
    if len(sys.argv) > 2:
        fn = sys.argv[2]

    DOM = fparse(fn)
    cambia_attributo(DOM, 'div > a', 'style', 'background-color:red')
    with open('docs.python.org-red.html', mode="w") as f:
        f.write(DOM.to_string())

