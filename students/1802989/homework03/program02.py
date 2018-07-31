from immagini import *

def scacchiera(h, w, img):
    '''Funzione usata per creare il dizionario a mo' di scacchiera, 
    ogni riga è una lettera, i num sono le colonne'''
    diz = dict()
    index = 0
    for j in range(0, h, 40):
        diz[index] = []
        for i in range(0, w, 40):
            diz[index].append( img[j][i] )
        index += 1
    return diz

def cammino(fname,  fname1):
    '''Funzione principale che contiene la prima mossa, il ris come stringa. k e num
    utilizzati per muovermi nella matrice 15x15. '''
    img = load(fname)
    w = len(img[0])
    h = len(img)
    diz = scacchiera(h, w, img)
    mossa = '0'
    ris = ''
    k = 0
    num = 0
    giro = 0
    while giro != 360:
        mossa, diz, giro, k, num, ris = hub(mossa, diz, giro, k, num, ris)
    diz[k][num] = (0,0,255)
    for k,v in diz.items():
        lst = []
        for el in v:
            for i in range(40):
                lst.append(el)
        diz[k] = lst
    immagine = crea_quadrato(diz)
    save(immagine, fname1)
    return ris

def hub(mossa, diz, giro, k, num, ris):
    if mossa == '0' :
        mossa, diz, giro, k, num, ris = mossa0(diz, giro, k, num, ris)
        return mossa, diz, giro, k, num, ris
    if mossa == '1' : 
        mossa, diz, giro, k, num, ris = mossa1(diz, giro, k, num, ris)
        return mossa, diz, giro, k, num, ris
    if mossa == '2' : 
        mossa, diz, giro, k, num, ris = mossa2(diz, giro, k, num, ris)
        return mossa, diz, giro, k, num, ris
    if mossa == '3' :
        mossa, diz, giro, k, num, ris = mossa3(diz, giro, k, num, ris)
        return mossa, diz, giro, k, num, ris
    return mossa, diz, giro, k, num, ris

def mossa0(diz, giro, k, num, ris):
    'Mossa che va verso destra'
    while num < 14 and diz[k][num+1] != (0,255,0) and diz[k][num+1] != (255,0,0):
        diz[k][num] = (0,255,0)
        ris += '0'
        giro = 0
        num += 1
    else:
        giro += 90
        return '1',diz, giro, k, num, ris
    
def mossa1(diz, giro, k, num, ris):
    'Mossa che va verso il basso'
    while k < 14 and diz[k+1][num] != (0,255,0) and diz[k+1][num] != (255,0,0):
        diz[k][num] = (0,255,0)
        ris += '1'
        giro = 0
        k += 1
    else:
        giro += 90
        return '2',diz, giro, k, num, ris
    
def mossa2(diz, giro, k, num, ris):
    'Mossa che va verso sinistra'
    while num > 0 and diz[k][num-1] != (0,255,0) and diz[k][num-1] != (255,0,0):
        diz[k][num] = (0,255,0)
        ris += '2'
        giro = 0
        num -= 1
    else:
        giro += 90
        return '3',diz, giro, k, num, ris
    
def mossa3(diz, giro, k, num, ris):
    'Mossa che va verso su'
    while k > 0 and diz[k-1][num] != (0,255,0) and diz[k-1][num] != (255,0,0):
        diz[k][num] = (0,255,0)
        ris += '3'
        giro = 0
        k -= 1
    else:
        giro += 90
        return '0',diz, giro, k, num, ris
    
def crea_quadrato(diz):
    'Funzione usata per creare il quadrato delle dimensioni richieste'
    immagine = []
    for v in diz.values():
        for i in range(40):
            immagine.append(v)
    return immagine