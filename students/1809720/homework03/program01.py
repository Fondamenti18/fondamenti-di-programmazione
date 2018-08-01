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
    
    import png
    iris = 0
    kris = 0
    
    immagine = load(filename)
    
    def full(i,k,r,c):
        i = i+1
        k = k+1
        hold = k
        r = r-1
        while(i<r and immagine[i][k]==c):
            k = hold
            while(k<r and immagine[i][k]==c):
                if(immagine[i][k]==c):
                    continue
                else:
                    return False
                k+=1
            i+=1
        return True
    

    def bottom_l(sl,ki,ii,c):
        j = 0
        lunghezza1 = 0
        while(j<sl):
            if (immagine[ii][ki]==c):
                lunghezza1+=1
            j+=1
            ki+=1
        return lunghezza1
    
    def lateral_l(sl,ki,ii,c):
        j = 0
        lunghezza1 = 0
        while(j<sl and immagine[ii][ki]==c):
            lunghezza1+=1
            j+=1
            ii+=1
        return ii,ki,lunghezza1
    
    def upper_l(i,k,c):
        sl = 0
        while(k<len(immagine[i]) and immagine[i][k]==c):
            sl+=1
            k+=1
        return sl,k
    
    def find(c):
        sl_old = 0
        i=0
        iris = 0
        kris = 0
        while(i<len(immagine)):
            k=0
            while(k<len(immagine[i])):
                if(immagine[i][k]==c):
                    ii = i
                    ki = k
                    sl,kf = upper_l(i,k,c)
                    a,b,sinistra = lateral_l(sl,ki,ii,c) #lato sinistro
                    sotto = bottom_l(sl,b,a-1,c)
                    a,b,destra = lateral_l(sl,kf-1,ii,c) #lato destro teoricamente
                    risultato = min(sinistra,sotto,destra,sl)
                    if(risultato>sl_old):
                        buba = full(i,k,risultato,c)
                        if buba:
                            sl_old = risultato
                            iris = i
                            kris = k
                k+=1
            i+=1
        return sl_old,kris,iris
    
    sl_old,kris,iris = find(c)
    
    return sl_old,(kris,iris)

