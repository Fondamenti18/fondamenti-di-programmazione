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

"""a=load("I1.png")
a=trova_connessioni((0,255,0),1,len(a),len(a[0]),a)
a=numpy.array(a)
connessioni=measure.label(a,connectivity=1)
per trovare pixel cercato faccio connessioni[y][x]
ed e equivalente alla matrice
"""
rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)

from immagini import *
import numpy
import copy
from scipy.ndimage.measurements import label
    
def ricolora(fname,lista, fnameout):
    matrice=load(fname)
    altezza=len(matrice)
    larghezza=len(matrice[0])
    output=[]
    for x,y,c1,c2 in lista:
        colore_da_cambiare=matrice[y][x]
        connessioni=trova_connessioni(colore_da_cambiare,altezza,larghezza,matrice)
        coordinata_punto=connessioni[y][x]
        matrice,area,perimetro=colorazione(connessioni,coordinata_punto,matrice,altezza,larghezza,c2,c1)
        output.append((area,perimetro))
    save(matrice,fnameout)
    return output

def trova_connessioni(colore_da_cambiare,altezza,larghezza,matrice):
    connessioni=copy.deepcopy(matrice)
    for j in range(altezza):
        for i in range(larghezza):
            if connessioni[j][i]==colore_da_cambiare:
                connessioni[j][i]=1
            else:
                connessioni[j][i]= 0
    connessioni=numpy.array(connessioni)
    labeled_array, num_features = label(connessioni)
    connessioni=(labeled_array.tolist())
    return connessioni

def colorazione(connessioni,coordinata_punto,matrice,altezza,larghezza,c1,c2):
    area=0
    perimetro=0
    for j in range(altezza):
        for i in range(larghezza):
            if connessioni[j][i]==coordinata_punto:
                matrice,areat,perimetrot=bordo(connessioni,coordinata_punto,j,i,altezza,larghezza,matrice,c2,c1)
                area+=areat
                perimetro+=perimetrot
    return matrice,area,perimetro

def bordo(connessioni,coordinata_punto,j,i,altezza,larghezza,matrice,c2,c1):
    destra=i+1
    sinistra=i-1
    basso=j+1
    alto=j-1
    perimetro=0
    area=0
    if destra<=larghezza-1 and sinistra>=0 and basso<=altezza-1 and alto>=0:
        if connessioni[j][destra]!=coordinata_punto or connessioni[j][sinistra]!=coordinata_punto or connessioni[basso][i]!=coordinata_punto or connessioni[alto][i]!=coordinata_punto:
            matrice[j][i]=c1
            perimetro+=1
            return matrice,area,perimetro
        else:
            matrice[j][i]=c2
            area+=1
            return matrice,area,perimetro
    else:
        matrice[j][i]=c1
        perimetro+=1
        return matrice,area,perimetro
