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
    lout=[]
    img=load(fname)
    w,h=len(img[0]),len(img)
    for k in lista:
        x,y,c1,c2=k[0],k[1],k[2],k[3]
        q1,q2,q3,q4=True,True,True,True
        a,p=0,0
        la,lp=[],[]
        c=img[y][x]
        while img[y][x]==c and 0<=x<w:
            x-=1
        if x<0:
            x+=1
        while img[y][x]==c and 0<=y<h:
            y-=1
        if y<0:
            y+=1
        while 0<=x<w:
            while 0<=y<h:
                j=0
                if (img[y][x]==c or img[y][x]==c1)and(q1==True or q2==True or q3==True or q4==True):
                    q1,q2,q3,q4=False,False,False,False
                    if x==0 or y==0 or x==w-1 or y==h-1:
                        img[y][x]=c2
                        if(x,y) not in lp:
                            lp.append((x,y))
                    if x-1>=0:
                        if img[y][x-1]==c or (x-1,y) in la or (x-1,y) in lp:
                            if(x-1,y) not in lp:
                                img[y][x-1]=c1
                            j+=1
                            if (x-1,y) not in la:
                                la.append((x-1,y))
                            q1=True
                        elif (x,y) in la:
                            img[y][x]=c2
                            if(x,y) not in lp:
                                lp.append((x,y))
                    if x+1<w:
                        if img[y][x+1]==c or (x+1,y) in la or (x+1,y) in lp:
                            if(x+1,y) not in lp:
                                img[y][x+1]=c1
                            j+=1
                            if (x+1,y) not in la:
                                la.append((x+1,y))
                            q2=True
                        elif (x,y) in la:
                            img[y][x]=c2
                            if(x,y) not in lp:
                                lp.append((x,y))
                    if y-1>=0:
                        if img[y-1][x]==c or (x,y-1) in la or (x,y-1) in lp:
                            if(x,y-1) not in lp:
                                img[y-1][x]=c1
                            j+=1
                            if (x,y-1) not in la:
                                la.append((x,y-1))
                            q3=True
                        elif (x,y) in la:
                            img[y][x]=c2
                            if(x,y) not in lp:
                                lp.append((x,y))
                    if y+1<h:
                        if img[y+1][x]==c or (x,y+1) in la or (x,y+1) in lp:
                            if(x,y+1) not in lp:
                                img[y+1][x]=c1
                            j+=1
                            if (x,y+1) not in la:
                                la.append((x,y+1))
                            q4=True
                        elif (x,y) in la:
                            img[y][x]=c2
                            if(x,y) not in lp:
                                lp.append((x,y))
                else:
                    break
                y+=1
            y=0
            x+=1
        p=len(lp)
        a=len(la)-p
        lout.append((a,p))
    save(img,fnameout)
    return(lout)
