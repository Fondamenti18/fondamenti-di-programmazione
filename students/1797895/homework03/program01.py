'''
Abbiamo immagini in formato png ottenute inserendo su di uno sfondo monocolore rettangoli 
di vari colori i cui assi sono sempre parallei agli assi dell'immagine.

Vedi ad esempio l'immagine pic1.png

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


def creazioneQ(mappa,yy,colore,xx,latorizz,latovert):
    inizio=yy
    vittoria=0
    maxim=0
    co=()
    while presente(mappa,xx,yy)==True and mappa[yy][xx]!=colore :
        xx=xx+1
    if presente(mappa,xx,yy)==True and mappa[yy][xx]==colore:
        co=(xx,yy)
        while mappa[yy][xx]==colore:
            latorizz+=1
            xx=xx+1
        xx=xx-1
        while mappa[yy][xx]==colore and latovert<latorizz:
            latovert+=1
            yy+=1
            if latorizz==latovert:
                vittoria=latorizz
    return vittoria,co,xx



def presente (pic,x,y):
    altezzaX,larghezzaX=len(pic),len(pic[0])
    return 0<=x<larghezzaX and 0<=y<altezzaX            

def quadrato(filename,c):
    immagine=load(filename)
    latorizz=0
    latovert=0
    coordinate=()
    x=0
    y=0
    maxim=0
    ncoordinate=()
    latomaggiore,coordinate,x=creazioneQ(immagine,y,c,x,latorizz,latovert)
    y=y+1
    while y<len(immagine):
        if x>=len(immagine):
           x=0
        while x<len(immagine):
           x=x+1
           latomaggiore,coordinate,x=creazioneQ(immagine,y,c,x,latorizz,latovert)
           if latomaggiore>maxim:
               maxim=latomaggiore
               ncoordinate=coordinate
        y=y+1
    return maxim,ncoordinate
