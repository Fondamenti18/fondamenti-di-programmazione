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
    altezza=len(img)
    larghezza=len(img[0])
    migliore=(0,larghezza,altezza)
    quadrati={}
    for riga in range(altezza):
        for colonna in range(larghezza):
            if(img[riga][colonna]==c):
                quadratoSx=0
                if(colonna!=0):
                    quadratoSx=quadrati.get((riga,colonna-1),0)
                quadratoSopra=0
                if(riga!=0):
                    quadratoSopra=quadrati.get((riga-1,colonna),0)
                    
                for lato in range(max(max(quadratoSx,quadratoSopra)-1,1), min(larghezza - colonna, altezza - riga)):
                    is_quadrato=scorriQuadrato(img,riga,colonna,lato,c)
                    if(is_quadrato==True):
                        quadrati[(riga,colonna)]=lato
                        if(lato>migliore[0] or (lato==migliore[0] and riga<migliore[2]) or (lato==migliore[0] and riga==migliore[2] and colonna==migliore[1]) ):
                            migliore=(lato,colonna,riga)
                    else:
                        break
    return migliore[0],(migliore[1],migliore[2])


def dimensioni(img,riga,colonna,colore):
    altezza=len(img)
    larghezza=len(img[0])
    latoAltezza=0
    latoLarghezza=0
    old_riga = riga
    while(riga<altezza) and (img[riga][colonna]==colore):
        latoAltezza+=1
        riga=riga+1
        
    while(colonna<larghezza) and (img[old_riga][colonna]==colore):
        latoLarghezza+=1
        colonna=colonna+1

    lato=min(latoAltezza,latoLarghezza)
    return lato
            

def scorriQuadrato(img,riga,colonna,lato,colore):
    #print(riga, colonna, lato)
    for i in range(riga,riga+lato):
        if(img[i][colonna + lato-1]!=colore):
            return False

    for i in range(colonna,colonna + lato):
        if(img[riga + lato-1][i]!=colore):
            return False
        
    return True        
                
            
def lunghezza(img):
    return len(img)

def larghezza(img):
    return len(img[0])
    
