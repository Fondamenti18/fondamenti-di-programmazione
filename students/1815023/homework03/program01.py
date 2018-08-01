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
    '''Implementare qui la funzione'''
    img = load(filename)
    w = len(img[0])
    h = len(img)
    maxSize = 0
    maxPos = (0,0)
    skipPixels = set()
    for y in range(h):
        for x in range(w):
            if img[y][x] == c and inside(x+maxSize,y+maxSize,w,h) and (x,y) not in skipPixels:

                    size,xD,yD = findMaxSquare(img,w,h,x,y,c)
                    #xD,yD sono le coordinate del pixel con colore diverso che hanno bloccato il quadrato
                    for j in range(yD-maxSize,yD+1):
                        for i in range(xD-maxSize,xD+1):
                            skipPixels.add((i,j))
                    if size > maxSize:
                        maxSize = size
                        maxPos = (x,y)      
    return (maxSize,maxPos)

def inside(x,y,w,h):
    return 0<=x<w and 0<=y<h


def findMaxSquare(img,w,h,x,y,c):
    size = 0
    while x<w:
        for i in range(size):
            if img[y+i][x+size] != c:
                return size,x+size,y+i
            elif img[y+size][x+i] != c:
                return size,x+i,y+size
        size += 1
        
        
