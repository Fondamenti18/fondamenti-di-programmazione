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
 
def size(img, offx, offy, c):
    w = 0
    for x in range(offx, len(img[0])):
        if img[offy][x] != c:
            break
        w += 1
    h = 0
    for y in range(offy, len(img)):
        if w == h:
            break
        for x in range(offx, offx+w):
            if img[y][x] != c:
                break
        else:
            h += 1
            continue
        break
    return min(w,h)
 
 
def quadrato(filename,c):
    '''Implementare qui la funzione'''
    img = load(filename)
    h, w = len(img), len(img[0])
    max = (0, ())
    for y in range(h):
        for x in range(w):
            if img[y][x] == c:
                s = size(img, x, y, c)
                if max[0] < s:
                    max = (s, (x, y))
    return max