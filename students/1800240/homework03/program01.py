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

def colore(img, x, y, l, c):
    
    alt = len(img)
    lun = len(img[0])
    
    px = x
    py = y
    
    while  y <= py <= (y + l) and x <= px <= (x + l):
        if py < alt and px < lun and img[py][px] == c:
            return True
        else:
            break
        py += 1
        px += 1
    
    else:
        return False
    
def quad(img, x, y, c):
    
    alt = len(img)
    lun = len(img[0])
    
    cx = x
    cy = y
   
    lato = 0
    
    while colore(img, cx, cy, lato, c) == True:
        if 0 <= cy < alt and 0 <= cx < lun:
            if img[cy][cx] == c:
                lato += 1
                cx += 1
                cy += 1
        else:
            break
        
    return lato
    
def quadrato(filename, c):
    
    img = load(filename)
    
    alt = len(img)
    lun = len(img[0])
    
    lati= []
    quadrati =[]
    
    for y in range(alt):
        for x in range(lun):
            if img[y][x] == c:
                lati.append(quad(img, x, y, c))
                quadrati.append([quad(img, x, y, c), (x, y)])
                
    for q in quadrati:
        if q[0] == max(lati):
            return tuple(q)