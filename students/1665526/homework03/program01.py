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
def trasmutaimg(filename,c): #per semplificarmi la vita, tramuto tutto in interi e non in tuple
    a=load(filename)
    for x in a:
        for i in range(len(x)):
            if x[i]==c:
                x[i]=1
            else:
                x[i]=0
    return a
def check(filename,c):
    a=trasmutaimg(filename,c)
    # print(a[60][80])
    for i in range(len(a)):
        if a[i][0] == 1:
            a[i][0]=1
    for i in range(len(a[0])):
        if a[0][i] ==1:
            a[0][i]=1
    for y in range(1,len(a)):
        for x in range(1,len(a[0])):
            if a[y][x]:
                s=[a[y-1][x],a[y][x-1],a[y-1][x-1]]
                s.sort()
                nminimo=s[0]+1
                a[y][x]=nminimo
    return a
def trovo_lato(filename,c):
    b=check(filename,c)
    for y in range(len(b)):
        b[y].sort()
        b[y]=[max(b[y])]#trovo il quad con il lato più grande
        lpg=max(b)[0]
    return lpg

def quadrato(filename,c):
    a=check(filename,c)
    t=trovo_lato(filename,c)
    for y in range(len(a)):
        for x in range(len(a[0])):
            if a[y][x]==t:
                return(t,(x-t+1,y-t+1))
                break

    #return lpg