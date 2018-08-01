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
    tree = fparse(fileIn)
    count = _conta_(tree, selettore, 0)
    return count

def _conta_(tree, selettore, count):
    count = 0
    selettore = clean(selettore)
    if not tree.istext():
        count += find_att(tree, selettore)
        if len(selettore.split()) == 2 and tree.tag in selettore:
            count += check_avo(tree, selettore[-1], 0)
        if tree.tag in selettore:
            count += padre_figlio(tree,selettore)
        if len(tree.content) > 0:
            for son in tree.content:
                count += _conta_(son, selettore, count)
        if tree.tag == selettore:
            count +=1
        if selettore[1:] in tree.attr:
            count +=1
        try:
            if tree.attr["id"] == selettore[1:]:
                count+=1
        except Exception as e:
            pass
    return count

def padre_figlio(tree,selettore):
    count = 0
    splitted = selettore.split()
    for word in splitted:
        for son in tree.content:
            if not son.istext():
                if son.tag == word:
                    count+=1
    return count

def clean(selettore):
    new_sel = ""
    bad_words = ["@", "[", "]", "!", "=", '"']
    for lett in selettore:
        if lett in bad_words:
            new_sel += " "
        else:
            new_sel += lett
    return new_sel

def find_att(tree, selettore):
    splitted = selettore.split()
    count = 0
    for key in splitted:
        if key in tree.attr:
            for val in splitted:
                if tree.attr[key] == val:
                    count += 1
    return count

def check_avo(tree, disc, count):
    count = 0
    if not tree.istext():
        for son in tree.content:
            count += check_avo(son, disc, count)
        if tree.tag == disc:
            count +=1
    return count

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    verifica = 0
    tree = fparse(fileIn)
    albero = _elimina_(tree, selettore)
    f = open(fileOut, w)
    f.write(albero)
    f.close()
    return None

def _elimina_(tree, selettore):
    rimuovi = []
    if not tree.istext():
        if len(tree.content) > 0:
            for son in tree.content:
                if son.tag != selettore[-1]:
                    tree = _elimina_(son, selettore)
                else:
                    rimuovi.append(son)
            for son in rimuovi:
                tree.content.remove(son)
    return tree

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    cambia = 0
    tree = fparse(fileIn)
    cambia += _cambia_(tree, selettore)
    return None

def _cambia_(tree, selettore):
    cambia = 0
    if not tree.istext():
        if len(tree.content) > 0:
            for son in tree.content:
                cambia += _cambia_(son, selettore)
    return 0
