# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 23:08:13 2017

@author: samue
"""

'''

Definiamo adiacenti di un pixel p di un immagine i pixel adiacenti a p in  orizzontale o in  verticale.
Se un pixel e' sul bordo dell'immagine il suo vicinato non comprende i pixel non contenuti nell'immagine.
Il pixel dell'immagine con coordinate(x,y) ha dunque come adiacenti i pixel   
con coordinate (x-1,y),(x+1,y),(x,y-1),(x,y+1) appartenenti all'immagine. 
 
Definiamo connessi due pixel se e' possibile dall'uno raggiungere l'altro spostandosi solo su   
pixel adiacenti e dello stesso colore (ovviamente perche' cio' sia possobile e' necessario 
che i due pixel abbiano lo stesso colore).

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo 
immagini.py .

Scrivere una funzione ricolora(fname, lista,  fnameout) che presi:
- il percorso di un file che contiene un'immagine in formato PNG
- una lista di quadruple del tipo (x,y,c1,c2) dove  x e y sono coordinate di un pixel dell'immagine e 
c1 e c2 due triple colore RGB
- il percorso di un file (fnameout) da creare
legge l'immagine in fname, esegue un'operazione di ricolorazione di alcuni pixel dell'immagine e 
registra l'immagine ricolorata nel file fnameout.

L'operazione di ricolorazione e' la seguente. Per ciascuna delle quadruple (x,y,c1,c2) della lista 
(nell'ordine), 
- tutti i pixel connessi al pixel  di coordinate (x,y) nell'immagine vanno ricolorati col colore c1, 
- tutti i pixel del perimetro (che si trovano sul 'bordo') della zona che si e' appena colorata devono 
essere ricolorati col colore c2.
Il perimetro della zona colorata è l'insieme dei pixel che non hanno tutti e 4 i vicini che fanno 
parte della zona ricolorata 
(ovvero almeno uno è di un colore diverso da quello che si sta ricolorando oppure almeno uno non 
esiste perchè sarebbe fuori dall'immagine)

Si consideri ad esempio l'immagine 'I1.png', l'invocazione di ricolora('I1.png',[(10,10,(255,0,0), 
(0,0,255))],’OUT1.png')
produrra' l'immagine 'OUT1.png' identica all'immagine di partenza se non per il fatto che,
 tutti i pixel adiacenti al pixel di coordinate (10,10) (e di colore verde), verranno ricolorati 
 di rosso ((255,0,0)), mentre i pixel sul bordo della zona inizialmente verde vengono ricolorati di blu.

Per ciascuna area ricolorata bisogna inoltre calcolare area interna e perimetro, che sono definite 
come segue:
- l'area interna e' il numero di pixel ricolorati con il colore c1
- il perimetro è il numero di pixel ricolorati con il colore c2

La funzone deve tornare la lista di coppie (area interna, perimetro) nello stesso ordine in cui sono 
state colorate le aree.
 
Per altri  esempi vedere il file grade03.txt 
'''

from immagini import *



import png

def load(fname):
    """ Carica la immagine PNG dal file fname.
        Torna una lista di liste di pixel.
        Ogni pixel è una tupla (R, G, B) dei 3 colori.
        Ciascun colore è un intero tra 0 e 255 compresi.
    """
    with open(fname, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            l = []
            for i in range(0, len(line), 3):
                l+=[(line[i], line[i+1], line[i+2])]
            img+=[l]
        return img

def save(img, filename):
    """ Salva la immagine img  nel file filename in formato PNG8.
        Img e' una lista di liste di pixel.
        Ogni pixel è una tupla (R, G, B) dei 3 colori.
        Ciascun colore è un intero tra 0 e 255 compresi.
    """
    pngimg = png.from_array(img,'RGB')
    pngimg.save(filename)
    

def colora(imm, h, k, colore, perimetro, new_color):
    #print("posizione ", h,k)
    
    puntoDiPartenza=True
    while puntoDiPartenza:
        if k<len(imm[h])-1 and imm[h][k+1]==colore:
            k=k+1
        else:
            puntoDiPartenza=False
            
    area=0
    Perimetr=1
    j=h
    jj=k
    #print("posizione ", h,k)
    imm[h][k]=perimetro        
    viaLibera=True
    
    direzione="basso"    
    while viaLibera:
        #print("posizione ", h,k)
        #print("direzione ", direzione)
        check=0
        if direzione == "basso":
            if k == len(imm[h])-1 or (imm[h][k+1]!=colore and imm[h][k+1]!=new_color and imm[h][k+1]!=perimetro):
                if h==len(imm)-1 or imm[h+1][k]!=colore:
                    direzione="sinistra"
                    check=check+1
                else:
                    imm[h][k]=perimetro
                    h=h+1
                    Perimetr=Perimetr+1
            elif imm[h][k+1]==colore:
                direzione="destra"
                check=check+1
            else:
                if h==len(imm)-1 or imm[h+1][k]!=colore:
                    direzione="sinistra"
                    check=check+1       
                else:
                    imm[h][k]=new_color
                    h=h+1
                    area=area+1
                
        if direzione == "sinistra":
            if h == len(imm)-1 or (imm[h+1][k]!=colore and imm[h+1][k]!=new_color and imm[h+1][k]!=perimetro):
                if k==0 or imm[h][k-1]!=colore:
                    direzione="alto"
                    check=check+1
                else:
                    imm[h][k]=perimetro
                    k=k-1
                    Perimetr=Perimetr+1
        
            elif imm[h+1][k]==colore:
                direzione="basso"
                check=check+1
            else:
                if k==0 or imm[h][k-1]!=colore:
                    direzione="alto"
                    check=check+1
                else:
                    imm[h][k]=new_color
                    k=k-1
                    area=area+1
        if direzione == "alto":
            if k == 0 or (imm[h][k-1]!=colore and imm[h][k-1]!=new_color and imm[h][k-1]!=perimetro):
                if h==0 or imm[h-1][k]!=colore:
                    direzione="destra"
                    check=check+1
                else:
                    imm[h][k]=perimetro
                    h=h-1
                    Perimetr=Perimetr+1
        
            elif imm[h][k-1]==colore:
                direzione="sinistra"
                check=check+1
            else:
                if h==0 or imm[h-1][k]!=colore:
                    direzione="destra"
                    check=check+1
                else:
                    imm[h][k]=new_color
                    h=h-1
                    area=area+1
        if direzione == "destra":
            if h == 0 or (imm[h-1][k]!=colore and imm[h-1][k]!=new_color and imm[h-1][k]!=perimetro):
                if k==len(imm[h])-1 or imm[h][k+1]!=colore:
                    direzione="basso"
                    check=check+1
                else:
                    imm[h][k]=perimetro
                    k=k+1
                    Perimetr=Perimetr+1
        
            elif imm[h-1][k]==colore:
                direzione="alto"
                check=check+1
            else:
                if k==len(imm[h])-1 or imm[h][k+1]!=colore:
                    direzione="basso"
                    check=check+1
                else:
                    imm[h][k]=new_color
                    k=k+1
                    area=area+1
        #print(check)
        if check == 4:
            imm[h][k]=new_color
            viaLibera=False
    imm[j-1][jj]=perimetro
    L=(area,Perimetr)
    return L
                
            
        
 
        
    
    
            
def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    immagine=load(fname)
    #print(immagine)
    
    L=[]
    color=()
    for x in lista:
        a=x[0]
        b=x[1]
        c=x[2]
        d=x[3]
        color=immagine[a][b]
        L.append(colora(immagine, b, a, color, d, c))
    save(immagine, fnameout)
    return(L)








"""ricolora('I1.png',[(10,10,(255,0,0),(0,0,255))],'test1.png')
ricolora('I1.png',[(10,10,(255,0,0),(0,0,255)),(90,10,(0,0,0),(0,255,0))],'test2.png')
ricolora('I1.png',[(10,10,(255,255255),(0,255,0)),(90,10,(0,0,255),(255,0,0))],'test3.png')
ricolora('I2.png',[(i*30+1,j*30+1,(255,255,255),(0,255,0)) for i in range(10) for j in range (10)if not (i+j)%2],'test4.png')
ricolora('I2.png',[(i*30+1,j*30+1,(0,0,0), (0,255,0)) for i in range(10) for j in range (10)if not (i+j)%2]+[(i*30+1,j*30+1,(255,0,0),(255,255,255)) for i in range(10) for j in range (10)if  (i+j)%2],'test5.png')
ricolora('I1.png',[(25,25,(0,0,0),(0,5*i,5*i)) for i in range(1,25)],'test6.png')
ricolora('I1.png',[(0,0,(0,0,0),(0,5*i,5*i)) for i in range(1,25)],'test7.png')
ricolora('I3.png',[(5*i+2,5*i+2,(0,255-6*i,0),(0,0,255-6*i)) for i in range(40)],'test8.png')
ricolora('I4.png',[(100,100,(255-x,255,255),(0,0,255-x)) for x in range(100)],'test9.png')
ricolora('I5.png',[(1,1,(255,255,255),(255,255,255)),(1,1,(255,0,0),(255,0,0))]*40,'test10.png')
ricolora('I6.png',[(200+j,200+j,(255-i,255*j,0),(255*j,255-i,0))for i in range(10) for j in range(2)],'test11.png')
ricolora('I7.png',[(204,204,(0,250,0),(240,0,250))for i in range(10) ],'test12.png')"""
