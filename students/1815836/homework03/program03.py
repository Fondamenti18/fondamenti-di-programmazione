
from immagini import *
import sys
sys.setrecursionlimit(14000)
lista1=[]
def ricolora(fname, lista, fnameout):
    global lista1
    img=load(fname)
    ret=[]
    for s in lista:
        p=0
        y=s[0]
        x=s[1]
        c1=s[2]
        c2=s[3]
        color=img[x][y]
        counter=0
        lista1=[]
        floodfill(img,x,y,c1,c2,color,counter)
        for a in lista1:
            test=0
            if (a[0]+1,a[1]) in lista1:
                test+=1
            if (a[0]-1,a[1]) in lista1:
                test+=1
            if (a[0],a[1]+1) in lista1:
                test+=1
            if (a[0],a[1]-1) in lista1:
                test+=1
            if test!=4:
                img[a[0]][a[1]]=c2
                p+=1
        lung=len(lista1)-p
        ret+=[(lung,p)]
    save(img,fnameout)
    return(ret)
def floodfill(img,x,y,c1,c2,color,counter):
    global lista1
    testc=0
    if (img[x][y] == color):  
        img[x][y] = c1 
        lista1+=[(x,y)]
        if x >= 0:
            floodfill(img,x-1,y,c1,c2,color,counter)
        else:
            testc+=1
        if x < len(img[0])-1:
            floodfill(img,x+1,y,c1,c2,color,counter)
        else:
            testc+=1            
        if y >= 0:
            floodfill(img,x,y-1,c1,c2,color,counter)
        else:
            testc+=1            
        if y < len(img)-1:
            floodfill(img,x,y+1,c1,c2,color,counter)
        else:
            testc+=1
        if(testc==4):
            return
