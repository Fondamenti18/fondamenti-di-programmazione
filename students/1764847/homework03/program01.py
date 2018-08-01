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

import immagini

def quadrato(filename,c):
    '''Prende in input il percoso file di una immaginee una tupla che rappresenta
    un colore, restituisce la dimensione del quadrato pieno più grande
    e la posizione (x,y) che corrisponde a dove inizia il quadrato'''
    immagine = immagini.load(filename)                  #lista di liste che contiene l'immagine
    h = len(immagine)
    l = len(immagine[0])
    mask = []
    for i in range(h):
        row = []
        for j in range(l):
            row+=[1]
        mask+=[row]
    a = 0
    d = {}                                              #dizionario vuoto
    for i in range(h):                                  #per ogni riga
        for j in range(l):                              #per ogni colonna
            if immagine[i][j] == c and mask[i][j] == 1: #se il pixel (i,j) == colore e il pixel non è stato mascherato 
                a = quad(immagine,j,i,c,l,h,mask)       #chiama la funzione quad e metti il risultato in a
                if not a in d:                          #se a non è nel dizionario
                    d[a] = j,i                          #assegno alla chiave a i valori j,i
    massimo = max(d)                                    #calcolo la chiave massima del dizionario (quadrato piu grande)
    return massimo, d[massimo]                          #restituisco la lunghezza del lato e le coordinate associate all chiave



def quad(lst,x,y,c,l,h,mask):
    i = y
    j = x
    count = 1 # assumo il punto x,y del colore c
    x_limit = x
    y_limit = y

    while True: # provo ad allargare il quadrato di 1 pixel la volta a destra e in basso

        i += 1
        j += 1
        while_break = 0
        
        # controllo di non aver superato l'altezza
        if i >= h:
            x_limit = j
            y_limit = i
            break
            
        # controllo di non aver superato la larghezza  
        if j >= l:
            x_limit = j
            y_limit = i
            break
        
        # controllo il punto i,j (sulla diagonale)
        if lst[i][j] != c:
            x_limit = j
            y_limit = i
            break
        
        # controllo la riga i-esima
        yy = i
        for xx in range (x, j):
            if lst[yy][xx] != c:
                x_limit = xx+1
                y_limit = i+1
                while_break = 1
                break
        
        if while_break == 1:
            break
        
        # controllo la colonna j-esima
        xx = j
        for yy in range (y, i):
            if lst[yy][xx] != c:
                x_limit = j+1
                y_limit = yy+1
                while_break = 1
                break
        
        if while_break == 1:
            break
        
        count += 1
    
    # maschero i pixel che non possono avere quadrati più grandi
    for xx in range (x, x_limit):
        for yy in range (y, y_limit):
            mask[yy][xx] = 0
    
    return count
