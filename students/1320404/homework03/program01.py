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

ATTENZIONE: Il timeout è impostqato a 10*N secondi (con N numero di test del grader).
'''

from immagini import load
from immagini import save
import immagini
from IPython.display import Image


def quadrato(filename,c):
    f=immagini.load(filename)   #trasforma l'immagine png in lista di liste#
    h = len(f)                  #   altezza  dell'immagine#
    l = len(f[0])                    #   lunghezza dell'immagine #
    ris=[0,(0,0)]
    RIS=[]
    superis=[0,(0,0)]
    riga=0
    xL=0
    yL=0
    
    for x in range(0,h,):
        for y in range(0,l):
            if f[x][y] == c: #and f[x-1][y-1] != c and (f[x][y-1] != c) and (f[x-1][y] != c):
                
                
                baseQ = posQ(f,x,y,h,l,c)[0]
 
                altQ  = posQ(f,x,y,h,l,c)[1]
                
                
                
                if baseQ == altQ:
                    
                    if baseQ == altQ == 1:
                        superis=[baseQ,(y,x)]
                    elif quadratoV(f,x,y,baseQ,altQ,c) == True and ris[0] < baseQ:
                        ris = [baseQ,(y,x)]
                elif baseQ != altQ:
                    if baseQ > altQ:
                        baseQ=altQ
                    elif altQ > baseQ:
                        altQ=baseQ
                    
                    if quadratoV(f,x,y,baseQ,altQ,c) == True and ris[0] < baseQ:
                        ris=[baseQ,(y,x)]         
    RIS=tuple(ris) 
              
    return RIS


            
def quadratoV(f,x,y,baseQ,altQ,c):
    for Xl in range(x,x+altQ):
        for yL in range(y,y+baseQ):
            if f[Xl][yL] == c:
                continue
            else:
                return False
    return True

def posQ(f,x,y,h,l,c):
    baseQ=1
    altQ=1
    for yL in range(y+1,l):
        if (f[x][yL] == c):
            baseQ = baseQ + 1
        else:
            break
    
    for xL in range(x+1,h):
        if (f[xL][y] == c):
            
            altQ = altQ + 1 
        else:
            break
        
    return baseQ,altQ    

def quadratoV2(f,x,y,baseQ,altQ,c):
    baseQ2=0
    altQ2=0
    if baseQ < altQ:
        for i in range(x,x+baseQ):
            if f[i][y]==c:
                altQ2 += 1
        return baseQ,altQ2        
    elif baseQ > altQ:
        for i in range(x,y+altQ):
            if f[x][i] == c:
                baseQ2 += 1
        return baseQ2,altQ        
                
    
            
               
         