# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 15:04:35 2017

@author: studente
"""
import png
from immagini import *
import numpy
def ricolora(fname, lista, fnameout):
    img=load(fname)
    risultati=[]
    alt=len(img)-1
    larg=len(img[0])-1
    for lis in lista:
        matrice=numpy.zeros((alt+1, larg+1), dtype=bool)
        listabordo=[]
        color=img[lis[1]][lis[0]]
        replace=lis[2]
        bordo=lis[3]
        coda=[[lis[1], lis[0], [True,True,True,True]]]
        perimetro=0
        area=1
        inizio=[lis[1], lis[0]]
        ''' s '''
        nome=' 1'
        test=0
        while coda:
            fb=0
            x=coda[0][1]
            y=coda[0][0]
            if coda[0][2][0]:
                try:
                    if matrice[y+1][x]:
                        fb+=1
                    elif img[y+1][x]==color:
                        coda.append([y+1, x,[True, False,True,True]])
                        img[y+1][x]=replace
                        matrice[y+1][x]=True
                        fb+=1
                        area+=1
                except IndexError:
                    pass
            else: fb+=1
            if coda[0][2][1]:
                if y>0:
                    if matrice[y-1][x]:
                        fb+=1
                    elif img[y-1][x]==color:
                        coda.append([y-1, x,[False,True,True,True]])
                        img[y-1][x]=replace
                        matrice[y-1][x]=True
                        fb+=1
                        area+=1
            else: fb+=1
            if coda[0][2][2]:
                try:
                    if matrice[y][x+1]:
                        fb+=1
                    elif img[y][x+1]==color:
                        coda.append([y, x+1,[True,True,True, False]])
                        img[y][x+1]=replace
                        matrice[y][x+1]=True
                        fb+=1
                        area+=1
                except IndexError:
                    pass
            else: fb+=1
            if coda[0][2][3]:
                if x>0:
                    if matrice[y][x-1]:
                        fb+=1
                    elif img[y][x-1]==color:
                        coda.append([y, x-1,[True,True,False,True]])
                        img[y][x-1]=replace
                        matrice[y][x-1]=True
                        fb+=1
                        area+=1
            else: fb+=1
            if fb<4:
                listabordo.append([y, x])
            coda.remove(coda[0]) 
        img[inizio[0]][inizio[1]]=replace
        listabordo=set(map(tuple,listabordo))
        for elem in listabordo:
            img[elem[0]][elem[1]]=bordo
            perimetro+=1
            area-=1
        risultati.append((area, perimetro))
        ''' test '''
        if test<5:
            test+=1
            nome=' 1'+nome
            save(img, nome)
    save(img, fnameout)
    return risultati