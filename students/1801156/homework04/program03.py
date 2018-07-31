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
from copy import deepcopy

class selector:
    '''classe che definisce ogni tag del selettore.'''
    def __init__(self, tag, diz):
        self.tag = tag
        self.diz = diz

def ini_selettore(selettore):
    '''inizializzazione del selettore'''
    sel = ''
    i = 0
    while i < len(selettore):
        if selettore[i].isalpha() and selettore[i-1] == ' ' and selettore[i-2] != '>':
            sel += '^ '
        sel += selettore[i]
        i += 1
    return ' ' + sel + ' '

def check_punto(sel, i, tag, diz, check_atr, lista_selettore):
    '''controllo se n esimo elemento del selettore e un punto.'''
    if sel[i] == '.':
        diz['class'] = sel[i+1: sel.index(' ', i)]
        lista_selettore.append(selector(tag, diz))
        lista_selettore.append('^')
        tag = ''
        diz = {}
        check_atr = True
    return sel, i, tag, diz, check_atr

def check_chiocciola(sel, i, tag, diz, check_atr, lista_selettore):
    '''controllo se n esimo elemento del selettore e una chiocciola.'''
    if sel[i] == '@':
        diz[sel[i+2: sel.index('=', i)]] = sel[sel.index('=', i)+2: sel.index(' ', i)-2]
        lista_selettore.append(selector(tag, diz))
        lista_selettore.append('^')
        tag = ''
        diz = {}
        check_atr = True
    return sel, i, tag, diz, check_atr

def check_cancelletto(sel, i, tag, diz, check_atr, lista_selettore):
    '''controllo se n esimo elemento del selettore e un cancelletto.'''
    if sel[i] == '#':
        diz['id'] = sel[i+1: sel.index(' ', i)]
        lista_selettore.append(selector(tag, diz))
        lista_selettore.append('^')
        tag = ''
        diz = {}
        check_atr = True
    return sel, i, tag, diz, check_atr

def check_operatore(sel, i, tag, diz, check_atr, lista_selettore):
    '''controllo se n esimo elemento del selettore e un operatore.'''
    if sel[i] == '>' or sel[i] == '^':
        if check_atr == False:
            lista_selettore.append(selector(tag, diz))
            lista_selettore.append(sel[i])
            tag = ''
            diz = {}
        else:
            lista_selettore[-1] = sel[i]
            check_atr = False
    return sel, i, tag, diz, check_atr

def check_len(sel, i, tag, diz, check_atr, lista_selettore):
    '''controllo se sono arrivato a ultimo elemento del selettore.'''
    if i == len(sel)-1:
        if check_atr == False:
            lista_selettore.append(selector(tag, diz))
            tag = ''
            diz = {}
        else:
            check_atr = False
    return sel, i, tag, diz, check_atr

def check_selettore(sel, i, tag, diz, check_atr, lista_selettore):
    '''controllo intero selettore sfruttando le funzioni precedenti.'''
    if sel[i].isalpha() and sel[i-1] == ' ':
        tag = sel[i: sel.index(' ', i)]    
    sel, i, tag, diz, check_atr = check_punto(sel, i, tag, diz, check_atr, lista_selettore)    
    sel, i, tag, diz, check_atr = check_chiocciola(sel, i, tag, diz, check_atr, lista_selettore)
    sel, i, tag, diz, check_atr = check_cancelletto(sel, i, tag, diz, check_atr, lista_selettore)
    sel, i, tag, diz, check_atr = check_operatore(sel, i, tag, diz, check_atr, lista_selettore)
    sel, i, tag, diz, check_atr = check_len(sel, i, tag, diz, check_atr, lista_selettore)    
    return sel, i, tag, diz, check_atr

def create_selettore(selettore):
    '''creazione di una lista che rappresenta il selettore.'''
    sel = ini_selettore(selettore)
    diz = {}
    tag = ''
    lista_selettore = []
    check_atr = False
    i = 0
    while i < len(sel):
        sel, i, tag, diz, check_atr = check_selettore(sel, i, tag, diz, check_atr, lista_selettore)
        i += 1
    return lista_selettore

def modifica_selettore(selettore):
    '''controllo se ultimo elemento della lista selettore e un carattere particolare.'''
    lista_selettore = create_selettore(selettore)
    if lista_selettore[-1] == '^':
        del lista_selettore[-1]
    return lista_selettore



