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


def stampa(file):
    if file.istext():
        pass
    else:
        print(file.tag)
        for child in file.content:
            stampa(child)


################################################# PRIMA FUNZIONE

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    file = fparse(fileIn)
    selettore = riconoscimento_selettore(selettore)
    if len(selettore) == 1:
        return ricerca_avo(file, [' '+selettore[0]])
    return conta(file, selettore)
    
                
def riconoscimento_selettore(selettore):
    l = selettore.split('>')
    temp = []
    for i in range(len(l)):
        l[i] = l[i].strip()
    for i in range(len(l)):
        if ' ' in l[i]:
            l1 = l[i].split()
            temp += [l1[0]] + ['%' + l1[1]]
        else:
            temp += [l[i]]
    return temp

def isfiglio(file, selettore):
    if selettore[0][0] == '#':
        return isattributo(file, selettore[0][1:], 'id')
    elif selettore[0][0] == '.':
        return isattributo(file, selettore[0][1:], 'class')
    elif selettore[0][0] == '@':
        temp = selettore[0].split('=')
        return isattributo(file, temp[1][1:len(temp[1])-2], temp[0][2:])
    elif len(selettore[0]) > 1 and selettore[0][1] == '#':
        return isattributo(file, selettore[0][2:], 'id')
    elif len(selettore[0]) > 1 and selettore[0][1] == '.':
        return isattributo(file, selettore[0][2:], 'class')
    elif len(selettore[0]) > 1 and selettore[0][1] == '@':
        temp = selettore[0].split('=')
        return isattributo(file, temp[0][3:], temp[1][1:len(temp[1])-2])
    elif selettore[0][0] == '%':
        return istag(file, selettore[0][1:])
    else:
        return istag(file, selettore[0])
    
def isattributo(file, selettore, attributo):
    if attributo in file.attr and selettore in file.attr[attributo]:
        return True
    else:
        return False
    
def istag(file, selettore):
    if file.tag == selettore:
        return True
    else:
        return False
            
def ricerca_figlio(file, selettore):
    if selettore[0][0] == '#':
        return attributo_figlio(file, selettore[0][1:], 'id')
    elif selettore[0][0] == '.':
        return attributo_figlio(file, selettore[0][1:], 'class')
    elif selettore[0][0] == '@':
        temp = selettore[0].split('=')
        return attributo_figlio(file, temp[1][1:len(temp[1])-2], temp[0][2:])
    else:
        return figlio_tag(file, selettore[0])
        
def attributo_figlio(file, selettore, attributo):
    for child in file.content:
        if not child.istext():
            if attributo in child.attr and selettore in child.attr[attributo]:
                return 1
    return 0

def figlio_tag(file, selettore):
    for child in file.content:
        if not child.istext():
            if child.tag == selettore:
                return 1
    return 0

def ricerca_avo(file, selettore):
    if selettore[0][1] == '#':
        return attributo_avo(file, selettore[0][2:], 'id')
    elif selettore[0][1] == '.':
        return attributo_avo(file, selettore[0][2:], 'class')
    elif selettore[0][1] == '@':
        temp = selettore[0].split('=')
        return attributo_avo(file, temp[1][1:len(temp[1])-2], temp[0][3:])
    else:
        return avo_tag(file, selettore[0][1:])
        
def attributo_avo(file, selettore, attributo):
    i = 0
    for child in file.content:
        if not child.istext():
            if attributo in child.attr and selettore in child.attr[attributo]:
                i += 1
            i += attributo_avo(child, selettore, attributo)
    return i

def avo_tag(file, selettore):
    i = 0
    for child in file.content:
        if not child.istext():
            if child.tag == selettore:
                i += 1
            i += avo_tag(child, selettore)
    return i

def conta(file, selettore, livello = 0):
    i = 0
    if len(selettore) == 1 and selettore[0][0] == '%' and ricerca_avo(file, selettore):
        i += 1
    elif len(selettore) == 1 and ricerca_figlio(file, selettore):
        i += 1
    elif len(selettore) >= 1 and selettore[0][0] == '%':
        if ricerca_avo(file, selettore):
            for child in file.content:
                if not child.istext():
                    if isfiglio(child, selettore):
                        i += conta(child, selettore[1:])
                    else:
                        i += conta(child, selettore)
    elif len(selettore) >= 1:
        if ricerca_figlio(file, selettore):
            for child in file.content:
                if not child.istext():
                    if isfiglio(child, selettore):
                        i  += conta(child, selettore[1:], livello + 1)
        elif livello == 0:
            for child in file.content:
                if not child.istext():
                    if isfiglio(child, selettore):
                        i += conta(child, selettore[1:])
                    else:
                        i += conta(child, selettore)
    return i

################################################# SECONDA FUNZIONE

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    file = fparse(fileIn)
    selettore = riconoscimento_selettore(selettore)
    radice = []
    cerca_radice(file, radice, selettore)
    selettore = selettore[1:]
    for nodo in radice:
        cancella(nodo, selettore)
    eliminazione(file)
    salva(file, fileOut)

def salva(file, fileOut):
    with open(fileOut, 'w', encoding = 'utf-8') as f:
        f.write(file.to_string())
    
def cerca_radice(file, radice, selettore):
    for child in file.content:
        if not child.istext():
            if isfiglio(child, selettore):
                radice += [child]
            cerca_radice(child, radice, selettore)
    
def cancella(nodo, selettore):
    if len(selettore) == 0:
        nodo.content = 'elimina'
    elif selettore [0][0] == '%':
        if ricerca_avo(nodo, selettore):
            for child in nodo.content:
                if not child.istext():    
                    if isfiglio(child, selettore):
                        cancella(child, selettore[1:])
                    else:
                        cancella(child, selettore)
    else:
        if ricerca_figlio(nodo, selettore):
            for child in nodo.content:
                if not child.istext():
                    if isfiglio(child, selettore):
                        cancella(child, selettore[1:])
                    else:
                        cancella(child, selettore)
            
def eliminazione(file):
    for child in file.content:
        if not child.istext():
            if child.content == 'elimina':
                del file.content[file.content.index(child)]
            else:
                eliminazione(child)
    
    
################################################# TERZA FUNZIONE

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    file = fparse(fileIn)
    selettore = riconoscimento_selettore(selettore)
    radice = []
    cerca_radice(file, radice, selettore)
    selettore = selettore[1:]
    for nodo in radice:
        cambia(nodo, selettore, chiave, valore)
    salva(file, fileOut)
    
    
def cambia(nodo, selettore, chiave, valore):
    if len(selettore) == 0:
        nodo.attr[chiave] = valore
    elif selettore [0][0] == '%':
        if ricerca_avo(nodo, selettore):
            for child in nodo.content:
                if not child.istext():    
                    if isfiglio(child, selettore):
                        cambia(child, selettore[1:], chiave, valore)
                    else:
                        cambia(child, selettore, chiave, valore)
    else:
        if ricerca_figlio(nodo, selettore):
            for child in nodo.content:
                if not child.istext():
                    if isfiglio(child, selettore):
                        cambia(child, selettore[1:], chiave, valore)
                    else:
                        cambia(child, selettore, chiave, valore)
    

