'''

Definiamo adiacenti di un pixel p di un immagine i pixel adiacenti a p in  orizzontale o in  verticale.
Se un pixel e' sul bordo dell'immagine il suo vicinato non comprende i pixel non contenuti nell'immagine.
Il pixel dell'immagine con coordinate(x,y) ha dunque come adiacenti i pixel   
con coordinate (x-1,y),(x+1,y),(x,y-1),(x,y+1) appartenenti all'immagine. 
 
Definiamo connessi due pixel se e' possibile dall'uno raggiungere l'altro spostandosi solo su   
pixel adiacenti e dello stesso colore (ovviamente perche' cio' sia possobile e' necessario 
che i due pixel abbiano lo stesso colore).

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una funzione ricolora(fname, lista,  fnameout) che presi:
- il percorso di un file che contiene un'immagine in formato PNG
- una lista di quadruple del tipo (x,y,c1,c2) dove  x e y sono coordinate di un pixel dell'immagine e c1 e c2 due triple colore RGB
- il percorso di un file (fnameout) da creare
legge l'immagine in fname, esegue un'operazione di ricolorazione di alcuni pixel dell'immagine e 
registra l'immagine ricolorata nel file fnameout.

L'operazione di ricolorazione e' la seguente. Per ciascuna delle quadruple (x,y,c1,c2) della lista (nell'ordine), 
- tutti i pixel connessi al pixel  di coordinate (x,y) nell'immagine vanno ricolorati col colore c1, 
- tutti i pixel del perimetro (che si trovano sul 'bordo') della zona che si e' appena colorata devono essere ricolorati col colore c2.
Il perimetro della zona colorata è l'insieme dei pixel che non hanno tutti e 4 i vicini che fanno parte della zona ricolorata 
(ovvero almeno uno è di un colore diverso da quello che si sta ricolorando oppure almeno uno non esiste perchè sarebbe fuori dall'immagine)

Si consideri ad esempio l'immagine 'I1.png', l'invocazione di ricolora('I1.png',[(10,10,(255,0,0), (0,0,255))],’OUT1.png')
produrra' l'immagine 'OUT1.png' identica all'immagine di partenza se non per il fatto che,
 tutti i pixel adiacenti al pixel di coordinate (10,10) (e di colore verde), verranno ricolorati 
 di rosso ((255,0,0)), mentre i pixel sul bordo della zona inizialmente verde vengono ricolorati di blu.

Per ciascuna area ricolorata bisogna inoltre calcolare area interna e perimetro, che sono definite come segue:
- l'area interna e' il numero di pixel ricolorati con il colore c1
- il perimetro è il numero di pixel ricolorati con il colore c2

La funzone deve tornare la lista di coppie (area interna, perimetro) nello stesso ordine in cui sono state colorate le aree.
 
Per altri  esempi vedere il file grade03.txt 
'''

from immagini import *
    

img = None
w   = None
h   = None

def calcAreaAndBorder(squareMatrix, smh, smw, smallestX1, smallestY1, pixel):
    area = 0
    border = 0

    for i in range(smh):
        for j in range(smw):

            # skip zeroes
            if squareMatrix[i][j] == 0:
                continue

            left   = True
            right  = True
            top    = True
            bottom = True

            if (j == 0) or (squareMatrix[i][j-1] == 0):
                left = False
            if (j == smw-1) or (squareMatrix[i][j+1] == 0):
                right = False 
            if (i == 0) or (squareMatrix[i-1][j] == 0):
                top = False 
            if (i == smh-1) or (squareMatrix[i+1][j] == 0):
                bottom = False

            realImgCoordX = smallestX1 + j
            realImgCoordY = smallestY1 + i

            # if all are 1s, this pixel will need a recolor
            if left & right & top & bottom:
                img[realImgCoordY][realImgCoordX] = pixel[2]
                area += 1
            else: # else is part of the border
                img[realImgCoordY][realImgCoordX] = pixel[3]
                border += 1
    
    return (area, border)


def initSquareMatrix(biggestX1, biggestY1, smallestX1, smallestY1, visitedCoords):
    squareMatrix = [ [] for i in range(biggestY1 - smallestY1 + 1) ]
    for i in range(len(squareMatrix)):
        squareMatrix[i] = [ 0 for i in range(biggestX1 - smallestX1 + 1) ]

    # fill with ones
    for spot in visitedCoords:
        relativeX = spot[0] - smallestX1
        relativeY = spot[1] - smallestY1
        squareMatrix[relativeY][relativeX] = 1

    return squareMatrix


def stackAppend(x, y, stack, targetColor, visitedCoords):
    # explore left pixel
    if (x > 0) and ((x-1, y) not in visitedCoords) and (img[y][x-1] == targetColor):
        visitedCoords.add((x-1, y))
        stack.append((x-1, y)) # will need to check this pixel's neightbors
    
    # explore right pixel
    if (x < w-1) and ((x+1, y) not in visitedCoords) and (img[y][x+1] == targetColor):
        visitedCoords.add((x+1, y))
        stack.append((x+1, y)) # will need to check this pixel's neightbors
        
    # explore top pixel
    if (y > 0) and ((x, y-1) not in visitedCoords) and (img[y-1][x] == targetColor):
        visitedCoords.add((x, y-1))
        stack.append((x, y-1)) # will need to check this pixel's neightbors
        
    # explore bottom pixel
    if (y < h-1) and ((x, y+1) not in visitedCoords) and (img[y+1][x] == targetColor):
        visitedCoords.add((x, y+1))
        stack.append((x, y+1)) # will need to check this pixel's neightbors


def explorePixel(pixel):
    # initialize stack
    stack = [(pixel[0], pixel[1])]
    targetColor = img[pixel[1]][pixel[0]]

    biggestX1  = pixel[0]
    smallestX1 = pixel[0]
    biggestY1  = pixel[1]
    smallestY1 = pixel[1]


    # every element inside here has a 1 in the recolor matrix 
    visitedCoords = set()
    visitedCoords.add((pixel[0], pixel[1]))


    while len(stack) != 0:
        coord = stack.pop()
        x = coord[0]
        y = coord[1]


        if x < smallestX1:
            smallestX1 = x
        if x > biggestX1:
            biggestX1 = x
        if y < smallestY1:
            smallestY1 = y
        if y > biggestY1:
            biggestY1 = y

        stackAppend(x, y, stack, targetColor, visitedCoords)
        

    # initialize to zero
    squareMatrix = initSquareMatrix(biggestX1, biggestY1, smallestX1, smallestY1, visitedCoords)


    # recolor and area check
    smh = len(squareMatrix)   # square matrix height 
    smw = len(squareMatrix[0])
    
    return calcAreaAndBorder(squareMatrix, smh, smw, smallestX1, smallestY1, pixel)



def ricolora(fname, lista, fnameout):
    global img
    global h
    global w

    img = load(fname)
    h = len(img)
    w = len(img[0])


    data = []
    for pixel in lista:
        data.append(explorePixel(pixel))

    save(img, fnameout)

    return data
    # debug = 0

# ricolora("I1.png", [(10,10,(255, 0, 0),(0,0,255))], "")

