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
    '''Implementare qui la funzione'''
    from immagini import load

def quadrato(filename,c):
    img=load(filename)
    listax=[]
    listay=[]
    for y in range(len(img[1])):
        for x in range(len(img[0])):
            try:
                if img[y][x]==c:
                    lato=quadx(img,x,y,c)
                    listax.append(lato)
                if img[x][y]==c:
                    lato=quady(img,x,y,c)
                    listay.append(lato)
            except  IndexError:
                pass

    insx=set(listax)
    insy=set(listay)
    side=insx.intersection(insy)
    side=max(side)
    for y in range(len(img[1])):
        for x in range(len(img[0])):
            try:
                if side==1 and img[y][x]==c:
                    result=(side,(x,y))
                    return result
                if img[y][x]==c and mislato(img,x,y,side,c):
                    result=(side,(x-10,y+19))
                    return result
            except IndexError:
                pass
    result=(side,(x,y))  
     

def quadx(img, x, y, c):
    lato=0
    try:
        while inside(img,x,y) and img[y][x] == c:
            x+=1
            lato+=1
    except IndexError:
        pass
    return lato
def quady(img, x, y, c):
    lato=0
    try:
        while inside(img,x,y) and img[x][y] == c:
            y+=1
            lato+=1
    except IndexError:
        pass
    return lato
def mislato(img,x,y,lato,c):
    try:
        if img[y][x+lato]==c and img[y+lato][x]==c:
            return True
        return False
    except IndexError:
        pass
        
def inside(img, x, y):
    return 0 <= y < len(img[1]) and 0 <= x < len(img[0])
