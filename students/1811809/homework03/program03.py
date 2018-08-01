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
from collections import deque

def getW(img):
    return len(img[0])

def getH(img):
    return len(img)

def valid(img, x, y, dx, dy, W, H):
    return 0 <= x + dx < W and 0 <= y + dy < H

def expand(img, sx, sy, dirs, W, H, visit, Q, t, c):
    nei = 0
    for d in dirs:
        if valid(img, sx, sy, d[0], d[1], W, H):
            vi = visit[sy+d[1]][sx+d[0]] != t
            ci = c == img[sy+d[1]][sx+d[0]]
            if vi and ci:
                Q.append((sx+d[0], sy+d[1]))
                visit[sy+d[1]][sx+d[0]] = t
            if (not vi) or ci:
                nei+=1
    return nei

def bfs(img, visit, sx, sy, c1, c2, t, W, H):
    Q = deque()
    c = img[sy][sx]

    Q.append((sx, sy))
    visit[sy][sx] = t

    area, prmtr = 0, 0
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while len(Q) != 0:
        sx, sy = Q.popleft()
        if expand(img, sx, sy, dirs, W, H, visit, Q, t, c) == 4:
            img[sy][sx] = c1
            area+=1
        else:
            img[sy][sx] = c2
            prmtr+=1
    return (area, prmtr)

def ricolora(fname, lista, fnameout):
    img = load(fname)
    W, H = getW(img), getH(img)
    lastVisit = [[-1 for _ in range(W)] for _ in range(H)]
    answ = []
    for t, q in enumerate(lista):
        answ.append(bfs(img, lastVisit, q[0], q[1], q[2], q[3], t, W, H))
    save(img, fnameout)
    return answ

if __name__=='__main__':
    #ricolora('test.png', [(0, 0, (255, 0, 0), (255, 255, 255)), (0, 0, (0, 0, 255), (255, 0, 0))], 'out.png')
    #ricolora('test.png', [(0, 0, (255, 0, 0), (255, 255, 255))], 'out.png')
    ricolora('test2.png', [(0, 0, (0, 0, 255), (255, 0, 0))], 'out.png')
