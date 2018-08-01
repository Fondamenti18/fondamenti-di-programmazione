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
    nrighe = len(img)
    ncolonne = len(img[0])
    r = (0, (0, 0))
    matrice_somma_dati = []
    for y in range(nrighe + 1):
        somma_dati = []
        for x in range(ncolonne + 1):
            somma_dati.append(0)
        matrice_somma_dati.append(somma_dati)
    for y in range(1, nrighe + 1):
        for x in range(1, ncolonne + 1):
            if (img[y-1][x-1] == c):
                sinistra = matrice_somma_dati[y][x-1]
                alto = matrice_somma_dati[y-1][x]
                sinistra_alto = matrice_somma_dati[y-1][x-1]
                matrice_somma_dati[y][x] = lato = min(sinistra, alto, sinistra_alto) + 1
                if lato > r[0]:
                    r = (lato, (x -lato, y - lato))
    return r
