from immagini import * 


per = 0
adia = 0
h=0
w=0
area = 1


def controlloPix(img, x, y, col):
    '''controllo se il pixel è contenuto nell'immagine e se il colore è giusto'''
    global h, w, err
    if 0 <= x < w and 0 <= y < h and img[y][x] == col   :
        return True
    return False

def repaint(img, x, y, colOr, colNuovo, cont):
    global area, per
    img[y][x] = colNuovo
    lista = [(y,x)]
    adia = 0
    
    for el in lista:
        adia = 0
        py = el[0]
        px = el[1]
        
        if (py, px+1) not in lista: 
            if controlloPix(img, px+1, py, colOr):
                img[py][px+1] = colNuovo
                adia = adia + 1
                area += 1
                lista += [(py, px+1)]
        else: adia = adia + 1
        
        if (py-1, px) not in lista:
            if controlloPix(img, px, py-1, colOr):
                img[py-1][px] = colNuovo
                area += 1
                adia = adia + 1
                lista += [(py-1, px)]
        else: adia = adia + 1

        if (py, px-1) not in lista:
            if controlloPix(img, px-1, py, colOr):
                img[py][px-1] = colNuovo
                area += 1
                adia = adia + 1
                lista += [(py, px-1)]
        else: adia = adia + 1
            
        if (py+1, px) not in lista:
            if controlloPix(img, px, py+1, colOr):
                img[py+1][px] = colNuovo
                adia = adia + 1
                area += 1
                lista +=[(py+1, px)]
        else: adia = adia + 1
            
        if adia < 4 : 
            img[py][px] = cont
            per += 1
    
    return img



def ricolora(fname, lista, fnameout):
    global h, w, area, per
    img = load(fname)
    h = len(img)
    w = len(img[0])
    ris = []
    
    for l in lista:
        y = l[1]
        x = l[0]
        
        colNuovo = l[2]
        colOr = img[y][x]
        cont = l[3]
        area = 1
        per = 0
        
        img = repaint(img, x, y, colOr, colNuovo, cont)
        area = area - per
        ris += [(area, per)]
        
    save(img, fnameout)
    
    return (ris)
