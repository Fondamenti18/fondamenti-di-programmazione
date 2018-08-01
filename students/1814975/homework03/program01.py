'''
Abbiamo immagini in formato png ottenute inserendo su di uno sfondo monocolore rettangoli 
di vari colori i cui assi sono sempre paralleli agli assi dell'immagine.

Vedi ad esempio l'immagine Img1.png

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una  funzione quadrato(filename, C) che prende in input:
- il percorso di un file (filename) che contiene un immagine in formato png della  tipologia appena descritta.
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


from immagini import *

def quadrato(filename,c):
    Implementare qui la funzione'''
    


from immagini import *

def controlla_in(img,x,y):
    return 0<=x<len(img[0]) and 0<=y<len(img)

def pieno_quad(quad,x,y,lato,c):
    cont=0
    for i in range(y,y+lato):
        for k in range(x,x+lato):
            if controlla_in(quad,k,i) and quad[i][k]==c:
                cont+=1
    return cont==lato*lato

def quadrato(filename,c):
    img=load(filename)
    px=0
    py=0
    xmigliore=0
    ymigliore=0
    diagmigl=0
    for p in range(len(img)):
        for j in range(len(img[0])):
            if img[p][j]==c:
                for diag in range(diagmigl,len(img[0])):
                    if controlla_in(img,j,p)==True and pieno_quad(img,j,p,diag,c)==True:
                        if diag > diagmigl:
                            diagmigl=diag
                            xmigliore=j
                            ymigliore=p
                    else:
                        break
    return(diagmigl,(xmigliore,ymigliore))
    
    
