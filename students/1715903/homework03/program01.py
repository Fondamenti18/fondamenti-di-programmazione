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
from PIL import Image

def quadrato(filename,c):
    im=Image.open(filename)
    imx,imy,lun,tl,ml=im.size[0],im.size[1],0,[],[]
    
    for y in range(imy):
        l=[]
        for x in range(imx):
            if y==0 or x==0:
                l.append(first(im,x,y,c))
            else:
                l.append(second(im,x,y,c,l,tl))
        tl.append(l)
    return mas(ml,tl,y,x)

def mas(ml,tl,y,x):
    ml=[max(i) for i in tl]
    y=ml.index(max(ml))
    ml=max(ml)
    x=tl[y].index(ml)
    x,y=x+1-ml,y+1-ml
    return ml,(x,y)
def first(im,x,y,c):
    if im.getpixel((x,y))==c:b=1
    else:b=0
    return b
def second(im,x,y,c,l,tl):
    if im.getpixel((x,y))==c:
        b=(min(l[x-1],tl[y-1][x],tl[y-1][x-1])+1)
    else:b=0
    return b





