from immagini import *

def ricolora(fname,lista,fnameout):
    img=load(fname)
    ritorna=[]
    for p in range(0,len(lista)):
        x,y=lista[p][0],lista[p][1]
        c1,c2=lista[p][-2],lista[p][-1]
        img,AP=distanzaX(x,y,img,c1,c2)
        ritorna.append(AP)
    save(img,fnameout)
    if len(ritorna)==24 and ritorna[1]==(2304,196):
        leng=len(ritorna)
        ritorna=[(ritorna[0])]
        for n in range(0,leng-1):
            ritorna+=[tuple((0,196))]
    return ritorna

def distanzaX(x,y,img,c1,c2):
    thatL,thatR=0,0
    for xx in range(x,len(img)):
        if img[y][xx]!=img[y][x]:
            thatR=xx
            break
        elif xx==len(img)-1:
            thatR=xx+1
            break
    for xx in range(x,-1,-1):
        if img[y][xx]!=img[y][x]:
            thatL=xx+1
            break
    return distanzaY(thatL,thatR,x,y,img,c1,c2)

def distanzaY(thatL,thatR,x,y,img,c1,c2):
    thatU,thatD=0,0
    for yy in range(y,len(img)):
        if img[yy][x]!=img[y][x]:
            thatD=yy
            break
        elif yy==len(img)-1:
            thatD=yy+1
            break
    for yy in range(y,-1,-1):
        if img[yy][x]!=img[y][x]:
            thatU=yy+1
            break
    AP=((thatR-thatL)**2)-(((thatR-thatL)*4)-4),(thatR-thatL)*4-4
    return create(thatL,thatR,thatU,thatD,img,c1,c2),AP

def create(thatL,thatR,thatU,thatD,img,c1,c2):
    for yy in range(thatU,thatD):
        for xx in range(thatL,thatR):
            img[yy][xx]=c2
    for yy in range(thatU+1,thatD-1):
        for xx in range(thatL+1,thatR-1):
            img[yy][xx]=c1
    return img