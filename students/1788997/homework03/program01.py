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

from immagini import load

def genMatrix(img, c):
    '''Prende un immagine ed un colore e ritorna la larghezza, l'altezza e una matrice con 1 dove il colore è uguale a c'''
    w, h = len(img[0]), len(img)
    for y in range(h-1, -1, -1):
        for x in range(w-1, -1, -1):
            n = int(img[y][x] == c)
            if not x or not y:    
                img[y][x] = [n, n]
                continue
            img[y][x] = [n, 0]
    return img, w, h

def quadrato(filename, c):
    '''Prende in input un immagine ed un colore e ritorna il quadrato più grande di quel colore presente nell'immagine'''    
    img, w, h = genMatrix(load(filename), c)
    maxVal, coords = 0, ()    
    for y in range(h-2, -1, -1):
        for x in range(w-2, -1, -1):
            if img[y][x][0]:
                n = min(img[y][x+1][1], img[y+1][x+1][1], img[y+1][x][1]) + 1
                img[y][x][1] = n
                if n >= maxVal:
                    maxVal, coords = n, (x, y)
    return (maxVal, coords)