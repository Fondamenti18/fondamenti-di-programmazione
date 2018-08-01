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

def conta_nodi(fileIn, selettore):
	doc=fparse(fileIn)
	#doc.print_tree()
	#print(doc.to_string())
	dicpf=dict()
	dicpf=trovapf(doc)
	for k in dicpf.keys():
		#print(k,len(dicpf[k]))
		sel=list()
	sel=selettore.split(' ')
	#print(sel)
	n=0
	count=0
	relpf=False
	dictrovati=dict()
	appodic=dict()
	while n<len(sel):
		if sel[n]=='>':
			relpf=True
			continue
		else:
			if n==0:
				if '#' in sel[n]:
					#print('Se',sel[n][1:])
					appodic=trovaid(sel[n][1:],dicpf,doc,False)
					#print('Appodic',appodic)
				else: appodic=trovatag(sel[n],dicpf,doc,False)
			else:
				if relpf==True:
					relpf=False
				if '#' in sel[n]:
					#print('Se',sel[n][1:])
					appodic=trovaid(sel[n][1:],dicpf,doc,False)
					#print('Appodic',appodic)
				else: appodic=trovatag(sel[n],dicpf,doc,False)
		cance=list()
		for l in appodic:
			if appodic[l]==False: cance.append(l)
		for i in range(len(cance)):
			del appodic[cance[i]]
		n+=1
	for l in appodic:
		#print('L',l)
		if appodic[l]==True: count+=1
	rel=False
	return count

	'''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
	#Inserite qui il vostro codice

def trovaid(id,dicpf,node,pf):
	dic=dict()
	if pf==True:
		for l in dicpf[node]:
			if l.attr!=None:
				#print('Eccomi',l.attr)
				dic[l]=True
			else:
				dic[l]=False
	else:
		#if node.attr!={}: #print('LOL',node.attr)
		if node.attr!={} and 'id' in node.attr.keys():
			#print('Sono qui!',node.attr)
			if node.attr['id']==id: dic[node]=True
			else: dic[node]=False
		if node.istext()==False:
			for l in dicpf[node]:
				#print(dicpf[node])
				#print('LAL',l.to_string())
				dic.update(trovaid(id,dicpf,l,False))
	#print('Cic',dic)
	return dic

def trovatag(tg,dicpf,node,pf):
	dic=dict()
	if pf==True:
		for l in dicpf[node]:
			if l.tag!='_text_':
				##print('Eccomi',l.attr)
				dic[l]=True
			else:
				dic[l]=False
	else:
		#if node.attr!={}: #print('LOL',node.attr)
		if node.tag==tg:
			#print('Sono qui!',node.attr)
			dic[node]=True
		else: dic[node]=False
		if node.istext()==False:
			for l in dicpf[node]:
				#print(dicpf[node])
				#print('LAL',l.to_string())
				dic.update(trovatag(tg,dicpf,l,False))
	#print('Cic',dic)
	return dic

	
def trovapf(node):
	dic=dict()
	if node.istext()==False:
		dic[node]=node.content
		for l in dic[node]:
			#print(l)
			dic.update(trovapf(l))
			#print(l)
	return dic
	
def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice

