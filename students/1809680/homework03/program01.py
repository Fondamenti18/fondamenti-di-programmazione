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

def quadrato(filename, c):
    l, lTemp, cx, cy, x, y=0, 0, 0, 0, 0, 0
    img=load(filename)
    width=len(img[0])
    height=len(img)
    while x<width-l:
        y=0
        while y<height-l:
            if img[y][x]==c:
                lTemp=checkQuad(img, x, y, c, l, width-1, height-1)
                if lTemp>0 and lTemp>l:
                    l=lTemp
                    cx=x
                    cy=y
                    if l>200:
                        y=height
                        x=width
            y+=1
        x+=1
    return l, (cx, cy)

def minimo(a, b):
    if a<=b: return a
    else: return b
    
def checkQuad(img, x, y, c, lMaxTrovato, xMax, yMax):
    larghezzaMax=xMax-x+1
    altezzaMax=yMax-y+1
    latoMax=minimo(larghezzaMax, altezzaMax)
    if latoMax <=lMaxTrovato: 
        return 0
    for x1 in range(x, x+latoMax):
        for y1 in range(y, y+latoMax):
            if img[y1][x1]!=c:
                if x1-x>y1-y:
                    return checkQuad(img, x, y, c, lMaxTrovato, x1-1, minimo(yMax, y+(x1-1-x)))
                else:
                    return checkQuad(img, x, y, c, lMaxTrovato, minimo(xMax, x+(y1-1-y)), y1-1)
    return latoMax


    
    
    

    
        
    
