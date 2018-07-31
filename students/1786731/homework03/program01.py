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


img = None
h   = None
w   = None
targetColor = (0,0,0)
maxsquare = 0

def computeCoefficient(x, y, sMatrix):
    zeroOrOne = 0 if img[y][x] != targetColor else 1

    if zeroOrOne == 1:
        leftBound = sMatrix[y][x-1]
        topBound  = sMatrix[y-1][x]
        topleftBound = sMatrix[y-1][x-1]

        coefficient = min(leftBound, topBound, topleftBound) + 1
        sMatrix[y].append(coefficient)
        return (coefficient, x, y)
    else:
        sMatrix[y].append(0)
        return (-1, 0, 0)

def computeFirstRow(sMatrix):
    for x in range(w):
        zeroOrOne = 0 if img[0][x] != targetColor else 1 
        sMatrix[0].append(zeroOrOne)

def computeFirstColumn(sMatrix):
    for y in range(1, h):
        zeroOrOne = 0 if img[y][0] != targetColor else 1 
        sMatrix[y].append(zeroOrOne)

def getSMatrix():
    return [[] for x in range(h)] # create array

def quadrato(filename,c):
    r, g, b = c

    # global definitions
    global img
    img = load(filename)
    global h
    h = len(img)
    global w
    w = len(img[0])
    global targetColor
    targetColor = c
    # global definitions - END 
    
    biggestCoefficient = (0, (0,0))

    sMatrix = getSMatrix() # create array
    computeFirstRow(sMatrix)
    computeFirstColumn(sMatrix)


    square = (h-1)*(w-1)
    # first row and column of each row already computed, range from 1 to h/w
    for i in range(0, square):
        y = i // (w-1) + 1  
        x = i % (w-1)  + 1  
        coeff = computeCoefficient(x, y, sMatrix)
            
        if coeff[0] > biggestCoefficient[0]:
            biggestCoefficient = coeff

    return (biggestCoefficient[0], 
            (biggestCoefficient[1] - biggestCoefficient[0] + 1, 
             biggestCoefficient[2] - biggestCoefficient[0] + 1))

    # end = 0


# quadrato("Ist3.png", (255,0,0))