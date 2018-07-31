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
    '''Implementare qui la funzione'''
    img=load(filename)
    ins=set()
    i=0
    l=0
    x=0
    y=0
    while i<len(img):
        j=0
        while j<len(img[i]):
            p=0
            if img[i][j]==c and not (i,j) in ins:
                e=j
                while img[i][e]==c:
                    p+=1
                    e+=1
                    if e==len(img[i]):
                        break
                k=i+1
                h=p
                while k<i+p-1:
                    u=j
                    p=0
                    while u<len(img[k]) and u<j+h:
                        if img[k][u]==c:
                            p+=1
                        u+=1
                    k+=1
                    h=p
                for g in range(i,i+p):
                    for f in range(j,j+p):
                        if i+p+1<len(img) and j+p+1<len(img[i]):
                            if img[g][j+p+1]!=c and img[i+p+1][f]!=c:
                                ins.add((g,f))
            if p>l:
                l=p
                x=i
                y=j
            j+=1
        i+=1
    return l,(y,x)                 
            
                