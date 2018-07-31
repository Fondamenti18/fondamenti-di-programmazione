'''
Abbiamo immagini in formato png ottenute inserendo su di uno sfondo monocolore rettangoli 
di vari colori i cui assi sono sempre paralleli agli assi dell'immagine.

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
import math
from math import sqrt,trunc

def quadrato(filename,c):
    img=load(filename)
    return confronta_pixel(img,c)

def confronta_pixel(img,c):
    lato=0
    pos=(0,0)
    w,h=len(img[0]),len(img)
    
    for x in range(h):
        for y in range(w):
            if img[x][y]==c:
                lato,pos=trova_quadrato(img,x,y,c,lato,pos)
    return lato,pos

def trova_quadrato(img,x,y,c,lato,pos):
    pos1=(y,x)
    d=0
    while 0<=y<len(img) and 0<=x<len(img[0]) and img[x][y]==c:
        d+=1
        x+=1
        y+=1
    
    l=trunc(sqrt(d**2))
    
    if pos==(0,0):
        return l,pos1
    else:
        if l<lato:
            return lato,pos
        elif l>lato:
            return l,pos1
        else:
            if (pos1[1]>pos[1]) or (pos1[1]==pos[1] and pos1[0]>pos[0]):
                return lato,pos
            else:
                return l,pos1