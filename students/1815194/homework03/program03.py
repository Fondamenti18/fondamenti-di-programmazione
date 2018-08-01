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
rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)  





def salva_tupla(img,y,x):
    yc=y
    lc=[]
    lc2=[]
    a=tuple()
    for yc in range(y,len(img)):
        if img[yc][x]==img[y][x]:
            a=(yc,x)
            lc.append(a)
            if yc==len(img)-1:
                lc2.append(a)
                break
            if img[yc+1][x]!=img[y][x]:  
                lc2.append(a)
                break
    for yc in range(y-1,-1,-1):
        if img[yc][x]==img[y][x]:
            a=(yc,x)
            lc.append(a)
            if yc==0:
                lc2.append(a)
                break
            if img[yc-1][x]!=img[y][x]:  
                lc2.append(a)
                break
    return lc,lc2
    
    
def ricolora(fname,lista,fnameout):
    img=load(fname)
    L=[]
    for el in lista:
        PERIMETRO=0
        AREA=0
        lc1=[]
        lc2=[]
        x=el[0]
        y=el[1]
        c1=el[2]
        c2=el[3]
        retu=tuple()
        for xc in range(x,len(img)):
            if xc==len(img)-1:
                lc2+=salva_tupla(img,y,xc)[0]
                AREA+=len(salva_tupla(img,y,xc)[0])
                PERIMETRO+=len(salva_tupla(img,y,xc)[0])
                
            elif img[y][xc]==img[y][x]:
                if img[y][xc+1]!=img[y][x]:
                    lc2+=salva_tupla(img,y,xc)[0]
                    AREA+=len(salva_tupla(img,y,xc)[0])
                    PERIMETRO+=len(salva_tupla(img,y,xc)[0])
                    
                    break
                else:
                    lc1+=salva_tupla(img,y,xc)[0]
                    AREA+=len(salva_tupla(img,y,xc)[0])                    
                    lc2+=salva_tupla(img,y,xc)[1]
                    PERIMETRO+=len(salva_tupla(img,y,xc)[1])
        for xc in range(x-1,-1,-1):
            if xc==0:
                lc2+=salva_tupla(img,y,xc)[0]
                AREA+=len(salva_tupla(img,y,xc)[0])
                PERIMETRO+=len(salva_tupla(img,y,xc)[0])
            elif img[y][xc]==img[y][x]:
                if img[y][xc-1]!=img[y][x]:
                    lc2+=salva_tupla(img,y,xc)[0]
                    AREA+=len(salva_tupla(img,y,xc)[0])
                    PERIMETRO+=len(salva_tupla(img,y,xc)[0])
                    
                    break
                else:
                    lc1+=salva_tupla(img,y,xc)[0]
                    AREA+=len(salva_tupla(img,y,xc)[0])
                    lc2+=salva_tupla(img,y,xc)[1]
                    PERIMETRO+=len(salva_tupla(img,y,xc)[1])
        for el in lc1:
            img[el[0]][el[1]]=c1
        for il in lc2:
            img[il[0]][il[1]]=c2
        AREA=AREA-PERIMETRO
        retu=(AREA,PERIMETRO)
        L.append(retu)
        
    save(img,fnameout)
    
    
    return L