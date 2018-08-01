from immagini import *
    
def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    img = load(fname)
    h = len(img)
    w = len(img[0])
    ris = list()
    ins = set()
    for tup in lista:
        area = list()
        perimetro = list()
        c = img[tup[1]][tup[0]]
        found = set()
        col1 = tup[2]
        col2 = tup[3]
        ins.add( (tup[1],tup[0]) )
        while ins:
            el = ins.pop()
            x = el[1]
            y = el[0]
            if (y-1) >= 0 and (y-1,x) not in found and img[y-1][x] == c:
                ins.add( (y-1,x) )
                found.add( (y-1,x) )
                if check_sup(img, y-1, x, h, w, c) == 0:
                    area.append( (y-1,x) )
                else:
                    perimetro.append( (y-1,x) )
            if (y+1) <= h-1 and (y+1,x) not in found and img[y+1][x] == c:
                ins.add( (y+1,x) )
                found.add( (y+1,x) )
                if check_inf(img, y+1, x, h, w, c) == 0:
                    area.append( (y+1,x) )
                else:
                    perimetro.append( (y+1,x) )
            if (x-1) >= 0 and (y,x-1) not in found and img[y][x-1] == c:
                ins.add( (y,x-1) )
                found.add( (y,x-1) )
                if check_right(img, y, x-1, h, w, c) == 0:
                    area.append( (y,x-1) )
                else:
                    perimetro.append( (y,x-1) )
            if (x+1) <= w-1 and (y,x+1) not in found and img[y][x+1] == c:
                ins.add( (y,x+1) )
                found.add( (y,x+1) )
                if check_left(img, y, x+1, h, w, c) == 0:
                    area.append( (y,x+1) )
                else:
                    perimetro.append( (y,x+1) )
        ris.append( (len(area), len(perimetro)) )
        for el in area:
            img[el[0]][el[1]] = col1
        for el in perimetro:
            img[el[0]][el[1]] = col2
    save(img, fnameout)
    return ris

def check_sup(img, y, x, h, w, c):
    cont = 3
    if (y-1) >= 0 and img[y-1][x] == c:
        cont -= 1
    if (x-1) >= 0 and img[y][x-1] == c:
        cont -= 1
    if (x+1) <= w-1 and img[y][x+1] == c:
        cont -= 1
    return cont

def check_inf(img, y, x, h, w, c):
    cont = 3
    if (y+1) <= h-1 and img[y+1][x] == c:
        cont -= 1
    if (x-1) >= 0 and img[y][x-1] == c:
        cont -= 1
    if (x+1) <= w-1 and img[y][x+1] == c:
        cont -= 1
    return cont

def check_right(img, y, x, h, w, c):
    cont = 3
    if (y-1) >= 0 and img[y-1][x] == c:
        cont -= 1
    if (y+1) <= h-1 and img[y+1][x] == c:
        cont -= 1
    if (x-1) >= 0 and img[y][x-1] == c:
        cont -= 1
    return cont

def check_left(img, y, x, h, w, c):
    cont = 3
    if (y-1) >= 0 and img[y-1][x] == c:
        cont -= 1
    if (y+1) <= h-1 and img[y+1][x] == c:
        cont -= 1
    if (x+1) <= w-1 and img[y][x+1] == c:
        cont -= 1
    return cont