from immagini import *
cord = []
def Quadrato(x,y,img):
    X = x
    Y = y
    y0 = 0
    lato = 0
    while img[Y][X] == img[y][x]:
        if Y == 0:
            X -= 1
            break
        X -= 1
    x0 = X + 1
    X = x
    while img[Y][X] == img[y][x]:
        if X == len(img[0])-1:
            X += 1
            break
        X += 1
    if (x-1>0 and x+1<len(img[0])) or img[y][x-1] == img[y][x]:
        lato = X - x0 - 1
    else:
        lato = 1
    latoP = X - x0 - 1
    X = x
    while img[Y][X] == img[y][x]:
        if Y == 0:
            Y -= 1
            break
        Y -= 1
    y0 = Y + 1
    return lato,latoP,x0,y0
def coloraIn(x,y,img,lato,cIn):
    for r in range(y+1,y+lato):
        for col in range(x+1,x+lato):
            img[r][col] = cIn
def coloraExt(x0,y0,img,lato,cOut):
    for col in range(x0,x0+lato+1):
        img[y0][col] = cOut
    for col in range(x0, x0 + lato+1):
        img[y0+lato][col] = cOut
    for r in range(y0+1,y0+lato):
        img[r][x0] = cOut
    for r in range(y0+1,y0+lato):
        img[r][x0+lato] = cOut
def colora(x,y,cIn,cOut,img):
    lato,latoP, x0, y0 = Quadrato(x, y, img)
    if (x,y) in cord:
        area = (lato-1)**2
    else:
        area = (latoP-1)**2
    perimetro = (latoP)*4
    coloraIn(x0,y0,img,latoP,cIn)
    coloraExt(x0,y0,img,latoP,cOut)
    return area,perimetro
def ricolora(fname, lista, fnameout):
    img = load(fname)
    altezza = len(img)
    larghezza = len(img[0])
    #print('altezza: %s larghezza: %s' %(altezza,larghezza))
    listaRis = []
    for elem in lista:
        x = elem[0]
        y = elem[1]
        c1 = elem[2]
        c2 = elem[3]
        areaElem,periElem = colora(x,y,c1,c2,img)
        cord.append((x, y))
        listaRis.append((areaElem,periElem))
    save(img,fnameout)
    return listaRis
#lista=[(0,0,(0,0,0),(0,5*i,5*i)) for i in range(1,25)]
#print(ricolora('I1.png',lista,'test7.png'))
