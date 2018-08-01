from immagini import *
def XY(pos):
    return pos*40
def colora(img,x,y,c,range):
    yC = y
    xC = x
    while yC<y+range:
        while xC<x+range:
            img[yC][xC] = c
            xC+=1
        xC = x
        yC+=1
def test(img,x,y,condizione):
    d = {0: 1, 1: 1, 2: -1, 3: -1}
    try:
        if condizione == 0 or condizione == 2:
            if x+d[condizione] == -1 or x+d[condizione] == 16:
                return False
            else:
                if (img[XY(y)][XY(x+d[condizione])] != (255,0,0) and
                        img[XY(y)][XY(x+d[condizione])] != (0,255,0)):
                    return True
                else:
                    return False
        elif condizione == 1 or condizione == 3:
            if y + d[condizione] == -1 or y + d[condizione] == 16:
                return False
            else:
                if (img[XY(y+d[condizione])][XY(x)] != (255,0,0) and
                        img[XY(y+d[condizione])][XY(x)] != (0,255,0)):
                    return True
                else:
                    return False
    except(IndexError) as e:
        return False
    if condizione == 4:
        return -1
def move(img,x,y,condizione,passato=False):
    d = {0:1,1:1,2:-1,3:-1}
    ok = test(img,x,y,condizione)
    while ok == False:
        condizione += 1
        ok = test(img,x,y,condizione)
    if ok == -1:
        condizione = 0
        ok = test(img, x, y, condizione)
        while ok == False:
            condizione += 1
            ok = test(img, x, y, condizione)
        if ok == -1:
            move = -1
        else:
            move = condizione
    else:
        move = condizione
    if condizione == 0 or condizione == 2:
        x = x + d[condizione]
    elif condizione == 1 or condizione == 3:
        y = y + d[condizione]
    return move,x,y
def cammino(fname,  fname1):
    sfin = ''
    img = load(fname)
    colora(img,0,0,(0,255,0),40)
    dir, x0, y0 = move(img, 0, 0, 0)
    cond = dir
    while cond != -1:
        colora(img,XY(x0),XY(y0),(0,255,0),40)
        sfin += str(dir)
        dir,x0,y0 = move(img,x0,y0,cond)
        cond = dir
    colora(img,XY(x0),XY(y0),(0,0,255),40)
    save(img,fname1)
    return sfin 