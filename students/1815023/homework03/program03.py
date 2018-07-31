'''

Definiamo adiacenti di un pixel p di un immagine i pixel adiacenti a p in  orizzontale o in  verticale.
Se un pixel e' sul bordo dell'immagine il suo vicinato non comprende i pixel non contenuti nell'immagine.
Il pixel dell'immagine con coordinate(x,y) ha dunque come adiacenti i pixel   
con coordinate (x-1,y),(x+1,y),(x,y-1),(x,y+1) appartenenti all'immagine. 
 
Definiamo connessi due pixel se e' possibile da0ll'uno raggiungere l'altro spostandosi solo su   
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
import sys
import time
sys.setrecursionlimit(5500)

rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)
lista=[(100,100,(255-x,255,255),(0,0,255-x)) for x in range(100)]

def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    img = load(fname)
    w=len(img[0])
    h=len(img)
    ris = []
    for task in lista:
        x,y,cArea,cPerim = task
        area, perimetro = coloraVicini(img,w,h,x,y,cArea,cPerim)
        ris.append((area,perimetro))

        
    save(img,fnameout)
    return ris


def inside(x,y,w,h):
    return 0<=x<w and 0<=y<h

def coloraVicini(img,w,h,x,y,cArea,cPerimetro):  
    startColor = img[y][x]
    analizza = [(x,y)]
    colorati = set()
    area = 1
    perimetro = 0
    i = 0
    while len(analizza) != 0: #finchè non ha finito di analizzare tutti i pixel,
        x,y = analizza[0] #analizza il primo elemento della lista

        img[y][x] = cArea
        colorati.add((x,y))

        nearPixels = [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
        vicini = 0
        for p in nearPixels:
            xp,yp = p
            
            if (xp,yp) in colorati:
                vicini += 1
            else:
                if inside(xp,yp,w,h) and img[yp][xp] == startColor:
                    img[yp][xp] = cArea
                    area += 1
                    if (xp,yp) not in analizza:
                        analizza.append((xp,yp))
                    colorati.add((xp,yp))
                    vicini += 1
                
     
        if vicini != 4:
            img[y][x] = cPerimetro
            colorati.add((x,y))
            perimetro += 1
            area -= 1
            
        analizza.pop(0) #elimina il pixel dalla lista da analizzare

    return area,perimetro