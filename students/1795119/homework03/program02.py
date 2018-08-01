from immagini import *

def colora(png, x, y, col):
    for k in range(40):
        for j in range(40):
            png[y+k][x+j] = col

def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    png = load(fname)
    rosso = (255, 0, 0)
    verde = (0, 255, 0)
    blu = (0, 0, 255)
    currentPos = (0, 0)
    direction = 0   #0 - destra; 1 - basso; 2 - sinistra; 3 - alto
    path = ""
    listpath = [currentPos]
    while True:
        x = currentPos[0]
        y = currentPos[1]
        if direction == 0:
            if x+40 < len(png[y]):
                if png[y][x+40] != rosso and (x+40,y) not in listpath:
                    currentPos = (x+40, y)
                    colora(png, x, y, verde)
                    path += "0"
                else:
                    direction += 1
            else:
                direction += 1
        if direction == 1:
            if y+40 < len(png):
                if png[y+40][x] != rosso and (x,y+40) not in listpath and y+40 < len(png):
                    currentPos = (x, y+40)
                    colora(png, x, y, verde)
                    path += "1"
                else:
                    direction += 1
            else:
                direction += 1
        if direction == 2:
            if png[y][x-40] != rosso and (x-40,y) not in listpath and x-40 >= 0:
                currentPos = (x-40, y)
                colora(png, x, y, verde)
                path += "2"
            else:
                direction += 1
        if direction == 3:
            if png[y-40][x] != rosso and (x,y-40) not in listpath and y-40 >= 0:
                currentPos = (x, y-40)
                colora(png, x, y, verde)
                path += "3"
            else:
                if listpath[-1] == listpath[-2] and listpath[-2] == listpath[-3] and listpath[-3] == listpath[-4]:
                    colora(png, x, y, blu)
                    save(png, fname1)
                    return path
                else:
                    direction = 0
        listpath += [currentPos]
