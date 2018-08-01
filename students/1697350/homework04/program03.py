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
import re


def findNumeroId(doc, selettore, listaOccurrences = []):
    if not doc.istext():
        if 'id' in doc.attr and doc.attr['id'] == selettore:
            listaOccurrences.append(1)
        for child in doc.content:
                findNumeroId(child,selettore, listaOccurrences)
    return listaOccurrences

def findNumeroTag(doc, selettore, listaOccurrences = []):
    if not doc.istext():
        if doc.tag == selettore:
            listaOccurrences.append(1)
        for child in doc.content:
            findNumeroTag(child, selettore, listaOccurrences)
    return listaOccurrences

def findNumeroClass(doc, selettore, listaOccurrences = []):
    if not doc.istext():
        if 'class' in doc.attr and selettore in doc.attr['class']:
            listaOccurrences.append(1)
        for child in doc.content:
            findNumeroClass(child, selettore, listaOccurrences)
    return listaOccurrences

def findNumeroAttr(doc, selettore, listaOccurrences = []):
    splitted = selettore.split("=")
    sel = splitted[0].strip()
    value = splitted[1].strip()
    if not doc.istext():
        if sel in doc.attr and value == doc.attr[sel]:
            listaOccurrences.append(1)
        for child in doc.content:
            findNumeroAttr(child, selettore, listaOccurrences)
    return listaOccurrences

def findNumeroPadreFiglio(doc, selettore, listaOccurrences = []):
    splitted = selettore.split(">")
    sel = splitted[0].strip()
    value = splitted[1].strip()
    if not doc.istext():
        for child in doc.content:
            listaOccurrences.append((doc.tag, child.tag))
            findNumeroPadreFiglio(child, selettore, listaOccurrences)
    count = 0
    for tupla in listaOccurrences:
        if (sel, value) == tupla:
            count += 1
    return  count

def findNumeroAvoDiscendente(doc,level=0, listaOccurrences = []):
    if not doc.istext():
        for child in doc.content:
            if not child.istext():
                listaOccurrences.append((level, child.tag))
            findNumeroAvoDiscendente(child,level+1, listaOccurrences)
    return listaOccurrences

def findAvoDiscendente(doc,level=0, listaOccurrences = []):
    if not doc.istext():
        for child in doc.content:
            if not child.istext():
                listaOccurrences.append((level,child.tag, child))
            findAvoDiscendente(child,level+1, listaOccurrences)
    return listaOccurrences

def findAvoDiscendente2(doc,level=0, listaOccurrences = []):
    if not doc.istext():
        for child in doc.content:
            if not child.istext():
                listaOccurrences.append((level,child.tag, child))
            findAvoDiscendente2(child,level+1, listaOccurrences)
    return listaOccurrences

def findIds(doc, selettore, listaOccurrences = []):
    if not doc.istext():
        if 'id' in doc.attr and doc.attr['id'] == selettore:
            listaOccurrences.append(doc)
        for child in doc.content:
            findIds(child,selettore, listaOccurrences)
    return listaOccurrences





def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    doc = fparse(fileIn)

    if '#' in selettore:
        selettore = selettore.replace("#", '')
        return len(findNumeroId(doc, selettore))
    elif '@' in selettore:
        selettore = selettore.replace('[', '').replace(']', '').replace('@', '').replace('"','')
        return len(findNumeroAttr(doc, selettore))
    elif '>' in selettore:

        return findNumeroPadreFiglio(doc, selettore)

    elif '.' in selettore:
        selettore = selettore.replace('.','')
        return len(findNumeroClass(doc, selettore))
    elif len(selettore.split(" ")) > 1:
        occorrenze = findNumeroAvoDiscendente(doc)
        splitted = selettore.split(" ")
        parent = splitted[0].strip()
        child = splitted[1].strip()
        count = 0
        actual_index = -1
        for elem in occorrenze:
            index = elem[0]
            value = elem[1]
            if parent == value:
                actual_index = index
            elif child == value and index > actual_index:
                count += 1
            else:
                actual_index = -1
        return count
    else:
        return len(findNumeroTag(doc, selettore))

def elimina_nodo(doc, nodo):
    if not doc.istext():
        try:
            doc.content.remove(nodo)
        except ValueError:
            pass

        for child in doc.content:
            if not child.istext():
                elimina_nodo(child, nodo)
    return doc

def changeNodo(doc, nodo, chiave, valore):
    if not doc.istext():
        try:
            for n in doc.content:
                if n == nodo:
                    n.attr[chiave] = valore
        except ValueError:
            pass

        for child in doc.content:
            if not child.istext():
                changeNodo(child, nodo, chiave, valore)
    return doc

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    doc = fparse(fileIn)
    if '#' in selettore:
        return
    elif '@' in selettore:
        return
    elif '>' in selettore:
        return
    elif '.' in selettore:
        return
    elif len(selettore.split(" ")) > 1:
        splitted = selettore.split(" ")
        parent = splitted[0].strip()
        child = splitted[1].strip()
        lista = findAvoDiscendente(doc)
        nodesToRemove = []
        actual_index = -1
        for elem in lista:
            index = elem[0]
            value = elem[1]
            nodo = elem[2]
            if parent == value:
                actual_index = index
            elif child == value and index > actual_index:
                nodesToRemove.append(nodo)
            else:
                actual_index = -1
        for n in nodesToRemove:
            elimina_nodo(doc, n)
        with open(fileOut, 'w') as out:
            out.write(doc.to_string())
    else:
        return



def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    doc = fparse(fileIn)
    if '#' in selettore:
        selettore = selettore.replace("#","")
        nodesToChange = findIds(doc, selettore)
        for n in nodesToChange:
            changeNodo(doc, n, chiave, valore)
        with open(fileOut, 'w') as out:
            out.write(doc.to_string())
        changeNodo(doc, doc, chiave, valore)
        with open(fileOut, 'w') as out:
            out.write(doc.to_string())
    elif '@' in selettore:
        return
    elif '>' in selettore:
        return
    elif '.' in selettore:
        return
    elif len(selettore.split(" ")) > 1:
        splitted = selettore.split(" ")
        parent = splitted[0].strip()
        child = splitted[1].strip()
        lista = findAvoDiscendente2(doc)
        nodesToRemove = []
        listaValues = []
        p_index = -1
        for elem in lista:
            index = elem[0]
            value = elem[1]
            nodo = elem[2]
            if parent == value:
                listaValues = []
                p_index = index
            elif child == value and index > p_index:
                listaValues2 = [x for x in listaValues if x <= p_index]
                if len(listaValues2) == 0:
                    nodesToRemove.append(nodo)
            else:
                listaValues.append(index)

        for n in nodesToRemove:
            changeNodo(doc, n, chiave, valore)
        with open(fileOut, 'w') as out:
            out.write(doc.to_string())
    else:
        return


