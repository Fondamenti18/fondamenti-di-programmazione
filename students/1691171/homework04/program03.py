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


def disc_per_attr(el, name, val, trovati, figlio = False):
    if name in el.attr.keys() and val in el.attr[name]:
        trovati.append(el)
    if isinstance(el.content, list):
        if figlio:
            for n in el.content:
                if (not n.istext()) and name in n.attr.keys() and val in n.attr[name]:
                    trovati.append(n)
        else:
            for n in el.content:
                if not n.istext():
                    disc_per_attr(n, name, val, trovati)

def disc_per_tag(el, name, trovati, figlio = False):
    if name == el.tag:
        trovati.append(el)
    if isinstance(el.content, list):
        if figlio:
            for n in el.content:
                if (not n.istext()) and name == n.tag:
                    trovati.append(n)
        else:
            for n in el.content:
                if not n.istext():
                    disc_per_tag(n, name, trovati)


def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    doc = fparse(fileIn)
    sel = selettore.split(' ')
    ls = [doc]
    trovati = []
    figlio = False
    i = 0
    while i < len(sel):
        if sel[i] == '>':
            figlio = True
        elif sel[i].startswith("#"):
            at = sel[i][1:]
            for el in ls:
                disc_per_attr(el, 'id', at, trovati, figlio)
            figlio = False
        elif sel[i].startswith("."):
            at = sel[i][1:]
            for el in ls:
                disc_per_attr(el, 'class', at, trovati, figlio)
            figlio = False
        elif sel[i].startswith("@["):
            att = sel[i][2:-1].split('=')
            nome = att[0]
            val = att[1].strip('"')
            for el in ls:
                disc_per_attr(el, nome, val, trovati, figlio)
            figlio = False
        else:
            for el in ls:
                disc_per_tag(el, sel[i], trovati, figlio)
            figlio = False

        if not figlio:
            ls = trovati
            trovati = []
        i += 1
    return len(ls)


def check_node(node, sel):
    if sel.startswith('#') and 'id' in node.attr:
        at = sel[1:]
        return at in node.attr['id']
    elif sel.startswith("."):
        at = sel[1:]
        if 'class' in node.attr.keys():
            b = at in node.attr['class']
            return b
        return False
    elif sel.startswith("@["):
        att = sel[2:-1].split('=')
        nome = att[0]
        val = att[1].strip('"')
        b = nome in node.attr.keys() and val in node.attr[nome]
        return b
    elif node.tag == sel:
        return True
    else:
        return False


def eliminazione(node, sels, s, figlio = False):
    if sels[s] == '>':
        eliminazione(node, sels, s+1, True)
    else:
        if figlio:
            i = 0
            while i < len(node.content):
                if isinstance(node.content, list):
                    c = check_node(node.content[i], sels[s])
                    if c and s == len(sels)-1:
                        del node.content[i]
                    elif c:
                        eliminazione(node.content[i], sels, s+1)
                i += 1
        else:
            i = 0
            while i < len(node.content):
                if isinstance(node.content, list):
                    c = check_node(node.content[i], sels[s])
                    if sels[s] == '>':
                        eliminazione(node.content[i], sels, s + 1, True)
                    if c and s == len(sels)-1:
                        del node.content[i]
                    elif c:
                        eliminazione(node.content[i], sels, s+1)
                    else:
                        eliminazione(node.content[i], sels, s)
                i += 1


def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    doc = fparse(fileIn)
    sels = selettore.split(" ")
    i = 0
    if check_node(doc, sels[i]) and i == len(sels) - 1:
        with open(fileOut, "w") as fout:
            fout.write("")
    elif check_node(doc, sels[i]):
        eliminazione(doc, sels, i+1, False)
    else:
        eliminazione(doc, sels, i, False)

    with open(fileOut, "w") as fout:
        fout.write(doc.to_string())


def cambiamento(node, sels, s, figlio = False, chiave = '', valore = ''):
    if isinstance(node.content, list):
        if figlio:
            j = 0
            while j < len(node.content):
                if check_node(node.content[j], sels[s]):
                    node.content[j].attr[chiave] = valore
                j += 1
        else:
            i = 0
            while i < len(node.content):
                if sels[s] == '>':
                    cambiamento(node.content[i], sels, s+1, True, chiave, valore)
                elif check_node(node.content[i], sels[s]) and s == len(sels)-1:
                    node.content[i].attr[chiave] = valore
                elif check_node(node.content[i], sels[s]):
                    cambiamento(node.content[i], sels, s+1, False, chiave, valore)
                else:
                    cambiamento(node.content[i], sels, s, False, chiave, valore)
                i += 1


def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    doc = fparse(fileIn)
    sels = selettore.split(" ")
    i = 0
    if check_node(doc, sels[i]) and i == len(sels) - 1:
        with open(fileOut, "w") as fout:
            fout.write("")
    elif check_node(doc, sels[i]):
        cambiamento(doc, sels, i + 1, False, chiave, valore)
    else:
        cambiamento(doc, sels, i, False, chiave, valore)

    with open(fileOut, "w") as fout:
        fout.write(doc.to_string())