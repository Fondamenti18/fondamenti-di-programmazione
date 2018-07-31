'''

Definiamo adiacenti di un pixel p di un immagine i pixel adiacenti a p in  orizzontale o in  verticale.
Se un pixel e' sul bordo dell'immagine il suo vicinato non comprende i pixel non contenuti nell'immagine.
Il pixel dell'immagine con coordinate(x,y) ha dunque come adiacenti i pixel   
con coordinate (x-1,y),(x+1,y),(x,y-1),(x,y+1) appartenenti all'immagine. 
 
Definiamo connessi due pixel se e' possibile dall'uno raggiungere l'altro spostandosi solo su   
pixel adiacenti e dello stesso colore (ovviamente perche' cio' sia possobile e' necessario 
che i due pixel abbiano lo stesso colore).

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una funzione ricolora(fname, lista,  fnameout) che presi:
- il percorso di un file che contiene un'immagine in formato PNG
- una lista di quadruple del tipo (x,y,c1,c2) dove  x e y sono coordinate di un pixel dell'immagine e c1 e c2 due triple colore RGB
- il percorso di un file (fnameout) da creare
legge l'immagine in fname, esegue un'operazione di ricolorazione di alcuni pixel dell'immagine e 
registra l'immagine ricolorata nel file fnameout.

L'operazione di ricolorazione e' la seguente. Per ciascuna delle quadruple (x,y,c1,c2) della lista (nell'ordine), 
- tutti i pixel connessi al pixel  di coordinate (x,y) nell'immagine vanno ricolorati col colore c1, 
- tutti i pixel del perimetro (che si trovano sul 'bordo') della zona che si e' appena colorata devono essere ricolorati col colore c2.
Il perimetro della zona colorata è l'insieme dei pixel che non hanno tutti e 4 i vicini che fanno parte della zona ricolorata 
(ovvero almeno uno è di un colore diverso da quello che si sta ricolorando oppure almeno uno non esiste perchè sarebbe fuori dall'immagine)

Si consideri ad esempio l'immagine 'I1.png', l'invocazione di ricolora('I1.png',[(10,10,(255,0,0), (0,0,255))],’OUT1.png')
produrra' l'immagine 'OUT1.png' identica all'immagine di partenza se non per il fatto che,
 tutti i pixel adiacenti al pixel di coordinate (10,10) (e di colore verde), verranno ricolorati 
 di rosso ((255,0,0)), mentre i pixel sul bordo della zona inizialmente verde vengono ricolorati di blu.

Per ciascuna area ricolorata bisogna inoltre calcolare area interna e perimetro, che sono definite come segue:
- l'area interna e' il numero di pixel ricolorati con il colore c1
- il perimetro è il numero di pixel ricolorati con il colore c2

La funzone deve tornare la lista di coppie (area interna, perimetro) nello stesso ordine in cui sono state colorate le aree.
 
Per altri  esempi vedere il file grade03.txt 
'''

from immagini import *

def inside(img, x, y):
    return 0 <= y < len(img) and 0 <= x < len(img[0])

def adiacentiugualidx(img,x,y):
    '''controlla se gli adiacenti hanno lo stesso colore escludendo il pixel a sinistra'''
    try:
        return img[y][x+1] == img[y][x] and img[y+1][x] == img[y][x] and img[y-1][x] == img[y][x]
    except:
        False

def adiacentiugualisx(img,x,y):
    '''controlla se gli adiacenti hanno lo stesso colore escludendo il pixel a destra'''
    try:
        return img[y][x-1] == img[y][x] and img[y+1][x] == img[y][x] and img[y-1][x] == img[y][x]
    except:
        False

def adiacentiugualisottodx(img,x,y):
    '''controlla se gli adiacenti hanno lo stesso colore escludendo il pixel sopra e a sinistra'''
    try:
        return img[y][x+1] == img[y][x] and img[y-1][x] == img[y][x]
    except:
        False

