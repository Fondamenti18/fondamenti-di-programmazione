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

def height(img):
    return len(img)

def width(img):
    return len(img[0])

def sali(img,i,x):
    ni=i
    nl=[]
    nl2=[]
    for ni in range(i,height(img)):
        if img[ni][x]==img[i][x]:
            coo=(ni,x)
            nl.append(coo)
            if ni==len(img)-1:
                nl2.append(coo)
                break
            if img[ni+1][x]!=img[i][x]:  
                nl2.append(coo)
                break
    return nl,nl2

def scendi (img,i,x):
    ni=i
    nl=[]
    nl2=[]
    for ni in range(i-1,-1,-1):
        if img[ni][x]==img[i][x]:
            coo=(ni,x)
            nl.append(coo)
            if ni==0:
                nl2.append(coo)
                break
            if img[ni-1][x]!=img[i][x]:  
                nl2.append(coo)
                break
    return nl,nl2

def savetupla(img,i,x):
   return sali(img,i,x)[0]+scendi(img,i,x)[0],sali(img,i,x)[1]+scendi(img,i,x)[1]    

def creal(img,i,x):
    li1=[]
    li2=[]
    perimetro=0
    area=0
    for nx in range(x,width(img)):
            if nx==height(img)-1:
                li2+=savetupla(img,i,nx)[0]
                area+=len(savetupla(img,i,nx)[0])
                perimetro+=len(savetupla(img,i,nx)[0])
            elif img[i][nx]==img[i][x]:
                if img[i][nx+1]!=img[i][x]:
                    li2+=savetupla(img,i,nx)[0]
                    area+=len(savetupla(img,i,nx)[0])
                    perimetro+=len(savetupla(img,i,nx)[0])
                    break
                else:
                    li1+=savetupla(img,i,nx)[0]
                    area+=len(savetupla(img,i,nx)[0])                    
                    li2+=savetupla(img,i,nx)[1]
                    perimetro+=len(savetupla(img,i,nx)[1])
    return area,perimetro,li1,li2
    

def aumental(img,i,x,perimetro,area,li1,li2):
    for nx in range(x-1,-1,-1):
            if nx==0:
                li2+=savetupla(img,i,nx)[0]
                area+=len(savetupla(img,i,nx)[0])
                perimetro+=len(savetupla(img,i,nx)[0])
            elif img[i][nx]==img[i][x]:
                if img[i][nx-1]!=img[i][x]:
                    li2+=savetupla(img,i,nx)[0]
                    area+=len(savetupla(img,i,nx)[0])
                    perimetro+=len(savetupla(img,i,nx)[0])                    
                    break
                else:
                    li1+=savetupla(img,i,nx)[0]
                    area+=len(savetupla(img,i,nx)[0])                    
                    li2+=savetupla(img,i,nx)[1]
                    perimetro+=len(savetupla(img,i,nx)[1])
    return area,perimetro,li1,li2

def ricolora(fname,lista,fnameout):
    img=load(fname)
    out=[]
    for el in lista:
        li1=[]
        li2=[]
        perimetro=0
        area=0
        x=el[0]
        i=el[1]
        c1=el[2]
        c2=el[3]
        area+=aumental(img,i,x,creal(img,i,x)[1],creal(img,i,x)[0],creal(img,i,x)[2],creal(img,i,x)[3])[0]
        perimetro+=aumental(img,i,x,creal(img,i,x)[1],creal(img,i,x)[0],creal(img,i,x)[2],creal(img,i,x)[3])[1]
        li1+=aumental(img,i,x,creal(img,i,x)[1],creal(img,i,x)[0],creal(img,i,x)[2],creal(img,i,x)[3])[2]
        li2+=aumental(img,i,x,creal(img,i,x)[1],creal(img,i,x)[0],creal(img,i,x)[2],creal(img,i,x)[3])[3]
        coloc1(img,li1,c1)
        coloc2(img,li2,c2)
        out.append((area-perimetro,perimetro))
    save(img,fnameout)
    return out

def coloc1(img,li1,c1):
    for el in li1:
        img[el[0]][el[1]]=c1

def coloc2(img,li2,c2):
    for el in li2:
        img[el[0]][el[1]]=c2