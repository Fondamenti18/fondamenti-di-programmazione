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
        seleziona un qualsiasi tag che ha  id="main_window"
        e' il figlio di un tag che ha   class="... class1 ..."
        e si trova all'interno (a qualsiasi livello di distanza) di un tag  div
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

'''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
def conta_nodi(fileIn, selettore):
    doc = load(fileIn)
    selettore = get_selector(selettore)
    counter = _conta_nodi(doc.content,selettore,0)
    return counter

def _conta_nodi(figli,selettore,counter):
    for child in figli:
        if(is_present(selettore,child)):
            counter+=1
        if not child.istext():
            counter = _conta_nodi(child.content,selettore,counter)
    return counter

def is_present(selettore,child):
    if(selettore[0] == 'attr'):
        key = selettore[1][0]
        value = selettore[1][1]
        for e in child.attr:
            if key == e:
                if value in child.attr[e]:
                    return True
    if(selettore[0] == 'tag'):
        if(selettore[1] == child.tag):return True
    if(selettore[0] == 'par'):
        for e in child.content:
            if(child.tag == selettore[1][0]):
                if(e.tag == selettore[1][1]):
                    return True
    return False


def get_selector(selettore):
    if '>' in selettore:
        return 'par',father_selector(selettore)
    elif '#' in selettore:
        return 'attr',['id',selettore[1:]]
    elif '.' in selettore:
        return 'attr',['class',selettore[1:]]
    elif '@' in selettore:
        return 'attr',img_selector(selettore)
    elif len(selettore) == 3 and selettore[1] == " ":
        return avo_selector(selettore)
    else:
        return 'tag',selettore

def avo_selector(selettore):
    return [selettore[0],selettore[2]]

def img_selector(selettore,i=0,key="",value=""):
    while not selettore[i].isalpha(): i += 1
    while selettore[i].isalpha():
        key += selettore[i]
        i += 1
    i = selettore.find('"')+1
    while(selettore[i].isdigit()):
        value+=selettore[i]
        i+=1
    return [key,value]

def father_selector(str):
    lst = []
    i = str.find(" ")
    lst.append(str[:i])
    i = str.find('>')+2
    lst.append(str[i:])
    return lst

def elimina_nodi(fileIn, selettore, fileOut):
    doc = load(fileIn)
    selettore = get_selector(selettore)
    nodi = _get_nodi(doc,selettore[0])
    kill = None
    for e in nodi:
        if(_kill_nodi(selettore[1],e)):
            kill = e
    tree= HTMLNode(doc.tag,doc.attr,doc.content,doc.closed)
    my_file = _elimina_nodi(kill,doc)
    print(my_file.print_tree())
    f = open(fileOut,'w')
    f.write(my_file)
    f.close()

def _elimina_nodi(kill,doc,my_index=0):
    i = 0
    for child in doc.content:
        i+=1
        if child.tag != kill.tag and child.content != kill.content:
            my_index = i
        elif(not child.istext()):
            _elimina_nodi(kill,doc)
    if(my_index > 0):
        doc.content.remove(doc.content[my_index-1])
        return doc

def _kill_nodi(a,tree,lst=[]):
    for child in tree.content:
        if a == child.tag:
            return True
        if (not child.istext()):
            return _kill_nodi(a,child)

def _get_nodi(doc,avo,lst=[]):
    for child in doc.content:
        if(child.tag == avo):
            lst.append(child)
        if(not child.istext()):
            lst = _get_nodi(child,avo,lst)
    return lst


def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    doc = load(fileIn)
    selettore = get_selector(selettore)
    nodi = _get_nodi(doc,selettore[0])
    kill = None
    for e in nodi:
        if(_kill_nodi(selettore[1],e)):
            kill = e
    my_file = _cambia_attributo(kill,doc,chiave,valore)
    f = open(fileOut,'w')
    f.write(my_file)
    f.close()

def _cambia_attributo(kill,doc,chiave,valore):
    i = 0
    for child in doc.content:
        i+=1
        if child.tag != kill.tag and child.content != kill.content:
            my_index = i
        elif(not child.istext()):
            _cambia_attributo(kill,doc)
    if(my_index > 0):
        doc.content.remove(doc.content[my_index-1])
        return doc

def load(fileIn):
    global my_file,main
    if main != None and my_file == fileIn: return main
    else:
        my_file = fileIn
        main = fparse(fileIn)
    return main

my_file = None
main = None