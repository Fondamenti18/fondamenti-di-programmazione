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
import sys
latoMax = 0
'''def checkEdge(img,x,y,col):
    global latoMax
    larghezza = len(img[0])
    altezza = len(img)
    checkColX = True
    checkColY = True
    countVar = 1
    maxX = 0
    maxY = 0
    #print('x: %s y: %s' %(x,y))
    while checkColX or checkColY:
        if int(x+countVar)<int(larghezza):
            if (img[y][x+countVar] != col and checkColX):
                #print('ENTRATO')
                checkColX = False
                maxX = countVar
        if (y+countVar<altezza):
            if (img[y+countVar][x] != col and checkColY):
                #print('ENTRATO2')
                checkColY = False
                maxY = countVar
        #print('x: %s y: %s' %(x+countVar,y+countVar))
        if int(x+countVar)>int(larghezza-1):
            checkColX = False
        if int(y+countVar)>int(altezza-1):
            checkColY = False
        if (checkColX or checkColY) == False:
            #print('checkX: %s checkY: %s' %(checkColX,checkColY))
            #input()
            pass
        countVar += 1
    #print('latoMax: %s MaxX: %s MaxY: %s'%(latoMax,maxX,maxY))
    if maxX>latoMax and maxY>latoMax:
        return True
    else:
        return False'''
def checkEdge(img,x,y,col):
    global latoMax
    larghezza = len(img[0])
    altezza = len(img)
    endX = x
    endY = y
    endX2 = x
    endY2 = y
    while endX < larghezza:
        if img[y][endX] != col:
            break
        else:
            endX += 1
    while endY < altezza:
        if img[endY][x] != col:
            break
        else:
            endY += 1
    while endX2 < larghezza and endY2 < altezza:
        if img[endY2][endX2] != col:
            break
        else:
            endY2 += 1
            endX2 += 1
    if ((endX-x)>latoMax and (endY-y)>latoMax) and ((endX2-x)>latoMax and (endY2-y)>latoMax):
        return True
    else:
        return False
def quadratiSucc(img,x,y,col,lato):
    match = True
    tempLato = lato+1
    larghezza = len(img)
    altezza = len(img[0])
    while match: 
        for cursore in range(tempLato):
            if y+cursore<altezza and x+cursore<larghezza:
                if img[y+cursore][x+lato] != col or img[y+lato][x+cursore] != col:
                    match = False
        tempLato += 1
    return tempLato
def findSquare(img,x,y,col):
    global latoMax
    Match = True
    isEdge = checkEdge(img,x,y,col)
    if isEdge:
        tempLato = latoMax + 1
        for riga in range(tempLato):
            for colonna in range(tempLato):
                try:
                    if img[y+riga][x+colonna]!=col:
                        Match = False
                        break
                except (IndexError):
                    Match = False
                    break
        if Match:
            latoMax +=1
            findSquare(img,x,y,col)
def quadrato(filename,c):
    img = load(filename)
    print('larghezza: %s altezza: %s' %(len(img[0]),len(img)))
    larghezza = len(img[0])
    altezza = len(img)
    colore = c
    global latoMax
    latoMaxTemp = 0
    cordinate = ()
    for riga in range(altezza):
        colonna = 0
        while colonna <= larghezza-1:
            if img[riga][colonna] == colore:
                findSquare(img,colonna,riga,colore)
                if latoMax != latoMaxTemp:
                    cordinate = (colonna,riga)
                    latoMaxTemp = latoMax
            colonna+=1
    cordinate = (latoMax,cordinate)
    return cordinate 
#sys.setrecursionlimit(5000)
#print(quadrato('Ist0.png',(255,255,255)))
'''quadrato('Ist4.png',(0,0,255))
   risultato: (201,(54,240)) '''




