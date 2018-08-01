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

def inside (img,i,j):
    iw,ih=len(img[0]),len(img)
    return 0<=i<iw and 0<=j<ih



def creaquad(pic,a,colore,b):
    lato1=0
    lato2=0
    origine=a
    vittoria=0
    massimo=0
    co=()
    while inside(pic,b,a)==True and pic[a][b]!=colore :
        b=b+1
    if inside(pic,b,a)==True and pic[a][b]==colore:
        co=(b,a)
        while pic[a][b]==colore:
            lato1+=1
            b=b+1
        b=b-1
        while pic[a][b]==colore and lato2<lato1:
            lato2+=1
            a+=1
            if lato1==lato2:
                vittoria=lato1
    return vittoria,co,b
                
            
                
                
                
from immagini import *
def quadrato(filename,c):
    immagine=load(filename)
    coordinate=()
    x=0
    y=0
    massimo=0
    nuovecoord=()
    latoquad,coordinate,x=creaquad(immagine,y,c,x)
    y=y+1
    while y<len(immagine):
        if x>=len(immagine):
            x=0
        while x<len(immagine):
            x=x+1
            latoquad,coordinate,x=creaquad(immagine,y,c,x)
            if latoquad>massimo:
                massimo=latoquad
                nuovecoord=coordinate
            y=y+1
    return massimo,nuovecoord
            
    
                
                
                    
                    
                
                
 
                
                

            
