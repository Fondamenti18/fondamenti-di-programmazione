from immagini import *

h = 0
w = 0

def trovaDim(img):
    '''data un immagine, trova l altezza e la larghezza'''
    global h, w
    h = len(img)
    w = len(img[0])

def convertiFoto(img, col):
    '''creo una matrice di dimensioni = all'immagine e assegno un 1 ai pixel con il colore interessato, altrimenti 0'''
    global h, w
    matrice = []
    for y in range(0, h):
        matrice.append([])
        for x in range(0, w):
            if img[y][x] == col: matrice[y] += [1]
            else : matrice[y] += [0]
    return matrice

def creaBaseMatrice(foto):
    '''creo una matrice ausiliare in cui copio la prima riga e la prima colonna della matreice creata precedentemente'''
    global h, w
    matrice = []
    for y in range(h):
        matrice.append([])
        matrice[y].append(foto[y][0])
    for x in range(1, w):
        matrice[0].append(foto[0][x])
    return matrice

def creaMatrice(foto):
    '''riempio la matrice ausiliare con una formula speciale'''
    global h, w
    matrice = creaBaseMatrice(foto)
    for y in range(1, h):
        for x in range(1, w):
            if foto[y][x] == 1:
                matrice[y].append(min(matrice[y][x-1], matrice[y-1][x-1], matrice[y-1][x]) +1)
            else: 
                matrice[y].append(0)
    
    return matrice

def rilevaQuadrato(matrice):
    '''esamino le righe della matrice ausiliare, ottenendo coordinate e dimensioni del quadrato desiderato'''
    global h
    lato = 0
    for y in range(0,h):
        l = max(matrice[y])
        if lato < l : 
            lato = l
            xi = (matrice[y].index(l))-(l-1)
            yi = y - (l-1)
            
    return (lato, (xi, yi))

def quadrato(filename,c):
    global h, w

    img = load(filename)
    
    trovaDim(img)
    
    matrice = convertiFoto(img, c)
    
    matrice = creaMatrice(matrice)
    
    lato, coordinate = rilevaQuadrato(matrice)
    
    return (lato, coordinate)


