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
    img=load(filename)
    p,t=[0,0],[0,0]
    o,b,k,j=0,0,0,0
    h,w=len(img),len(img[0])
    for y in range(h):
        for x in range(w):
            if img[y][x]==c:
                k+=1
                p[0],p[1]=x,y
                if 0 <= (p[1]+k) < h and 0 <= (p[0]-k) < w:
                    for z in range(k):
                        if img[p[1]+z][p[0]]==c and img[p[1]+z][p[0]-z]==c:
                            o+=1
                        else:
                            k-=1
                            pass
                    if k>b and k==o:
                        for y1 in range(k):
                            for x1 in range(k):
                                if img[p[1]+y1][p[0]-x1]==c:
                                    j+=1
                                else:
                                    break
                        if j==(k*k):
                            b=k
                            t[0]=p[0]-k+1
                            t[1]=p[1]
                    o,j=0,0
                else:
                    k-=1
            else:
                k=0
        k=0
    return(b,(t[0],t[1]))