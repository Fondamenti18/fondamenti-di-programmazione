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
    lm=0
    f=load(filename)
    for i in range(len(f)):
        for e in range(len(f[i])):
            l=0
            lo=0
            ld=0
            if f[i][e]==c:
                lo+=1
                ld+=1
                i2=i
                e2=e
                while e2+1<len(f[0]) and f[i2][e2+1]==c:
                    lo+=1
                    e2+=1
                i2=i
                e2=e
                while e2+1<len(f[0]) and i2+1<len(f) and f[i2+1][e2+1]==c:
                    ld+=1
                    e2+=1
                    i2+=1
                if ld<lo:
                    l=ld
                else:
                    l=lo
                lo=1
                i2=i
                e2=e
                while i2+1<len(f) and f[i2+1][e2]==c:
                    lo+=1
                    i2+=1
                if lo<l:
                    l=lo
                i2=0
                e2=0
                for i2 in range(i,i+l):
                    for e2 in range(e,e+l):
                        if f[i2][e2]!=c:
                            l=0
                            break
                    if l==0:
                        break
            if l>lm:
                lm=l
                y=i
                x=e
    return lm,(x,y)
                    
