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

def inBound(img,y,x):
    return y>=0 and y<len(img) and x>=0 and x<len(img[0])

def getAdjacent(img, alreadyVisited, x, y, color):
    queue = [(y,x)]
    adj = set()
    while len(queue)>0:
        currentPosition = queue.pop()
        #ricordo che ho gia controllato questo pixel
        alreadyVisited[y][x] = 1
        
        y = currentPosition[0]
        x = currentPosition[1]
        if img[y][x] == color:
            adj.add((y,x))
        else:
            continue
        
        if inBound(img,y,x+1) and alreadyVisited[y][x+1]==0:
            queue.append((y,x+1))
        if inBound(img,y,x-1) and alreadyVisited[y][x-1]==0:
            queue.append((y,x-1))
        if inBound(img,y+1,x) and alreadyVisited[y+1][x]==0:
            queue.append((y+1,x))
        if inBound(img,y-1,x) and alreadyVisited[y-1][x]==0:
            queue.append((y-1,x))
       
    return adj

def getPerimeter(img, adj, color):
    per = set()
    for pixel in adj:
        y = pixel[0]
        x = pixel[1]
        miss = 0
        if not inBound(img,y,x+1) or img[y][x+1]!=img[y][x]:
            miss +=1
        if not inBound(img,y,x-1) or img[y][x-1]!=img[y][x]:
            miss +=1
        if not inBound(img,y+1,x) or img[y+1][x]!=img[y][x]:
            miss +=1
        if not inBound(img,y-1,x) or img[y-1][x]!=img[y][x]:
            miss +=1
        if miss>0:
            per.add(pixel)
    return per
    
def buildAlreadyVisited(w,h):
    alreadyVisited=[]
    for j in range(0, h):
        row=[]
        for i in range(0, w):
            row.append(0)
        alreadyVisited.append(row)
    return alreadyVisited
   
def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    ret=[]
    img = load(fname)
    for quad in lista:
        x = quad[0]
        y = quad[1]
        color1 = quad[2]
        color2 = quad[3]
        alreadyVisited = buildAlreadyVisited(len(img[0]),len(img))        
        colorToReplace = img[y][x]
        
        adj = getAdjacent(img, alreadyVisited, x, y, colorToReplace)
        per = getPerimeter(img, adj, colorToReplace)
        
        for pixel in adj:
            y = pixel[0]
            x = pixel[1]
            img[y][x] = color1
        for pixel in per:
            y = pixel[0]
            x = pixel[1]
            img[y][x] = color2
        ret.append((len(adj)-len(per),len(per)))
    save(img,fnameout)
    return ret
