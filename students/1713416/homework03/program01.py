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
	immagine = load(filename)
	h, b = (len(immagine), len(immagine[0]))
	l = (0, (0, 0))
	for y in range(h):
		r = l[0]
		for x in range(b - r):
			if immagine[y][x] == c:
				nl = trovalato(immagine, x, y, h, b, c)
				if nl[0] > l[0] and controlla(immagine, nl[1][0], nl[1][1], nl[0], c):
					l = max([nl, l], key = lambda x: (x[0], (-x[1][1], -x[1][0])))
	return l	

def trovalato(immagine, x, y, h, b, c):
	i = x + 1
	j = y + 1
	while (j < h and i < b) and (immagine[j][x] == c and immagine[y][i] == c):
		i += 1
		j += 1
	return (i - x), (x, y)
	
def controlla(immagine, x, y, l, c):
	flag = True
	for j in range(1, l):
		for i in range(1, l):
			flag = flag and immagine[y + j][x + i] == c
			if not flag:
				return flag
	return flag
