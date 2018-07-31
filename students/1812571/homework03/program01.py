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

def preProcess(image, c):
    
    preProcessedImageColumnLength = [[-1 for y in range(len(image[0]))] for x in range(len(image))]
    lengthCnt = 1
    for lineCnt in range(len(image)-1,-1,-1):
        for columnCnt in range(len(image[lineCnt])-1,-1,-1):
            if (image[lineCnt][columnCnt] == c):
                preProcessedImageColumnLength[lineCnt][columnCnt] = lengthCnt
                lengthCnt += 1
            else:
                lengthCnt = 1
                
    return preProcessedImageColumnLength

def checkCoord(coordX,coordY,image,preprocessedC,biggestSquare):
    currentLength = 0
    smallerEdge = 1000000
                
    for innerLineCnt in range(coordX,len(image)):
        if (preprocessedC[innerLineCnt][coordY] < smallerEdge):
            smallerEdge = preprocessedC[innerLineCnt][coordY]
        if ((smallerEdge <= currentLength) or (smallerEdge < biggestSquare)):
            break
        currentLength += 1
        
    return currentLength

    
def trovaQuadrati(image, c):
    biggestSquare = [-1,-1,-1]
    preprocessedColumns = preProcess(image, c)
    previousPPV = -1
    for columnCnt in range(0, len(image[0])):
        if (len(image[0])-columnCnt < biggestSquare[2]):
            break
        for lineCnt in range(0, len(image)):
            if (image[lineCnt][columnCnt] == c):
                prePreviousPPV = previousPPV
                previousPPV = preprocessedColumns[lineCnt][columnCnt]
                if (prePreviousPPV >= previousPPV):
                    continue

                length = checkCoord(lineCnt,columnCnt,image,preprocessedColumns,biggestSquare[2])   
                if (length > biggestSquare[2]):
                    biggestSquare = [lineCnt, columnCnt, length]

    return biggestSquare                    
                    
    
            
def quadrato(filename,c):
    image = load(filename)
    biggestSquare = trovaQuadrati(image,c)
    return biggestSquare[2], (biggestSquare[1], biggestSquare[0])
    