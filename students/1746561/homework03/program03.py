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

import time 
from immagini import *

def height(img): return len(img)
def width(img): return len(img[0])
def inside(img,i,j):
    w, h=width(img),height(img)
    return 0<=i<w and 0<=j<h

def get_color(img,l): return [img[j][i] for j in range(height(img)) for i in range(width(img)) if i == l[0] and j == l[1]]

def lun(img):
    c = 1
    try:
        for j in range(height(img)):
            if img[j] != img[j+1]:
                c += 1
    except IndexError: pass
    return int(height(img) / c)

def process(img, c): return [(i,j) for j in range(height(img)) for i in range(width(img)) if img[j][i] == c[0]] #Crea lista colorata

def quadm(l):
    ls= []
    lq = []
    for n in range(len(l)):
        try:
            if (l[n][0]+1 == l[n+1][0]) and (l[n][1]+1 ==l[n+1][1]): 
                ls.append(l[n])
                lq.append(ls)
                ls = []
            ls.append(l[n])
        except IndexError: lq.append(ls)
    return list(filter(None, lq))

def quadM(ls):
    l, lq = [],[]
    for n in range(len(ls)):
        try:
            if (ls[n][1] == ls[n+1][0]):
                l.append(ls[n])
                lq.append(l)
                l = []     
            l.append(ls[n])
        except IndexError: lq.append(l)
    return lq
    return lq

def edge(lq, l):
    dic = {}
    for q in lq:
        if (l[0],l[1]) in q:
            dic = {}
            try:
                for n in range(len(q)): #0 bordi 1 dentro
                    if (q[n][0] == min(q)[0]) or (q[n][0] == max(q)[0]) or\
                        (q[n][1] == min(q)[1]) or (q[n][1] == max(q)[1]):
                        dic.update({q[n]:0})
                    else: dic.update({q[n]:1})
            except IndexError: dic.update({q[n]:0})
    return dic
        
def ricolora(fname, lista, fnameout):
    img = load(fname)
    m = lun(img) #lunghezza ogni singolo quadrato
    for l in lista:
        c = get_color(img, l)
        ls = process(img,c) 
        if min(ls)[1] == m:
            lq = quadM(ls)
        else: 
            lq = quadm(ls)
        dic = edge(lq, l)
        dk = list(dic.keys())
        dv = list(dic.values())
        for k,v in zip(dk,dv):
            if v == 1: img[k[1]][k[0]] = l[2]
            if v == 0: img[k[1]][k[0]] = l[3]
        save(img, fnameout)
    
if __name__ == '__main__':
    rosso = (255,   0,   0)
    blu   = (  0,   0, 255)
    verde = (  0, 255,   0)
    nero  = (  0,   0,   0)
    bianco= (255, 255, 255)
    giallo= (255, 255,   0)
    cyan  = (  0, 255, 255)
    magenta= (255,  0, 255)
    start = time.time()
    ricolora('I1.png',[(10,10,rosso,blu),(90,10,nero,verde)],'test2.png')
    print('------ %s seconds ------' %(time.time() - start))