from immagini import *

def cammino(fname,  fname1):
    img=load(fname)
    x=0
    y=0
    intention='right'
    white=(255,255,255)
    black=(0,0,0)
    green=(0,255,0)
    blue=(0,0,255)
    condition = True
    steps=''
    turns_counter=0
    while condition:
        if turns_counter == 4:
            img=color(x,y,blue,img)
            save(img,fname1)
            condition=False
            return steps
        else: intention, turns_counter, steps, x, y, img= move_side(intention, turns_counter, steps, x, y, img, green, black, white)

def color(x,y,color,img):
    for i_y,row in enumerate(img[y:y+40]):
        for i_x,item in enumerate(row[x:x+40]):
            img[y+i_y][x+i_x] = color
    return img

def move_side(intention, turns_counter, steps, x, y, img, green, black, white):
    if intention == 'right':
        intention, turns_counter, steps, x, y, img=move_right(intention, turns_counter, steps, x, y, img, green, black, white)
    elif intention == 'left':
        intention, turns_counter, steps, x, y, img=move_left(intention, turns_counter, steps, x, y, img, green, black, white)
    else: intention, turns_counter, steps, x, y, img=move_tb(intention, turns_counter, steps, x, y, img, green, black, white)
    return intention, turns_counter, steps, x, y, img

def move_tb(intention, turns_counter, steps, x, y, img, green, black, white):
    if intention == 'down':
        intention, turns_counter, steps, x, y, img=move_down(intention, turns_counter, steps, x, y, img, green, black, white)
    elif intention == 'up':
        intention, turns_counter, steps, x, y, img=move_up(intention, turns_counter, steps, x, y, img, green, black, white)
    return intention, turns_counter, steps, x, y, img

def move_right(intention, turns_counter, steps, x, y, img, green, black, white):
    if x<560:
        if img[y][x+40] == black or img[y][x+40] == white:
            img=color(x,y,green,img)
            x=x+40
            steps+='0'
            turns_counter=0
        else:
            intention='down'
            turns_counter+=1
    else:
        intention='down'
        turns_counter+=1
    return intention, turns_counter, steps, x, y, img

def move_down(intention, turns_counter, steps, x, y, img, green, black, white):
    if y<560:
        if img[y+40][x] == black or img[y+40][x] == white:
            img=color(x,y,green,img)
            y=y+40
            steps+='1'
            turns_counter=0
        else:
            intention='left'
            turns_counter+=1
    else:
        intention='left'
        turns_counter+=1
    return intention, turns_counter, steps, x, y, img

def move_left(intention, turns_counter, steps, x, y, img, green, black, white):
    if x>0:    
        if img[y][x-40] == black or img[y][x-40] == white:
            img=color(x,y,green,img)
            x=x-40
            steps+='2'
            turns_counter=0
        else:
            intention='up'
            turns_counter+=1
    else:
        intention='up'
        turns_counter+=1
    return intention, turns_counter, steps, x, y, img

def move_up(intention, turns_counter, steps, x, y, img, green, black, white):
    if y>0:
        if img[y-40][x] == black or img[y-40][x] == white:
            img=color(x,y,green,img)
            y=y-40
            steps+='3'
            turns_counter=0
        else:
            intention='right'
            turns_counter+=1
    else:
        intention='right'
        turns_counter+=1
    return intention, turns_counter, steps, x, y, img