from immagini import *

percorso = ''
ngiri = 0

def creaPiccola():
    '''creo un'immagine 15x15'''
    img= []   
    for y in range(15):
        img.append([])
        for x in range(15):
            img[y].append((0,0,0))
    return img
            
def clona(imgG, imgP):
    '''copio l'iimagine originale in quella 15x15'''
    for y in range(15):
        for x in range(15):
            imgP[y][x] = imgG[y*40][x*40]
    return imgP

def controlloPix(img, x, y):
    '''controllo se il pixel è contenuto nell'immagine se il colore non è rosso o verde'''
    if 0 <= x < 15 and 0 <= y < 15 and img[y][x] != (255, 0, 0) and img[y][x] != (0, 255, 0):
        return True
    return False

def destra(img, x=0, y=0):
    global ngiri
    global percorso
    for px in range(x, 15):
        if controlloPix(img, px+1, y):
            img[y][px] = (0, 255, 0)
            percorso += '0'
            ngiri = 0
        else:
            ngiri += 1
            if ngiri < 4 : 
                img = giu(img, px, y)
            else:
                img[y][px] = (0, 0, 255)
                return img
            break
    return img

def giu(img, x, y):
    global ngiri
    global percorso
    for py in range (y, 15):
        if controlloPix(img, x, py+1):
            img[py][x] = (0, 255, 0)
            percorso += '1'
            ngiri = 0
        else:
            ngiri += 1
            if ngiri < 4 :
                img = sinistra(img, x, py)
            else:
                img[py][x] = (0, 0, 255)
                return img
            break
    return (img)

def sinistra(img, x, y):
    global ngiri
    global percorso
    for px in range(x, -1, -1):
        if controlloPix(img, px-1, y):
            img[y][px] = (0, 255, 0)
            percorso += '2'
            ngiri = 0
        else:
            ngiri +=1
            if ngiri < 4 :
                img = su(img, px, y)
            else:
                img[y][px] = (0, 0, 255)
                return img
            break
    return (img)

def su(img, x, y):
    global ngiri
    global percorso
    for py in range(y, -1, -1):
        if controlloPix(img, x, py-1):
            img[py][x] = (0, 255, 0)
            percorso += '3'
            ngiri = 0
        else :
            ngiri += 1
            if ngiri < 4:
                img = destra(img, x, py)
            else:
                img[py][x] = (0, 0, 255)
                return img
            break
    return (img)

def converti(imgG, imgP):
    '''copio l'immagine piccola in quella più grande'''
    for y in range(0, 15):
        for x in range(0, 15):
            for py in range(y*40, y*40+40):
                for px in range(x*40, x*40+40):
                    imgG[py][px] = imgP[y][x]
    return imgG

def cammino(fname,  fname1):
    global percorso
    percorso = ''
    
    img = load(fname)
    imgp = clona(img , creaPiccola())
    
    imgp = destra(imgp)
    
    img = converti(img, imgp)
    
    save(img, fname1)

    return(percorso)