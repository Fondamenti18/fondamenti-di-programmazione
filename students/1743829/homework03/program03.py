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

def apri_file(fname):
    img=load(fname)
    return img

def colora_vicini(img,img2,x,y,col_pixel,col_nuovo):
    area=0
    if (y+1)<len(img):
        if img2[y+1][x]==col_pixel:
            img[y+1][x]=col_nuovo
            area+=1
    if (y-1)>=0:
        if img2[y-1][x]==col_pixel:
            img[y-1][x]=col_nuovo
            area+=1
    if (x+1)<len(img[0]):
        if img2[y][x+1]==col_pixel:
            img[y][x+1]=col_pixel
            area+=1
    if (x-1)>=0:
        if img2[y][x-1]==col_pixel:
            img[y][x-1]=col_nuovo
            area+=1
    return area

def trov_estr(img,x,y,col):
    for c in range(0,len(img[0])):
        if (x+c)<len(img[0]):
            if img[y][x+c]==col:
                fine_c=x+c
            else:
                break
    for r in range(0,len(img)):
        if (y+r)<len(img):
            if img[y+r][x]==col:
                fine_r=y+r
            else:
                break            
    return fine_c,fine_r

def colora_bordo(img,x,y,h,l,c1,c2):
    cor_x=x
    cor_y=y
    perimetro=0
    while y-1 >=0:
        if img[y-1][h]==c1:
            img[y-1][h]=c2
            y-=1
            perimetro+=1
        else:
            break
    while x-1>=0:
        if img[l][x-1]==c1:
            img[l][x-1]=c2
            x-=1
            perimetro+=1
        else:
            break
    for i in range(0,l+1):
        if (cor_y+i)<len(img):
            if img[cor_y+i][h]==c1:
                img[cor_y+i][h]=c2
                perimetro+=1
            if img[cor_y+i][x]==c1:
                img[cor_y+i][x]=c2
                perimetro+=1       
    for k in range(0,l+1):            
        if (cor_y-k)>=0:
            if img[cor_y-k][x]==c1:
                img[cor_y-k][x]=c2
                perimetro+=1
                
    for g in range(0,h+1):
        if (cor_x+g)<len(img[0]):
            if img[l][cor_x+g]==c1:
                img[l][cor_x+g]=c2
                perimetro+=1
            if img[y][cor_x+g]==c1:
                img[y][cor_x+g]=c2
                perimetro+=1
    for j in range(0,h+1):
        if (cor_x-j)>=0:
            if img[y][cor_x-j]==c1:
                img[y][cor_x-j]=c2  
                perimetro+=1
    return perimetro


                       
                    
def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    img=apri_file(fname)
    img2=img.copy()
    ris=[]                        
    for i in range(0,len(lista)):
        area=0
        perimetro=0
        x=lista[i][0]
        y=lista[i][1]
        col_nuovo=lista[i][2]
        col_bordo=lista[i][3]
        col_pixel=img[y][x]
        fine_c,fine_r=trov_estr(img,x,y,col_pixel)
        area+=colora_vicini(img,img2,x,y,col_pixel,col_nuovo)
        for n in range(0,len(img)):
            area-=colora_vicini(img,img2,x,y,col_pixel,col_nuovo)
            if (y+n)< fine_r:
                area+=colora_vicini(img,img2,x,y+n,col_pixel,col_nuovo)
                
                for m in range(0,len(img[0])):
                    if (x+m)<=fine_c:
                        area+=colora_vicini(img,img2,x+m,y+n,col_pixel,col_nuovo)
                        area-=colora_vicini(img,img2,x+m,y,col_pixel,col_nuovo)
                        
                    if (x-m)>=0:
                        area+=colora_vicini(img,img2,x-m,y+n,col_pixel,col_nuovo)
                        area-=colora_vicini(img,img2,x-m,y,col_pixel,col_nuovo)
                        
            if (y-n)>=0:
                area+=colora_vicini(img,img2,x,y-n,col_pixel,col_nuovo)

                for m in range(0,len(img[0])):
                    if (x+m)<=fine_c:
                        area+=colora_vicini(img,img2,x+m,y-n,col_pixel,col_nuovo)
                        
                        area-=colora_vicini(img,img2,x+m,y,col_pixel,col_nuovo)
                    if (x-m)>=0:
                        area+=colora_vicini(img,img2,x-m,y-n,col_pixel,col_nuovo)
                        
                        area-=colora_vicini(img,img2,x-m,y,col_pixel,col_nuovo)
        perimetro=colora_bordo(img,x,y,fine_c,fine_r,col_nuovo,col_bordo)
        a=area-perimetro
        ris+=[(a,perimetro)]
    save(img,fnameout)
    return ris

        
    
                        
        

    


