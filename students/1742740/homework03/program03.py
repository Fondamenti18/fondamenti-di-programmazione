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

def inside(img,x,y):
    return 0<=y<len(img) and 0<=x<len(img[0])

def disegna_quadrato(img,xs,ys,xd,yd,c):#angolo in alto dx (x,y),(h,w)dimensioni quadrato , c colore
    for px in range(xs,xd):
        for py in range(ys,yd):
            if inside(img,px,py):
                img[py][px]=c

def disegna_rettcavo(img,xs,ys,xd,yd,c,k): #disegna rettangolo cavo con angoli in (xs,ys) e (xd,yd) con colore c e spessore k
    for py in range(ys,yd):
        for px in range(xs,xd):
            if not (xs+k<=px<xd-k and ys+k<=py<yd-k):
                img[py][px]=c

def trovaAS(img,x,y): #funzione che trova l'angolo in alto a sinistra
    px=x
    py=y
    pixel=img[y][x]
    if inside(img,px-1,py-1) and (img[py][px-1]==pixel or img[py-1][px]==pixel): #scorre in diagonale finche i pixel adiacenti non sono di colore diverso
        susx=img[py-1][px-1]
        while susx==pixel:
            px=px-1
            py=py-1
            if inside(img, px - 1, py - 1) and (img[py][px-1]==pixel or img[py-1][px]==pixel):
                susx=img[py-1][px-1]
            else:break
    if inside(img,px,py-1):
        su=img[py-1][px]
        while su==pixel: #scorre in alto
            py=py-1
            if inside(img,px,py-1):
                su=img[py-1][px]
            else:break
    if inside(img,px-1,py): #scorre a sinistra
        sx=img[py][px-1]
        while sx==pixel:
            px=px-1
            if inside(img,px-1,py):
                sx=img[py][px-1]
            else:break
    return px,py

def trovaBD(img,x,y): #funzione che trova l'angolo in basso a destra
    px=x
    py=y
    pixel=img[y][x]
    if inside(img,px+1,py+1) and (img[py][px+1]==pixel or img[py+1][px]==pixel):
        giudx=img[py+1][px+1]
        while giudx==pixel: #scorre in diagonale finche i pixel adiacenti non sono di colore diverso
            px=px+1
            py=py+1
            if inside(img, px + 1, py + 1) and (img[py][px+1]==pixel or img[py+1][px]==pixel):
                giudx=img[py+1][px+1]
            else:break
    if inside(img,px,py+1):
        giu=img[py+1][px]
        while giu==pixel: #scorre in basso
            py=py+1
            if inside(img,px,py+1):
                giu=img[py+1][px]
            else:break
    if inside(img,px+1,py):
        dx=img[py][px+1]
        while dx==pixel: #scorre a destra
            px=px+1
            if inside(img,px+1,py):
                dx=img[py][px+1]
            else:break
    return px,py

def ricolora(fname, lista, fnameout):
    immagine=load(fname)
    l_coppie=[]
    for i in range(len(lista)):
        if i>0:
            cvec=(lista[i-1])[2]
        else:
            cvec= None
        x,y,c1,c2=lista[i]
        px_al,py_al=trovaAS(immagine,x,y)
        px_ba,py_ba=trovaBD(immagine,x,y)
        if c1==cvec and (x ==px_al) and (y == py_al): #se ricolora lo stesso quadrato con colore uguale l'area e' 0
            area=0
        else:
            disegna_quadrato(immagine, px_al, py_al, px_ba, py_ba, c1)
            area=((px_ba-px_al)-1)*((py_ba-py_al)-1)
        disegna_rettcavo(immagine, px_al, py_al, px_ba + 1, py_ba + 1, c2, 1)
        perimetro=2*(px_ba-px_al)+2*(py_ba-py_al)
        l_coppie.append((area, perimetro))
    save(immagine,fnameout)
    return l_coppie