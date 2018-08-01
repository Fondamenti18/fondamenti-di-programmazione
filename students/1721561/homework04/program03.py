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

def count(node):
	'''Ritorna il numero di nodi dell'albero di questo nodo'''
	cnt = 1
	if not node.istext():
		for child in node.content:
			cnt += count(child)
	return cnt

def height(node):
	'''Ritorna l'altezza dell'albero con radice questo nodo, cioè il massimo numero di nodi in un cammino radice-foglia'''
	h = 1
	if not node.istext():
		for child in node.content:
			h = max(h, height(child) + 1)
	return h

def find_by_tag(node, tag):
	'''Ritorna una lista dei nodi che hanno il tag'''
	ret = []
	if node.tag == tag: 
		ret += [node]
	if not node.istext():
		for child in node.content:
			ret += find_by_tag(child,tag)
	return ret

def remove_by_tag(node, tag):
	'''Rimuove dall'albero tutti i nodi con il tag, esclusa la radice, cioè il nodo su cui è invocato il metodo.'''
	if node.istext(): 
		return
	for child in node.content:
		remove_by_tag(child,tag)
	newcont = []
	for child in node.content:
		if child.tag == tag:
			if not child.istext():
				newcont += child.content
		else:
			newcont += [child]
	node.content = newcont

def print_recursively(doc):
	print(doc.tag)
	print(doc.attr)
	print(doc.content)
	print(doc.closed)
	print("\n")
	for node in doc.content:
		if not node.istext():
			print_recursively(node)

def conta_nodi(fileIn, selettore):
	'''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
	#Inserite qui il vostro codice
	doc = fparse(fileIn)
	print_recursively(doc)

#def elimina_nodi(fileIn, selettore, fileOut):
#    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
#    #Inserite qui il vostro codice
#
#def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
#    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
#    #Inserite qui il vostro codice

conta_nodi('page1-3.html', 'p a')