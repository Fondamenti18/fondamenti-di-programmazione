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
    return len(img[0])

def height(img):
    return len(img)

def is_inside(x, y, img):
    return 0 <= x < width(img) and 0 <= y < height(img)

def find_coords(matrix):
    massimo = max(c for rows in matrix for c in rows)
    result = []
    for r in range(height(matrix)):
        for c in range(width(matrix)):
            if matrix[r][c] == massimo:
                result.append((massimo, (c-massimo+1, r-massimo+1)))
                break
    return sorted(result, key = lambda x: (-x[0], x[1][0]))[0]
    
def quadrato(filename,c):
    img = load(filename)
    rows, cols = height(img), width(img)
    counts = [[0]*cols for _ in range(rows)]
    for i in range(rows):     
        for j in range(cols): 
            if img[i][j] == c:
                counts[i][j] = (1 + min(counts[i][j-1],  
                    counts[i-1][j],  
                    counts[i-1][j-1] 
                    )) if is_inside(j, i, img) else 1 
    return find_coords(counts)

    
          
            