def verifica_diz(nodo, diz):
    '''controllo se in un tag sono presenti tutti gli attributi del selettore.'''
    cont = 0
    for key in diz:
        if key not in nodo.attr or (diz[key] != nodo.attr[key] and diz[key] not in nodo.attr[key]): #uso not in perche' c'e' il caso in cui il nome della classe e' presente tra altri caratteri
            cont += 1
    return cont



def search_nodo_cont(nodo, tag, diz, lista_nodi):
    '''conto i nodi uguali a quello richiesto.'''
    if nodo.tag == tag or tag == '':
        if verifica_diz(nodo, diz) == 0:
            lista_nodi += [nodo]

def search_nodo(nodo, tag, diz, lista_nodi):
    '''cerco un nodo a qualsiasi profondita.'''
    if nodo.istext() == False:
        search_nodo_cont(nodo, tag, diz, lista_nodi)
        for child in nodo.content:
            search_nodo(child, tag, diz, lista_nodi)

def search_subnodo(nodo, tag, diz, lista_ris):
    '''cerco solo i figli di un nodo.'''
    if nodo.istext() == False:
        if nodo.tag == tag or tag == '':
            if verifica_diz(nodo, diz) == 0:
                lista_ris += [nodo]

def conta_nodi_search_subnodo(lista_ris, lista_selettore, i, lista_risultato):
    '''cerco solo i figli.'''
    for nodo in lista_ris:
        for figlio in nodo.content:
            search_subnodo(figlio, lista_selettore[i].tag, lista_selettore[i].diz, lista_risultato)

def conta_nodi_search_nodo(lista_ris, lista_selettore, i, lista_risultato):
    '''cerco tutti i tag a qualsiasi profondita.'''
    for nodo in lista_ris:
        for figlio in nodo.content:
            search_nodo(figlio, lista_selettore[i].tag, lista_selettore[i].diz, lista_risultato)

def conta_nodi(fileIn, selettore):
    '''torna il numero di nodi presenti in albero, che soddisfano il selettore css.'''    
    doc = fparse(fileIn)
    lista_selettore = modifica_selettore(selettore)
    lista_risultato = []
    lista_ris = []
    i = 0
    search_nodo(doc, lista_selettore[0].tag, lista_selettore[0].diz, lista_risultato)
    while i < len(lista_selettore):
        if i % 2 == 0:
            if lista_selettore[i-1] == '>':
                lista_ris = deepcopy(lista_risultato)
                lista_risultato = []
                conta_nodi_search_subnodo(lista_ris, lista_selettore, i, lista_risultato)
            elif lista_selettore[i-1] == '^':
                lista_ris = deepcopy(lista_risultato)
                lista_risultato = []
                conta_nodi_search_nodo(lista_ris, lista_selettore, i, lista_risultato)
        i += 1
    return len(lista_risultato)



def cancella_del(nodo, tag, diz, lista_figli, check):
    '''inserisco una x al tag da cancellare.'''
    if nodo.tag == tag or tag == '':
        if verifica_diz(nodo, diz) == 0:
            if check == True:
                nodo.tag = 'x'
            lista_figli += [nodo]

def cancella(nodo, tag, diz, lista_figli, check = False):
    '''cerco tutti i nodi da cancellare.'''
    if nodo.istext() == False:
        cancella_del(nodo, tag, diz, lista_figli, check)
        for child in nodo.content:
            cancella(child, tag, diz, lista_figli, check)
    return nodo

def cancella_sub(nodo, tag, diz, lista_figli, check = False, check_ric = False):
    '''cerco i figli che soddisfano le condizioni.'''
    if nodo.istext() == False:
        cancella_del(nodo, tag, diz, lista_figli, check)
        if check_ric == False:
            for child in nodo.content:
                cancella_sub(child, tag, diz, lista_figli, check, True)
    return nodo

import html
def to_string_mod(nodo):
    '''elimino tutti i tag che contengono la x.'''
    if nodo.istext():
        return html.escape(nodo.content,False)
    if nodo.tag != 'x':
        doc = nodo.open_tag()
        if nodo.closed:
            for child in nodo.content:
                if child.tag != 'x':
                    doc += to_string_mod(child)
            doc += nodo.close_tag()
        return doc

def elimina_nodi_cancellasubnodi(lista_figli, lista_selettore, i, lista_ap, check_mod):
    '''cerco i figli di un nodo.'''
    for figlio in lista_figli:
        cancella_sub(figlio, lista_selettore[i].tag, lista_selettore[i].diz, lista_ap, check_mod)            

