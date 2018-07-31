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

import sys
from immagini import *


def out_of_range(arr, x, y):
    return x < 0 or x >= len(arr) or y < 0 or y >= len(arr[0])


def near(img, x, y, c):
    return x > 0 and x < len(img[0])-1 and y > 0 and y < len(img)-1 and img[x+1][y] == c and img[x][y+1] == c and img[x-1][y] == c and img[x][y-1] == c


def ricolora_impl(img, x, y, c, old):
    if out_of_range(img, x, y) or img[x][y] != c or (x,y) in old:
        return []

    old.append((x, y))
    p1 = ricolora_impl(img, x+1, y, c, old)
    p2 = ricolora_impl(img, x, y+1, c, old)
    p3 = ricolora_impl(img, x-1, y, c, old)
    p4 = ricolora_impl(img, x, y-1, c, old)
    return [(x,y)]+p1+p2+p3+p4
    
    
def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    img = load(fname)
    sys.setrecursionlimit(len(img)*len(img[0]))
    ris = []
    for comp in lista:
        x = comp[0]
        y = comp[1]
        c = img[x][y]
        c1 = comp[2]
        c2 = comp[3]
        coords = ricolora_impl(img, x, y, c, [])
        area = []
        perimeter = []
        for coord in coords:
            if near(img, coord[1], coord[0], c):
                area.append(coord)
            else:
                perimeter.append(coord)
        for p in area:
            img[p[1]][p[0]] = c1
        for p in perimeter:
            img[p[1]][p[0]] = c2
        ris.append((len(area), len(perimeter)))
    save(img, fnameout)
    return ris
    
    

