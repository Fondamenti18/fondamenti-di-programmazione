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
    sequenza = selettore.split()
    return conta_CSS(DOM,sequenza)

    
def conta_CSS(DOM, sequenza, stop=False):
    '''Torna la sequenza di nodi che soddisfa il selettore.
    Se stop=True il primo selettore deve corrispondere a questo nodo, altrimenti viene cercato anche in profondità.
    Gestisce lo '>' che limita la profondità di ricerca del selettore seguente ai soli figli.
    '''
    first, *rest = sequenza
    res = 0

    if first == '>': return conta_CSS(DOM, rest, True)
    
    if  match_CSS(DOM, first):
        if not rest: return 1
        for tag in DOM.content:
            res += conta_CSS(tag, rest, False)
    elif DOM.istext(): pass
    elif not stop:
        for tag in DOM.content:
            res += conta_CSS(tag, sequenza, False)
    return res

def match_CSS(DOM, selettore):
    fc   = selettore[0]             # primo carattere
    rest = selettore[1:]            # resto del selettore
    if DOM.tag == '_text_':
        return False
    if fc == '.':                 
        return 'class' in DOM.attr and rest in DOM.attr['class'].split()
    if fc == '#':                 
        return 'id' in DOM.attr and DOM.attr['id'] == rest
    if fc == '@':                 
        rest = rest.strip('[]')     
        k,v = rest.split('=')       
        v = v.strip('\'"')          
        return k in DOM.attr and DOM.attr[k] == v
    return selettore == DOM.tag


def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    DOM = fparse(fileIn)
    cambia_CSS(DOM, selettore.split(), chiave, valore)
    with open(fileOut, mode="w") as f:
        f.write(DOM.to_string())


def cambia_CSS(DOM, sequenza, chiave, valore,stop=False,):
    first, *rest = sequenza

    if first == '>':
        cambia_CSS(DOM, rest, chiave, valore,True)
        return

    if  match_CSS(DOM, first):
        if not rest:
            DOM.attr[chiave] = valore
            return 
        for tag in DOM.content:
            cambia_CSS(tag, rest, chiave, valore, False)
    elif DOM.istext():
        pass
    elif not stop:
        for tag in DOM.content:
            cambia_CSS(tag, sequenza, chiave, valore,False)
    return 
    
def elimina_nodi(fileIn, selettore, fileOut):
    DOM = fparse(fileIn)
    elimina_CSS(DOM,selettore.split(),DOM)
    with open(fileOut, mode="w") as f:
        f.write(DOM.to_string())

def elimina_CSS(DOM, sequenza, padre,stop=False,):
    first, *rest = sequenza
    if first == '>':
        elimina_CSS(DOM, rest, DOM, True)
        return
    if  match_CSS(DOM, first):
        if not rest:
            padre.content.remove(DOM)
            return 
        else:
            for tag in DOM.content:
                elimina_CSS(tag, rest, DOM, False)
    elif DOM.istext():
        pass
    elif not stop:
        for tag in DOM.content:
            elimina_CSS(tag, sequenza, DOM,False)
    return 