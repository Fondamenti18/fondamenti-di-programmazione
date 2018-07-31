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

def getSquare (matrix, ir, ic, color, sideSize):
    
    currentIr = ir
    currentIc = ic
    isSquareFilled = True
    
    while currentIr < ir+sideSize and isSquareFilled:
        while currentIc < ic+sideSize and isSquareFilled:
            if matrix[currentIr][currentIc] != color:
                isSquareFilled = False
            else:
                currentIc+=1
        currentIr+=1
        currentIc = ic
                   
    return { 'x': ic, 'y': ir, 'sideSize': sideSize, 'isSquareFilled': isSquareFilled }

def getSquareSide (matrix, ir, ic, color):
    
    isColor = True
    sideSize = 0
    icX = ic
    irY = ir
    
    while icX < len(matrix[ir]) and irY < len(matrix) and isColor:
        if matrix[ir][icX] == color and matrix[irY][ic] == color:
            sideSize+=1
            icX+=1
            irY+=1
        else:
            isColor = False
    
    return sideSize

def quadrato(filename,c):
    '''Implementare qui la funzione'''
    
    img = load(filename)
    
    currentSquare = { 'x': 0, 'y': 0, 'sideSize': 0 }
    
    for ir in range(0, len(img)):
        for ic in range(0, len(img[ir])):
            if img[ir][ic] == c:
                sideSize = getSquareSide(img, ir, ic, c)

                if sideSize > currentSquare.get('sideSize'):
                
                    infoSquare = getSquare(img, ir, ic, c, sideSize)
                    if infoSquare.get('isSquareFilled'):
                       currentSquare = infoSquare
                       
    return (currentSquare.get('sideSize'), (currentSquare.get('x'), currentSquare.get('y')))
