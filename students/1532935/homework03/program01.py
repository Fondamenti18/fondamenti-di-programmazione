'''
Abbiamo immagini in formato png ottenute inserendo su di uno sfondo monocolore rettangoli 
di vari colori i cui assi sono sempre parallei agli assi dell'immagine.

Vedi ad esempio l'immagine Img1.png

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una  funzione quadrato(filename, C) che prende in input:
- il percorso di un file (filename) che contine un immagine in formato png della  tipologia appena descritta.
- una tupla C che rappresenta un colore in formato RGB (3 valori interi tra 0 e 255 compresi)

La funzione deve restituire nell'ordine:
- la lunghezza del lato del quadrato pieno di dimensione massima e colore C interamente visibile nell'immagine. 
- le coordinate  (x,y)  del pixel dell'immagine che corrisponde alla posizione 
all'interno dell'immagine del punto in alto a sinistra del quadrato. 

In caso ci siano più quadrati di dimensione massima, va considerato quello il cui punto 
in alto a sinistra occupa la riga minima  (e a parita' di riga la colonna minima) all'interno dell' immagine. 

Si può assumere che nell'immagine e' sempre  presente almeno un pixel del colore cercato.

Per gli esempi vedere il file grade01.txt

ATTENZIONE: Il timeout è impostato a 10*N secondi (con N numero di test del grader).
'''
from immagini import *

def my_crop(startx,endx,statry,endy,im):
    n=endx-startx+1
    m=endy-statry+1
    impart=[  0 for i in range(0,n*m) ] 
    k=0
    for i in range(startx,endx+1):
        for j in range(statry,endy+1):
            impart[k]=im[i][j]
            k+=1
    return impart


    return im
import immagini
def check_color(row,col,i,j,im,colorin):
    Step=0
    state=True
    while(state & (i+Step<row)&(j+Step<col)):
        partsel=my_crop(i,i+Step,j,j+Step,im)
        if(all(colorin == a for a in partsel)):
            Step+=1
        else:
            state=False;
    return i ,j,Step

def quadrato(filename,c):
    maxresult=0
    indexrow=0
    indexcol=0
    im=immagini.load(filename)
    row=len(im)
    col=len(im[0])
    #print(str(row) +' '+str(col))
    for i in range(row):
        print(str(i))
        for j in range(col):
            if(im[i][j]==c):
                m,n,step= check_color(row,col,i,j,im,c)
                if(step>maxresult):
                    maxresult=step
                    indexrow=n
                    indexcol=m
                
    return (maxresult,(indexrow, indexcol))


















    
