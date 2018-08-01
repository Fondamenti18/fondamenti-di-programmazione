'''

Definiamo adiacenti di un pixel p di un immagine i pixel adiacenti a p in  orizzontale o in  verticale.
Se un pixel e' sul bordo dell'immagine il suo vicinato non comprende i pixel non contenuti nell'immagine.
Il pixel dell'immagine con coordinate(x,y) ha dunque come adiacenti i pixel   
con coordinate (x-1,y),(x+1,y),(x,y-1),(x,y+1) appartenenti all'immagine. 
 
Definiamo connessi due pixel  e' possibile  dall'uno raggiungere l'altro spostandosi solo su   
pixel adiacenti e dello stesso colore (ovviamente perche' cio' sia possobile e' necessario 
che i due pixel abbiano lo stesso colore).

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.png .

scrivere una funzione ricolora(fname, lista,  fnameout) che presi:
- il percorso di un file che contiene un'immagine in formato PNG
- una lista di triple del tipo (x,y,c1,c2) dove  x e y sono coordinate di pixel dell'immagine e c1 e c2   triple di  colori RGB
- il percorso di un file (fnameout)
legge l'immagine in fname, esegue un'operazione di ricolorazione di alcuni pixel dell'immagine e 
registra l'immagine ricolorata nel file fnameout e restituisce una lista di coppie di interi. 
L'operazione di ricolorazione e' la seguente. Per ciascuna delle triple (x,y,c1,c2) della 
lista, considerate nell'ordine in cui compaiono nella lista,  tutti i pixel connessi 
al pixel  di coordinate (x,y) nell'immagine vanno ricolorati col colore c1 e il bordo dell'area ricolorata 
(vale a dire i pixel ricolorati adiacenti a pixel che non sono stati ricolorati)
va ricolorato col colore c2. 
Nella lista restituita, ad ogni  elemento (x,c1,c2) 
della lista ricevuta in input corrisponde una coppia di interi. 
Il primo intero e'  il numero di pixel connessi al pixel x,y 
che sono stati ricolorati con il colore c1, il secondo numero e'  il numero di pixel adiacenti a x,y che sono stati 
ricolorati con c2.
Si consideri ad esempio l'immagine 'I1.png', l'invocazione di 
ricolora('I1.png',[(10,10,(255,0,0),(0,255,0))],’risTest1.png')
produrra' l'immagine 'risTest.png' identica all'immagine di partenza se non per il fatto che,
 tutti i pixel adiacenti al pixel di coordinate (10,10) (e di colore verde), verranno ricolorati 
 di rosso ((255,0,0)) e poi i pixel al bordo dell'area ricolorata saranno ricolorati di blu (0,255,0). 
Per altri  esempi vedere il file grade03.txt 
'''

from immagini import *
    
def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    img=load(fname)
    w=len(img[0])
    h=len(img)
    listaout=[]
    for tupl in lista:
        x,y,c1,c2=tupl
        c=img[y][x]
        da_colorare={(x,y)}
        ricolorati=set()
        area=0
        perimetro=0
        while da_colorare:
            x,y=da_colorare.pop()
            s=0
            for dx,dy in {(-1,0),(0,1),(1,0),(0,-1)}:
                if  (0<=x+dx<w and 0<=y+dy<h) and (img[y+dy][x+dx]==c or (x+dx,y+dy)  in ricolorati):
                    s+=1
                    if img[y+dy][x+dx]==c and (x+dx,y+dy)  not in ricolorati: da_colorare.add((x+dx,y+dy))
            if s==4:
                img[y][x]=c1
                area+=1
            else:
                img[y][x]=c2
                perimetro+=1
            ricolorati.add((x,y))
        listaout+=[(area,perimetro)]
        #print(area,perimetro)
    save(img, fnameout)
    return listaout

def ricolora1(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    img=load(fname)
    w=len(img[0])
    h=len(img)
    listaout=[]
    for tup in lista:
        x,y,c1,c2=tup
        c=img[y][x]
        da_colorare={(x,y)}
        ricolorati=set()
        area=0
        perimetro=0
        while da_colorare:
            x,y=da_colorare.pop()
            vicini=s=0
            for dx,dy in {(-1,0),(0,1),(1,0),(0,-1)}:
                if 0<=x+dx<w and 0<=y+dy<h: 
                    vicini+=1
                    if  img[y+dy][x+dx]!=c and (x+dx,y+dy) not  in ricolorati: 
                        s+=1
            if s==0 and vicini==4:
                img[y][x]=c1
                area+=1
            else:
                img[y][x]=c2
                perimetro+=1
            ricolorati.add((x,y))
            for dx,dy in {(-1,0),(0,1),(1,0),(0,-1)}:
                if 0<=x+dx<w and 0<=y+dy<h and img[y+dy][x+dx]==c and (x+dx,y+dy) not in ricolorati:
                    da_colorare.add((x+dx,y+dy))
        listaout+=[(area,perimetro)]
    save(img, fnameout)
    return listaout

