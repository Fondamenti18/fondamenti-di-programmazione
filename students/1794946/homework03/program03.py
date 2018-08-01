
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

La funzione deve tornare la lista di coppie (area interna, perimetro) nello stesso ordine in cui sono state colorate le aree.
 
Per altri  esempi vedere il file grade03.txt 
'''

from immagini import *

def inside(img, x, y):
    return 0 <= x < len(img[0]) and 0 <= y < len(img)

def color(controllo, area, perimetro,img):
    single=set()
    if controllo[-1]==single:
        return area,perimetro
    for el in controllo[-1]:
        x=el[0]
        y=el[1]
        if (x,y) not in area:
            if (x,y) not in perimetro:
                t=inside(img, x+1, y) and img[y][x+1]==img[y][x]
                z=inside(img, x-1, y) and img[y][x-1]==img[y][x]
                l=inside(img, x, y+1) and img[y+1][x]==img[y][x]
                d=inside(img, x, y-1) and img[y-1][x]==img[y][x]
                if t==True and z==True and l==True and d==True:                                
                    area.add((x,y))
                    if not any((x+1, y) in i for i  in controllo):
                        single.add((x+1,y))
                    if not any((x, y+1) in i for i  in controllo):
                        single.add((x,y+1))
                    if not any((x-1, y) in i for i  in controllo):
                        single.add((x-1,y))
                    if not any((x, y-1) in i for i  in controllo):
                        single.add((x,y-1))
                else:
                    perimetro.add((x,y))
                    if t==True and not any((x+1, y) in i for i  in controllo):
                        single.add((x+1,y))
                    if l==True and not any((x, y+1) in i for i  in controllo):
                        single.add((x,y+1))
                    if z==True and not any((x-1, y) in i for i  in controllo):
                        single.add((x-1,y))
                    if d==True and not any((x, y-1) in i for i  in controllo):
                        single.add((x,y-1))
    controllo.append(single)
    return color(controllo, area, perimetro,img)	
                                        
                             

def ricolora(fname, lista, fnameout):
    img=load(fname)
    lista2=[]
    for el in lista:
        x=el[0]
        y=el[1]
        c1=el[2]
        c2=el[3]
        single=set()
        single.add((x,y))
        area=set()
        controllo=[single]
        perimetro=set()
        ap=color(controllo, area, perimetro,img)
        for i in ap[0]:
            x=i[0]
            y=i[1]
            img[y][x]=c1
        for u in ap[1]:
            x=u[0]
            y=u[1]
            img[y][x]=c2
        lista2.append((len(ap[0]), len(ap[1])))
    save(img, fnameout)
    return lista2

   
rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)

'''

ricolora('I1.png',[(10,10,rosso,blu)],'test1.png')
ricolora('I1.png',[(10,10,rosso,blu),(90,10,nero,verde)],'test2.png')
ricolora('I1.png',[(10,10,bianco,blu),(90,10,verde,rosso)],'test3.png')
lista=[(i*30+1,j*30+1,bianco,verde) for i in range(10) for j in range (10)if not (i+j)%2]
ricolora('I2.png',lista,'test4.png')
lista0=[(i*30+1,j*30+1,nero, verde) for i in range(10) for j in range (10)if not (i+j)%2]
lista1=[(i*30+1,j*30+1,rosso,bianco) for i in range(10) for j in range (10)if  (i+j)%2]
ricolora('I2.png',lista0+lista1,'test5.png')
lista6=[(25,25,(0,0,0),(0,5*i,5*i)) for i in range(1,25)]
ricolora('I1.png',lista6,'test6.png')
lista7=[(0,0,(0,0,0),(0,5*i,5*i)) for i in range(1,25)]
ricolora('I1.png',lista7,'test7.png')
lista8=[(5*i+2,5*i+2,(0,255-6*i,0),(0,0,255-6*i)) for i in range(40)]
ricolora('I3.png',lista8,'test8.png')
ricolora
ricolora
ricolora
ricolora
ricolora
'''
