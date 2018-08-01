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
    rows = len(load(filename))
    cols = len(img[0])
    counts = [[0]*cols for x in range(rows)]
    lunghezza_quadrato_massimo = 0
    coordinate_quadrato_massimo = (0,0)
    for i in reversed(range(rows)):
        for j in reversed(range(cols)):
            if img[i][j] != c:
                continue
            if i == rows - 1 or j == cols - 1:
                counts[i][j] = 1
            else:
                counts[i][j] = 1 + min(counts[i][j+1], counts[i+1][j], counts[i+1][j+1])
            if counts[i][j] >= lunghezza_quadrato_massimo:
                lunghezza_quadrato_massimo = counts[i][j]
                coordinate_quadrato_massimo = (j,i)
    return lunghezza_quadrato_massimo, coordinate_quadrato_massimo