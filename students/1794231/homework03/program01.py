# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 20:01:52 2017

@author: VALERIO
"""
def load(fname):
    with open(fname, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            l = []
            for i in range(0, len(line), 3):
                l+=[(line[i], line[i+1], line[i+2])]
            img+=[l]
        return img
import numpy
import png
def quadrato(filename,c):
    img=load(filename)
    risultato=[0, (0, 0)]
    alt=len(img)
    larg=len(img[0])
    lriga=0
    listarighe=[]
    ind=0
    fine=False
    lung=1
    termina=0
    matrice=numpy.ones((alt, larg), dtype='bool')
    for y in range(alt):
        listarighe.append([])
        for x in range(larg-1, -1, -1):
            if img[y][x]==c:
                lriga+=1
                listarighe[ind].insert(0, lriga)
            else:
                lriga=0
                listarighe[ind].insert(0, 0)
                matrice[y][x]=False
        ind+=1
        lriga=0
    while termina==0:
        fine=False
        for y in range(alt):
            for x in range(larg):
                pos=(x,y)
                if matrice[y][x]:
                    for righeinc in range(lung):
                        if listarighe[y+righeinc][x]>=lung:
                            fine=True
                        else:
                            matrice[y][x]=False
                            fine=False
                            break
                if fine:
                    break
            if fine:
                break
        alt-=1
        larg-=1
        lung+=1
        if fine:
            risultato[0]=lung-1
            risultato[1]=pos
        else:
            termina=1
            
    risultatotup=(risultato[0], risultato[1])
    return risultatotup