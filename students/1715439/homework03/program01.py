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
    img=load(filename)
    h=len(img)
    w=len(img[0])
    print(h)
    print(w)
    diz={}
    for y in range(h):
        
        for x in range(w):
        
            if img[y][x]==c: 
            
                diz[1]=(x,y)
             
                n=1
                if x+n in range(w) and y+n in range(h):
                    while not is_quadrato_c(img,x+n,y+n,c,n):
                        n+=1
                    else:
                        lato=n
                        P=(x,y)
                    
                        if not lato in diz.keys():
                            diz[lato]=P
                            #print(diz)
    return max(diz.keys()), diz[max(diz.keys())]



def is_quadrato_c(immagine,X,Y,c,n):
    ris=[]
  
    if Y in range(len(immagine)) and X in range (len(immagine[0])):
        for j in range (Y-n,Y):
            if immagine[j][X]==c:
                ris+='1'
            else:
                ris+='0'
     
    
        for i in range (X-n,X+1):
    
            if immagine[Y][i]==c:
                ris+='1'
            else:
                ris+='0' 
    else: 
        ris+='0'
    return '0' in ris
#ritorna true se il quadrato costruito dal vertice in basso a destra di lato n NON è tutto del colore chiesto
                
            

