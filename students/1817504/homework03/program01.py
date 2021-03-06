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
    img=load(filename)
    L=0
    for py in range(len(img)):
        for px in range(len(img[0])):
            if img[py][px]==c:
                l=calcola_lato(img,py,px,c,L)
                if l>L:
                    L=l
                    Vertice=(px,py)
    return L,Vertice

def inside(img,y,x):
    return 0<=y<len(img) and 0<=x<len(img[0])

def calcola_lato(img,y,x,c,L):
    l=1
    while inside(img,y+l,x+l) \
           and img[y][x+l]==c \
           and img[y+l][x]==c \
           and img[y+l][x+l]==c:
            l+=1
    if l>L:
        lato=1
        while lato<l:
            if test_colore(img,y,x,lato,c)==False:
                return lato
            lato+=1
        return lato
    return 0

def test_colore(img,y,x,l,c):
    for i in range(1,l):
        if img[y+l][x+i]!=c or img[y+i][x+l]!=c:
            return False
    return True