def elimina_nodi_cancellanodi(lista_figli, lista_selettore, i, lista_ap, check_mod):
    '''cerco i nodi a qualsiasi profondita.'''
    for figlio in lista_figli:
        cancella(figlio, lista_selettore[i].tag, lista_selettore[i].diz, lista_ap, check_mod)

def elimina_nodi(fileIn, selettore, fileOut):
    '''elimina da albero tutti i nodi che soddisfano il selettore css (compreso il loro contenuto).'''
    doc = fparse(fileIn)
    lista_selettore = modifica_selettore(selettore)
    lista_figli = []
    check_mod = False
    i = 0
    if len(lista_selettore) == 1:
        cancella(doc, lista_selettore[0].tag, lista_selettore[0].diz, lista_figli, True)
    else:
        cancella(doc, lista_selettore[0].tag, lista_selettore[0].diz, lista_figli)
    while i < len(lista_selettore):
        if i == len(lista_selettore)-1:
            check_mod = True
        if i % 2 == 0:
            if lista_selettore[i-1] == '>':
                lista_ap = []
                elimina_nodi_cancellasubnodi(lista_figli, lista_selettore, i, lista_ap, check_mod)
                lista_figli = lista_ap    
            elif lista_selettore[i-1] == '^':
                lista_ap = []
                elimina_nodi_cancellanodi(lista_figli, lista_selettore, i, lista_ap, check_mod)
                lista_figli = lista_ap
        i += 1
    del_doc = to_string_mod(doc)
    file = open(fileOut, 'w', encoding='utf8')
    file.write(del_doc)



def modifica_mod(nodo, tag, diz, check, chiave, valore, lista_figli):
    '''modifico un nodo.'''
    if nodo.tag == tag or tag == '':
        if verifica_diz(nodo, diz) == 0:
            if check == True:
                nodo.attr[chiave] = valore
            lista_figli += [nodo]

def modifica(nodo, tag, diz, lista_figli, check = False, chiave = '', valore = ''):
    '''ricerco un nodo che soddisfa i requisiti.'''
    if nodo.istext() == False:
        modifica_mod(nodo, tag, diz, check, chiave, valore, lista_figli)
        for child in nodo.content:
            modifica(child, tag, diz, lista_figli, check, chiave, valore)
    return nodo

def modifica_sub(nodo, tag, diz, lista_figli, check = False, check_ric = False, chiave = '', valore = ''):
    '''cerco tutti i figli che soddisfano i requisiti.'''
    if nodo.istext() == False:
        modifica_mod(nodo, tag, diz, check, chiave, valore, lista_figli)
        if check_ric == False:
            for child in nodo.content:
                modifica_sub(child, tag, diz, lista_figli, check, True, chiave, valore)
    return nodo

def cambia_attributo_norm(lista_figli, lista_selettore, i, lista_ap, check_mod, chiave, valore):
    '''controllo tutti i nodi a qualsiasi profondita.'''
    for figlio in lista_figli:
        modifica_sub(figlio, lista_selettore[i].tag, lista_selettore[i].diz, lista_ap, check_mod, chiave, valore)

def cambia_attributo_sub(lista_figli, lista_selettore, i, lista_ap, check_mod, chiave, valore):
    '''controllo unicamente i nodi figli.'''
    for figlio in lista_figli:
        modifica(figlio, lista_selettore[i].tag, lista_selettore[i].diz, lista_ap, check_mod, chiave, valore)

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''modifica tutti i nodi presenti in albero che soddisfano il selettore css.'''
    doc = fparse(fileIn)
    lista_selettore = modifica_selettore(selettore)
    lista_figli = []
    check_mod = False
    i = 0
    if len(lista_selettore) == 1:
        modifica(doc, lista_selettore[0].tag, lista_selettore[0].diz, lista_figli, True, chiave, valore)
    else:
        modifica(doc, lista_selettore[0].tag, lista_selettore[0].diz, lista_figli)
    while i < len(lista_selettore):
        if i == len(lista_selettore)-1:
            check_mod = True
        if i % 2 == 0:
            if lista_selettore[i-1] == '>':
                lista_ap = []
                cambia_attributo_norm(lista_figli, lista_selettore, i, lista_ap, check_mod, chiave, valore)
                lista_figli = lista_ap    
            elif lista_selettore[i-1] == '^':
                lista_ap = []
                cambia_attributo_sub(lista_figli, lista_selettore, i, lista_ap, check_mod, chiave, valore)
                lista_figli = lista_ap
        i += 1
    file = open(fileOut, 'w', encoding='utf8')
    file.write(doc.to_string())