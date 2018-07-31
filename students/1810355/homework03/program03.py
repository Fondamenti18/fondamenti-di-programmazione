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
import sys
sys.setrecursionlimit(1000000000)  
rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)

def ricolora(fname, lista, fnameout):
    img=load(fname)        
    lista_della_vittoria=[]
    for el  in lista:
        ascissa=el[0]
        ordinata=el[1]
        per=el[3]
        c_area=el[2]
        coordinate_bordo=[]
        l=[]
                    
        def dimmi_colore(img,x,y):
            
            return img[y][x]
        c=dimmi_colore(img,ascissa,ordinata)
        lista_perimetro=[]
        
        def colore_area(img,x,y,c,area):                    
            try:                                                                 
                if img[y][x+1]==c:
                    img[y][x+1]=magenta
                    h=[]
                    h.append(y)
                    h.append(x+1)
                    l.append(h)
                    colore_area(img,x+1,y,c,area) 
                    
                if img[y][x-1]==c:
                    img[y][x-1]=magenta
                    h=[]
                    h.append(y)
                    h.append(x-1)
                    l.append(h)
                    colore_area(img,x-1,y,c,area)
                    
                if img[y+1][x]==c:
                    img[y+1][x]=magenta
                    h=[]
                    h.append(y+1)
                    h.append(x)
                    l.append(h)
                    
                    colore_area(img,x,y+1,c,area)
                    
                if img[y-1][x]==c:
                    img[y-1][x]=magenta
                    h=[]
                    h.append(y-1)
                    h.append(x)
                    l.append(h)
                    
                    colore_area(img,x,y-1,c,area)                                                                        
                else:
                    return 0   
            except: 
                IndexError
            
        colore_area(img,ascissa,ordinata,c,el[2])
        lista_perimetro=[]
        lista_area=[]
        for q in l:
            o=q[1]
            p=q[0]
            
            try: 
                if img[p][o+1]!=magenta or img[p][o-1]!=magenta or img[p+1][o]!=magenta or img[p-1][o]!=magenta:
                
                   lista_perimetro.append(q)
                
                else:
                    lista_area.append(q)
            except IndexError:
                lista_perimetro.append([p,o])
                                                                                                                  
        for el in lista_perimetro:  
            img[el[0]][el[1]]=per
            
        for m  in lista_area:
            img[m[0]][m[1]]=c_area
                   
        
        save(img,fnameout)
        lista_della_vittoria.append((len(lista_area),len(lista_perimetro)))                 
    
    
    return(lista_della_vittoria)




                  
                
                
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    