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

cont1 = 0

def conta_nodi(fileIn, selettore):
	'''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
	global cont1
	cont1 = 0
	tree = fparse(fileIn)
	ricorsione_nodi(tree, selettore, ' ')
	return cont1

def ricorsione_nodi(tree, sel, mod) :
	global cont1
	l = sel.split(' ', 1)
	m = []
	cerca(tree, l[0], mod, m)
	if len(l) == 1 :
		if len(m) > 0 :
			cont1 += len(m)
		return
	mod = ' ',
	j = 0
	if l[1][0] == '>' :
		mod = '>'
		j += 2
	for i in m :
		ricorsione_nodi(i, l[1][j:], mod)

def cerca(tree, sel, mod, m) :
	if mod == '>' :
		controlla(tree, sel, m)
		for child in tree.content :
			controlla(child, sel, m)

	else :
		if tree.tag is '_text_' :
			return 
		controlla(tree, sel, m)
		for child in tree.content :
			cerca(child, sel, mod, m)

def controlla(tree, sel, m) :
	if sel[0] == '.' :
		if 'class' in tree.attr.keys() and sel[1 :] in tree.attr['class']:
			m.append(tree)
	elif sel[0] == '#' :
		if 'id' in tree.attr.keys() and tree.attr['id'] == sel[1 :] :
			m.append(tree)
	elif sel[0] == '@' :
		i = sel.index('=')
		if sel[2 : i] in tree.attr.keys() and tree.attr[sel[2 : i]] == sel[i + 2 : len(sel) - 2] :
			m.append(tree)
	else :
		if tree.tag == sel :
			m.append(tree)


def elimina_nodi(fileIn, selettore, fileOut):
	'''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
	

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
	'''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
	#Inserite qui il vostro codice

