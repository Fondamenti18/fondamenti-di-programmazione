from immagini import save
from collections import deque
import png
    
def ricolora(fname, lista, fnameout):

    img = load(fname)
    h = len(img)
    w = len(img[0])
    ls = []
    for el in lista:
        A = 0
        P = 0
        coord = up(img, h, w, el, el[0], el[1], img[el[1]][el[0]])
        larg = wide(img, coord, img[el[1]][el[0]], w)
        alt = heig(img, coord, img[el[1]][el[0]], h)
        img, A, P = area(larg, alt, img[el[1]][el[0]], coord, img, el[2], el[3])
        ls.append( (A,P) )
    save(img, fnameout)
    return list(ls)

def up(img, h, w, el, x, y, c):

    while img[y-1][x] and img[y-1][x] == c:
        y -= 1
    while img[y][x-1] and img[y][x-1] == c:
        x -= 1
    return (y,x)

def wide(img, coord, c, w):

    cont = 0
    apg = coord[1]
    while img[coord[0]][apg] == c and apg < w-1:
        cont += 1
        apg += 1
        if apg == w-1:
            cont += 1
    return cont

def heig(img, coord, c, h):

    cont = 0
    apg = coord[0]
    while img[apg][coord[1]] == c and apg < h-1:
        cont += 1
        apg += 1
        if apg == h-1:
            cont += 1
    return cont

def area(larg, alt, c, coord, img, colore, colore2):

    cont = 0
    cont2 = 0
    x = coord[1]
    y = coord[0]
    for j in range(alt):
        for i in range(larg):
            if y+j == y or x+i == x or y+j == y+alt-1 or x+i == x+larg-1:
                img[y+j][x+i] = colore2
                cont2 += 1
            elif img[y+j][x+i] == c:
                cont += 1
                img[y+j][x+i] = colore
    return img, cont, cont2

def load(fname):

    with open(fname, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = deque()
        for line in png_img:
            l = deque()
            for i in range(0, len(line), 3):
                l+=[(line[i], line[i+1], line[i+2])]
            img+=[l]
        return img
    
if __name__=='__main__':
    
    lista=[(5*i+2,5*i+2,(0,255-6*i,0),(0,0,255-6*i)) for i in range(40)]
    print(ricolora ('I3.png',lista,'test8.png') )