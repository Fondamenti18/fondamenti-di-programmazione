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
from png import *
from immagini import *

def pastelli(picture,longitudine,latitudine):
    for i in range(latitudine, latitudine+1):
        for c in range(longitudine-1, longitudine):
            picture[i][c]=(255,255,255)
    return picture 


def veloce(a, c):
    tempoy=[]
    lati=[]
    coordinate=[]
    for x in range(len(a)):
            for y in range(len(a[0])):
                if a[x][y]==c:
                    d=x
                    q=y
                    while a[d][q]==c: 
                      b=y
                      while a[d][b]==c: 
                              if a[d][b+1] != c:
                         #aggiunge la y in una lista temporanea per controllare che sia un quadrato
                                    tempoy.append(b-(y-1))
                                    
                                    if a[d+1][b] != c:
                                      lunghezza=d-(x-1)                          
                                 #controlla che sia un quadrato
                                      if tempoy.count(tempoy[0])==len(tempoy) and lunghezza==tempoy[len(tempoy)-1]: 
                                          lati.append(lunghezza)
                                          le=[y,x]
                                          #if a[x-1][y] != c and a[x][y-1] !=c and a[x][y]==c :
                                          coordinate+=([le])
                                          
                                         #le coordinate sono sbagliate
                                      else:
                                          del tempoy[:]
                              b+=1            
                      d+=1        
    dizionario=dict(zip(lati, coordinate))
    
         
         
    return dizionario




'''

def sbirulina(a, x, y, c):
    lunghezza=1
    while x+lunghezza <len(a)-1 and y+lunghezza <len(a[0])-1:
        for dio in range( lunghezza):
            if a[x+dio][y+lunghezza] != c or a[x+lunghezza][y+dio] !=c:
               return lunghezza
        lunghezza+=1
    return lunghezza
'''
def quadrato(filename, c):
     a=load(filename) 
     dizionario=veloce(a, c)
     d=max(dizionario)
     
    # print(d)
     f1=dizionario[d][0]
     f2=dizionario[d][1]
     #a=pastelli(a,f2,f1)
     #save(a,gts1)
     return (d, (f1, f2))
     #pene=0
     #scorrono tutta l'immagine
     




                            
                
        