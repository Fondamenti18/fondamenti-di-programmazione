from immagini import *
nero=(0,0,0)
bianco=(255,255,255)
verde=(0,255,0)
blue=(0,0,255)
rosso=(255,0,0)
def cammino(fname,  fname1):
    im=load(fname)
    s=''
    a1,b1,gr=go_right(im,0,0)
    s+=gr[1:]
    while True:
        c1,d1,gd=go_down(im,a1+40,b1)
        s+=gd
        e1,f1,gl=go_left(im,c1,d1-40)
        s+=gl
        g1,h1,gu=go_up(im,e1-40,f1)
        s+=gu
        a1,b1,gr=go_right(im,g1,h1+40)
        s+=gr
        if c1==e1==g1==a1 and d1==f1==h1==b1: # if all the coordinates are same 
            if s[-1]==str(3):
                draw_quad(im,g1,h1,40,blue)
            if s[-1]==str(2):
                 draw_quad(im,e1,f1,40,blue)
            if s[-1]==str(1):
                 draw_quad(im,c1,d1,40,blue)
            if s[-1]==str(0):
                 draw_quad(im,a1,b1,40,blue)
            break                             # then break the while loop
    save(im,fname1)
    return s

def go_right(im,x,y): # go right function
    moves=''
    while True:
        if IndexError:
            try:
                im[x][y]==nero or im[x][y]==bianco
            except IndexError:
                y-=40
                break
        if im[x][y]==nero or im[x][y]==bianco:
            draw_quad(im,x,y,40,verde)
            y+=40
            moves+='0'
        else:
            y-=40
            break
    return x,y,moves

def go_down(im,x,y): # go down function
    moves=''
    while True:
        if IndexError:
            try:
                im[x][y]==nero or im[x][y]==bianco
            except IndexError:
                x-=40
                break
        if im[x][y]==nero or im[x][y]==bianco:
            draw_quad(im,x,y,40,verde)
            x+=40
            moves+='1'
        else:
            x-=40
            break
    return x,y,moves

def go_left(im,x,y): #go left function
    moves=''
    while True:
        if y<0:
            y+=40
            break
        if im[x][y]==(0,0,0) or im[x][y]==(255,255,255):
            draw_quad(im,x,y,40,verde)
            y-=40
            moves+='2'
        else:
            y+=40
            break
    return x,y,moves
    
def go_up(im,x,y): #go up function
    moves=''
    while True:
        if x<0:
            x+=40
            break
        if im[x][y]==nero or im[x][y]==bianco:
            draw_quad(im,x,y,40,verde)
            x-=40
            moves+='3'
        else:
            x+=40
            break
    return x,y,moves
    
def draw_quad(img,r,co,h,c): #draw square function
    for i in range(r,r+h):
        for j in range(co,co+h):
            img[i][j]=c
            
