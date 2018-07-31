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


def Tree(filein):
    root= fparse(filein)
    return root
    
def scomponi_selettori(selettore):
    L= []
    L = selettore.split()
    return L
    
def isFoglia(nodo):
    if nodo.content == []:
        return True
    else:
        return False
    
def isValidAttribute(nodo, attributo):
	print('VALID ATTRI NODO = ',nodo)
	print('VALID ATTRI = ',nodo.attr)
	print('DEVO CERCARE = ',attributo)
	print('............................................................')
	for a in nodo.attr.keys():
		print('cerco attributo        ----------------------------------> ',attributo)
		print('in    nodo.attr.get(a) ----------------------------------> ',nodo.attr.get(a))
		print('key   a                ----------------------------------> ',a)
		if '#' in attributo:
			attributo = attributo[1:]
		if '@' in attributo:
			print('								AT !!!!')
			if a in attributo:
				return True
		if '.' in attributo:
			attributo2 = attributo[1:]
			if attributo2 in nodo.attr.get(a):
				return True
		if attributo == nodo.attr.get(a):
			return True
	return False

def getValidChild(nodo, tag):
	valid = 0
	print('CHECKANDO DI VALIDARE TAG: ',tag)
	for t in nodo.content:
		print(' OOOO possibili figli -> ',t.tag)
		if t.tag == tag:
			print(' -------> TAG VALID 1 <-----------')
			valid+=1
	return valid

def getValidChildProfonda(nodo, tag):
	global count
	print('CHECKANDO DI VALIDARE TAG: ',tag)
	for t in nodo.content:
		print(' OOOO possibili figli -> ',t.tag)
		if t.tag == tag:
			print(' -------> TAG VALID 1 <-----------')
			count+=1
		else:
			if t.tag != '_text_':
				getValidChildProfonda(t, tag)
		
		
def findValidChildProfonda(nodo, tag):
	print('CHECKANDO DI VALIDARE TAG: ',tag)
	for t in nodo.content:
		print(' OOOO possibili figli -> ',t.tag)
		if t.tag == tag:
			print(' -------> TAG VALID 1 <-----------')
			return t
		else:
			if t.tag != '_text_':
				return getValidChildProfonda(t, tag)
	
def conta_multi_selettore(root, singoli,i):
	global count
	print('len SINGOLI = ',len(singoli),'                  current i = ',i)
	#if i > len(singoli):
	#	return count
	if i==len(singoli) and isValidAttribute(root,singoli[i]):
		count+= 1
	if i==len(singoli)-1:
		count += getValidChild(root,singoli[i])
	else:
		for figlio in root.content:
			print('esaminando tag: ',figlio.tag)
			if figlio.tag != '_text_' and i < len(singoli):
				if figlio.tag == singoli[i]:
					print('VAI SCAVAAAAAAAAAAAAA')

					conta_multi_selettore(figlio, singoli,i+2)
				else:
					conta_multi_selettore(figlio, singoli,i)
					
def conta_multi_selettore_complex(root, main, singoli,i):
	global count
	print('len SINGOLI = ',len(singoli),'                  current i = ',i)
	#if i > len(singoli):
	#	return count
	if(i!=0):
		if i==len(singoli) and isValidAttribute(root,singoli[i]):
			count+= 1
		if i==len(singoli)-1:
			#count += getValidChild(root,singoli[i])
			print('		Siamo alla frutta ROOT:       ',root.tag)
			print('		Siamo alla frutta singoli[i]: ',singoli[i])
			getValidChildProfonda(root,singoli[i])	
			print('COUNT = ',count)			
			#if singoli[i] == root.tag:
			#	count+=1
	else:
		for figlio in root.content:
			print('esaminando tag: ',figlio.tag)
			if figlio.tag != '_text_' and i < len(singoli):
				if i == 0 and figlio.tag == main:
					print('	------------------------------	M A I N  trovato')
					conta_multi_selettore_complex(figlio, main, singoli,i+1)
				if i!=0 and figlio.tag == singoli[i]:
					print('VAI SCAVAAAAAAAAAAAAA')
					conta_multi_selettore_complex(figlio,main, singoli,i+2)
				else:
					conta_multi_selettore_complex(figlio,main, singoli,i)
					
					

def changeAttributo(nodo, attributo, chiave, valore):
	print('VALID ATTRI NODO = ',nodo)
	print('VALID ATTRI = ',nodo.attr)
	print('DEVO CERCARE = ',attributo)
	print('............................................................')
	nodo.attr[key] = value

			
					
