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

def width(img):
    '''larghezza immagine'''
    return len(img[0])


def height(img):
    '''Altezza immagine'''
    return len(img)


def inside(img, x, y):
    '''True se il pixel è
        nell'immagine'''
    iw, ih = width(img), height(img)
    return 0<=x<iw and 0<=y<ih


def to_bin(img, c):

    for y in range(0, height(img)):
        for x in range(0, width(img)):
            if img[y][x] == c:
                img[y][x] = 1
            else:
                img[y][x] = 0
    return img

def quadrato(filename,c):

    img = to_bin(load(filename), c)

    dyn = []

    for y in range(0, height(img)+1):

        dyn.append([])

        for x in range(0, width(img)+1):

            if y == 0 or x == 0:
                dyn[y].append(0)
                continue

            if img[y-1][x-1] == 0:
                dyn[y].append(0)
                continue

            dyn[y].append(min(dyn[y-1][x], dyn[y-1][x-1], dyn[y][x-1]) + 1)

    max_l = 0
    max_coords = ()

    for y in range(0, height(dyn)):
        for x in range(0, width(dyn)):

            if not max_coords or dyn[y][x] > max_l:
                max_l = dyn[y][x]
                max_coords = (x-max_l, y-max_l)

            elif dyn[y][x] == max_l:
                if y-1 < max_coords[1]:
                    max_l = dyn[y][x]
                    max_coords = (x-max_l, y-max_l)
                elif y-1 == max_coords[1] and x-1 < max_coords[0]:
                    max_l = dyn[y][x]
                    max_coords = (x-max_l, y-max_l)

    return (max_l, max_coords)