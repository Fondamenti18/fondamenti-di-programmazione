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

def tipologia(selettore):
    if len(selettore.split(' ')) > 1:
        if '>' in selettore:
            tipo = 'pf'
            padre = ''
            figlio = ''
            for i in selettore:
                if i == ' ':
                    break
                padre += i
            for i in selettore[::-1]:
                if i == ' ':
                    break
                figlio += i
            figlio = figlio[::-1]
            return padre,figlio,tipo
        else:
            tipo = 'ad'
            avo = ''
            discendente = ''
            for i in selettore:
                if i == ' ':
                    break
                avo += i
            for i in selettore[::-1]:
                if i == ' ':
                    break
                discendente += i
            discendente = discendente[::-1]
            return avo,discendente,tipo
    else:
        if selettore[0] == '#': 
            sel = selettore[1:]
            tipo = 'id'
        elif selettore[0] == '.':
            sel = selettore[1:]
            tipo = 'class'
        elif selettore[0] == '@':
            sel = selettore[2:-1]
            sel = sel.replace('"','')
            tipo,sel = sel.split('=')[0],sel.split('=')[1]
        else:
            sel = selettore
            tipo = 'tag'
        return sel,tipo

def conta(sel, diz, tipo, x = -1):
    contatore = 0
    x += 1
    if tipo == 'tag':
        if x < len(diz):
            if diz[x] == sel:
                contatore += 1
            contatore += conta(sel,diz,tipo,x)
        return contatore
    if x < len(diz.keys()):
        if sel in diz[list(diz.keys())[x]] and list(diz.keys())[x] == tipo : 
            contatore += 1
        contatore += conta(sel,diz,tipo,x)
    return contatore


def padrefiglio(padre, figlio, lista):
    contatore = 0
    if lista == []:
        return contatore
    if str(type(lista)) == "<class 'my_html.HTMLNode'>":
        if lista.tag == padre:
            if lista.content[0].tag == figlio:
                contatore += 1
            contatore += padrefiglio(padre, figlio, lista.content[1:])
    else:
        if lista[0].tag == figlio:
            contatore += 1
        contatore += padrefiglio(padre,figlio,lista[1:])
    return contatore

def cancellapf(padre, figlio, lista):
    if lista == []:
        return
    if str(type(lista)) == "<class 'my_html.HTMLNode'>":
        if lista.tag == padre:
            if lista.content[0].tag == figlio:
                del lista.content[0]
            cancellapf(padre,figlio, lista.content[1:])
    else:
        if lista[0].tag == figlio:
            del lista[0]
        cancellapf(padre,figlio,lista[1:])
    return 


def avodiscendente(avo, discendente, lista, salta = False):
    contatore = 0
    if lista.tag == '_text_':
        return contatore
    if lista.tag == avo or salta == True:
        salta = True
        for i in lista.content:
            if i.tag == discendente:
                contatore += 1
    for i in range(1,len(lista.content),2):
        contatore += avodiscendente(avo,discendente,lista.content[i],salta)
    return contatore

def cancellaav(avo, discendente, lista, salta = False):
    if lista.tag == '_text_':
        return 
    if lista.tag == avo or salta == True:
        salta = True
        for i in lista.content:
            if i.tag == discendente:
                del i
    for i in range(1,len(lista.content),2):
        cancellaav(avo,discendente,lista.content[i],salta)
    return 


def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    doc = fparse(fileIn)
    contatore = 0
    tipo = tipologia(selettore)
    if len(tipo) == 3:
        if tipo[2] == 'pf':
            padre = tipo[0]
            figlio = tipo[1]
            for i in range(1,len(doc.content[1].content),2):
                contatore += padrefiglio(padre,figlio,doc.content[1].content[i])
        else:
            avo = tipo[0]
            discendente = tipo[1]
            for i in range(1,len(doc.content[1].content),2):
                contatore += avodiscendente(avo,discendente,doc.content[1].content[i])
    else:
        if tipo[1] == 'tag':
            listatag = []
            for i in range(1,len(doc.content[1].content),2):
                listatag += [doc.content[1].content[i].tag]
            contatore += conta(tipo[0],listatag,tipo[1])
        else:
            for i in range(1,len(doc.content[1].content),2):
                contatore += conta(tipo[0],doc.content[1].content[i].attr,tipo[1])
    return contatore




def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    doc = fparse(fileIn)
    tipo = tipologia(selettore)
    if len(tipo) == 3:
        if tipo[2] == 'pf':
            padre = tipo[0]
            figlio = tipo[1]
            for i in range(1,len(doc.content[1].content),2):
                cancellapf(padre,figlio,doc.content[1].content[i])
        else:
            avo = tipo[0]
            discendente = tipo[1]
            for i in range(1,len(doc.content[1].content),2):
                cancellaav(avo,discendente,doc.content[1].content[i])
    else:
        if tipo[1] == 'tag':
            listatag = []
            for i in range(1,len(doc.content[1].content),2):
                listatag += [doc.content[1].content[i].tag]
            cancella(tipo[0],listatag,tipo[1])
        else:
            for i in range(1,len(doc.content[1].content),2):
                cancella(tipo[0],doc.content[1].content[i].attr,tipo[1])
    with open(fileOut,'w',encoding='utf-8') as f:
        f.write(doc.to_string())


def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
