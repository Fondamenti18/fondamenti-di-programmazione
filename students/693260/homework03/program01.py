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

img = []

larghezza_img = 0

altezza_img = 0

colorecercato = ()

massimolatoquadratoipotetico = 0

def quadratomonocromatico(startx, starty, lato, colore):
    
    global img
    
    global larghezza_img
    
    global altezza_img
    
    indicecellax = startx + lato - 1
    
    indicecellay = starty + lato - 1
    
    areaquadrato = lato * lato
    
    numeropixeldelcolorecercato = 0
        
    ind_y = starty
    
    while ind_y < altezza_img and ind_y <= indicecellay:
        
        ind_x = startx    
        
        while ind_x < larghezza_img and ind_x <= indicecellax:    
            
            if img[ind_y][ind_x] == colore:
                
                numeropixeldelcolorecercato += 1
                
                #print("Colore uguale. Contatore incrementato a", numeropixeldelcolorecercato, " Cella", ind_x, ind_y)
                
                if numeropixeldelcolorecercato == areaquadrato:
                    
                    return(startx, starty, -1, -1)
    
            else:
                
                 #print("Esco in quanto la cella ha un colore diverso dal cercato. La cella e:", ind_x, ind_y)
                
                return [-1, -1, indicecellax, indicecellay]
            
            
            
            ind_x += 1
         
        ind_y += 1

    return [-1, -1, ind_x, ind_y]
    
def quadrato(filename,c):
    '''Implementare qui la funzione'''
    global img 
    
    img = load(filename)
    
    # Calcolo le misure dell immagine data
    
    global larghezza_img
    
    global altezza_img
    
    larghezza_img = len(img[0])
   
    altezza_img = len(img)
        
    global colorecercato
    
    colorecercato = c

    #Calcolo il massimo lato iniziale dell ipotetico quadrato contenuto nell immagine
    
    if larghezza_img < altezza_img:
        
        massimolatoquadratoipotetico = larghezza_img
        
    else:
        
        massimolatoquadratoipotetico = altezza_img
       
    for latoquadratoipotetico in range(massimolatoquadratoipotetico, 0, -1):
        
        da_l = 0
        
        da_a = 0
        
        l_trovata = -1
        
        a_trovata = -1
        
        l_diversa = 0
        
        a_diversa = 0
        
        while (l_trovata == -1 and a_trovata == -1):
            
            #print("Sto controllando il quadrato di lato", latoquadratoipotetico, " partendo da", da_l, da_a)
            
            l_trovata, a_trovata, l_diversa, a_diversa = quadratomonocromatico(da_l, da_a, latoquadratoipotetico, c)           
            
            if l_trovata != -1 and a_trovata != -1:
                
                return latoquadratoipotetico, (l_trovata, a_trovata)
            
            if da_l + 1 + latoquadratoipotetico > larghezza_img:
                
                da_l = 0
                
                if da_a + 1 + latoquadratoipotetico > altezza_img:
                   
                    break
                    
                else:
                    
                    da_a += 1

                        
            else:
                    
                da_l = da_l + 1
                    
                