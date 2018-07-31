#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 18:58:40 2017

@author: teresa
"""
from immagini import *
def inside(img,x,y):
    return 0<=x<len(img[0]) and 0<=y<len(img)

def calcolaaltezza(img,x,y,colore,c1):
    altezza1=0
    altezza2=0
    riga=1
    while(inside(img,x,y-riga)and y-riga>=0):
        if(img[y-riga][x]!=colore):
            break
        else:
            altezza1+=1
            '''img[y-riga][x]=c1'''
            riga+=1
    yvertice=riga
    riga=1
    while(inside(img,x,y+riga) and y+riga<len(img)):
        if(img[y+riga][x]!=colore):
            break
        else:
            altezza2+=1
            '''img[y+riga][x]=c1'''
            riga+=1
    return yvertice,altezza1+altezza2+1
   



def calcolalarghezza(img,x,y,colore,c1):
    larghezza1=0
    larghezza2=0
    colonna=1
    while(inside(img,x-colonna,y)and x-colonna>=0):
        if(img[y][x-colonna]!=colore):
            break
        else:
            larghezza1+=1
            '''img[y][x-colonna]=c1'''
            colonna+=1
    xvertice=colonna
    colonna=0
    while(inside(img,x+colonna,y) and x+colonna<len(img[0])):
        if(img[y][x+colonna]!=colore):
            break
        else:
            larghezza2+=1
            '''img[y][x+colonna]=c1'''
            colonna+=1
    return xvertice,larghezza1+larghezza2
   
def ricolora(fname,lista,fnameout):
    img=load(fname)
    lista1=[]
    area=0
    perimetro=0
    xvertice=0
    yvertice=0
    k=1
    for g in lista:
        area=0
        perimetro=0
        x=g[0]
        y=g[1]
        c1=g[2]
        c2=g[3]
        colore=img[y][x]
        
        xv,larghezza=calcolalarghezza(img,x,y,colore,c1)
        yv,altezza=calcolaaltezza(img,x,y,colore,c1) 
        t=int((len(img))/(altezza))
        
        '''for riga in range(yvertice,yvertice+altezza):
            for colonna in range(xvertice,xvertice+larghezza):
                if(img[riga][colonna]==colore ):
                    img[riga][colonna]=c2
        
            for riga in range(yvertice+1,yvertice+altezza-1):
                for colonna in range(xvertice+1,xvertice+larghezza-1):
                    if(img[riga][colonna]==c2 ):
                        img[riga][colonna]=c1  '''
        
        
        
        
         
        for riga in range(yvertice,yvertice+altezza):
            for colonna in range(xvertice,xvertice+larghezza):
                if(img[riga][colonna]==colore ):
                    img[riga][colonna]=c2
        
        for riga in range(yvertice+1,yvertice+altezza-1):
            for colonna in range(xvertice+1,xvertice+larghezza-1):
                if(img[riga][colonna]==c2 ):
                    img[riga][colonna]=c1      
        
        area=(larghezza-2)*(altezza-2)
        perimetro=2*larghezza+2*(larghezza-2)
        save(img,fnameout)
        lista1+=[(area,perimetro)]
        xvertice=xvertice+larghezza
        k+=1
        if(k>t+1):
         xvertice=0
         yvertice=yvertice+altezza
        
        
    return  lista1