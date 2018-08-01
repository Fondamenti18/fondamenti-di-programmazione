"""
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
"""
import re
from my_html import HTMLNode, fparse

ATTR_RE = re.compile(r"\[([\w]+)=\"([\w]+)\"]")


class jQuery:
    def __init__(self, selector, node):
        self.selector = jquery_fn_parse_selector(selector)
        self.node = node
        self.result = [node]

    def get(self):
        if not len(self.selector):
            return self.result

        direct_child = False
        instr = self.selector.pop(0)
        if instr == ">":
            direct_child = True
            if not len(self.selector):
                raise SyntaxError("Invalid selector!")

            instr = self.selector.pop(0)

        temp_result = []
        for n in self.result:
            temp_result += jquery_fn_find(instr, n, direct_child)

        self.result = temp_result

        return self.get()

    def remove(self):
        removables = self.get()
        if self.node in removables:
            return HTMLNode(*[""]*3)

        jquery_fn_remove(removables, self.node, self.node)

    def attr(self, name, value):
        elements = self.get()
        for element in elements:
            element.attr[name] = value


def jquery_fn_parse_selector(selector):
    if not len(selector):
        return []

    result = []
    selector = [x for x in selector.replace(">", " >").split(" ") if len(x)]
    for e in selector:
        if e[0] == "#":
            result.append(("id", e[1:]))

        elif e[0] == ".":
            result.append(("class", e[1:]))

        elif e[0] == "@":
            attr = ATTR_RE.match(e[1:])
            if not attr:
                raise SyntaxError("Invalid selector!")

            result.append(attr.groups())

        elif e[0] == ">" and len(e) != 1:
                raise SyntaxError("Invalid selector!")

        else:
            result.append(e)

    return result


def jquery_fn_find(element, node, direct_child=False, deep=0):
    if direct_child and deep > 1:
        return []

    elif type(element) == tuple and element[0] in node.attr and element[1] in node.attr[element[0]].split(" ") \
            or node.tag == element:
        return [node]

    elif node.tag == "_text_":
        return []

    result = []
    for subnode in node.content:
        result += jquery_fn_find(element, subnode, direct_child, deep+1)

    return result


def jquery_fn_remove(elements, node, father):
    if node in elements:
        del father.content[father.content.index(node)]

    else:
        if node.tag != "_text_":
            for sn in node.content:
                jquery_fn_remove(elements, sn, node)


def conta_nodi(fileIn, selettore):
    """Torna il numero di nodi dell'albero, che soddisfano il selettore CSS."""
    return len(jQuery(selettore, fparse(fileIn)).get())


def elimina_nodi(fileIn, selettore, fileOut):
    """Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)"""
    root = fparse(fileIn)
    jQuery(selettore, root).remove()
    open(fileOut, "w").write(root.to_string())


def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    """Modifica tutti i nodi dell'albero che soddisfano il selettore CSS"""
    root = fparse(fileIn)
    jQuery(selettore, root).attr(chiave, valore)
    open(fileOut, "w").write(root.to_string())
