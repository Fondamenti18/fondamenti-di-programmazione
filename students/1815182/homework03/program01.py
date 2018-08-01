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
rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)


def lato(img, x, y, c):
    lato=0
    while dentro(img, x, y)==True and img[y][x]==c:
        lato=lato+1
        x=x+1
        y=y+1
    return lato


def dentro(img, x, y):
    return 0<=x<len(img[0]) and 0<=y<len(img)     


def pieno(img, x, y, lato, c):
    for j in range (y,y+lato):
        for d in range (x,x+lato):
            if img[j][d]!=c:
                return False
    return True
        

def quadrato(filename,c):
    img=load(filename)
    cont=0
    l=0
    ms=0
    cord=(0, 0)
    for j in range(len(img)):
        for d in range(len(img[0])):
            if img[j][d]==c:
                l=lato(img, d, j, c)
                if l>ms: 
                    if pieno(img, d, j, l, c)==True:
                        ms=l
                        cord=(d, j)
                    else:
                        while l>ms :
                            l=l-1
                            if pieno(img, d, j, l, c)==True:
                                ms=l
                                cord=(d, j)
                                break
    return (ms, cord)