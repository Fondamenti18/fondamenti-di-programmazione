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
    immagine1=load(filename)
    immagine=load(filename)
    lato1=0
    coordinate=tuple()
    for riga in range(len(immagine)):
        for pixel in range(len(immagine[riga])):
            lato=0
            while immagine[riga+lato][pixel]==c and immagine[riga][pixel+lato]==c and immagine[riga+lato][pixel+lato]==c :
                    #print(riga+lato,pixel+lato)
                    #print(riga,pixel)
                    lato+=1
                    if quadratoContenuto(immagine,pixel,riga,lato,lato,c)==True:
                        if lato>lato1:
                            lato1=lato
                            coordinate=(pixel,riga)
    return (lato1,coordinate)
                

def contenuto(img,i,j):
    #ritorna true se il pixel(i,j) è dentro l'immagine img, false altrimenti
    iw, ih = righe(img), colonne(img)
    return 0 <= i <= iw and 0 <= j <= ih
def righe(img): return len(img)
def colonne(img): return len(img[0])
def quadratoContenuto(img, x, y, larghezza, altezza, colore):
    for riga in range(y,y+altezza):
        for colonna in range(x,x+larghezza):
            #cambio il colore dei pixel con il colore dato
            if contenuto(img,riga,colonna):
                if img[riga][colonna]!=colore :
                    return False
    else:
        return True

                        
                        
                