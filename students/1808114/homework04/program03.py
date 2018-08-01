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

def conta(nodo, selettore):
    lista = []
    if not nodo.istext():
        if selettore[0] == 'tag' and selettore[1] == nodo.tag:
            return [nodo]
        elif selettore[0] in list(nodo.attr.keys()) and selettore[1] in nodo.attr[selettore[0]]:
            return [nodo]
        for child in nodo.content:
            lista += conta(child, selettore)
    return lista

def conta_figli(lista_nodi, selettore):
    lista = []
    for x in lista_nodi:
        if not x.istext():
            if selettore[0] == 'tag' and selettore[1] == x.tag:
                lista += [x]
            elif selettore[0] in list(x.attr.keys()) and selettore[1] in x.attr[selettore[0]]:
                lista += [x]
    return lista

def esplicita_selettore(selettore):
    pr = selettore[0]
    if pr == '.':
        return 'class', selettore[1:]
    elif pr == '#':
        return 'id', selettore[1:]
    elif pr == '@':
        selettore = selettore[2:len(selettore)-1].replace('\"','').split('=')
        return selettore[0],selettore[1]
    else:
        return 'tag', selettore

def normalizza_selettore(selettore):
    lista = []
    while True:
        n = selettore.find(' ')
        if n != -1:
            if '>' not in [selettore[n-1],selettore[n+1]]:
                lista.append(selettore[:n])
                selettore = selettore[n+1:]
            else:
                selettore = selettore.replace(' ', '', 2)
        else:
            break
    lista.append(selettore)
    for x in range(len(lista)):
        lista[x] = lista[x].split('>')
    for y in range(len(lista)):
        for x in range(len(lista[y])):
            lista[y][x] = esplicita_selettore(lista[y][x])
    return lista

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    #Inserite qui il vostro codice
    a = fparse(fileIn)
    lista_nodi = [a]
    lista_sel = normalizza_selettore(selettore)
    for y in range(len(lista_sel)):
        lista_conta = []
        for z in range(len(lista_nodi)):
            lista_conta += conta(lista_nodi[z], lista_sel[y][0])
        if len(lista_sel[y]) > 1:
            lista_nodi = lista_conta[:]
            lista_conta = []
            for x in range(1, len(lista_sel[y])):
                for z in range(len(lista_nodi)):
                    lista_conta += conta_figli(lista_nodi[z].content, lista_sel[y][x])
        lista_nodi = lista_conta[:]
    return len(lista_nodi)

def elimina(nodo, eliminare):
    if not nodo.istext():
        if eliminare in nodo.content:
            del nodo.content[nodo.content.index(eliminare)]
            return
        else:
            for child in nodo.content:
                elimina(child, eliminare)
    return

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice
    a = fparse(fileIn)
    lista_nodi = [a]
    lista_sel = normalizza_selettore(selettore)
    for y in range(len(lista_sel)):
        lista_conta = []
        for z in range(len(lista_nodi)):
            lista_conta += conta(lista_nodi[z], lista_sel[y][0])
        if len(lista_sel[y]) > 1:
            lista_nodi = lista_conta[:]
            lista_conta = []
            for x in range(1, len(lista_sel[y])):
                for z in range(len(lista_nodi)):
                    lista_conta += conta_figli(lista_nodi[z].content, lista_sel[y][x])
        lista_nodi = lista_conta[:]
    for x in lista_nodi:
        elimina(a, x)

    with open(fileOut, 'w', encoding = 'utf-8') as out:
        out.write(a.to_string())
    return

def modifica(nodo, chiave, valore):
    if not nodo.istext():
        nodo.attr[chiave] = valore
    return nodo

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
    a = fparse(fileIn)
    lista_nodi = [a]
    lista_sel = normalizza_selettore(selettore)
    for y in range(len(lista_sel)):
        lista_conta = []
        for z in range(len(lista_nodi)):
            lista_conta += conta(lista_nodi[z], lista_sel[y][0])
        if len(lista_sel[y]) > 1:
            lista_nodi = lista_conta[:]
            lista_conta = []
            for x in range(1, len(lista_sel[y])):
                for z in range(len(lista_nodi)):
                    lista_conta += conta_figli(lista_nodi[z].content, lista_sel[y][x])
        lista_nodi = lista_conta[:]
    for x in lista_nodi:
        x = modifica(x, chiave, valore)
    with open(fileOut, 'w', encoding = 'utf-8') as out:
        out.write(a.to_string())
    return