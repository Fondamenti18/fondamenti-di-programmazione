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

def analisi(imma, c, x, y, h, l):
    dim = 0
    while dim < (h-y)-1 and dim < (l-x)-1:
        if imma[y+dim][x] != c or imma[y][x+dim] != c or imma[y+dim][x+dim] != c:
            break
        elif imma[y+int(dim/1.3)][x+dim] != c or imma[y+dim][x+int(dim/1.3)] != c:
            break
        elif imma[y+(dim//2)][x+dim] != c or imma[y+dim][x+(dim//2)] != c:
            break
        elif imma[y+(dim//3)][x+dim] != c or imma[y+dim][x+(dim//3)] != c:
            break
        elif imma[y+(dim//7)][x+dim] != c or imma[y+dim][x+(dim//7)] != c:
            break
        dim+=1
    return dim

def search(imma, c, x, y, h, l, dimens):
    dim2=0
    while y+dim2 < h-1 and  x+dim2 < l-1:
        for con in range(dim2):
            if imma[y+con][x+dim2] != c or imma[y+dim2][x+con] != c:
                return dim2
        dim2+=1
    return dim2

def quadrato(filename, c):
    '''Implementare qui la funzione'''
    imma = load(filename)
    dim = 0
    h = len(imma)
    l = len(imma[0])
    for y in range(h):
        for x in range(l):
            if imma[y][x] == c:
                provv = analisi(imma, c, x, y, h, l)
                if provv > dim:
                    ris = search(imma, c, x, y, h, l, dim)
                    if ris > dim:
                        dim = ris
                        coord = (x,y)
    return dim, coord