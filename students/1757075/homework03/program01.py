'''
Abbiamo immagini in formato png ottenute inserendo su di uno sfondo monocolore 
    rettangoli di vari colori i cui assi sono sempre parallei agli assi 
    dell'immagine.

Vedi ad esempio l'immagine Img1.png

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo 
    preparato nel modulo immagini.py .

Scrivere una  funzione quadrato(filename, C) che prende in input:
- il percorso di un file (filename) che contine un immagine in formato png 
    della  tipologia appena descritta.
- una tupla C che rappresenta un colore in formato RGB 
    (3 valori interi tra 0 e 255 compresi)

La funzione deve restituire nell'ordine:
- la lunghezza del lato del quadrato pieno di dimensione massima e colore C
     interamente visibile nell'immagine. 
- le coordinate  (x,y)  del pixel dell'immagine che corrisponde alla posizione 
all'interno dell'immagine del punto in alto a sinistra del quadrato. 

In caso ci siano più quadrati di dimensione massima, va considerato quello 
    il cui punto in alto a sinistra occupa la riga minima  
    (e a parita' di riga la colonna minima) all'interno dell' immagine. 

Si può assumere che nell'immagine e' sempre  presente almeno un pixel 
    del colore cercato.

Per gli esempi vedere il file grade01.txt

ATTENZIONE: Il timeout è impostato a 10*N secondi 
    (con N numero di test del grader).
'''

from immagini import *

def quadrato(filename,rgb):# prima 'rgb' era 'c'
    ''' funzione principale '''
    # rappresentazione sotto forma liste di liste di triple
    vet = load(filename)
    ris = (0,(0,0))

    r = 0    # righe
    # per ogni riga
    while r < len(vet):
        c = 0       # colonne
        # per ogni elemnto in riga
        while c < len(vet[0]):
            if vet[r][c] == rgb:
                if possibile(vet, r,c, ris[0], rgb):
                    lung = espandi(vet, 1, [r], c, c+1, rgb)
                    if lung > ris[0]:
                        ris = (lung,(c,r))
            c += 1      # incremento
        r += 1      # incremento
    
    return ris
    
def possibile(vet, y,x, ris, rgb):
    ''' calcola se il quadrato possibile abbia lato maggiore del risultato attuale
    '''
    latoX,latoY = 0,0   # lunghezza lati
    y2 = y              # variabile di comodo per iterare dopo nella riga
    # finche' non esco da vettore e colore e' giusto
    while y < len(vet) and vet[y][x] == rgb:
        y += 1          # incremento contatore
        latoY += 1      # incremetno lunghezza lato
    while x < len(vet[0]) and vet[y2][x] == rgb:
        x += 1
        latoX += 1
    return confronto(latoX,latoY, ris)

def confronto(latoX,latoY, ris):
    ''' Confronto se il lato minore e maggiore del lato attuale '''
    # lato x < lato y
    if latoX < latoY:
        return latoX > ris
    # lato y <= lato x
    return latoY > ris

def espandi(vet, lato, ls, cIniz, c, rgb):
    '''
        intput: vettore, lato(lungezza attuale del quadrato), 
                ls(lista di righe da controllare), c(colonna), 
                cIniz(colonnada cui parto per controllare riga),
                rgb(colore da controllare)
        to do: la funzione calcola se i pixel adiacenti al quadrato sono 
                del colore corretto(procedendo verso destra e in basso)
        return: lunghezza del lato
    '''
    flag = colonna(vet, ls, c, rgb) and riga(vet, ls[-1]+1, cIniz, c, rgb)
    # se c'e' problema
    if flag == False:
        return lato
    ls.append(ls[-1]+1)
    return espandi(vet, lato+1, ls, cIniz, c+1, rgb)
        
    
def colonna(vet, ls, c, rgb):
    ''' 
        metodo che calcola se la colonna accanto al quadrato e' del colore 
        e se non esce da vettore
    '''
    # se esco da matrice
    if c == len(vet[0]):
        return False
    # per ogni riga controllo colonna
    for r in ls:
        if vet[r][c] != rgb:
            return False
    return True
    
def riga(vet, r, cIniz, c, rgb):
    ''' 
        controlla se la riga sotto il quadrato contiene tutti pixel del 
        colore rgb e se non esce da vettore
    '''
    # se esco da matrice
    if r == len(vet):
        return False
    # controllo ogni elemento della riga
    while cIniz <= c:
        if vet[r][cIniz] != rgb:
            return False
        cIniz += 1
    return True

#print(quadrato('Ist1.png',(255,0,0)))