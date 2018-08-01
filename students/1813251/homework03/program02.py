# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 08:02:58 2017

@author: Alessio
"""

from immagini import *

def versoon(img, w, verso, axy, contatore=0):

    if contatore > 4: return False
    if  verso == 0:
        return destra(img, w, verso, axy, len(img), contatore)
    elif verso == 1:
        return giu(img, w, verso, axy, len(img), contatore)
    elif verso == 2:
        return sinistra(img, w, verso, axy, len(img), contatore)
    elif verso == 3:
        return su(img, w, verso, axy, len(img), contatore)
    else: return False

def destra(img, w, verso, axy, l, contatore):

    if axy[1] == l-w:
        return versoon(img, w, 1, axy, contatore+1)
    elif img[axy[0]][axy[1]+w] == (255,255,255) or img[axy[0]][axy[1]+w] == (0,0,0) :
        colora(img, w, axy)
        return [0, [axy[0], axy[1]+w]]
    else: return versoon(img, w, 1, axy, contatore+1)
    
def sinistra(img, w, verso, axy, l, contatore):

    if axy[1] == 0:
        return versoon(img, w, 3, axy, contatore+1)
    elif img[axy[0]][axy[1]-w] == (255,255,255) or img[axy[0]][axy[1]-w] == (0,0,0):
        colora(img, w, axy)
        return [2, [axy[0], axy[1]-w]]
    else: return versoon(img, w, 3, axy, contatore+1)

def su(img, w, verso, axy, h, contatore):

    if axy[0] == 0:
        return versoon(img, w, 0, axy, contatore+1)
    elif img[axy[0]-w][axy[1]] == (255,255,255) or img[axy[0]-w][axy[1]] == (0,0,0):
        colora(img, w, axy)
        return [3, [axy[0]-w, axy[1]]]
    else: return versoon(img, w, 0, axy, contatore+1)

def giu(img, w, verso, axy, h, contatore):

    if axy[0] == h-w:
        return versoon(img, w, 2, axy, contatore+1)
    elif img[axy[0]+w][axy[1]] == (255,255,255) or img[axy[0]+w][axy[1]] == (0,0,0):
        colora(img, w, axy)
        return [1, [axy[0]+w, axy[1]]]
    else: return versoon(img, w, 2, axy, contatore+1)
    
def colora(img, q, bxy, stop = False):
    col = (0,255,0)
    if stop == True: 
        col = (0,0,255)
    for y in range(bxy[0], bxy[0]+q):
        for x in range(bxy[1], bxy[1]+q):
            img[y][x] = col
    return
    

def cammino(fname,  fname1):
    img = load(fname)
    i=40
    bxy = [0, 0]
    versok = 0
    output = ''
    while True:
        array = versoon(img, i, versok, bxy, 0)
        if array != False:
            versok = array[0]
            bxy = array[1]
            output += str(versok)
        else: break
    colora(img, i, bxy, True)
    save(img, fname1)
    return output
