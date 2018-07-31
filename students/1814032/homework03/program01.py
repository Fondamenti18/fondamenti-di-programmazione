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
	img = load(filename)
	w = len(img[0])
	h = len(img)
	r = [0,(0,0)]
	excluded = dict()
	for x in range(w):	#analyzing columns instead of rows in order to get the rightmost square (and eventually topmost)
		for y in range(h):
			if (excluded.get((x,y)) == None) & (img[y][x] == c):
				t = expand(x,y,img,w,h,c,excluded)
				r[:] = [r,t][t[0] > r[0]]
	return r[0],r[1]
	
def expand(x,y,img,w,h,c,excluded):
	D = 1
	end_of_image = (x+D >= w) | (y+D >= h)
	while (not end_of_image) and (checkBorder(x,y,img,D,c,excluded)):
		D += 1
		end_of_image = (x+D >= w) | (y+D >= h)
	return [D,(x,y)]

def checkBorder(x,y,img,D,c,excluded):
	for d in range(D,-1,-1):
		if (img[y+d][x+D] != c):
			eraseSP(x,y,x+D,y+d,excluded)
			return False
		if (img[y+D][x+d] != c):
			eraseSP(x,y,x+d,y+D,excluded)
			return False
	return True
	
def eraseSP(x,y,xt,yt,excluded):
	for yn in range(y,yt+1):
		for xn in range(x,xt+1):
			excluded[(xn,yn)] = 'x'
	return