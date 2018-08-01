# -*- coding: utf-8 -*-
'''
Abbiamo immagini in formato png ottenute inserendo su di uno sfondo monocolore rettangoli 
di vari colori i cui assi sono sempre parallei agli assi dell'immagine.

Vedi ad esempio l'immagine Img1.png

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una  funzione quadrato(filename, C) che prende in input:
- il percorso di un file (filename) che contine un immagine in formato png della  tipologia appena descritta.
- una tupla C che rappresenta un colore in formato RGB (3 valori interi tra 0 e 255 compresi)

La funzione deve restituire nell'ordine:
- la lunghezza del lato del quadrato pieno di dimensione massima e colore C interamente visibile nell'immagine. 
- le coordinate  (x,y)  del pixel dell'immagine che corrisponde alla posizione 
all'interno dell'immagine del punto in alto a sinistra del quadrato. 

In caso ci siano più quadrati di dimensione massima, va considerato quello il cui punto 
in alto a sinistra occupa la riga minima  (e a parita' di riga la colonna minima) all'interno dell' immagine. 

Si può assumere che nell'immagine e' sempre  presente almeno un pixel del colore cercato.

Per gli esempi vedere il file grade01.txt

ATTENZIONE: Il timeout è impostato a 10*N secondi (con N numero di test del grader).
'''

from immagini import *
def quadrato(filename,c):
	img=load(filename)
	punto=(0,0)
	max=1
	y=0
	n=0
	for a in img:
		x=0
		for b in a:
			cont=0
			if b==c:
				if n==0:
					punto=(x,y)
				if  (len(img)-y)>max and (len(img[0])-x)>max and max<calcolo_diag(x,y,img,c) and max<calcolo_orizz(x,y,img,c) and max<calcolo_vert(x,y,img,c):
					i=y
					j=x
					while img[i][j]==c and (i+1)<(len(img)) and (j+1)<(len(img[0])) and controlla_contorno(x,y,j,i,img,c)==1 and img[y+1][x+1]==c:
						cont+=1
						i+=1
						j+=1
					if cont>max:
						max=cont
						punto=(x,y)
				n+=1
			x+=1
		y+=1
	return(max,punto)
		
def controlla_contorno(x,y,j,i,img,c):
	old_x=x
	old_y=y
	n=0
	while x<j and n!=999999:
		if img[y][x]!=c:
			n=999999
		x+=1
	while y<i and n!=999999:
		if img[y][x]!=c:
			n=999999
		y+=1
	while x>old_x and n!=999999:
		if img[y][x]!=c:
			n=999999
		x=x-1
	while y>old_y and n!=999999:
		if img[y][x]!=c:
			n=999999
		y=y-1
	if n!=999999:
		return 1
	else:
		return 0
		
def calcolo_orizz(x,y,img,c):
	n=1
	cont=1
	while (y+n)<(len(img)) and (x+n)<(len(img[0])) and img[y][x+n]==c:
		cont+=1
		n+=1
	return cont
	
def calcolo_vert(x,y,img,c):
	n=1
	cont=1
	while (y+n)<(len(img)) and (x+n)<(len(img[0])) and img[y+n][x]==c:
		cont+=1
		n+=1
	return cont
def calcolo_diag(x,y,img,c):
	n=1
	cont=1
	while (y+n)<(len(img)) and (x+n)<(len(img[0])) and img[y+n][x+n]==c:
		cont+=1
		n+=1
	return cont
		
	
		
				
	
	
	
	

