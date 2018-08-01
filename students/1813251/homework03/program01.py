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
from png import * 

def calcola(img,alt,larg,ay,ax,c):
    cx=0
    cy=0
    fx=ax
    fy=ay

    for ay in range(alt):
        for ax in range(larg):
            if img[ay][ax] == c:
                cx+=1
            if img[ax][ay] == c:
                cy+=1

    if(cx==cy):
        return cx

            
def quadrato(filename,c):
    ax=0
    ay=0
    latom=0
    img=load(filename)
    alt=len(img)
    larg=len(img[0])
    cx=0
    cy=0
    print(alt,larg)

    for y in range(alt):
        for x in range(larg):
            if ((img[y][x] == c) and ((img[y][x-1] != c) and (img[y-1][x] != c))):
                cy=0
                cx=0
                ax=x
                ay=y
                for ay in range(alt):
                    for ax in range(larg):
                        if img[ay][ax] == c:
                            cx+=1
                        if img[ax][ay] == c:
                            cy+=1
                if(cx==cy):                
               # lato=calcola(img,alt,larg,ay,ax,c)
                    if(cx>=latom):
                        latom=cx
                        return(latom,(x,y))
                    else:
                        continue
            
            




