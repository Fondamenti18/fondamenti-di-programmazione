
from immagini import *

def coloreSquare(img, position, c=(0, 255, 0)):
    for y in range(40):
        for x in range(40):
            img[position[0]+y][position[1]+x]= c
    return 

def cammino(fname,  fname1):
    result=''
    step=0
    controll=0
    position=[0,0]
    direction=[40,0,-40,0]
    img=load(fname)
    coloreSquare(img, position)
    while controll<5:
        if not(-1<(position[0]+direction[step%4-1])< 600 and -1<(position[1]+direction[step%4])< 600)or img[position[0]+direction[step%4-1]][position[1]+direction[step%4]] in {(255, 0, 0), (0, 255, 0)}:
            step+=1
            controll+=1
        else:#if img[position[0]+direction[step%4-1]][position[1]+direction[step%4]] in {white, black}:
            position[0]+=direction[step%4-1]
            position[1]+=direction[step%4]
            coloreSquare(img, position)
            result+=(str(step%4))
            controll=0
    coloreSquare(img, position, (0, 0, 255))
    save(img, fname1)
    return result
    
    
