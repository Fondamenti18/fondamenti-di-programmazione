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

def cambiare_valore(img, c):
    '''cambiare il valore di ogni pixel in base al colore.'''
    for h in range(0, len(img)):
        for w in range(0, len(img[0])):
            if img[h][w] == c:
                img[h][w] = 2
            else:
                img[h][w] = 1

def min_valore(img):
    '''calcolare il minimo valore.'''
    for h in range(1, len(img)):
        for w in range(1, len(img[0])):
            if img[h][w] != 1:
                img[h][w] = min(img[h-1][w-1], img[h-1][w], img[h][w-1])+1

def calcolo_lato(img, c):
    '''calcolare il lato.'''
    cambiare_valore(img, c)
    min_valore(img)
    max_value = 0
    max_h = 0
    max_w = 0
    for h in range(0, len(img)):
        for w in range(0, len(img[0])):
            if max_value < img[h][w]:
                max_value = img[h][w]
                max_h = h
                max_w = w
    return(max_value-1, (max_w-max_value+2, max_h-max_value+2))

def quadrato(filename,c):
    '''calcolare il lato del quadrato piu' grande e la sua pozione.'''
    img = load(filename)
    return calcolo_lato(img, c)