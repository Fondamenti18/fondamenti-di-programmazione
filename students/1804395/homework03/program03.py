
from immagini import *
from sys import setrecursionlimit

h, w= 0, 0
controllo=set()

def outRange(y, x):
    return not (-1<y<h and -1<x<w)

def colora (img, backColor, x, y, c1, c2):
    global controllo
    controllo.add((x,y))
    A, P, border= 0, 0, 0
    for px in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if((px[0], px[1]) in controllo): continue
        controllo.add((x,y))
        if outRange(px[1], px[0]):
            border=1
        elif img[px[1]][px[0]]== backColor:
            commodo= colora(img, backColor, px[0], px[1], c1, c2)
            A+= commodo[0]
            P+= commodo[1]
        else:
            border=1
    if border:
        P+=1
        img[y][x]= c2
    else:
        A+=1
        img[y][x]= c1
    return A, P
  
def ricolora(fname, lista, fnameout):
    setrecursionlimit(99999999)
    img= load(fname)
    global h, w, controllo
    h= len(img)
    w= len(img[1])
    result= []
    for quadrupla in lista:
        controllo=set()
        area, perimetro= colora(img, img[quadrupla[1]][quadrupla[0]], *quadrupla)
        result.append((area, perimetro))
    save(img, fnameout)
    return result
    

