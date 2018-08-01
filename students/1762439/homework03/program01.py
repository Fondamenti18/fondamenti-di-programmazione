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

#def quadrato(filename,c):
 #   '''Implementare qui la funzione'''
def contr(img, y,yf, x, xf, c):
    quad = True
    try:
        for a in range(y, yf):
            for b in range(x, xf):
                if img[a][b]  != c:
                    quad = False
                    break
    except IndexError:
        quad = False        
    return quad            
#print(contr('Ist1.png',40,43,1,3 , (255,0,0)))                  
                
#save(prova,'Ist4.png' )
#Image.open('Ist4.png').show()    
def quadrato(filename, c):
    img = load(filename)
    lista1 = []
    lato = 0
    coppia = ()
    w, h = len(img[0]),len(img)
#    for y in reversed(range(h)):
#        for x in range(w):
#            if img[y][x] == c:
#                lista1 += [(y,x)]
    for y in range(h):
        for x in range(w):
            if img[y][x] == c:
                lista1 += [(y,x)]
    for y,x in lista1:
        if y + lato <= h and x + lato <= w:
            #for lato in range(w):#for k in range(lato+1 ):
                try:
                    if all(img[y+k][x] == c for k in range(lato+1)) and all(img[y][x+k] == c for k in range(lato+1)):
                    
                
                        while contr(img, y, y+lato, x, x+lato, c):
                            lato += 1
                            coppia = (x,y)
                        #img[y][x] = (0,0,255)
                except IndexError:
                    pass
    return (lato-1, coppia)
