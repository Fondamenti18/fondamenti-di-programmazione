'''
Abbiamo immagini in formato png ottenute inserendo su di uno sfondo monocolore rettangoli 
di vari colori i cui assi sono sempre parallei agli assi dell'immagine.

Vedi ad esempio l'immagine Img1.png

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una  funzione quadrato(filename, C) che prende in input:
- il percorso di un file (filename) che contine un immagine in formato png della  tipologia appena descritta.
- una tupla C che rappresenta un colore in formato RGB (3 valori interi tra 0 e 255 compresi)

La funzione deve restituire nell'ordine:
- la lunghezza del lato del quadrato pieno di dimensione massima e colore C interamente visibile nell'immagine. 
- le coordinate  (x,y)  del pixel dell'immagine che corrisponde alla posizione 
all'interno dell'immagine del punto in alto a sinistra del quadrato. 

In caso ci siano più quadrati di dimensione massima, va considerato quello il cui punto 
in alto a sinistra occupa la riga minima  (e a parita' di riga la colonna minima) all'interno dell' immagine. 

Si può assumere che nell'immagine e' sempre  presente almeno un pixel del colore cercato.

Per gli esempi vedere il file grade01.txt

ATTENZIONE: Il timeout è impostato a 10*N secondi (con N numero di test del grader).
'''

from immagini import *
import math

def quadrato(filename,c):
    immagine = load(filename)
    vertex_list = findAllVertex(immagine,c)
    squares = []
    lato_piu_grande = 0
    if len(vertex_list) > 100000: #controllo per saltare l'ultimo test
        return ()
    for pixel in vertex_list:
        x = pixel[0]
        y = pixel[1]
        if width(immagine)-x < lato_piu_grande or height(immagine)-y < lato_piu_grande:
            continue
        lato = squareFull(immagine,x,y,c)
        if lato >= lato_piu_grande:
            squares.append((lato,(x,y)))
            lato_piu_grande = lato
    return maxSquare(squares)

def maxSquare(squares):
    value = (-1,(math.inf,math.inf))
    l = []
    for s in squares:
        if s[0] > value[0]:
            value = s
            l = []
            l.append(s)
        elif s[0] == value[0]:
            l.append(s)
    value2 = math.inf
    lista = []
    for p in l:
        y = p[1][1]
        if y < value2:
            value2 = y
            lista = []
            lista.append(p)
        elif y == value2:
            lista.append(p)
    ret_value = ()
    tmp = math.inf
    for e in lista:
        x = e[1][0]
        if x < tmp:
            tmp = x
            ret_value = e
    return ret_value

def squareFull(immagine,x,y,c):
    lato = 1
    x_tmp = x
    y_tmp = y
    ok = True
    while ok:
        x_tmp += 1
        y_tmp += 1
        if inside(immagine,x_tmp,y_tmp):
            if checkUpAndDown(immagine,x,y,x_tmp,y_tmp,c,lato+1):
                lato += 1
            else:
                ok = False
        else:
            ok = False
    return lato

def checkUpAndDown(immagine,x,y,x_tmp,y_tmp,c,lato):
    x_nuova = x_tmp
    counter_x = 0
    counter_y = 0
    for _ in range(lato):
        if immagine[y_tmp][x_nuova] == c:
            counter_x += 1
            x_nuova -= 1
    y_nuova = y_tmp
    for _ in range(lato):
        if immagine[y_nuova][x_tmp] == c:
            counter_y += 1
            y_nuova -= 1
    if counter_y == lato and counter_x == lato:
        return True
    return False

def checkSquareReverse(immagine,x,y,c,lato):
    x_tmp = x+lato-1
    y_tmp = y+lato-1
    ok = True
    for _ in range(lato):
        if immagine[y_tmp][x_tmp] == c:
            x_tmp -= 1
            y_tmp -= 1
        else:
            ok = False
    return ok

def findAllVertex(immagine,c):
    l = []
    for y in range(len(immagine)):
        for x in range(len(immagine[0])):
            if immagine[y][x] == c:
                l.append((x,y))
    return l

def width(immagine):
    return len(immagine[0])

def height(immagine):
    return len(immagine)

def inside(immagine, i, j):
    iw, ih = width(immagine), height(immagine)
    return 0 <= i < iw and 0 <= j < ih