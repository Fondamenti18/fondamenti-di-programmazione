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
from pprint import pprint


def checkSqr(file,x,y,counter,c): #funzione che controlla se un quadrato ha solo pixel di quel colore
    marky = y-(counter-1)
    markx = x-(counter-1)
    for i in range(y-marky):
        if file[marky+i][markx+i] != c:
            return False
        if file[marky+i][x] != c:
            return False
        if file[marky+i][markx] != c:
            return False
        if file[marky][markx+i] != c:
            return False
        
    for h in range(marky,y): 
        for w in range(markx,x+1):
            if file[h][w] != c:
                return False
    return True

def CheckSqrMax(x,y,counter,latoSqr,upLeftPix): #funzione che controlla se il quadrato è piu in alto di quello prima 
    if counter > latoSqr:
        latoSqr = counter
        upLeftPix = (x-(latoSqr-1),y-(latoSqr-1))
    return latoSqr,upLeftPix


def quadrato(filename,c):
    file = load(filename)
    latoSqr = 0
    upLeftPix=()
    for y in range(len(file)):
        counter = 1
        controllo = True
        for x in range(len(file[y])):
            if counter == y+1 :
                break  
            if file[y][x] == c:
                if counter < y and controllo == True:
                    counter += 1
            #print(x,y)
                if counter > latoSqr:
                    if  checkSqr(file,x,y,counter,c):
                        controllo = True
                        latoSqr,upLeftPix = CheckSqrMax(x,y,counter,latoSqr,upLeftPix)
                    else:
                        controllo = False
            else:
                counter = 0
    #print('\n lato ', latoSqr, '\n cordinate', upLeftPix)
    return latoSqr,upLeftPix