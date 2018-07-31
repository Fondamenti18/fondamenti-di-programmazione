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
from immagini import load
def inizio(img,c,x,y):
    l=0
    xi = 0 
    yi = 0
    for i in range(x,len(img)-1):
        for o in range(y,len(img[0])-1):
            if img[i][o] == c:
                xi=i
                yi=o
                l=1
                break
            else:
                continue
        if l!=0:
            break
    return xi,yi

def quadrato(filename,c):
    img = load(filename)
    latof = 0
    for x in range(len(img)):
        for y in range(len(img[0])):
            x,y = inizio(img,c,x,y)
            xi = x
            yi = y
            while inside(img,y,x) and img[x][y] == c:
                y += 1
                x += 1                
            xf=x-1
            yf=y-1 
            pieno(xf,yf,xi,yi,x,y,img,c)
            lato = (xf - xi + 1)
            if lato > latof:
                latof = lato
                xfinale = xi
                yfinale = yi
            if yi < len(img[0])-1:
                y = yi + 1
                x = xi
            elif xi < len(img)-1:
                y = 0
                x = xi + 1
            else:
                break
    return latof,(yfinale,xfinale)

def inside(img,x,y):
    return 0<=y<len(img) and 0<=x<len(img[0])
def pieno(xf,yf,xi,yi,x,y,img,c):
    while xf>xi:
        o=0
        for x in range(xi,xf+1):
            for y in range(yi,yf+1):
                if img[x][y]!=c:
                    o=1
                    break
        if o==1:
            xf-=1
            yf-=1
        else:
            break
    return xf,yf
        

        
    
            
    
    
    
                

               
 
                
            
    
            
            
