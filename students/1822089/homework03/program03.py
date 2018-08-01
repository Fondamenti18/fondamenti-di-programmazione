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
    area_perimetro=readList(img,lista)
    save(img,fnameout)
    return area_perimetro

#Scorre la lista
def readList(img,lista):
    area_perimetro=[]
    for tupla in lista:
        img,area,perimetro=editImg(img,tupla[0],tupla[1],tupla[2],tupla[3],img[tupla[1]][tupla[0]])
        area_perimetro.append((area,perimetro))
    return area_perimetro

perimetro=0
p_calcolato=False
changed=set() #Conterrà tutti i pixel già colorati

#Lavora sull'immagine
def editImg(img,xStart,yStart,c1,c2,cStart):
    global p_calcolato #flag per evitare di contare un pixel 2 volte per il perimetro (ad esempio per gli angoli)
    global perimetro
    global changed
    changed=set()
    perimetro=0
    area=0
    
    #Conterrà tutti i pixel collegati a (x,y)
    points = set()
    points.add((xStart,yStart))
    
    while not points is False:
            
        try:
            #Ottengo un punto di coordinate (x,y) e lo elimino dal set
            (x,y) = points.pop()
        except KeyError: #Errore generato quando non ci sono più elementi da cancellare nel set
            break
        
        p_calcolato=False
        #Color border
        b_left(img,x,y,c2,cStart)
        b_right(img,x,y,c2,cStart)
        b_up(img,x,y,c2,cStart)
        b_down(img,x,y,c2,cStart)
        
        if img[y][x]!=c2:
            img[y][x]=c1 #Colora il pixel dell'area
            changed.add((x,y))
            area+=1
        
        points=points.union(addPoints(img,x,y,cStart))
        
    return img,area,perimetro

def b_left(img,x,y,c2,cStart):
    global perimetro
    global p_calcolato
    global changed
    
    if x<1: #Prima colonna dell'immagine
        img[y][x]=c2
        changed.add((x,y))
        perimetro+=1
        p_calcolato=True
    #Pixel a sinistra: se è diverso dal colore di partenza e non è un pixel che è stato colorato, allora (x,y) = c2
    elif img[y][x-1]!=cStart and (x-1,y) not in changed:
        img[y][x]=c2
        changed.add((x,y))
        perimetro+=1
        p_calcolato=True
    return

def b_right(img,x,y,c2,cStart):
    global perimetro
    global p_calcolato
    global changed
    
    if x==len(img[0])-1:
        if p_calcolato==False:
            img[y][x]=c2
            changed.add((x,y))
            perimetro+=1
            p_calcolato=True
    elif img[y][x+1]!=cStart and (x+1,y) not in changed and p_calcolato==False:
        img[y][x]=c2
        changed.add((x,y))
        perimetro+=1
        p_calcolato=True
    return

def b_up(img,x,y,c2,cStart):
    global perimetro
    global p_calcolato
    global changed
    
    if y<1:
        if p_calcolato==False:
            img[y][x]=c2
            changed.add((x,y))
            perimetro+=1
            p_calcolato=True
    elif img[y-1][x]!=cStart and (x,y-1) not in changed and p_calcolato==False:
        img[y][x]=c2
        changed.add((x,y))
        perimetro+=1
        p_calcolato=True
    return

def b_down(img,x,y,c2,cStart):
    global perimetro
    global p_calcolato
    global changed
    
    if y==len(img)-1:
        if p_calcolato==False:
            img[y][x]=c2
            changed.add((x,y))
            perimetro+=1
            p_calcolato=True
    elif img[y+1][x]!=cStart and (x,y+1) not in changed and p_calcolato==False:
        img[y][x]=c2
        changed.add((x,y))
        perimetro+=1
        p_calcolato=True
        
    return

otherPoints=set()

#Gestisce i punti che dovranno essere controllati
def addPoints(img,x,y,cStart):
    global otherPoints
    otherPoints=set()
    
    if x>0:
        leftPoint(img,x,y,cStart)
    if x<len(img[0])-1:
        rightPoint(img,x,y,cStart)
    if y>0:
        upPoint(img,x,y,cStart)
    if y<len(img)-1:
        downPoint(img,x,y,cStart)
    return otherPoints

#Left point
def leftPoint(img,x,y,cStart):
    global changed
    global otherPoints
    if img[y][x-1]==cStart and (x-1,y) not in changed:
        otherPoints.add((x-1,y))
    return
#Right point
def rightPoint(img,x,y,cStart):
    global changed
    global otherPoints
    if img[y][x+1]==cStart and (x+1,y) not in changed:
        otherPoints.add((x+1,y))
    return
#Up point
def upPoint(img,x,y,cStart):
    global changed
    global otherPoints
    if img[y-1][x]==cStart and (x,y-1) not in changed:
        otherPoints.add((x,y-1))
    return
#Down point
def downPoint(img,x,y,cStart):
    global changed
    global otherPoints
    if img[y+1][x]==cStart and (x,y+1) not in changed:
        otherPoints.add((x,y+1))
    return

