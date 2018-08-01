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
    lista_parametri=modifica(img,lista)
    save(img,fnameout)
    return lista_parametri


def modifica(img,lista):
    lista_attributi=[]
    for parametri in lista:
        lista_attributi+=[colora(img,parametri)]
    return lista_attributi

def colora(img,parametri):
    y,x,c1,c2=parametri
    if (x,y)==reset(img,x,y):
        attributi=interno(img,x,y,img[x][y],c1,c2)
    else:
        attributi=mod_pixel(img,x,y,img[x][y],c1,c2)
    return attributi


def mod_pixel(img,x,y,c,c1,c2):
    area,perimetro=0,0
    j=y
    while 0<=j<len(img) and 0<=x<len(img[0]) and img[x][j]==c:
        if 0<=j+1<len(img) and 0<=x<len(img[0]) and img[x][j+1]==c:
            img[x][j]=c1
            area+=1
        else:
            img[x][j]=c2
            perimetro+=1
        j+=1
    j=y-1
    while 0<=j<len(img) and 0<=x<len(img[0]) and img[x][j]==c:
        if 0<=j-1<len(img) and 0<=x<len(img[0]) and img[x][j-1]==c:
            img[x][j]=c1
            area+=1
        else:
            img[x][j]=c2
            perimetro+=1
        j-=1

    i=x+1        
    while 0<=y<len(img) and 0<=i<len(img[0]) and img[i][y]==c:
        if 0<=y<len(img) and 0<=i+1<len(img[0]) and img[i+1][y]==c:
            img[i][y]=c1
            area+=1
        else:
            img[i][y]=c2
            perimetro+=1
        i+=1
    i=x-1
    while 0<=y<len(img) and 0<=i<len(img[0]) and img[i][y]==c:
        if 0<=y<len(img) and 0<=i-1<len(img[0]) and img[i-1][y]==c:
            img[i][y]=c1
            area+=1
        else:
            img[i][y]=c2
            perimetro+=1
        i-=1
        
    att1=quadrante1(img,x-1,y+1,c,c1,c2)
    att2=quadrante2(img,x-1,y-1,c,c1,c2)
    att3=quadrante3(img,x+1,y-1,c,c1,c2)
    att4=quadrante4(img,x+1,y+1,c,c1,c2)
    
    area+=att1[0]+att2[0]+att3[0]+att4[0]
    perimetro+=att1[1]+att2[1]+att3[1]+att4[1]
    
    return area,perimetro

def quadrante1(img,x,y,c,c1,c2):
    area,perimetro=0,0
    while 0<=y<len(img) and 0<=x<len(img[0]) and img[x][y]==c:
        j=y
        while 0<=j<len(img) and 0<=x<len(img[0]) and img[x][j]==c:
            if inside(img,x,j+1) and inside(img,x-1,j) and img[x][j+1]==c and img[x-1][j]==c:
                img[x][j]=c1
                area+=1
            else:
                img[x][j]=c2
                perimetro+=1
            j+=1
        x-=1
    return area,perimetro

def quadrante2(img,x,y,c,c1,c2):
    area,perimetro=0,0
    while 0<=y<len(img) and 0<=x<len(img[0]) and img[x][y]==c:
        j=y
        while 0<=j<len(img) and 0<=x<len(img[0]) and img[x][j]==c:
            if inside(img,x,j-1) and inside(img,x-1,j) and img[x][j-1]==c and img[x-1][j]==c:
                img[x][j]=c1
                area+=1
            else:
                img[x][j]=c2
                perimetro+=1
            j-=1
        x-=1
    return area,perimetro

def quadrante3(img,x,y,c,c1,c2):
    area,perimetro=0,0
    while 0<=y<len(img) and 0<=x<len(img[0]) and img[x][y]==c:
        j=y
        while 0<=j<len(img) and 0<=x<len(img[0]) and img[x][j]==c:
            if inside(img,x,j-1) and inside(img,x+1,j) and img[x][j-1]==c and img[x+1][j]==c:
                img[x][j]=c1
                area+=1
            else:
                img[x][j]=c2
                perimetro+=1
            j-=1
        x+=1
    return area,perimetro

def quadrante4(img,x,y,c,c1,c2):
    area,perimetro=0,0
    while 0<=y<len(img) and 0<=x<len(img[0]) and img[x][y]==c:
        j=y
        while 0<=j<len(img) and 0<=x<len(img[0]) and img[x][j]==c:
            if inside(img,x,j+1) and inside(img,x+1,j) and img[x][j+1]==c and img[x+1][j]==c:
                img[x][j]=c1
                area+=1
            else:
                img[x][j]=c2
                perimetro+=1
            j+=1
        x+=1
    return area,perimetro

def inside(img,x,j):
    return 0<=j<len(img) and 0<=x<len(img[0])


def interno(img,x,y,c,c1,c2):
    area=0
    l=lunghezza(img)
    x0,y0=reset(img,x,y)
    
    for px in range(x0,x0+l):
        for py in range(y0,y0+l):
            if 0<=py<len(img) and 0<=px<len(img[0]) and img[px][py]==c:
                img[px][py]=c1
                area+=1
    perimetro=bordo(img,x0,y0,l,c2)
    
    return area-perimetro,perimetro


def bordo(img,x,y,l,c2):
    perimetro=0
    for px in range(x,x+l):
        img[px][y]=c2
        img[px][y+l-1]=c2
        perimetro+=2
    for py in range(y,y+l):
        img[x][py]=c2
        img[x+l-1][py]=c2
        perimetro+=2
    return perimetro-4

def reset(img,x,y):
    i,j=0,0
    while (0<=y<len(img) and 0<=x-i<len(img[0])) and img[x-i][y]==img[x][y]:
        i+=1
    x0=x-i+1
    while (0<=y-j<len(img) and 0<=x<len(img[0])) and img[x][y-j]==img[x][y]:
        j+=1
    y0=y-j+1
    return x0,y0

def lunghezza(img):
    l=0
    for y in range(len(img[0])):
        if img[0][y]==img[0][y+1]:
            l+=1
        else:
            break
    return l+1