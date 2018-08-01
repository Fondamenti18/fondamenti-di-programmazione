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

def connected(img, y, x):
    color = img[x][y]
    to_process = [(x, y)]
    height = len(img)
    lenght = len(img[0])
    area = list()
    border = list()
    while len(to_process) > 0:
        for item in to_process:
            pixel = to_process.pop(0)
            adjacent = [(pixel[0]+1, pixel[1]), (pixel[0], pixel[1]+1), (pixel[0]-1, pixel[1]), (pixel[0], pixel[1]-1)]
            count = 0
            for adj in adjacent:
                if 0 <= adj[0] < height and 0 <= adj[1] < lenght:
                    if img[adj[0]][adj[1]] == color:
                        if (adj[0], adj[1]) not in area + border + to_process:
                            to_process.append(adj)
                        count += 1
                else:
                    continue
            if count < 4:
                border.append(pixel)
            else:
                area.append(pixel)
    return area, border


def ricolora(fname, lista, fnameout):
    img = load(fname)
    recolored = list()
    for quadruple in lista:
        x = quadruple[0]
        y = quadruple[1]
        area_c = quadruple[2]
        border_c = quadruple[3]
        to_recolor = connected(img, x, y)
        for pixel_area in to_recolor[0]:
            img[pixel_area[0]][pixel_area[1]] = area_c
        for pixel_border in to_recolor[1]:
            img[pixel_border[0]][pixel_border[1]] = border_c
        recolored.append((len(to_recolor[0]), len(to_recolor[1])))
    save(img, fnameout)
    return recolored