def cambia_multi_selettore_complex(root, main, singoli,i,chiave,valore):
	global count
	#print('len SINGOLI = ',len(singoli),'                  current i = ',i)
	#if i > len(singoli):
	#	return count
	if(i!=0):
		#if i==len(singoli) and isValidAttribute(root,singoli[i]):
		#	count+= 1
		if i==len(singoli)-1:
			#count += getValidChild(root,singoli[i])
	#		print('		Siamo alla frutta ROOT:       ',root.tag)
	#		print('		Siamo alla frutta singoli[i]: ',singoli[i])
			findNodo = findValidChildProfonda(root,singoli[i])	
	#		print('TTTTTTTTTT',findNodo)
			if findNodo != None:
	#			print('================================================ FIND')
				changeAttributo(findNodo,singoli[i],chiave,valore)
	else:
		for figlio in root.content:
	#		print('esaminando tag: ',figlio.tag)
			if figlio.tag != '_text_' and i < len(singoli):
				if i == 0 and figlio.tag == main:
	#				print('	------------------------------	M A I N  trovato')
					cambia_multi_selettore_complex(figlio, main, singoli,i+1,chiave,valore)
				if i!=0 and figlio.tag == singoli[i]:
	#				print('VAI SCAVAAAAAAAAAAAAA')
					cambia_multi_selettore_complex(figlio,main, singoli,i+2,chiave,valore)
				else:
					cambia_multi_selettore_complex(figlio,main, singoli,i,chiave,valore)
	
def conta_singolo_selettore(root, singolo):
    global count
    if isValidAttribute(root,singolo):
        count+= 1
    if not isFoglia(root):
        count += getValidChild(root,singolo)
        for figlio in root.content:
            if figlio.tag != '_text_':
                return conta_singolo_selettore(figlio, singolo)
        
    
count = 0        

def conta_nodi(fileIn, selettore):
	global count
	count = 0
	root = Tree(fileIn)
	L = scomponi_selettori(selettore)
	multi = False
	for b in L:
		if b == '>':
			multi = True
	#print('LLLLL = ',L)
	#print('ROOT = ',root)
	k = 0
	if multi:
	#	print('**************************** CONTA MULTI SELETTORE *********************')
		conta_multi_selettore(root,L,0)
	#	print(' OOOOOOOOOOOOOOOOOOOOOOOOO')
	#	print(' OOOOOOOOOOOOOOOOOOOOOOOOO')
	#	print('COUNT = ',count)	
	#	print(' OOOOOOOOOOOOOOOOOOOOOOOOO')
	#	print(' OOOOOOOOOOOOOOOOOOOOOOOOO')
		k+=count
	elif not multi and len(L) > 1:
	#	print('**************************** CONTA MULTI SELETTORE COMPLEX *********************')
		main = L[0]
	#	print(' COMPLEX OK ++++++++++++++++++++++++++')
		conta_multi_selettore_complex(root, main, L,0)
		k+=count
	else:
	#	print('**************************** CONTA NORMAL *********************')
		for sel in L:
			count = 0
			#if sel != '>':
	#		print('.---------- sel = ',sel)
			conta_singolo_selettore(root,sel)
	#		print('SEL RESULT: ',count)
			k+=count
	return k
            
    

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
	root = Tree(fileIn)
	L = scomponi_selettori(selettore)
	multi = False
	for b in L:
		if b == '>':
			multi = True
	#print('LLLLL = ',L)
	#print('ROOT = ',root)
	k = 0
	if multi:
	#	print('**************************** CAMBIA MULTI SELETTORE *********************')

	elif not multi and len(L) > 1:
	#	print('**************************** CAMBIA MULTI SELETTORE COMPLEX *********************')
		main = L[0]
		cambia_multi_selettore_complex(root, main, L,0,chiave,valore)
		#with open(fileOut) as f:
		#	root.to_string() = f.write()
	else:
	#	print('**************************** CAMBIA NORMAL *********************')
		for sel in L:
			conta_singolo_selettore(root,sel)


def stampa(tree):
    #print(tree.tag)
    #print('ATTRIBUTI: ',tree.attr)
    figli = tree.content    
    for f in tree.content:
       # print('FIGLI:     ',f.tag)
        if f.tag != '_text_':
            stampa(f)
    
    
'''
L = scomponi_selettori('div table tr')    
print(L)
root = Tree('page1-3.html')
print(root)
stampa(root)
'''