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

def quadrato(filename,c):
    img = load(filename)
    latomax = 0
    for x in range(height(img)):
        for y in range(width(img)):
            if img[x][y]==c:
                x0 = x
                y0= y
                x,y=diagonale(img,x,y,c)
                x3,y3 = x,y
                lato = (x3 - x0 + 1)
                if lato > latomax:
                    x3=controllo_quadrato2(x0,x3,y0,y3,c,x,y,img)
                lato = (x3 - x0 + 1)
                if lato > latomax:
                    latomax = lato
                    finx = x0
                    finy = y0
                x = x0
    return latomax,(finy,finx)

def diagonale(img,x,y,c):
    while True:
        y += 1
        x += 1
        if x >= len(img)-1 or y >= len(img[0])-1 or img[x][y] != c :
            x -= 1
            y -= 1
            break
    return x,y

def controllo_quadrato(x0,x3,y0,y3,c,x,y,check,img):
    for x in range(x0,x3+1):
        for y in range(y0,y3+1):
            if img[x][y] != c:
                check = False
                break
        if not check:
            break
    return check

def controllo_quadrato2(x0,x3,y0,y3,c,x,y,img):
    while True:
        if (x3 - x0 + 1)< width(img)/2:
            check = True
            if x3 > x0:
                 check=controllo_quadrato(x0,x3,y0,y3,c,x,y,check,img)
                 if not check:
                    x3 -= 1
                    y3 -= 1
                 else:
                    break
            else:
                break
        else:
            x3 -= 1
            y3 -= 1
    return x3
def width(img):
	'''Ritorna la larghezza dell'immagine img.'''
	return len(img[0])
def height(img):
	'''Ritorna l'altezza dell'immagine img.'''
	return len(img)
