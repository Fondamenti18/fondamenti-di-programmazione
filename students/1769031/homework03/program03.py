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
import png 

def load(filename):
    with open(filename,mode='rb') as f:
        r=png.Reader(file=f)
        iw,ih,png_img,_=r.asRGB8()
        img=[]
        for png_row in png_img:
            row=[]
            for i in range(0,len(png_row),3):
                row.append((png_row[i+0],
                            png_row[i+1],
                            png_row[i+2]))
            img.append(row)
    return img,iw,ih

def create(iw,ih):
    matrix=[]
    for _ in range(ih+1):
        row=[]
        for _ in range(iw+1):
            row.append(0)
        matrix.append(row)
    return matrix

def save(filename,img):
    pngimg=png.from_array(img,'RGB')
    pngimg.save(filename)

def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    img,iw,ih=load(fname)
    listav=[]
    for h in lista:
        Area=0
        Perimetro=0
        x,y,c1,c2=h
        matrix=create(iw,ih)
        c=img[x][y]
        for i in range(len(img)):
            for j in range(len(img[0])):
                if img[i][j]==c:
                    matrix[i][j]=1
                if img[i][j]!=c:
                    matrix[i][j]=0
        matrix[x][y]+=1
        Yessa=matrix[x][y]
        Found=True
        while Found:
            allah=Yessa
            Yes=False
            for i in range(len(img)):
                for j in range(len(img[0])):
                    control=[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
                    if matrix[i][j]==allah:
                        for (k,l) in control:
                            if matrix[k][l]==1:
                                matrix[k][l]+=allah
                                Yes=True
                                Yessa=matrix[k][l]
                    if i==len(img)-1 and j==len(img[0])-1 and matrix[i][j]!=allah and Yes==False:
                        Found=False
            if Yes==True:
                allah=Yessa
        for i in range(len(img)):
            for j in range(len(img[0])):
                if matrix[i][j]==1:
                    matrix[i][j]=0
        for i in range(len(img)):
            for j in range(len(img[0])):
                if matrix[i][j]>1:
                    control=[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
                    for (k,l) in control:
                        if matrix[k][l]==0:
                            matrix[i][j]=1
        for i in range(len(img)):
            for j in range(len(img[0])):
                if matrix[i][j]>1:
                    Area+=1
                    img[j][i]=c1
                if matrix[i][j]==1:
                    Perimetro+=1
                    img[j][i]=c2
        listav.append((Area,Perimetro))
    save(fnameout,img)
    return listav