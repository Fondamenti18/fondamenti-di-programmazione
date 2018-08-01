# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 21:33:16 2017

@author: User
"""
from immagini import *
    
def ricolora(fname, lista, fnameout):
    immagine=load(fname)
    risultato=[]
    img=immagine.copy()
    for (x,y,c1,c2) in lista:
        lista=[(x,y)]
        verificate=[(x,y)]
        area=0
        p=0
        while lista!=[]:
           lista2=lista
           for (px,py) in lista2:
                contatore=0
                if inside(immagine,px,py-1) and immagine[py-1][px]==immagine[py][px] and (px,py-1) not in verificate :
                      verificate.append((px,py-1))
                      lista.append((px,py-1))
                if inside(immagine,px,py+1) and immagine[py+1][px]==immagine[py][px] and (px,py+1) not in verificate  :
                      lista.append((px,py+1))
                      verificate.append((px,py+1))
                if inside(immagine,px-1,py) and immagine[py][px-1]==immagine[py][px] and (px-1,py) not in verificate  :
                      lista.append((px-1,py))
                      verificate.append((px-1,py))
                if inside(immagine,px+1,py) and immagine[py][px+1]==immagine[py][px] and (px+1,py) not in verificate  :
                      lista.append((px+1,py))
                      verificate.append((px+1,py))
                if (px,py-1) in verificate and (px,py+1) in verificate and (px+1,py) in verificate and (px-1,py) in verificate:
                    area+=1
                    img[py][px]=c1
                else:
                    p+=1
                    img[py][px]=c2
                lista.remove((px,py))
        risultato.append((area,p))
        immagine=img.copy()
    save(immagine,fnameout)
    return risultato
                
       
       
          
        
    


def inside(img,x,y):
    return 0<= x < len(img[0]) and 0<= y < len(img)