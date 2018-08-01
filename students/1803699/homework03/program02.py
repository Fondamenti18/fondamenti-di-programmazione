from immagini import *

def cammino(fname,  fname1):
    scacchiera=load(fname)
    posx=0
    posy=0
    angolo=0
    fstring=''
    spins=0
    white=(255,255,255)
    black=(0,0,0)
    paint(scacchiera,0,0,(0,255,0))
    while spins<4:
        angolo=fixangle(posx,posy,angolo)
        sqcoord=findnext(posx,posy,angolo)
        nextx=sqcoord[0]
        nexty=sqcoord[1]
        sqcolor=scacchiera[nexty][nextx]
        if sqcolor==black or sqcolor==white:
            posx=nextx
            posy=nexty
            scacchiera=paint(scacchiera,posx,posy,(0,255,0))
            spins=0
            fstring+=str(angolo)
        else:
            angolo+=1
            if angolo>3:
                angolo-=4
            spins+=1
    scacchiera=paint(scacchiera,posx,posy,(0,0,255))
    save(scacchiera,fname1)
    return fstring
    
    
def findnext(x,y,angolo):
    if angolo==0:
        nextsq=(x+40,y)
    elif angolo==1:
        nextsq=(x,y+40)
    elif angolo==2:
        nextsq=(x-40,y)
    else:
        nextsq=(x,y-40)
    return nextsq

def fixangle(x,y,angolo):
    if x==0:
        if y==0 and (angolo==2 or angolo==3):
            angolo=0
        elif angolo==2:
            angolo=3
    elif x==560:
        if y==560 and (angolo==0 or angolo==1):
            angolo=2
        elif angolo==0:
            angolo=1
    elif y==0 and angolo==3:
        angolo=0
    elif y==560 and angolo==1:
        angolo=2
    return angolo

def paint(img,x,y,color):
    for i in range(0,40):
        for t in range(0,40):
            img[y+t][x+i]=color
    return img