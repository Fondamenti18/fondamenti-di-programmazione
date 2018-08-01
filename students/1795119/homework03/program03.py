from immagini import *
import copy

def analizza(img, x, y, cbase, num):
    if x < len(img) and y < len(img[0]) and x >= 0 and y >= 0:
        if img[x][y] == cbase:
            img[x][y] = num
            return True
    return False

def coda(img, x, y, num):
    lista = []
    lista.append((x,y))
    cbase = img[x][y]
    for elem in lista:
        x = elem[0]
        y = elem[1]
        if analizza(img, x, y, cbase, num):
            lista.append((x-1, y))
            lista.append((x+1, y))
            lista.append((x, y-1))
            lista.append((x, y+1))
    return cbase

def formatta(img):
    num = 0
    colors = set()
    for i,x in enumerate(img):
        for k,y in enumerate(x):
            if not str(y).isnumeric():
                cbase = coda(img, i, k, num)
                colors.add((cbase, num))
                num += 1
    return colors

def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    img = load(fname)
    col = copy.deepcopy(img)
    colors = formatta(img)
    res = []
    f = False
    for i,x in enumerate(lista):
        if f:
            img = copy.deepcopy(col)
            colors = formatta(img)
            f = False
        num = img[x[1]][x[0]]
        a, p, f = colora(col, img, num, x[2], x[3], colors)
        res += [(a, p)]
    save(col, fnameout)
    return res

def colora(img, png, num, c, c2, colors):
    area = 0
    per = 0
    flag = False
    n = len(colors)
    colors.add((c, n))
    if c == c2:
        n2 = n
    else:
        n2 = len(colors)
        colors.add((c2, n2))
    col = len(png[0])
    row = len(png)
    for i,x in enumerate(png):
        for k,y in enumerate(x):
            if y == num:
                if k == 0 or k == col-1 or i == 0 or i == row-1:
                    img[i][k] = c2
                    png[i][k] = n2
                    per += 1
                    continue
                else:
                    if k+1 < col:
                        if img[i][k+1] != img[i][k]:
                            png[i][k] = n2
                            img[i][k] = c2
                            if c2 == img[i][k+1]:
                                flag = True
                            per += 1
                            continue
                    if i+1 < row:
                        if img[i+1][k] != img[i][k]:
                            png[i][k] = n2
                            img[i][k] = c2
                            if c2 == img[i+1][k]:
                                flag = True
                            per += 1
                            continue
                    if i-1 >= 0:
                        if (png[i-1][k] != n or img[i-1][k] != c) and png[i-1][k] != n2:
                            png[i][k] = n2
                            img[i][k] = c2
                            if c2 == img[i-1][k]:
                                flag = True
                            per += 1
                            continue
                    if k-1 >= 0:
                        if (png[i][k-1] != n or img[i][k-1] != c) and png[i][k-1] != n2:
                            png[i][k] = n2
                            img[i][k] = c2
                            if c2 == img[i][k-1]:
                                flag = True
                            per += 1
                            continue
                png[i][k] = n
                img[i][k] = c
                area += 1
    return area, per, flag
