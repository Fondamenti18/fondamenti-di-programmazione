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
import numpy as np
from scipy.ndimage.measurements import label
import copy
rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)
def ricolora(fname,lista,output):
    listone = []
    immagine=load(fname)
    altezza=len(immagine)
    larghezza=len(immagine[0])
    matrice_temporanea=[]
    for x,y,c,c2 in lista:
        px=immagine[y][x]
        matrice_temporanea,pixd=connessioni(c,immagine,px,altezza,larghezza,y,x)
        immagine,a,p=calcola(matrice_temporanea,immagine,pixd,c,c2)
        listone.append((a,p))
    save(immagine,output)
    return listone
        
        
def connessioni(c,immagine,px,altezza,larghezza,y,x):
    matrice_temporanea=copy.deepcopy(immagine)
    for i in range(altezza):
        for j in range(larghezza):
            if immagine[i][j]==px:
                matrice_temporanea[i][j]=1
            else:
                matrice_temporanea[i][j]=0
    matrice_temporanea=np.array(matrice_temporanea)
    labeled_array, num_features = label(matrice_temporanea)
    matrice_temporanea=(labeled_array.tolist())
    pixd=matrice_temporanea[y][x]
    return matrice_temporanea,pixd
 
def calcola(img,immagine,pixd,c,c2):
    bordo = 0
    interno = 0
    for i in range(len(img)):
        for j in range(len(img[0])):
            if img[i][j] == pixd:
                if limiti(i,j,c2,img) == True :
                    immagine[i][j] = c2
                    bordo = bordo + 1
                elif contorno(i,j,c2,img,pixd) == True:
                    immagine[i][j] = c2
                    bordo = bordo + 1
                else :
                    immagine[i][j] = c
                    interno = interno + 1
    return immagine , interno , bordo
def contorno(i,j,c2,img,pixd):
    a = img[i][j+1]
    b = img[i][j-1]
    c = img[i+1][j]
    d = img[i-1][j]
    if a != pixd or b != pixd or c != pixd or d != pixd  :
        return True
    else :
        return False
def limiti(i,j,c2,img):
    a = j+1
    b = j-1
    c = i+1
    d = i-1
    if d < 0 or b < 0 or a >= len(img[0]) or c >= len(img) :
        return True
    else:
        return False


    

    

    


