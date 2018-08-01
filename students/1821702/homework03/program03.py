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

def checkpx(x0,y0,im):
    i = 0
    px = im[y0][x0]
    if px == pixeldestra(x0,y0,im):
        i += 1
    if px == pixelsinistra(x0,y0,im):
        i += 1
    if px == pixelsopra(x0,y0,im):
        i += 1
    if px == pixelsotto(x0,y0,im):
        i += 1
    return i
def pixeldestra(a,b,im):
    x1 = a + 1
    y1 = b
    pixel = ()
    if (x1 < len(im) and x1 >= 0):
        pixel = (im[y1][x1])
    return pixel

def pixelsinistra(a,b,im):
    x1 = a - 1
    y1 = b
    pixel = ()
    if (x1 < len(im) and x1 >= 0):
        pixel = (im[y1][x1])
    return pixel

def pixelsotto(a,b,im):
    x1 = a
    y1 = b + 1
    pixel = ()
    if (y1 < len(im) and y1 >= 0):
        pixel = (im[y1][x1])
    return pixel

def pixelsopra(a,b,im):
    x1 = a
    y1 = b - 1
    pixel = ()
    if (y1 < len(im) and y1 >= 0):
        pixel = (im[y1][x1])
    return pixel

def trovapxbordo(x0,y0,im,pxad,pxbor): 
    if checkpx(x0,y0,im) == 4:
        if [x0,y0] not in pxad:
            pxad.append([x0,y0])
    else:
        if [x0,y0] not in pxbor:
            pxbor.append([x0,y0])
    return pxad,pxbor

def pxconnessi(x0,y0,im,pxconn):
    px = im[y0][x0]
    if px == pixeldestra(x0,y0,im):
        if [x0+1,y0] not in pxconn:
            pxconn.append([x0+1,y0])
    if px == pixelsinistra(x0,y0,im):
        if [x0-1,y0] not in pxconn:
            pxconn.append([x0-1,y0])
    if px == pixelsotto(x0,y0,im):
        if [x0,y0+1] not in pxconn:
            pxconn.append([x0,y0+1])
    if px == pixelsopra(x0,y0,im):
        if [x0,y0-1] not in pxconn:
            pxconn.append([x0,y0-1])
    return pxconn
    
def controllo(x0,y0,im,c1,c2):
    pxconn = [[x0,y0]]
    pxad = []
    pxbor = []
    for x in pxconn:
        pxconn = pxconnessi(x[0],x[1],im,pxconn)
        pxad,pxbor = trovapxbordo(x[0],x[1],im,pxad,pxbor)
    im,p,a = colora(im,pxbor,pxad,c1,c2)
    return im,a,p

def colora(im,pxbor,pxad,c1,c2):
    perimetro = len(pxbor)
    area = len(pxad)
    for x in pxad:
        im[x[1]][x[0]] = c1
    for x in pxbor:
        im[x[1]][x[0]] = c2
    return im,perimetro,area

def ricolora(fname,lista,fnameout):
    f = load(fname)
    risultato = []
    for i in range(0,len(lista)):
        x0 = lista[i][0]
        y0 = lista[i][1]
        c1 = lista[i][2]
        c2 = lista[i][3]
        f,area,perimetro = controllo(x0,y0,f,c1,c2)
        risultato.append((area,perimetro))
    save(f,fnameout)
    return risultato
