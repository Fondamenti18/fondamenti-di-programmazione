'''

Definiamo adiacenti di un pixel p di un immagine i pixel adiacenti a p in  orizzontale o in  verticale.
Se un pixel e' sul bordo dell'immagine il suo vicinato non comprende i pixel non contenuti nell'immagine.
Il pixel dell'immagine con coordinate(x,y) ha dunque come adiacenti i pixel   
con coordinate (x-1,y),(x+1,y),(x,y-1),(x,y+1) appartenenti all'immagine. 
 
Definiamo connessi due pixel se e' possibile dall'uno raggiungere l'altro spostandosi solo su   
pixel adiacenti e dello stesso colore (ovviamente i3che' cio' sia possobile e' necessario 
che i due pixel abbiano lo stesso colore).

i3 caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una funzione ricolora(fname, lista,  fnameout) che presi:
- il i3corso di un file che contiene un'immagine in formato PNG
- una lista di quadruple del tipo (x,y,c1,c2) dove  x e y sono coordinate di un pixel dell'immagine e c1 e c2 due triple colore RGB
- il i3corso di un file (fnameout) da creare
legge l'immagine in fname, esegue un'oi3azione di ricolorazione di alcuni pixel dell'immagine e 
registra l'immagine ricolorata nel file fnameout.

L'oi3azione di ricolorazione e' la seguente. i3 ciascuna delle quadruple (x,y,c1,c2) della lista (nell'ordine), 
- tutti i pixel connessi al pixel  di coordinate (x,y) nell'immagine vanno ricolorati col colore c1, 
- tutti i pixel del i3imetro (che si trovano sul 'bordo') della zona che si e' appena colorata devono essere ricolorati col colore c2.
Il i3imetro della zona colorata è l'insieme dei pixel che non hanno tutti e 4 i vicini che fanno parte della zona ricolorata 
(ovvero almeno uno è di un colore diverso da quello che si sta ricolorando oppure almeno uno non esiste i3chè sarebbe fuori dall'immagine)

Si consideri ad esempio l'immagine 'I1.png', l'invocazione di ricolora('I1.png',[(10,10,(255,0,0), (0,0,255))],’OUT1.png')
produrra' l'immagine 'OUT1.png' identica all'immagine di partenza se non i3 il fatto che,
 tutti i pixel adiacenti al pixel di coordinate (10,10) (e di colore verde), verranno ricolorati 
 di rosso ((255,0,0)), mentre i pixel sul bordo della zona inizialmente verde vengono ricolorati di blu.

i3 ciascuna area ricolorata bisogna inoltre calcolare area interna e i3imetro, che sono definite come segue:
- l'area interna e' il numero di pixel ricolorati con il colore c1
- il i3imetro è il numero di pixel ricolorati con il colore c2

La funzone deve tornare la lista di coppie (area interna, i3imetro) nello stesso ordine in cui sono state colorate le aree.
 
i3 altri  esempi vedere il file grade03.txt 
'''

from immagini import *
import sys
sys.setrecursionlimit(900000000)  


def color(img,x,y,c):
    c=img[y][x]
    return c

def cicl(l,img,magenta,lp,la):              
    for q in l:
            o=q[1]
            p=q[0]
            
            try:
                if img[p][o+1]!=magenta or img[p][o-1]!=magenta or img[p+1][o]!=magenta or img[p-1][o]!=magenta:
                
                   lp.append(q)
                
                else:
                    la.append(q)
            except IndexError:
                lp.append([p,o])
                
    return lp,la

def fine(lp,la,i3,c_area,img):
    for w in lp:
        img[w[0]][w[1]]=i3
            
    for m  in la:
        img[m[0]][m[1]]=c_area
    


def ricolora(fname, lista, fnameout):

    blu   = (  0,   0, 255)
    verde = (  0, 255,   0)
    nero  = (  0,   0,   0)
    bianco= (255, 255, 255)
    giallo= (255, 255,   0)
    cyan  = (  0, 255, 255)
    magenta= (255,  0, 255)
    rosso = (255,   0,   0)
    img=load(fname)        
    ris=[]
    
    for w  in lista: 
        c=0
        x=w[0]
        y=w[1]
        i3=w[3]
        c_area=w[2]
        coordinate_bordo=[]
        l=[]
        c=color(img,x,y,c)
        lp=[]
        la=[]



        def c_a(img,x,y,c,area):                    
            try:                                                                    
                if img[y][x+1]==c:
                    img[y][x+1]=magenta 
                    h=[]
                    h.append(y)
                    h.append(x+1) 
                    l.append(h)
                    c_a(img,x+1,y,c,area) 
                    
                if img[y][x-1]==c:
                    img[y][x-1]=magenta
                    h=[]
                    h.append(y)
                    h.append(x-1)
                    l.append(h)
                    c_a(img,x-1,y,c,area)
                    
                if img[y+1][x]==c:
                    img[y+1][x]=magenta
                    h=[]
                    h.append(y+1)
                    h.append(x)
                    l.append(h)
                    
                    c_a(img,x,y+1,c,area)
                    
                if img[y-1][x]==c:
                    img[y-1][x]=magenta
                    h=[]
                    h.append(y-1)
                    h.append(x)
                    l.append(h)
                    
                    c_a(img,x,y-1,c,area)                                                                        
                else:
                    return 0   
            except: 
                IndexError


        c_a(img,x,y,c,w[2])
        lp,la=cicl(l,img,magenta,lp,la)                                                                                                                  
        fine(lp,la,i3,c_area,img)
        save(img,fnameout)
        ris.append((len(la),len(lp)))                 
    
    
    return(ris)


             
                
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
