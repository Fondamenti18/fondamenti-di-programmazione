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

def width(image):
	return len(image[0])

def height(image):
	return len(image)

def inside(x, y, image):
	return 0 <= x < width(image) and 0 <= y < height(image)

def quadrato(filename,c):
	'''
	'''
	img = load(filename)
	lato_max = 0
	for y in range(height(img)):
		for x in range(width(img)):
			lato_temp = 1
			if inside(x, y, img) and img[y][x] == c:
				n = 1
				while (inside(x, y, img) and img[y+n][x] == c and img[y+n][x+n] == c and img[y][x+n]):
					lato_temp += 1
					n += 1
				if lato_temp > lato_max:
					lato_max = lato_temp
					coordinate = (x, y)
			else:
				next
	return lato_max, coordinate

if __name__ == '__main__':
	quadrato('Ist1.png',(255,0,0))