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
    
   
            
        
            
                
def interno(img, x, y):
    return 0 <= y < len(img) and 0 <= x < len(img[0])    

    
    



        
        
        
        
        
def connessi(x,y,img):
    
    l=[(x,y)]
   
    for i in l:
        ins=set(l)
       
        
        for xy in [[i[0]+1,i[1]],[i[0]-1,i[1]],[i[0],i[1]+1],[i[0],i[1]-1]]:
            xx=xy[0]
            yy=xy[1]
            
            if (xx+1,yy) in ins and (xx-1,yy) in ins and (xx,yy+1) in ins and (xx,yy-1) in ins:
                pass
            
            if interno(img,xx,yy) and img[yy][xx]==img[y][x] and (xx,yy) not in ins:
                l.append((xx,yy))
        
            
    
    return set(l)
            
            

def ricolora(fname, lista, fnameout):
    img0=load(fname)
    coppie=[]
    diz={}
    
    for quadr in lista:
        perimetro=set()
        x=quadr[0]
        y=quadr[1]
        c1=quadr[2]
        c2=quadr[3]
        
        cont_a=0
        cont_p=0
        
        if (x,y) not in diz.keys():
            lista_conn=connessi(x,y,img0)
            diz[(x,y)]=lista_conn
        else:
            lista_conn=diz[(x,y)]
        for x_y in lista_conn:
            xc=x_y[0]
            yc=x_y[1]
            
            if (xc+1,yc) not in lista_conn or (xc-1,yc) not in lista_conn or (xc,yc+1) not in lista_conn or (xc,yc-1) not in lista_conn:
                img0[yc][xc]=c2
                cont_p+=1
                perimetro.add((xc,yc))
                
            else:
                img0[yc][xc]=c1
                cont_a+=1
        if (x,y) not in perimetro: 
            diz[(x,y)].difference_update(perimetro)
    
                        
                    
                
        else:
            diz[(x,y)]=perimetro
        coppie.append((cont_a,cont_p))
    
    
    save(img0,fnameout)
    return coppie