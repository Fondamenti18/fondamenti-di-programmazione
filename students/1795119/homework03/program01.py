from immagini import *
import sys
sys.setrecursionlimit(1000)

def formatta(elem, destra, sotto):
    if destra >= elem and sotto >= elem:
        return elem + 1
    return formatta(elem-1, destra, sotto)

def init(img, c):
    for i,y in enumerate(img):
        for k,x in enumerate(y):
            if x != c:
                img[i][k] = 0
            else:
                img[i][k] = 1
    return img

def res(img):
    l = 0
    ind = 0
    for i,x in enumerate(img):
        if max(x) > l:
            l = max(x)
            ind = i
    return l, (img[ind].index(l)-l+1, ind-l+1)

def quadrato(filename, c):
    png = load(filename)
    img = init(png, c)
    l = (0, (0, 0))
    for i,y in enumerate(img[:-1]):
        for k,x in enumerate(y[:-1]):
            if x != 0:
                destra = img[i][k+1]
                sotto = img[i+1][k]
                diagonale = img[i+1][k+1]
                if diagonale != 0 and destra != 0 and sotto != 0:
                    img[i+1][k+1] = formatta(x, destra, sotto)
    return res(img)
