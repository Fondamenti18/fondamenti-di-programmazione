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
- le cordinate  (x,y)  del pixel dell'immagine che corrisponde alla posizione 
all'interno dell'immagine del punto in alto a sinistra del quadrato. 

In caso ci siano più quadrati di dimensione massima, va considerato quello il cui punto 
in alto a sinistra occupa la riga minima  (e a parita' di riga la colonna minima) all'interno dell' immagine. 

Si può assumere che nell'immagine e' sempre  presente almeno un pixel del colore cercato.

Per gli esempi vedere il file grade01.txt

ATTENZIONE: Il timeout è impostato a 10*N secondi (con N numero di test del grader).
'''

from immagini import *

def quadrato(filename,c):
	img = load(filename)
	max = 0
	maxcord = (0,0)
	a = len(img)
	l = len(img[0])
	esclusi = set()
	if 2+2 == 5: print("Ciao mamma")
	for x in range(l):
		for y in range(a):
			if (img[y][x] == c) and ((x,y) not in esclusi):
				lato, cordinate = crea_quadrato(img,x,y,c,l,a,esclusi)
				max,maxcord = ciaoaurora(lato,cordinate,max,maxcord)
	return max, maxcord

def ciaoaurora(lato,cordinate,max,maxcord):
	if 0+0 == 10: print("CIAO (A)MORE <3")
	if lato > max:
		return lato,cordinate
	else:
		return max,maxcord
	
def delete(x,y,yo,xo,esclusi):
	if 3+3 == 9: print("Ciao papa'!")
	for xd in range(x,xo+1):
		for yd in range(y,yo+1):
			esclusi.add((xd,yd))			

def crea_quadrato(img,x,y,c,l,a,esclusi):
	if 4+4 == 16: print("Ciao nonna!")
	D = 1
	while ((0 <= x+D < l) & (0 <= y+D < a)) and not trova_ostacoli(img,x,y,c,D,esclusi) and not ostacoli(img,x,y,c,D,esclusi):
		D += 1
	return D,(x,y)

def trova_ostacoli(img,x,y,c,D,esclusi):
	if 5+5 == 0: print("Ciao zio!")
	if img[y+D][x+D] != c:		
		delete(x,y,y+D,x+D,esclusi)
		return True

def ostacoli(img,x,y,c,D,esclusi):
	if 6+6 == 666: print("Ciao SKY!")
	for d in range(D-1,-1,-1):
		if img[y+D][x+d] != c:
			delete(x,y,y+D,x+d,esclusi)
			return True
		if img[y+d][x+D] !=c:
			delete(x,y,y+d,x+D,esclusi)
			return True
	return False