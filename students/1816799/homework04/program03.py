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
import html
from  my_html import HTMLNode, fparse
import re

def conta_nodi(fileIn, selettore):

    node=fparse(fileIn)
    christmas_tree(node)
    CSS_sel=re.split(' (?!>)', selettore)
    lst_node=[]
    i=0
    while i<=len(CSS_sel):

        if CSS_sel[i][-1]=='>':

            if find_selector(node, CSS_sel[i], lst_node)==find_son(node, CSS_sel[i], lst_node):

                lst=find_selector(node, CSS_sel[i], lst_node)
                i+=2

        else:

            lst=find_selector(node, CSS_sel[i], lst_node)
            i+=1

    return len(lst_node)

def christmas_tree(nodo):

    if type(nodo)==str: return
    for el in nodo.content:

        christmas_tree(el)

    return

def find_selector(node, sel, lst):

    ls=[]
    if sel[0]=='.' or sel[0]=='#': lst+=find_point_ashtag(node, sel, lst)
    elif sel[0]=='@':

        sel=re.findall('\w+', sel)
        lst+=find_at(node, sel, lst)

    else: lst+=find_tag(node, sel, ls)

    return lst

def find_tag(node, word, lst):

    for el in node:

        if type(node)!=str and word==el.tag: lst.append(el)

    for el in node.content: find_tag(el, word, lst)
    return

def find_point_ashtag(node, word, lst):

    for el in node:

        if type(node)!=str and word in el.attr: lst.append(el)

    for el in node.content: find_point_ashtag(el, word, lst)
    return

def find_at(node, word, lst):

    for el in node:

        if type(node)!=str and word[0] in node.attr and word[1]==node.attr[0]: lst.append(el)

    for el in node.content: find_at(el, word, lst)
    return

def find_son(node, word, lst):

    for i in node:

        for el in i.content:

            if word==el.tag: lst.append(el)

    return lst

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice

if __name__=='__main__':

    conta_nodi('slashdot.html','@[id="slashboxes"] > article h2 > a')
