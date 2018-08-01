from immagini import *

def f():
    s=False
    c=False
    return s,c

def fun(c,s):
    if c==True:
        s=True
    return s

def inside(img, x, y):
    return 0 <= y < len(img) and 0 <= x < len(img[0])

def draw(img, x, y, w, h, c):
    for px in range(x, x+w):
        for py in range(y, y+h):
            img[py][px] = c

def cammino(fname,  fname1):
    img = load(fname)
    bl=(0,0,0)
    b=(255,255,255)
    gr=(0,255,0)
    x=40
    y=0
    l=40
    draw(img,0,0,l,l,(0,255,0))
    passi=''
    while True:
        c1 = True
        for i in range(0,15):         #destra
            if inside(img,x,y) and (img[y][x] == bl or img[y][x] == b):
                draw(img,x,y,l,l,gr)
                x += l
                passi += '0'
                s1,c1 = f()
            else:
                x = x-l
                y += l
                s1=fun(c1,s1)
                break
        c2 = True
        for i in range(0,15):                                                         #sotto
            if inside(img,x,y) and (img[y][x] == bl or img[y][x] == b):
                draw(img,x,y,l,l,gr)
                y += l
                passi += '1'
                s2, c2 = f()
            else:
                y = y-l
                x = x-l
                s2=fun(c2,s2)
                break
        c3 = True
        for i in range(0,15):                                                              #sinistra
            if inside(img,x,y) and (img[y][x] == bl or img[y][x] == b):
                draw(img,x,y,l,l,gr)
                x = x-l
                s3, c3 = f()
                passi += '2'
            else:
                x += l
                y = y-l
                if c3 == True:
                    s3 = True
                break
        c4 = True
        for i in range(0,15):                                                                   #sopra
            if inside(img,x,y) and (img[y][x] == bl or img[y][x] == b):
                draw(img,x,y,l,l,gr)
                y = y-l
                passi += '3'
                s4, c4 = f()
            else:
                y += l
                x += l
                if c4 == True:
                    s4 = True
                break
        if s1 == True and s2 == True and s3 == True and s4 == True:
            x = x-l
            draw(img,x,y,l,l,(0,0,255))
            break
    save(img,fname1)
    return passi
