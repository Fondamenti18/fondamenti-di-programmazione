from immagini import *

def quadrato(filename,c):
    img=load(filename)
    lmax=0
    storedn=1
    lenrow=len(img[0])
    lencol=len(img)
    storedt=lenrow+1
    for i in range(0,lencol-lmax):
        row=img[i]
        for t in range(0,lenrow):
            if lenrow>t+lmax and lencol>i+lmax:
                if row[t]==c and row[t+lmax]==c and img[i+lmax][t]==c and img[i+lmax][t+lmax]==c:
                    if t==storedt:
                        n=storedn
                    else:
                        n=1
                    while t+n+1<lenrow and i+n+1<lencol:
                        if addtosidelen(img,t,i,n,c)=='Go':
                            n+=1
                        else:
                            break
                    if n>lmax:
                            lmax=n
                            coords=(t,i)
                    storedn=n-1
                    storedt=t+1
    return (lmax,coords)


def addtosidelen(img,x,y,sidelen,c):
    checkrow=y+sidelen
    checkcol=x+sidelen
    for i in range(0,sidelen):
        if img[checkrow][x+i]==c and img[y+i][checkcol]==c:
            continue
        else:
            return 'Stop'
    return 'Go'

def decolorside(img,x,y,sidelen):
    for i in range(0,sidelen):
        img[y][x+i]=(256,256,256)
    return img