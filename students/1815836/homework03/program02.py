
from immagini import *
st=''
def cammino(fname,  fname1):
    global st
    img1=load(fname)
    cr=(255,0,0)
    cv=(0,255,0)
    c=0
    x=0
    y=0
    st=''
    draw_rect(img1,0,0,40,40,cv)
    movimento_est(x,y,img1,cr,cv,c)
    save(img1,fname1)
    return(st)          
def movimento_est(x,y,img1,cr,cv,c):
    global st 
    if c>4:
        draw_rect(img1,y,x,40,40,(0,0,255))
        return(st)
    w=True
    while w==True :
        if ((y+40)<=599) and (img1[x][y+40]!=cr) and (img1[x][y+40]!=cv):
            y=y+40
            st=st+'0'
            draw_rect(img1,y,x,40,40,cv)
            c=0
        else:
            w=False
    c+=1
    movimento_sud(x,y,img1,cr,cv,c)        
def movimento_sud(x,y,img1,cr,cv,c):
    global st
    w=True
    while w==True :
        if (x+40)<=599 and img1[x+40][y]!=cr and img1[x+40][y]!=cv:
            x=x+40
            st=st+'1'
            draw_rect(img1,y,x,40,40,cv)
            c=0
        else:
            w=False
    c+=1
    movimento_ovest(x,y,img1,cr,cv,c)         
def movimento_ovest(x,y,img1,cr,cv,c):
    global st
    w=True
    while w==True :
        if  0<=(y-40) and img1[x][y-40]!=cr and img1[x][y-40]!=cv:
            y=y-40
            st=st+'2'
            draw_rect(img1,y,x,40,40,cv)
            c=0
        else:
            w=False
    c+=1
    movimento_nord(x,y,img1,cr,cv,c)    
def movimento_nord(x,y,img1,cr,cv,c):
    global st
    w=True
    while w==True :
        if 0<=(x-40) and img1[x-40][y]!=cr and img1[x-40][y]!=cv:
            x=x-40
            st=st+'3'
            draw_rect(img1,y,x,40,40,cv)
            c=0
        else:
            w=False
    c+=1
    movimento_est(x,y,img1,cr,cv,c)
def draw_rect(img,x,y,w,h,c):
    for px in range(x,x+w):
        for py in range(y,y+h):
            img[py][px]=c
        try:
            img[py][px]=c
        except IndexError:
            pass

