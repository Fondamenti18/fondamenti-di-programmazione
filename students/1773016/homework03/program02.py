from immagini import *
def getXY(position):
    return position*40
def coloraQuadrato(img,x,y,col,rangeQ):
    yCount = y
    xCount = x
    while yCount<y+rangeQ:
        while xCount<x+rangeQ:
            img[yCount][xCount] = col
            xCount+=1
        xCount = x
        yCount+=1
def testSuccessivo(img,xCorr,yCorr,cond):
    diz = {0: 1, 1: 1, 2: -1, 3: -1}
    try:
        if cond == 0 or cond == 2:
            if xCorr+diz[cond] == -1 or xCorr+diz[cond] == 16:
                return False
            else:
                if (img[getXY(yCorr)][getXY(xCorr+diz[cond])] != (255,0,0) and
                        img[getXY(yCorr)][getXY(xCorr+diz[cond])] != (0,255,0)):
                    return True
                else:
                    return False
        elif cond == 1 or cond == 3:
            if yCorr + diz[cond] == -1 or yCorr + diz[cond] == 16:
                return False
            else:
                if (img[getXY(yCorr+diz[cond])][getXY(xCorr)] != (255,0,0) and
                        img[getXY(yCorr+diz[cond])][getXY(xCorr)] != (0,255,0)):
                    return True
                else:
                    return False
    except(IndexError) as e:
        return False
    if cond == 4:
        return -1
def funMovimento(img,xCorr,yCorr,cond,passato=False):
    diz = {0:1,1:1,2:-1,3:-1}
    okDir = testSuccessivo(img,xCorr,yCorr,cond)
    while okDir == False:
        cond += 1
        okDir = testSuccessivo(img,xCorr,yCorr,cond)
    if okDir == -1:
        cond = 0
        okDir = testSuccessivo(img, xCorr, yCorr, cond)
        while okDir == False:
            cond += 1
            okDir = testSuccessivo(img, xCorr, yCorr, cond)
        if okDir == -1:
            move = -1
        else:
            move = cond
    else:
        move = cond
    if cond == 0 or cond == 2:
        xCorr = xCorr + diz[cond]
    elif cond == 1 or cond == 3:
        yCorr = yCorr + diz[cond]
    return move,xCorr,yCorr
def cammino(fname,  fname1):
    strada = ''
    img = load(fname)
    coloraQuadrato(img,0,0,(0,255,0),40)
    direzione, xCorrente, yCorrente = funMovimento(img, 0, 0, 0)
    condizione = direzione
    while condizione != -1:
        coloraQuadrato(img,getXY(xCorrente),getXY(yCorrente),(0,255,0),40)
        strada += str(direzione)
        direzione,xCorrente,yCorrente = funMovimento(img,xCorrente,yCorrente,condizione)
        condizione = direzione
    coloraQuadrato(img,getXY(xCorrente),getXY(yCorrente),(0,0,255),40)
    save(img,fname1)
    return strada
#print(cammino('I1.png','t1.png'))
'''
   Funzione: cammino('I2.png','t2.png')
   Risutati: '0001211111111111122333333333333'
   000112223
'''