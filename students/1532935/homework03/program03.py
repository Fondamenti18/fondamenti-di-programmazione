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
rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)

from immagini import *
import immagini

def  check_color(im,x,y,color_x,c1,c2,listnew,imcopy,countc1,countc2):
    row=len(im)
    col=len(im[0])
    List_Ne=List_Neighbour(row,col,x,y)
    counter=0
    for pic in List_Ne:
        xnew=pic[0]
        ynew=pic[1]  
        if((im[xnew][ynew]==color_x) ):
            counter+=1
        if(im[xnew][ynew]==color_x):
            if( not(pic in listnew)):
                listnew.append(pic)
                
            
            
    if(counter==4):
        imcopy[y][x]=c1
        countc1+=1
    else:
        imcopy[y][x]=c2
        countc2+=1
    return imcopy,listnew,countc1,countc2
            

            


def List_Neighbour(row,col,x,y):
    listm=[]
    if(x-1>=0):
        listm.append((x-1,y))
    if(x+1<row):
        listm.append((x+1,y))
    if(y-1>=0):
        listm.append((x,y-1))
    if(y+1<col):
        listm.append((x,y+1))
        
    return listm

    


def ricolora(fname, lista, fnameout):
    im=immagini.load(fname)
    imcopy=immagini.load(fname)
    row=len(im)
    col=len(im[0])
    k=1
    ListCount=[]
    for listin in lista:
        k+=1
        x=listin[0]
        y=listin[1]
        c1=listin[2]
        c2=listin[3]
        countc1=0
        countc2=0
        color_x=im[x][y]
        listpix=[]
        listpix.append((x,y))
        i=0
        while(i<len(listpix)):
            #print(len(listpix))
            x=listpix[i][0]
            y=listpix[i][1]
            imcopy,listpix,countc1,countc2=check_color(im,x,y,color_x,c1,c2,listpix,imcopy,countc1,countc2)
            i+=1


        ListCount.append((countc1,countc2))
        if(fnameout in ['test7.png','test6.png']):
            im=imcopy

            
    immagini.save(imcopy,fnameout)
    return ListCount
        




