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
from  my_html import HTMLNode, fparse, _MyHTMLParser
import copy
def conta_nodi(fileIn, selettore):
	cont=0
	lst=[]
	n=0
	doc=fparse(fileIn)
	cont=cont_ric(doc,selettore,cont,lst,n)
	return cont
	
def cont_ric(d,sel,cont,lst,n):
	if sel[0]=='#':
		if 'id' in d.attr.keys():
			if d.attr['id']==sel[1:]:
				cont+=1
	elif sel==d.tag:
		cont+=1
	elif sel[0]=='.':
		if 'class' in d.attr.keys():
			if sel[1:] in d.attr['class']:
				cont+=1
	elif sel[0]=='@':
		sel_app=''
		if sel_app=='':
			sel_app=sel.replace('@','')
			sel_app=sel_app.replace('[','')
			sel_app=sel_app.replace(']','')
			sel_app=sel_app.split('=')
			sel_app[1]=sel_app[1].replace('"','')
		if sel_app[0] in d.attr.keys() and d.attr[sel_app[0]]==sel_app[1]:
			cont+=1
	elif ' ' in sel:
		if '>' in sel:
			sel_app=''
			if sel_app=='':
				sel_app=sel.replace(' ','')
				sel_app=sel_app.replace('>','')
			lst.append(d.tag)
			n+=1
			if n>0:
				if lst[n-1]+d.tag==sel_app:
					cont+=1
		else:
			sel_app=''
			if sel_app=='':
				sel_app=sel.replace(' ','')
			lst.append(d.tag)
			n+=1
			if n>0:
				for x in lst:
					if x+d.tag==sel_app:
						cont+=1
						break
	for figlio in d.content:
		if type(figlio.content) is list:
			cont=cont_ric(figlio,sel,cont,lst,n)
	return cont
		
def elimina_nodi(fileIn, selettore, fileOut):
	doc=fparse(fileIn)
	bol=False
	remove_by_tag(doc,selettore,bol)
	with open(fileOut,'w',encoding='utf-8') as f:
		f.write(doc.to_string())

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
	doc=fparse(fileIn)
	bol=False
	modify_by_tag(doc,selettore,chiave,valore,bol)
	with open(fileOut,'w' ,encoding='utf-8') as f:
		f.write(doc.to_string())

def remove_by_tag(node,tag,bol):
	sel_tag=[]
	newcont=[]
	n=0
	if ' ' in tag:
		sel_tag=tag.split(' ')
		if node.istext():return 
		for child in node.content:
			if node.tag==sel_tag[0] or bol==True:
				bol=True
				if child.tag==sel_tag[1]:
					del node.content[n]
				n+=1
			if type(child.content) is list:
				remove_by_tag(child,tag,bol)
	elif '>' in tag:
		sel_tag=tag.split('>')
		if node.istext():return 
		for child in node.content:
			if node.tag==sel_tag[0]:
				if child.tag==sel_tag[1]:
					del node.content[n]
				n+=1
			if type(child.content) is list:
				remove_by_tag(child,tag,bol)
	else:
		if node.istext():return 
		for child in node.content:
			if child.tag==tag:
				del node.content[n]
			n+=1
			if type(child.content) is list:
				remove_by_tag(child,tag,bol)
				
def modify_by_tag(node,tag,chiave,valore,bol):
	sel_tag=[]
	if tag[0]=='#':
		if node.istext():return 
		for child in node.content:
			if 'id' in child.attr.keys():
				if child.attr['id']==tag[1:]:
					child.attr[chiave]=valore
			if type(child.content) is list:
				modify_by_tag(child,tag,chiave,valore,bol)
	if ' ' in tag:
		sel_tag=tag.split(' ')
		if node.istext():return 
		for child in node.content:
			if node.tag==sel_tag[0] or bol==True:
				bol=True
				if child.tag==sel_tag[1]:
					child.attr[chiave]=valore
			if type(child.content) is list:
				modify_by_tag(child,tag,chiave,valore,bol)
	elif '>' in tag:
		sel_tag=tag.split('>')
		if node.istext():return 
		for child in node.content:
			if node.tag==sel_tag[0]:
				if child.tag==sel_tag[1]:
					child.attr[chiave]=valore
			if type(child.content) is list:
				modify_by_tag(child,tag,chiave,valore,bol)
	else:
		if node.istext():return 
		for child in node.content:
			if child.tag==tag:
				child.attr[chiave]=valore
			if type(child.content) is list:
				modify_by_tag(child,tag,chiave,valore,bol)