import png

from immagini import *

def colora_verde(img,x,y):
    for i in range(x,x+40):
        for j in range(y,y+40):
            img[i][j]=(0,255,0)
    return(img)

def colora_blu(img,x,y):
    for i in range(x,x+40):
        for j in range(y,y+40):
            img[i][j]=(0,0,255)
    return(img)

def cammino(fname,fname1):
    img=load(fname)
    x=0
    y=0
    stringa=''
    cont=0
    while True:
        while True:
            if cont==4:
                img=colora_blu(img,x,y)
                save(img,fname1)
                return(stringa)
            y=y+40
            if y>=len(img):
                cont+=1
                y=y-40
                break
            if img[x][y]==(255,255,255) or img[x][y]==(0,0,0):
                cont=0
                img=colora_verde(img,x,y-40)
                #print(img[x][y-40])
                #print('\n')
                stringa+='0'
            else:
                cont+=1
                y=y-40
                break
       #print(stringa+'\n')
        #print(str(cont)+'\n') 
        while True:
            if cont==4:
                img=colora_blu(img,x,y)
                save(img,fname1)
                return(stringa)
            x=x+40
            if x>=len(img):
                cont+1
                x=x-40
                break
            if img[x][y]==(255,255,255) or img[x][y]==(0,0,0):
                cont=0
                img=colora_verde(img,x-40,y)
                stringa+='1'
            else:
                cont+=1
                x=x-40
                break
        #print(stringa+'\n')
        #print(str(cont)+'\n') 
        while True:
            if cont==4:
                img=colora_blu(img,x,y)
                save(img,fname1)
                return(stringa)
            y=y-40
            if y<0:
                cont+=1
                y=y+40
                break
            if img[x][y]==(255,255,255) or img[x][y]==(0,0,0):
                cont=0
                img=colora_verde(img,x,y+40)
                stringa+='2'
            else:
                cont+=1
                y=y+40
                break
        #print(stringa+'\n')
       # print(str(cont)+'\n') 
        while True:
            if cont==4:
                img=colora_blu(img,x,y)
                save(img,fname1)
                return(stringa)
            x=x-40
            #print(img[x][y])
            if x<0:
                cont+=1
                x=x+40
                break
            if img[x][y]==(255,255,255) or img[x][y]==(0,0,0):
                cont=0
                img=colora_verde(img,x+40,y)
                stringa+='3'
            else:
                cont+=1
                x=x+40
                break
        #print(stringa+'\n')
        #print(str(cont)+'\n')            