def adiacentiugualisopradx(img,x,y):
    '''controlla se gli adiacenti hanno lo stesso colore escludendo il pixel sotto e a sinistra'''
    try:
        return img[y][x+1] == img[y][x] and img[y+1][x] == img[y][x] 
    except:
        False

def adiacentiugualisottosx(img,x,y):
    '''controlla se gli adiacenti hanno lo stesso colore escludendo il pixel sopra e a destra'''
    try:
        return img[y][x-1] == img[y][x] and img[y-1][x] == img[y][x]
    except:
        False

def adiacentiugualisoprasx(img,x,y):
    '''controlla se gli adiacenti hanno lo stesso colore escludendo il pixel sotto e a destra'''
    try:
        return img[y][x-1] == img[y][x] and img[y+1][x] == img[y][x]
    except:
        False

    
def ricolora(fname, lista, fnameout):
    img = load(fname)
    listar = []
    for i in lista:
        x = i[0]
        y = i[1]
        c1 = i[2]
        c2 = i[3]
        area = 0
        perimetro = 0

        while inside(img,x+1,y) and adiacentiugualidx(img,x+1,y) :               #controlla andando a destra
            img[y][x+1] = c1
            area += 1
            yc = y+1

            while adiacentiugualisopradx(img,x+1,yc) and inside(img,x,yc):       #controlla sopra
                img[yc][x+1] = c1
                area += 1
                yc += 1
            img[yc][x+1] = c2
            perimetro += 1
            yc = y-1

            while adiacentiugualisottodx(img,x+1,yc) and inside(img,x+1,yc):       #controlla sotto
                img[yc][x+1] = c1
                area += 1
                yc = yc-1
            img[yc][x+1] = c2
            perimetro += 1
            x += 1

        img[y][x+1] = c2
        perimetro += 1

        #terminabordo
        while img[y][x+1] == c2 and img[y+1][x+1] == img[y+2][x+1]:               
            img[y+1][x+1] = c2
            perimetro += 1
            y += 1
            if not inside(img,x+1,y+1) or not inside(img,x+1,y+2) or not inside(img,x+1,y):
                break
        img[y+1][x+1] = c2
        perimetro += 1
        y = i[1]
        while img[y][x+1] == c2 and img[y-1][x+1] == img[y-2][x+1]:
            img[y-1][x+1] = c2
            perimetro += 1
            y = y-1
            if not inside(img,x+1,y-1) or not inside(img,x+1,y-2) or not inside(img,x+1,y):
                break
        img[y-1][x+1] = c2
        perimetro += 1
        y = i[1]
        #termina bordo

        x = i[0]
        while inside(img,x,y) and adiacentiugualisx(img,x,y):            #controlla andando a sinistra
            img[y][x] = c1
            area += 1
            yc = y+1

            while adiacentiugualisoprasx(img,x,yc) and inside(img,x,y):       #controlla sopra
                img[yc][x] = c1
                area += 1
                yc += 1
            img[yc][x] = c2
            perimetro += 1
            yc = y-1

            while adiacentiugualisottosx(img,x,yc) and inside(img,x,yc):       #controlla sotto
                img[yc][x] = c1
                area += 1
                yc = yc-1
            img[yc][x] = c2
            perimetro += 1
            x = x-1

        img[y][x] = c2
        perimetro += 1

        #terminabordo
        while img[y][x] == c2 and inside(img,x,y+1) and img[y+1][x] == img[y+2][x]:
            img[y+1][x] = c2
            perimetro += 1
            y += 1
            if not inside(img,x,y+1) or not inside(img,x,y+2) or not inside(img,x,y):
                break
        img[y+1][x] = c2
        perimetro += 1
        y = i[1]
        while img[y][x] == c2 and inside(img,x+1,y-1) and img[y-1][x] == img[y-2][x]:
            img[y-1][x] = c2
            perimetro += 1
            y = y-1
            if not inside(img,x,y-1) or not inside(img,x,y-2) or not inside(img,x,y):
                break
        img[y-1][x] = c2
        perimetro += 1
        #terminabordo

        listar += [(area,perimetro)]

    save(img,fnameout)
    return listar
    
                    



