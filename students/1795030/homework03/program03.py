#!/usr/bin/env python
# -*- coding: utf-8 -*-


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


def ricolora(fname, lista, fnameout):

    r = []

    img = load(fname)

    for i in lista:
        m = [[0 for x in range(len(img[0]))] for y in range(len(img))]
        x = i[0]
        y = i[1]
        c1 = i[2]
        c2 = i[3]
        area = riempi(img, m, x, y, img[y][x], c1)
        peri = bordo(img, m, c2)
        r.append((area - peri, peri))

    save(img, fnameout)

    return r



def riempi(img, m, x, y, colore, nuovo_colore):
    area = 0
    da_esplorare = [(x, y)]
    while len(da_esplorare) > 0:
        inizio = da_esplorare.pop()
        x = inizio[0]
        y = inizio[1]
        x1 = x
        while x1 >= 0 and img[y][x1] == colore and m[y][x1] == 0:
            x1 -= 1
        x2 = x + 1
        while x2 < len(img[y]) and img[y][x2] == colore and m[y][x2] == 0:
            x2 += 1
        area += x2 - x1 - 1
        for x in range(x1 + 1, x2):
            img[y][x] = nuovo_colore
            m[y][x] = 1
            if y > 0 and img[y - 1][x] == colore and m[y - 1][x] == 0:
                da_esplorare.append((x, y - 1))
            if y < len(img) - 1 and img[y + 1][x] == colore and m[y + 1][x] == 0:
                da_esplorare.append((x, y + 1))
    return area


def bordo(img, m, colore_bordo):
    peri = 0
    for y in range(0, len(m)):
        for x in range(0, len(m[y])):
            if m[y][x] == 1 and (y == 0 or y == len(m) - 1 or x == 0 or x == len(m[y]) - 1 or m[y][x - 1] == 0 or m[y][x + 1] == 0 or m[y - 1][x] == 0 or m[y + 1][x] == 0):
                peri += 1
                img[y][x] = colore_bordo
    return peri





'''if __name__ == "__main__":
    rosso = (255,   0,   0)
    blu   = (  0,   0, 255)
    verde = (  0, 255,   0)
    nero  = (  0,   0,   0)
    bianco= (255, 255, 255)
    giallo= (255, 255,   0)
    cyan  = (  0, 255, 255)
    magenta= (255,  0, 255)
    #print ricolora('I1.png',[(10,10,rosso,blu)],'test1.png')
    print ricolora('I1.png', [(25, 25, (0, 0, 0), (0, 5, 5)), (25, 25, (0, 0, 0), (0, 10, 10))],'test1.png')'''












