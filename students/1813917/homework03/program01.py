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
    lq = [(0,(0,0))]
    img = load(filename)
    width = len(img[0]) - 1
    height = len(img) - 1
    for riga in range(height):
        for pixel in range(width):
            if img[riga][pixel] == c:
                new_lq = controllo_quadrato(img, riga, pixel, c, lq)
    return new_lq[0]
    #print(new_lq[0])

def controllo_quadrato(img, y, x, c, lq):
    # Controllo la X
    lq_copy = lq[:]
    ix = x
    iy = y
    lato = 1
    while  x < (len(img[0]) - 1) and y < (len(img) - 1) and img[iy][x + 1] == c and img[y + 1][ix] == c:
        x += 1
        y += 1
        lato += 1
    pieno = controlla_dentro(img, x, y, ix, iy, c)
    if pieno:
        coordinate = ix, iy
        quadrato = lato , coordinate
        if lato > lq[0][0]:
            del lq[0]
            lq.append(quadrato)
            if coordinate > lq_copy[0][1] and lq_copy[0] == lato:
                del lq[0]
                lq.append(lq_copy[0])
    return lq

def controlla_dentro(img, x, y, ix, iy, c):
    for riga in range(iy, y + 1):
        for pixel in range(ix, x + 1):
            if img[riga][pixel] != c:
                return False
    else:
        return True
            
#quadrato('Ist3.png',(255,0,0))
