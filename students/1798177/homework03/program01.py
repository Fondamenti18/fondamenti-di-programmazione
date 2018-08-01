# Abbiamo immagini in formato png ottenute inserendo su di uno sfondo monocolore
# rettangoli di vari colori i cui assi sono sempre parallelli agli assi
# dell'immagine.
# Vedi ad esempio l'immagine Img1.png.
#
# Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo
# preparato nel modulo immagini.py.
#
# Scrivere una funzione quadrato(filename, C) che prende in input:
# - il percorso di un file (filename) che contiene un immagine in formato png
#   della tipologia appena descritta.
# - una tupla C che rappresenta un colore in formato RGB (3 valori interi tra 0
#   e 255 compresi)
#
# La funzione deve restituire nell'ordine:
# - la lunghezza del lato del quadrato pieno di dimensione massima e colore C
#   interamente visibile nell'immagine.
# - le coordinate (x,y) del pixel dell'immagine che corrisponde alla posizione
#   all'interno dell'immagine del punto in alto a sinistra del quadrato.
#
# In caso ci siano più quadrati di dimensione massima, va considerato quello il
# cui punto in alto a sinistra occupa la riga minima (e a parità di riga la
# colonna minima) all'interno dell'immagine.
#
# Si può assumere che nell'immagine è sempre presente almeno un pixel del
# colore cercato.
#
# Per gli esempi vedere il file grade01.txt
#
# ATTENZIONE: Il timeout è impostato a 10*N secondi (con N numero di test del
# grader).
#
# Svolto da Emanuele Petriglia.

from immagini import load, save

ROW = 0
COLUMN = 1

def get_square(cache):
    '''Ritorna il lato e il punto iniziale del quadrato più grande presente in
    'cache'.
    '''
    max_side = cache[0][0]
    max_row = max_column = 0

    # Quando trova il numero maggiore in assoluto allora quello è il punto
    # finale del quadrato massimale.
    for row in range(0, len(cache)):
        for column in range(0, len(cache[0])):
            if max_side < cache[row][column]:
                max_side = cache[row][column]
                max_row = row
                max_column = column

    # Non è possibile usare l'operatore -= perchè altrimenti Python effettua
    # prima la somma con +1.
    max_row = max_row - max_side + 1
    max_column = max_column - max_side + 1

    # La richiesta dell'esercizio usa un sistema di coordinate inverso rispetto
    # alla rappresentazione nel codice (le colonne e le righe sono invertite).
    return max_side, (max_column, max_row)

def fill_default(cache, img, color):
    '''Imposta la prima riga e colonna della cache 'cache' con i valori
    corrispettivi dell'immagine 'img' (1 se 'color' è uguale altrimenti 0).
    '''
    for row in range(0, len(img)):
        # In Python il valore 'True' può essere interpretato come 1 numerico,
        # il 'False' come 0 numerico.
        cache[row][0] = img[row][0] == color

    for column in range(0, len(img[0])):
        cache[0][column] = img[0][column] == color

    return cache

def get_init_cache(img, color):
    '''Inizializza la cache, ossia una matrice di ugual grandezza a 'img' con
    valori di default a 0, tranne per la prima riga e colonna. Queste ultime due
    linee vengono già calcolate con il colore 'color'.
    '''
    cache = []

    for row in range(0, len(img)):
        line = []
        for column in range(0, len(img[0])):
            line.append(0)
        cache.append(line)

    return fill_default(cache, img, color)

def get_max_square(img, color):
    '''Ritorna il quadrato di colore 'color' trovato nell'immagine 'img';
    prima ritorna la grandezza del lato, poi il punto.
    '''
    # L'algoritmo prevede una 'cache' di supporto, ossia una tabella contente
    # numeri, che indicano quanti quadrati terminano in ogni punto. Per
    # trovare il quadrato maggiore di cerca poi il punto maggiore nella cache,
    # e da lì si può calcolare il punto di origine.
    cache = get_init_cache(img, color)

    for row in range(1, len(img)):
        for column in range(1, len(img[0])):
            if img[row][column] == color:
                cache[row][column] = min(cache[row][column - 1], \
                                         cache[row - 1][column], \
                                         cache[row - 1][column - 1]) + 1
            else:
                cache[row][column] = 0

    return get_square(cache)

def quadrato(filename, c):
    return get_max_square(load(filename), c)
