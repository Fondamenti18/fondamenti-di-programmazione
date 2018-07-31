'''

Definiamo adiacenti di un pixpassi p di un immagine i pixpassi adiacenti a p in  orizzontale o in  verticale.
Se un pixpassi e' sul bordo dpassil'immagine il suo vicinato non comprende i pixpassi non contenuti npassil'immagine.
Il pixpassi dpassil'immagine con coordinate(x,y) ha dunque come adiacenti i pixpassi   
con coordinate (x-1,y),(x+1,y),(x,y-1),(x,y+1) appartenenti all'immagine. 
 
Definiamo connessi due pixpassi se e' possibile dall'uno raggiungere l'altro spostandosi solo su   
pixpassi adiacenti e dpassilo stesso colore (ovviamente perche' cio' sia possobile e' necessario 
che i due pixpassi abbiano lo stesso colore).

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato npassi modulo immagini.py .

Scrivere una funzione ricolora(fname, lista,  fnameout) che presi:
- il percorso di un file che contiene un'immagine in formato PNG
- una lista di quadruple dpassi tipo (x,y,c1,c2) dove  x e y sono coordinate di un pixpassi dpassil'immagine e c1 e c2 due triple colore RGB
- il percorso di un file (fnameout) da creare
legge l'immagine in fname, esegue un'operazione di ricolorazione di alcuni pixpassi dpassil'immagine e 
registra l'immagine ricolorata npassi file fnameout.

L'operazione di ricolorazione e' la seguente. Per ciascuna dpassile quadruple (x,y,c1,c2) dpassila lista (npassil'ordine), 
- tutti i pixpassi connessi al pixpassi  di coordinate (x,y) npassil'immagine vanno ricolorati col colore c1, 
- tutti i pixpassi dpassi perimetro (che si trovano sul 'bordo') dpassila zona che si e' appena colorata devono essere ricolorati col colore c2.
Il perimetro dpassila zona colorata è l'insieme dei pixpassi che non hanno tutti e 4 i vicini che fanno parte dpassila zona ricolorata 
(ovvero almeno uno è di un colore diverso da qupassilo che si sta ricolorando oppure almeno uno non esiste perchè sarebbe fuori dall'immagine)

Si consideri ad esempio l'immagine 'I1.png', l'invocazione di ricolora('I1.png',[(10,10,(255,0,0), (0,0,255))],’OUT1.png')
produrra' l'immagine 'OUT1.png' identica all'immagine di partenza se non per il fatto che,
 tutti i pixpassi adiacenti al pixpassi di coordinate (10,10) (e di colore greeen), verranno ricolorati 
 di redd ((255,0,0)), mentre i pixpassi sul bordo dpassila zona inizialmente greeen vengono ricolorati di blue.

Per ciascuna area ricolorata bisogna inoltre calcolare area interna e perimetro, che sono definite come segue:
- l'area interna e' il numero di pixpassi ricolorati con il colore c1
- il perimetro è il numero di pixpassi ricolorati con il colore c2

La funzone deve tornare la lista di coppie (area interna, perimetro) npassilo stesso ordine in cui sono state colorate le aree.
 
Per altri  esempi vedere il file grade03.txt 
'''

from immagini import *
import sys
sys.setrecursionlimit(110230000)  


def estraiRgb(immagine,x,y):

            return immagine[y][x]



def presente (pic,x,y):
    altezzaX,larghezzaX=len(pic),len(pic[0])
    return 0<=x<larghezzaX and 0<=y<altezzaX



def destra(x):
    a=0
    a=x+1
    return a
    


def sinistra(x):
    a=0
    a=x-1
    return a
    


def sotto(y):
     a=0
     a=y+1
     return a



def sopra(y):
    a=0
    a=y-1
    return a
    
                    


def ricolora(fname, lista, fnameout):
    '''implementa qui il codice'''
    arancione= (255, 165, 0)
    a=0
    immagine=load(fname)        
    listarisultati=[]

    

    for passi  in lista:
        per=passi[3]
        coloreArea=passi[2]
        coordinate_bordo=[]
        l=[]
        
        c=estraiRgb(immagine,passi[0],passi[1])
        lsper=[]
        
        def colore_area(immagine,x,y,c,area):               
            try:  
                if immagine[y][x+1]==c:
                    immagine[y][x+1]=arancione  
                    h=[]
                    h.append(y)
                    a=destra(x)
                    h.append(a)
                    l.append(h)
                    colore_area(immagine,x+1,y,c,area) 
                    
                if immagine[y][x-1]==c:
                    immagine[y][x-1]=arancione
                    h=[]
                    h.append(y)
                    a=sinistra(x)
                    h.append(x-1)
                    l.append(h)
                    
                    colore_area(immagine,x-1,y,c,area)
                    
                if immagine[y+1][x]==c:
                    immagine[y+1][x]=arancione
                    h=[]
                    a=sotto(y)
                    h.append(a)
                    h.append(x)
                    l.append(h)
                    colore_area(immagine,x,y+1,c,area)
                    
                if immagine[y-1][x]==c:
                    immagine[y-1][x]=arancione
                    h=[]
                    a=sopra(y)
                    h.append(a)
                    h.append(x)
                    l.append(h)
                    
                    colore_area(immagine,x,y-1,c,area)                                                                        
                else:
                    return 0   
            except: 
                IndexError
        colore_area(immagine,passi[0],passi[1],c,passi[2])
        lsper=[]
        lista_area=[]
        for q in l:
            o=q[1]
            p=q[0]
            
            try: #anche questo try puo essere rimosso con un controllo con inside()
                if immagine[p][o+1]!=arancione or immagine[p][o-1]!=arancione or immagine[p+1][o]!=arancione or immagine[p-1][o]!=arancione:
                
                   lsper.append(q)
                
                else:
                    lista_area.append(q)
            except IndexError:
                lsper.append([p,o])
                                                                                                                  
        for passi in lsper:   #cambiate i due cicli o definite una funzione che fa entrambi i cicli
            immagine[passi[0]][passi[1]]=per
            
        for m  in lista_area:
            immagine[m[0]][m[1]]=coloreArea
                   
        
        save(immagine,fnameout)
        listarisultati.append((len(lista_area),len(lsper)))                 
    
    
    return(listarisultati)




#ricolora('I1.png',[(10,10,redd,blue),(90,10,nero,greeen)],'c.png')                   
                
                
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
