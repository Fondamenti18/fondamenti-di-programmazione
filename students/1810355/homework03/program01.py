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
    immagine=load(filename)
    coordi=()
    ascissa=0
    ordinata=0
    maxi=0
    larghezza=len(immagine[0])
    altezza=len(immagine)
    n=()
    latoq,coordi,x=crea(immagine,ordinata,c,ascissa)
    ordinata=somma(ordinata)
    while ordinata<len(immagine):
        if ascissa>=len(immagine):
            ascissa=0
        while ascissa<len(immagine):
            ascissa=somma(ascissa)
            latoq,coordi,ascissa=crea(immagine,ordinata,c,ascissa)
            if latoq>maxi :
                maxi=latoq
                n=coordi
            ordinata=somma(ordinata)
    return maxi,n




def crea(i,origine,colore,b):
    latoA=0
    latoB=0
    
    fine=0
    
    co=()
    while dentro(i,b,origine)==True and i[origine][b]!=colore :
        b=somma(b)
    if dentro(i,b,origine)==True and i[origine][b]==colore:
        co=(b,origine)
        while i[origine][b]==colore:
            latoA=somma(latoA)
            b=somma(b)
        b=sottrai(b)
        while i[origine][b]==colore and latoB<latoA:
            latoB=somma(latoB)
            origine=somma(origine)
            if uguaglianza(latoA,latoB) is True :
                fine=latoA
    return fine,co,b
                
def uguaglianza(a,b):
    return a==b            
def somma(b):
    return b+1
def sottrai(b):
    return b-1                
            
                
from immagini import *


def dentro (immagine,x,y):
    
    return 0<=x<len(immagine[0]) and 0<=y<len(immagine)

            
    
                
                
                    
                    
                
                
 
                
                

            
