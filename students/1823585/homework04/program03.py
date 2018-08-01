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
    html_root = fparse(fileIn)
    nodi = trova_nodi(html_root, selettore.split(" "))
    return len(nodi)

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    html_root = fparse(fileIn)
    nodi_padre_figlio = trova_nodi(html_root, selettore.split(" "))
    for padre,figlio in nodi_padre_figlio:
        padre.content.remove(figlio)
    with open(fileOut,'w', encoding='utf8') as f:
        f.write(html_root.to_string())

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
    html_root = fparse(fileIn)
    nodi_padre_figlio = trova_nodi(html_root, selettore.split(" "))
    for padre,nodo in nodi_padre_figlio:
        nodo.attr[chiave] = valore
    with open(fileOut,'w', encoding='utf8') as f:
        f.write(html_root.to_string())


def trova_nodi(node, selettori, genitore=None):
    if not selettori:
        return []
    selettori = selettori[:]
    parent_and_child_nodes = []
    direct_child = False
    if selettori[0] == ">":
        selettori.pop(0)
        direct_child = True

    if selector_matches(node, selettori[0]):
        selettori.pop(0)
        if not selettori:
            parent_and_child_nodes.append( (genitore, node) )
            return parent_and_child_nodes
    elif direct_child:
        return []

    figli_not_text = [f for f in node.content if not isinstance(f,str)]

    if not figli_not_text:
        return parent_and_child_nodes

    for figlio in figli_not_text:
        parent_and_child_nodes.extend( trova_nodi(figlio, selettori, genitore=node) )

    return parent_and_child_nodes
    

def selector_matches(node,selector):
    "True se un tag matcha un singolo selector"
   
    if selector.startswith("#"):
        if selector[1:] == node.attr.get('id'):
            return True

    if selector.startswith("."):
        if selector[1:] in node.attr.get('class', ' ').split(' '):
            return True

    if selector.startswith("@"):
        nuova_stringa = selector[1:].replace("[","").replace("]","").replace('"',"")
        a,v = nuova_stringa.split("=")
        if v == node.attr.get(a, None):
            return True

    if selector == node.tag:
        return True

    return False