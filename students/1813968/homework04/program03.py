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
import string

cont=0
file=""
tipo=""
parola=[]

def conta_nodi(fileIn, selettore):
	global file,cont
	cont=0
	file=""
	file=fparse(fileIn)
	controllo_selettore(selettore)
	conta(file)
	return cont
	

def controllo_selettore(selettore):
	global parola,tipo,file
	parola2=""
	punteggiatura="@#."
	parola=[]
	tipo=""
	c=False
	for i in selettore:
		if i in punteggiatura:
			if c==False:
				tipo=i
				c=True
		elif i==" " and parola2!="" or i=="=":
			parola.append(parola2)
			parola2=""
		elif not i in string.punctuation:
			parola2+=i
	parola.append(parola2)
	if tipo=="" and len(parola)!=1:
		tipo="p"
	
def conta(file):
	global cont
	for i in file.content:
		if not i.istext():
			if (tipo=="" or tipo==".") and (parola[0] in i.attr.keys() or parola[0] in i.tag):
				cont+=1
			elif tipo=="#" and "id" in i.attr.keys():
				if i.attr["id"]==parola[0]:
					cont+=1
			elif tipo=="@" and parola[0] in i.attr.keys() and parola[1] in i.attr.values():
				cont+=1
			elif tipo=="p" and parola[0]==i.tag and parola[1]==i.content:
				cont+=1
			conta(i)
	
			
def elimina_nodi(fileIn, selettore, fileOut):
    global file
	

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
	global file
