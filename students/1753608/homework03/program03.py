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

def paint(img,x,y,c0,c1,c2,done):
    lst = set(list())
    lst.add((x,y))
    brd = set(list())
    perim = 0
    area = 0
    while(len(lst) != 0):
        r = lst.pop()
        area+=1
        x = r[0]
        y = r[1]
        img[x][y] = c1
        done.add((x,y))
        try:
            if (img[x + 1][y] != c0  and (x+1,y) not in done):
                brd.add((x,y))
            elif(is_valid(img,x+1,y,c0) and (x+1,y) not in done):
                lst.add((x+1, y))
        except:
            brd.add((x, y))
        try:
            if (img[x][y+1] != c0 and (x,y+1) not in done):
                brd.add((x, y))
            elif(is_valid(img,x,y+1,c0) and (x,y+1) not in done):
                lst.add((x, y + 1))
        except:
            brd.add((x, y))
        try:
            if (img[x-1][y] != c0 and (x-1,y) not in done):
                brd.add((x, y))
            elif(x-1 >= 0 and is_valid(img,x-1,y,c0) and (x-1,y) not in done):
                lst.add((x-1, y))
        except:
            brd.add((x, y))
        try:
            if (img[x][y-1] != c0 and (x,y-1) not in done):
                brd.add((x, y))
            elif(y-1 >= 0 and is_valid(img,x,y-1,c0) and (x,y-1) not in done):
                lst.add((x, y-1))
        except:
            brd.add((x, y))

    for tupla in brd:
        x = tupla[0]
        y = tupla[1]
        img[x][y] = c2

    perim = len(brd)
    area -= perim
    return img,area,perim

def is_valid(img,x,y,c0):
    return img[x][y] == c0

def ricolora(fname, lista, fnameout):
    img = load(fname)
    geometry = []
    for e in lista:
        done = set(list())
        x = e[1]
        y = e[0]
        c0 = img[x][y]
        c1 = e[2]
        c2 = e[3]
        paint_fn = paint(img,x,y,c0,c1,c2,done)
        img = paint_fn[0]
        geometry.append((paint_fn[1],paint_fn[2]))

    save(img,fnameout)
    return geometry