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

def maxQuad(img,x,y,w,h,dim,c):
    while True:
            for y1 in range(y,y+dim):
                for x1 in range(x,x+dim):
                    if img[y1][x1] != c:
                        return dim-1        
            dim+=1
            
def quadrato(filename,c):
    '''Implementare qui la funzione'''
    dimensione=0
    maxDim=0
    maxX=0
    maxY=0
    img=load(filename)
    w=len(img[0])
    h=len(img)
    for y in range(0,h):
        for x in range(0,w): 
            if img[y][x] == c: 
                if x+maxDim<w and y+maxDim<h: 
                    mQ = maxQuad(img,x,y,w,h,maxDim,c)                     
                    if mQ > maxDim: 
                        maxDim = mQ
                        maxX = x
                        maxY = y
                    
    return (maxDim, (maxX, maxY))
