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
    colore = set([c, c])
    latom = 0
    lato = 0
    coord = ()
    for y in range(len(img)):
        for x in range(len(img[y])):
            if img[y][x] == c:
                lato = 0
                lato = larghezza(x, y, img, c)
                if lato > latom:
                    lato = costruisci(x, y, lato, colore, img, latom)
                
            if lato > latom:
                latom = lato
                coord = (x,y)
    return(latom, coord)
                    
                
                
def larghezza(x, y, img, c):
    latoo = 0
    latov = 0
    n = 0
    d = 0
    while x + n < len(img[0]) and img[y][x+n] == c :
        n += 1
        latoo += 1
    while y + d < len(img) and img[y + d][x] == c:
        d += 1
        latov +=1
    lato = min(latoo, latov)
    return lato

def costruisci(x, y, lato, colore, img, latom):
    a = set()
    if lato == 1:
        return lato
    else:
        for c in range(lato):
            for b in range(lato):
                a.add(img[y + c][x + b])
            if a & colore != colore:
                lato -= 1
                if lato < latom:
                    return 1
                costruisci(x, y, lato, colore, img)
                
        if a.union(colore) == colore:
            return lato
    return 1
        
    
    
    
    
    
    
    