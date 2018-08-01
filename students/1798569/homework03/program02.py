
from immagini import *

rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
quad=40

def inside(img, x, y):
    return 0 <= y < len(img) and 0 <= x < len(img[0])

def draw_rect(img, x, y, w, h, c):
    for px in range(x, x+w):
        for py in range(y, y+h):
            img[py][px] = c

def cammino(fname,  fname1):
    img = load(fname)
    x=40
    y=0
    end=[]
    continua=[]
    if inside (img,x,y):        
        draw_rect(img,0,0,quad,quad,verde)
    listaP=' '
    cnt=0
    '''Riempimento liste di controllo'''
    while cnt<4:    
        continua+=[True]
        end+=[False]
        cnt+=1
    '''Ciclo in cui il robot continua a muoversi finchè non rimane bloccato in ogni direzione'''
    while True:
        
        '''Movimento a destra'''
        continua[0] = [True]
        while True:    
            if inside(img,x,y) and img[y][x] != rosso and img[y][x] != verde:
                draw_rect(img,x,y,quad,quad,verde)
                x += quad
                listaP += '0'
                end[0]= [False]
                continua[0] = [False]
            else:
                x -= quad
                y += quad
                if continua[0] == [True]:
                    '''Il robot da questa posizione non può muoversi a destra'''
                    end[0] = [True]
                break
                    
        '''Movimento sotto'''
        continua[1] = [True]
        while True:                                                         
            if inside(img,x,y) and img[y][x] != rosso and img[y][x] != verde:
                draw_rect(img,x,y,quad,quad,verde)
                y += quad
                listaP += '1'
                end[1] = [False]
                continua[1] = [False]
            else:
                y -= quad
                x -= quad              
                if continua[1] == [True]:
                    '''Il robot da questa posizione non può muoversi sotto'''
                    end[1] = [True]
                break
                    
        '''Movimento a sinistra'''
        continua[2] = [True]
        while True:                                                              
            if inside(img,x,y) and img[y][x] != rosso and img[y][x] != verde:
                draw_rect(img,x,y,quad,quad,verde)
                x -= quad
                end[2] = [False]
                listaP += '2'
                continua[2] = [False]
            else:
                x += quad
                y -= quad
                if continua[2] == [True]:
                    '''Il robot da questa posizione non può muoversi a sinistra'''
                    end[2] = [True]
                break
                    
        '''Movimento sopra'''
        continua[3] = [True]
        while True:                                                                  
            if inside(img,x,y) and img[y][x] != rosso and img[y][x] != verde:
                draw_rect(img,x,y,quad,quad,verde)
                y -= quad
                end[3] = [False]
                listaP += '3'
                continua[3] = [False]
            else:
                y += quad
                x += quad
                if continua[3] == [True]:
                    '''Il robot da questa posizione non può muoversi sopra'''
                    end[3] = [True]
                break
            
        '''Controlla che il robot sia rimasto bloccato in ogni direzione'''
        if end[0] == [True] and end[1] == [True] and end[2] == [True] and end[3] == [True]:
            x -= quad
            if inside (img,x,y):
                draw_rect(img,x,y,quad,quad,blu)
            break
    while listaP[0]==' ':     
        listaP=listaP[1:]  
    save(img,fname1)
    return listaP


            

    


    
    




