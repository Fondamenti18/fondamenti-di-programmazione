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
    img=load(fname)
    risposta=[]
    for i in lista:
        c=img[i[1]][i[0]]
        area=set()
        perimetro=set()        
        zona=calcola_zona(img,i[0],i[1],c)
        for j in zona:
            if adiacenti(img,c,j[0],j[1],area)==4: area.add(j)
            else: perimetro.add(j)
        img=colora(colora(img,i[2],area),i[3],perimetro)        
        risposta+=[(len(area),len(perimetro))]
    save(img,fnameout)
    return risposta
            
def calcola_zona(img,x,y,c):
    zona=[(x,y)]
    for i in zona:
        if (i[0]+1,i[1]) not in zona:
            if inside(img,i[0]+1,i[1]) and img[i[1]][i[0]+1]==c:
                zona+=[(i[0]+1,i[1])]
        if (i[0],i[1]+1) not in zona:
            if inside(img,i[0],i[1]+1) and img[i[1]+1][i[0]]==c:
                zona+=[(i[0],i[1]+1)]
        if (i[0]-1,i[1]) not in zona:
            if inside(img,i[0]-1,i[1]) and img[i[1]][i[0]-1]==c:
                zona+=[(i[0]-1,i[1])]
        if (i[0],i[1]-1) not in zona:
            if inside(img,i[0],i[1]-1) and img[i[1]-1][i[0]]==c:
                zona+=[(i[0],i[1]-1)]
    return set(zona)

        

def inside(img,x,y):
    return 0<=x<len(img[0]) and 0<=y<len(img)

def adiacenti(img,c,x,y,area):
    for i in {(1,0),(0,1),(-1,0),(0,-1)}:
        if (x+i[0],y+i[1]) not in area:
            if inside(img,x+i[0],y+i[1])==False or img[y+i[1]][x+i[0]]!=c:
                return 1
    return 4

def colora(img,c,pixel):
    for i in pixel:
        img[i[1]][i[0]]=c
    return img
