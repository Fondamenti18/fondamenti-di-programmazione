from immagini import *

def findSqr(img, lim):
    
    for i in range(len(img)):
        occ = 0
        for j in range(len(img[0])):
            if img[i][j] >= lim:
                occ += 1
            else:
                occ = 0
            if occ == lim:
                return True, (i, j - lim + 1)
    return False, (None, None)
    


def quadrato(filename,c):
    img = load(filename)
    x = 0
    y = 0
    
    for i in range(len(img)):
        for j in range(len(img[0])):
            if img[i][j] == c:
                img[i][j] = 1
            else:
                img[i][j] = 0
    
    for i in range(len(img[0])):
        occ =  0
        for j in range(len(img) - 1, -1, -1):
            if img[j][i] == 1:
                occ += 1
                img[j][i] = occ
            else:
                occ = 0
    
    lim = 1
    
    while True:
        
        result = findSqr(img, lim)
        if not result[0]:
            break
        x = result[1][0]
        y = result[1][1]
        lim += 1
        
        
    return lim - 1, (y,x)