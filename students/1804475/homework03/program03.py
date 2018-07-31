from immagini import *
import copy
import sys
sys.setrecursionlimit(3300)
 
def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    w = load(fname)
    risulato = list()
    vero = True
    errato = False
    coordinata = lista[0][0]
    ascissa = lista[0][1]
    for s in lista:
        if s[0] != coordinata or s[1] != ascissa:
            errato = True
            break
    if not errato:
        immagine = propagation(copy.deepcopy(w), coordinata, ascissa)
        vero= False
        z = [(w[ascissa][coordinata], 1)]
    for i,s in enumerate(lista):
        coordinata = s[0]
        ascissa = s[1]
        if vero:
            z = list()
            immagine = copy.deepcopy(w)
            elimina(immagine, z)
            vero = False
        num = immagine[ascissa][coordinata]
        a, p, vero = coloration(w, immagine, num, s[2], s[3], z)
        risulato.append((a, p))
    save(w, fnameout)
    return risulato

def adjacent(img, r, h,  v):
    f = r.copy()
    for i in f[h:]:
        q = i[0]
        o = i[1]
        if (q,o-1) not in r and o-1 >= 0:
            if img[q][o-1] == v:
                img[q][o-1] = 1
                r+=[(q, o-1)]
        if (q-1,o) not in r and q-1 >= 0:
            if img[q-1][o] == v:
                img[q-1][o] = 1
                r+=[(q-1, o)]
        if (q+1,o) not in r and q+1 < len(img):
            if img[q+1][o] == v:
                img[q+1][o] = 1
                r+=[(q+1, o)]
        if (q,o+1) not in r and q+1 < len(img[0]):
            if img[q][o+1] == v:
                img[q][o+1] = 1
                r+=[(q, o+1)]
    if r != f:
        adjacent(img, r, len(f), v)
    return


def colori(g, l):
    for i in g:
        if i[1] == l:
            return i[0]
 
def elimina(png, colors):
    s = 0
    for r,t in enumerate(png):
        for c,f in enumerate(t):
            if not str(f).isnumeric():
                png[r][c] = s
                colors.append((f, s))
                h = f
                s =s+ 1
            else:
                h = colori(colors, f)
            if c+1 < len(png[0]):
                if png[r][c+1] == h:
                    png[r][c+1] = png[r][c]
            if r+1 < len(png):
                if png[r+1][c] == h:
                    png[r+1][c] = png[r][c]
 

 
def propagation(png, n, f):
    lista = [(n,f)]
    s = png[n][f]
    png[n][f] = 1
    adjacent(png, lista, 0, s)
    return png
 
def coloration(img, png, n, col, bordo, ss):
    a = 0
    peri = 0
    val = len(ss)
    ss += [(col, val)]
    val2 = val
    if col != bordo:
        val2 = len(ss)
        ss += [(bordo, val2)]
    e = False
    for r,x in enumerate(png):
        for c,y in enumerate(x):
            if y == n:
                if c == 0 or c == len(png[0])-1 or r == 0 or r == len(png)-1:
                    img[r][c] = bordo
                    png[r][c] = val2
                    peri =peri+ 1
                    continue
                else:
                    if r+1 < len(png):
                        if img[r+1][c] != img[r][c]:
                            if bordo == img[r+1][c]:
                                e = True
                            img[r][c] = bordo
                            png[r][c] = val2
                            peri =peri+ 1
                            continue
                    if r-1 >= 0:
                        if img[r-1][c] != img[r][c] and img[r-1][c] != bordo and png[r-1][c] != val:
                            if bordo == img[r-1][c]:
                                e = True
                            img[r][c] = bordo
                            png[r][c] = val2
                            peri =peri+ 1
                            continue
                    if c+1 < len(png[0]):
                        if img[r][c+1] != img[r][c]:
                            if bordo == img[r][c+1]:
                                e = True
                            img[r][c] = bordo
                            png[r][c] = val2
                            peri =peri+ 1
                            continue
                    if c-1 >= 0:
                        if img[r][c-1] != img[r][c] and img[r][c-1] != bordo and png[r][c-1] != val:
                            if bordo == img[r][c-1]:
                                e = True
                            img[r][c] = bordo
                            png[r][c] = val2
                            peri =peri+ 1
                            continue
                img[r][c] = col
                png[r][c] = val
                a =a+ 1
    return a, peri, e
 



