# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 18:21:18 2017

@author: Daniele
"""

from immagini import *
rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)

def colora_quad(img, x, y, lato, colore):
    for i in range(y,y+lato):
        for j in range(x,x+lato):
            img[i][j]=colore

def cammino(fname,  fname1):
    img=load(fname)
    x=0
    y=0
    colora_quad(img, x, y, 40, verde)
    s=''
    cont=0
    while cont<49:
        
        if x<560:
            if img[y][x+40]==bianco or img[y][x+40]==nero:
                x=x+40
                while img[y][x]==bianco or img[y][x]==nero:
                    if x>=len(img):
                        x=x-40
                        break
                    colora_quad(img, x, y, 40, verde)
                    x=x+40
                    s=s+'0'
                    if x>=len(img):
                        x=x-40
                        break
                    if img[y][x]==rosso or img[y][x]==verde:
                        x=x-40
                        break
        
        
        if y<560:
            if img[y+40][x]==bianco or img[y+40][x]==nero:
                y=y+40
                while img[y][x]==bianco or img[y][x]==nero:
                    if y>=len(img):
                        y=y-40
                        break
                    colora_quad(img, x, y, 40, verde)
                    y=y+40
                    s=s+'1'
                    if y>=len(img):
                        y=y-40
                        break
                    if img[y][x]==rosso or img[y][x]==verde:
                        y=y-40
                        break
        
        
        
        if img[y][x-40]==bianco or img[y][x-40]==nero:
            x=x-40
            while img[y][x]==bianco or img[y][x]==nero:
                if x<0:
                    x=x+40
                    break
                colora_quad(img, x, y, 40, verde)
                x=x-40
                s=s+'2'
                if img[y][x]==rosso or img[y][x]==verde or x<0:
                    x=x+40
                    break
       
        
        
        if img[y-40][x]==bianco or img[y-40][x]==nero:
            y=y-40
            while img[y][x]==bianco or img[y][x]==nero:
                if y<0:
                    y=y+40
                    break
                colora_quad(img, x, y, 40, verde)
                y=y-40
                s=s+'3'
                if img[y][x]==rosso or img[y][x]==verde or y<0:
                    y=y+40
                    break
    

        cont=cont+1
    colora_quad(img, x, y, 40, blu)
    save(img, fname1)
    return s