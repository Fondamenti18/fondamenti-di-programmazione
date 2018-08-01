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

'''def inside(img,x,y):
        return 0<=y<righe(img) and 0<=x<colonne(img)

def colonne(img):return len(img[0])
def righe(img):return len(img)

def draw_rect(img,x,y,w,h,c):
    for px in range(x,x+w):
        for py in range(y,y+h):
            if inside(img,px,py) and img[py][px]=c:'''


def destra(img, x, y, c, count):
    if x+1 < len(img[y]):
        if img[y][x+1]==c:
            return count+destra(img, x+1, y, c, count)
    return 1

def sotto(img, x, y, c, count, d):
    if y+1 < len(img):
        s=0
        for i in range(d):
            if img[y+1][x+i]==c:
                s+=1
        if s==d:
            return count+sotto(img, x, y+1, c, count,d)
    return 1

def quadrato(filename,c):
    '''Implementare qui la funzione'''
    img=load(filename)
    l=0
    pos=(0,0)
    for i,y in enumerate(img):
        k=0
        while k < len(img[0]):
            if y[k]==c:
                d=destra(img, k, i, c, 1)
                s=sotto(img, k ,i, c, 1,d)
                if d <= s and d > l:
                    l=d
                    pos=(k, i)
                if s < d and s > l:
                    l=s
                    pos=(k, i)
            k+=1
    return (l,pos)
                


                
                
                
