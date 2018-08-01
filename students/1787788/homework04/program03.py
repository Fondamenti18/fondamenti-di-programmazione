
from  my_html import HTMLNode, fparse
from lxml import etree
from io import StringIO

##def recursive_avo(elemento, figlio, somma):
##	if figlio == elemento.tag:
##		somma[0] += 1
		
		
##def num_tag_avo_discendente(DOM, selettore, somma, tagNuovo, figlio):
##	if DOM.istext():
##		return 0
##	for elemento in DOM.content:
##		while(elemento.content != []):
##			if(DOM.tag == tagNuovo):
##				recursive_avo(elemento, figlio ,somma)
##			for item in elemento.content:
##				recursive_avo(item, figlio, somma)
##		num_tag_avo_discendente(elemento, selettore, somma, tagNuovo, figlio)
##	return somma
			
			
def num_tag(DOM, selettore, somma, listaChiave):
	if DOM.istext():
		return 0
	elif listaChiave != []:
		if(DOM.attr.get(listaChiave[0])):
			if(selettore in DOM.attr[listaChiave[0]]):
				somma[0] += 1
		for t in DOM.content:
			num_tag(t, selettore, somma, listaChiave)
		return somma
	elif ' ' in selettore:
		if '>' in selettore:
			if not DOM.closed:
				return 0
			else:
				splittata = selettore.split('>')
				tagNuovo = splittata[0][:-1]
				figlio = splittata[1][1:]
				if(tagNuovo in DOM.tag):
					for t in DOM.content:
						if(figlio in t.tag):
							somma[0] += 1
						if not t.istext():
							break
				for t in DOM.content:
						num_tag(t, selettore, somma, listaChiave)
				return somma
		##else:
		##	if not DOM.closed:
		##		return 0
		##	else:
		##		splittata = selettore.split(' ')
		##		tagNuovo = splittata[0]
		##		figlio = splittata [1]
		##		num_tag_avo_discendente(DOM, selettore, somma, tagNuovo, figlio)
	else:
		if(DOM.tag == selettore):
			somma[0] += 1
		for t in DOM.content:
			num_tag(t, selettore, somma, listaChiave)
		return somma
		
def ControllaSelettore(selettore, listaChiave):
	if(selettore[0] == '.'):
		listaChiave += ['class']
		selettore = selettore[1:]
	elif(selettore[0] == '#'):
		listaChiave += ['id']
		selettore = selettore[1:]
	elif(selettore[0] == '@'):
		splittata = selettore.split('=')
		listaChiave += [splittata[0][2:]]
		selettore = splittata[1][1:-2]
	return selettore
		
def conta_nodi(fileIn, selettore):
##	parser = etree.HTMLParser() 
##	tree   = etree.parse(StringIO(fileIn), parser)
##	tipo = ControllaSelettore(selettore)
##	if(tipo=='id' or tipo=='class'):
##		xpath = "//*[contains(@"+ tipo + ",'" + selettore[1:] + "')]"
##	num = tree.xpath('count(//[width=300])')
##	print(num)
	documento = fparse(fileIn)
	listaChiave = []
	selettore = ControllaSelettore(selettore, listaChiave)
	somma = [0]
	somma = num_tag(documento, selettore, somma, listaChiave)
	return(somma[0])
	
	
def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
