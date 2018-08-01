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
	listaq = []
	pos = 0
	for y in range(len(img)):
		for x in range(len(img[0])):
			if img[y][x] == c:
				l, col, r = 1, y, x
				pos = (x,y)
				while (img[y][r+1] == c and r+1 < (len(img[0]))) and (img[col+1][x] == c and col+1 < (len(img))) and (img[col+1][r+1] == c):
					l += 1
					r += 1
					col += 1
				listaq += [(l,(pos))]
	max = listaq[0]
	for q in listaq:
		if (q[0] > max[0]):
			max = q
	return max
		