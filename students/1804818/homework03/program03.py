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
    lista_1=[]
    aree_perimetri=[]
    for el in lista:
        lista_1+=[[el[0], el[1], el[2], el[3]]]
    for el_1 in lista_1:
        cont_a=1
        cont_p=0
        lista_3_y=[]
        lista_3_x=[]
        x=el_1[0]
        y=el_1[1]
        c1=el_1[2]
        c2=el_1[3]
        lista_2=[]
        cont=0
        c0=img[y][x]
        img[y][x]=c1
        while 0<=(x+1)<len(img[0]) and img[y][x+1]==c0:
            cont+=1
            x+=1
            if img[y][x]!=c1:
                cont_a+=1
            img[y][x]=c1
            lista_2+=[[y, x]]
            
        img[y][x]=c2
        lista_3_y+=[y]
        lista_3_x+=[x]
        x-=cont
        cont=0
        while 0<=(y+1)<len(img) and img[y+1][x]==c0:
            cont+=1
            y+=1
            if img[y][x]!=c1:
                cont_a+=1
            img[y][x]=c1
            lista_2+=[[y, x]]
        img[y][x]=c2
        lista_3_y+=[y]
        lista_3_x+=[x]
        y-=cont
        cont=0
        while 0<=(x-1)<len(img[0]) and img[y][x-1]==c0:
            cont+=1
            x-=1
            if img[y][x]!=c1:
                cont_a+=1
            img[y][x]=c1
            lista_2+=[[y, x]]
        img[y][x]=c2
        lista_3_y+=[y]
        lista_3_x+=[x]
        x+=cont
        cont=0
        while 0<=(y-1)<len(img) and img[y-1][x]==c0:
            cont+=1
            y-=1
            if img[y][x]!=c1:
                cont_a+=1
            img[y][x]=c1
            lista_2+=[[y, x]]
        img[y][x]=c2
        lista_3_y+=[y]
        lista_3_x+=[x]
        y+=cont
        cont=0
        min_y=min(lista_3_y)
        max_y=max(lista_3_y)
        min_x=min(lista_3_x)
        max_x=max(lista_3_x)
        cont_p=((max_y-min_y)+(max_x-min_x))*2
        for py in range(min_y, max_y+1):
            for px in range(min_x, max_x+1):
                img[min_y][px]=c2
                img[py][max_x]=c2
                img[max_y][px]=c2
                img[py][min_x]=c2
        
        for coor in lista_2:
            y=coor[0]
            x=coor[1]
            while 0<=(y+1)<len(img) and img[y+1][x]==c0:
                cont+=1
                y+=1
                if img[y][x]!=c1:
                    cont_a+=1
                img[y][x]=c1
                #lista_2+=[[y, x]]
            y-=cont
            cont=0
            while 0<=(x-1)<len(img[0]) and img[y][x-1]==c0:
                cont+=1
                x-=1
                if img[y][x]!=c1:
                    cont_a+=1
                img[y][x]=c1
                #lista_2+=[[y, x]]
            x+=cont
            cont=0
            while 0<=(y-1)<len(img) and img[y-1][x]==c0:
                cont+=1
                y-=1
                if img[y][x]!=c1:
                    cont_a+=1
                img[y][x]=c1
                #lista_2+=[[y, x]]
            y+=cont
            cont=0
            while 0<=(x+1)<len(img[0]) and img[y][x+1]==c0:
                cont+=1
                x+=1
                if img[y][x]!=c1:
                    cont_a+=1
                img[y][x]=c1
                #lista_2+=[[y, x]]
            x-=cont
            cont=0
        aree_perimetri+=[((cont_a-4), cont_p)]
    save(img, fnameout)
    return aree_perimetri
    