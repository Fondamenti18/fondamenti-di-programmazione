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

from immagini import load, save
near = [[0,1],[1,0],[-1,0],[0,-1]]

def checkBounds(x, y, img, w, h, checked, color): 
    r = []
    for pos in near:
        if not (0 <= y+pos[1] < h and 0 <= x+pos[0] < w): continue
        if img[y+pos[1]][x+pos[0]] == color:
            r.append((y+pos[1], x+pos[0]))
        else: r.append(1)
    return r

def paintPx(y, x, img, drawColor1, drawColor2, w, h):
    ls, checked, bord, body, color = [(y,x)], {(y,x)}, [], [], img[y][x]
    while len(ls) > 0:
        px = ls.pop()
        bounds = checkBounds(px[1], px[0], img, w, h, checked, color)
        toadd = [p for p in bounds if p != 1 and p not in checked]
        ls += toadd
        for p in toadd: checked.add(p)
        if len(bounds) == 4:
            if sum(1 for p in bounds if p != 1) == 4:
                body.append(px)
                continue
        bord.append(px) 

    for y,x in body:
        img[y][x] = drawColor1
    for y,x in bord:
        img[y][x] = drawColor2
    return (len(body), len(bord))
def ricolora(fname, lista, fnameout):
    img, res = load(fname), []    
    w, h = len(img[0]), len(img)
    for qdp in lista:
        res.append(paintPx(qdp[1], qdp[0], img, qdp[2], qdp[3], w, h))
    save(img, fnameout)
    return res