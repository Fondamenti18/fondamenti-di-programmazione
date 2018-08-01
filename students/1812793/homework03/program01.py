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

def quadrato(filename,c):
    y=0
    mas=0
    img=load(filename)
    for riga in img:
        if len(img)-y>mas:
            x=0
            for pixel in riga:
                if pixel==c and len(img[0])-x>mas:
                    a=calcola(img,x,y,c)
                    if a>mas:
                        mas=a
                        co=(x,y)
    
                x+=1
        y+=1
    return mas,co
            
def calcola(img,x,y,c):
    cont=0
    a=x
    b=y
    colonne=len(img[b])
    righe=len(img)
    while img[b][a]==c and a<colonne-1 and b<righe-1 and controlla(img,x,y,cont,c):
        cont+=1
        a+=1
        b+=1
    return cont

def controlla(img,x,y,cont,c):
    r=True
    for i in range(y+cont,y-1,-1):
        if img[i][x+cont]!=c:
            r=False
            break
    for j in range(x+cont,x-1,-1):
        if img[y+cont][j]!=c:
            r=False
            break
    return r
    
               
                
#print(quadrato("Ist3.png",(255,0,0)))
