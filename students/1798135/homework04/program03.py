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

def controllo(nodo,lista,Figlio=False):
	ris=False
	if not nodo.istext():
		if lista[0].isalpha():
			if lista[0]==nodo.tag:
				if len(lista) >1:
					lista2=lista[1:]
					for figli in nodo.content:
						ris=controllo(figli,lista2,True)
						if ris:
							return True
				else:
					return True
			else:
				pass
		elif lista[0][0]==".":
			a=nodo.attr
			chk=a.get("class")
			if chk==None:
				return False
			if lista[0][1:] in chk:
				if len(lista) >1:
					lista2=lista[1:]
					for figli in nodo.content:
						ris=controllo(figli,lista2,True)
						if ris:
							return True
				else:
					return True
			else:
				pass

		elif lista[0][0]=="#":
			a=nodo.attr
			chk=a.get("id")
			if chk==None:
				pass
			if lista[0][1:] == chk:
				if len(lista) >1:
					lista2=lista[1:]
					for figli in nodo.content:
						ris=controllo(figli,lista2,True)
						if ris:
							return True
				else:
					return True
			else:
				pass
		elif lista[0][0]=="@":
			a=nodo.attr
			appoggio=lista[0].split("=")
			chk=a.get(appoggio[0][2:])
			if chk==None:
				return False
			#print(chk ,"chk---controllo",appoggio[1][:-2])
			if appoggio[1][1:-2] == chk:
				if len(lista) >1:
					lista2=lista[1:]
					for figli in nodo.content:
						ris=controllo(figli,lista2,True)
						if ris:
							return True
				else:
					return True
			else:
				pass
		elif lista[0]==">":
			lista2=lista[1:]
			ris=controllo(nodo,lista2)
			if ris:
				return True
			elif ris==False:
				return False		
		if Figlio:
			for x in nodo.content:
				if not x.istext():
					ris=controllo(x,lista,True)
					if ris:
						return True
		return False


def conta(nodo,lista):
	c=0
	for x in nodo.content:
		if not x.istext():			
			trovato=controllo(x,lista)
			if trovato:
				c+=1
			c+=conta(x,lista)
	return c


def conta_nodi(fileIn, selettore):
	radice=fparse(fileIn)
	selettore=selettore.split()
	c=conta(radice,selettore)
	return c

def cancella(nodo,selettore):
			#print(nodo. tag," in corso  ", nodo.attr,"  ", selettore)
			ris=[]
			if len(selettore)>1:
				if controllo(nodo,selettore):
					lista2=selettore[1:]
					if lista2[0]==">":
						lista2=lista2[1:]
					for x in nodo.content:
						if not x.istext():
							ris=ris+cancella(x,lista2)
					return ris


			elif len(selettore)==1:
				if controllo(nodo,selettore):
					ris.append(nodo)
				else:
					for x in nodo.content:
						if not x.istext():
							ris=cancella(x,selettore)
			return ris

def elimina(nodo,selettore):
		l=[]
		c=[]
		ris=controllo(nodo,selettore)
		if ris:
			c.append(nodo)
		if c:
			pass
		for x in nodo.content:
			if not x.istext():
				#if controllo(x,selettore):
				l=l+c
				l=l+elimina(x,selettore)

		return l

def c_v(origine,l_e):	
	for canc in l_e:
		if canc in origine.content:
			origine. content.remove(canc)
		else:
			for x in origine.content:
				if not x.istext():
					c_v(x,l_e)

					
def elimina_nodi(fileIn, selettore, fileOut):
	radice=fparse(fileIn)
	selettore=selettore.split()
	l=elimina(radice,selettore)	
	ll=cancella(l[0],selettore)
	c_v(l[0],ll)
	save=radice.to_string()
	with open(fileOut,"w") as fout:
		fout.write(save)

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
	radice=fparse(fileIn)
	selettore=selettore.split()
	l=elimina(radice,selettore)
	ll=cancella(l[0],selettore)
	c_c(l[0],ll,chiave,valore)
	save=radice.to_string()
	with open(fileOut,"w") as fout:
		fout.write(save)


def c_c(origine,l_e,chiave, valore):
	for canc in l_e:
		if canc in origine.content:
			for x in origine.content:
				if x==canc:
					x.attr[chiave]=valore
		else:
			for x in origine.content:
				if not x.istext():
					c_c(x,l_e,chiave, valore)
