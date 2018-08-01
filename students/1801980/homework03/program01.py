# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 07:28:35 2017

@author: ricca
"""
import png

from immagini import *


def funzione(img,riga,colonna,c):
    contx=0
    conty=0
    for l in range(riga, len(img)):
        if img[l][colonna]==c:
            contx +=1
        else:
            break
    for g in range(colonna, len(img[0])):
        if img[riga][g]==c:
            conty+=1
        else: 
            break
    contz = min(contx,conty)
    for l in range(riga, riga+contz):
        for t in range(colonna, colonna+contz):
            if img[l][t]!=c:
               return(-1)
    return contz
        
                       
def quadrato(filename,c):
    img=load(filename)
    lista=[]
    for riga in range (0,len(img)):
        for colonna in range (0,len(img[0])):
            if img[riga][colonna]==c and img[riga-1][colonna]!=c and img[riga][colonna-1]!=c: 
                coordinate=colonna,riga
                contz = funzione(img,riga,colonna,c)
                lista.append((contz, coordinate))
    massimo=scegli(lista)
    return(massimo)

def scegli(lista):
    massimo=lista[0]
    for i in range(1,len(lista)):
        temp = lista[i]
        if temp[0] > massimo[0]:
            massimo=temp
            continue
        if lista[i][0]==massimo[0]:
            if temp[1][0]<massimo[1][0]:
                massimo=temp
                continue
            elif temp[1][0]>massimo[1][0]:
                continue
            if temp[1][1]<massimo[1][1]:
                massimo=temp
                continue
            elif temp[1][1]>massimo[1][1]:
                continue
    return(massimo)
           