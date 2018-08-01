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

ATTENZIONE: Il timeout è impostato a 10*N secondi (con N numero di test del grader).'''
import time
from immagini import *
latoMax = 0
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
def checkColore(img,x,y,col,riga):
    succX = x + 1
    succY = y + 1
    lato = 1
    larghezza = len(img[0])
    altezza = len(img)
    if riga:
        while succX<larghezza and img[y][succX] == col:
            lato+=1
            succX+=1
    else:
        while succY<altezza and img[succY][x] == col:
            lato+=1
            succY += 1
    if not riga:
        succX = succY
    return succX,lato
def creaList(img,col):
    lista = []
    altezza = len(img)
    larghezza = len(img[0])
    for riga in range(altezza):
        colonna = 0
        while colonna < larghezza:
            if img[riga][colonna] == col:
                xSucc,lato = checkColore(img,colonna,riga,col,True)
                tempColonna = colonna
                while tempColonna < xSucc:
                    lista.append([lato,(tempColonna,riga)])
                    lato -= 1
                    tempColonna += 1
                colonna = xSucc
            else:
                colonna += 1
    return lista
def quadrato(filename,c):
    img = load(filename)
    print('larghezza: %s altezza: %s' % (len(img[0]), len(img)))
    colore = c
    listaElem = creaList(img,c)
    listaElem.sort()
    global latoMax
    latoMaxTemp = 0
    cordinate = ()
    for elem in listaElem:
        findSquare(img, elem[1][0], elem[1][1], colore)
        if latoMax != latoMaxTemp:
            cordinate = (elem[1][0], elem[1][1])
            latoMaxTemp = latoMax
    cordinate = (latoMax, cordinate)
    return cordinate

#Start_Timer=time.time()
#print("--- %s seconds ---" % (time.time() - Start_Timer))
'''quadrato('Ist4.png',(0,0,255))
   risultato: (201,(54,240))        n°pix: 920062
   quadrato('Ist2.png',(255,0,0))
   risultato: (30, (60, 50))
'''
