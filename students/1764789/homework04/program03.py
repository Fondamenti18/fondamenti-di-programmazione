# -*- coding: utf-8 -*-
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
    # Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.
    root = fparse(fileIn)
    return len(trova_nodi(root, selettore.split()))

def elimina_nodi(fileIn, selettore, fileOut):
    # Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)
    root = fparse(fileIn)
    elimina_nodo(root, selettore.split())
    with open(fileOut, 'w', encoding='utf8') as f:
        f.write(root.to_string())
        f.close()

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    # Modifica tutti i nodi dell'albero che soddisfano il selettore CSS
    root = fparse(fileIn)
    cambia_attributo_nodi(root, selettore.split(), chiave, valore)
    with open(fileOut, 'w', encoding='utf8') as f:
        f.write(root.to_string())
        f.close()

# ########################################################################
# UTILITY
# ########################################################################
def trova_nodi(nodo, lista_selettori_base):
    # La lista dei nodi discendenti del nodo corrente che soddisfano 
    # il selettore CSS corrispondente al secondo argomento del metodo.
    lista_nodi = []
    # Se la lista di selettori base e' vuota ritorna una lista nodi vuota
    if len(lista_selettori_base) == 0:
        return lista_nodi
    # Ai nodi di testo non puo' essere applicata alcuna condizione
    # e pertanto e' ritornata una lista nodi vuota.
    if nodo.istext():
        return lista_nodi
    # Si verifica se il primo elemento della lista di selettori base non 
    # sia proprio '>'. In questo caso il nodo corrente deve soddisfare
    # la condizione relativa al selettore base successivo nella lista.
    # Se questa condizione non e' verificata e' ritornata la lista vuota.
    if lista_selettori_base[0] == '>':
        if verifica_nodo(nodo, lista_selettori_base[1]):
            if len(lista_selettori_base) == 2:
                lista_nodi += [nodo]
            else:
                for nodo_figlio in nodo.content:
                    lista_nodi += trova_nodi(nodo_figlio, lista_selettori_base[2:])
        return lista_nodi
    # Si verifica se il nodo corrente il primo selettore base
    if verifica_nodo(nodo, lista_selettori_base[0]):
        if len(lista_selettori_base) == 1:
            lista_nodi += [nodo]
        else:
            for nodo_figlio in nodo.content:
                lista_nodi += trova_nodi(nodo_figlio, lista_selettori_base[1:])
        return lista_nodi
    # Il nodo corrente non soddisfa il primo selettore base
    # pertanto si procede nell'esplorazione dell'albero
    for nodo_figlio in nodo.content:
        lista_nodi += trova_nodi(nodo_figlio, lista_selettori_base)
    return lista_nodi

def verifica_nodo(nodo,selettore_base):
    if selettore_base[:1] == ".":
        if "class" in nodo.attr:
            if selettore_base[1:] in nodo.attr["class"].split():
                return True
        return False
    elif selettore_base[:1] == "#":
        if "id" in nodo.attr:
            if selettore_base[1:] == nodo.attr["id"]:
                return True
        return False
    elif selettore_base[:1] == "@":
        av = get_attributo_valore(selettore_base)
        if av[0] in nodo.attr:
            if av[1] == nodo.attr[av[0]]:
                return True
        return False
    else:
        return nodo.tag == selettore_base
    
def get_attributo_valore(selettore_attributo_valore):
    s = selettore_attributo_valore
    s = s.replace('@','')
    s = s.replace('[','')
    s = s.replace(']','')
    l = s.split('=')
    return (l[0],l[1][1:][:-1])

# E' analoga alla trova nodi soltanto che i nodi che soddisfano il 
# selettore CSS vengono modificati e non ritornati
def cambia_attributo_nodi(nodo, lista_selettori_base, chiave, valore):
    # Se la lista di selettori base e' vuota ritorna 
    if len(lista_selettori_base) == 0:
        return
    # I nodi di testo non hanno attributi quindi ritorna
    if nodo.istext():
        return
    # Si verifica se il primo elemento della lista di selettori base non 
    # sia proprio '>'. In questo caso il nodo corrente deve soddisfare la
    # condizione relativa al selettore base successivo nella lista dei 
    # selettori. Se questa condizione non e' verificata ritorna.
    if lista_selettori_base[0] == '>':
        if verifica_nodo(nodo, lista_selettori_base[1]):
            if len(lista_selettori_base) == 2:
                cambia_attributo_nodo(nodo, chiave, valore)
            else:
                for nodo_figlio in nodo.content:
                    cambia_attributo_nodi(nodo_figlio, lista_selettori_base[2:], chiave, valore)
    # Si verifica se il nodo corrente soddisfa il primo selettore base
    if verifica_nodo(nodo, lista_selettori_base[0]):
        if len(lista_selettori_base) == 1:
            cambia_attributo_nodo(nodo, chiave, valore)
        else:
            for nodo_figlio in nodo.content:
                cambia_attributo_nodi(nodo_figlio, lista_selettori_base[1:], chiave, valore)
    # Il nodo corrente non soddisfa il primo selettore base
    # pertanto si procede nell'esplorazione dell'albero
    for nodo_figlio in nodo.content:
        cambia_attributo_nodi(nodo_figlio, lista_selettori_base, chiave, valore)

def cambia_attributo_nodo(nodo, chiave, valore):
    nodo.attr[chiave] = valore

# E' analoga alla trova nodi soltanto che i nodi che soddisfano il 
# selettore CSS vengono rimossi e non ritornati
def elimina_nodo(nodo, lista_selettori_base):
    # Se la lista di selettori base e' vuota ritorna 
    if len(lista_selettori_base) == 0:
        return False
    # I nodi di testo non hanno attributi quindi ritorna
    if nodo.istext():
        return False
    # Si verifica se il primo elemento della lista di selettori base non 
    # sia proprio '>'. In questo caso il nodo corrente deve soddisfare la
    # condizione relativa al selettore base successivo nella lista dei 
    # selettori. Se questa condizione non e' verificata ritorna.
    if lista_selettori_base[0] == '>':
        if verifica_nodo(nodo, lista_selettori_base[1]):
            if len(lista_selettori_base) == 2:
                return True
            else:
                indici_nodi = []
                for nodo_figlio in nodo.content:
                    if elimina_nodo(nodo_figlio, lista_selettori_base[2:]) == True:
                        indici_nodi.append(nodo.content.index(nodo_figlio))
                for indice in indici_nodi[::-1]:
                    del nodo.content[indice]
    # Si verifica se il nodo corrente soddisfa il primo selettore base
    if verifica_nodo(nodo, lista_selettori_base[0]):
        if len(lista_selettori_base) == 1:
            return True
        else:
            indici_nodi = []
            for nodo_figlio in nodo.content:
                if elimina_nodo(nodo_figlio, lista_selettori_base[1:]) == True:
                    indici_nodi.append(nodo.content.index(nodo_figlio))
            for indice in indici_nodi[::-1]:
                del nodo.content[indice]
    # Il nodo corrente non soddisfa il primo selettore base
    # pertanto si procede nell'esplorazione dell'albero
    indici_nodi = []
    for nodo_figlio in nodo.content:
        if elimina_nodo(nodo_figlio, lista_selettori_base) == True:
            indici_nodi.append(nodo.content.index(nodo_figlio))
    for indice in indici_nodi[::-1]:
        del nodo.content[indice]
    return False