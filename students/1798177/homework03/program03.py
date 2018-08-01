# Definiamo adiacenti di un pixel p di un immagine i pixel adiacenti a p in
# orizzontale o in verticale. Se un pixel è sul bordo dell'immagine il suo
# vicinato non comprende i pixel non contenuti nell'immagine. Il pixel
# dell'immagine con coordinate(x,y) ha dunque come adiacenti i pixel con
# coordinate (x-1,y), (x+1,y), (x,y-1), (x,y+1) appartenenti all'immagine.
#
# Definiamo connessi due pixel se è possibile dall'uno raggiungere l'altro
# spostandosi solo su pixel adiacenti e dello stesso colore (ovviamente perchè
# ciò sia possibile è necessario che i due pixel abbiano lo stesso colore).
#
# Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo
# preparato nel modulo immagini.py.
#
# Scrivere una funzione ricolora(fname, lista,  fnameout) che presi:
#   - il percorso di un file che contiene un'immagine in formato PNG;
#   - una lista di quadruple del tipo (x,y,c1,c2) dove x e y sono coordinate di
#     un pixel dell'immagine e c1 e c2 due triple colore RGB;
#   - il percorso di un file (fnameout) da creare.
# legge l'immagine in fname, esegue un'operazione di ricolorazione di alcuni
# pixel dell'immagine e registra l'immagine ricolorata nel file fnameout.
#
# L'operazione di ricolorazione è la seguente. Per ciascuna delle quadruple
# (x,y,c1,c2) della lista (nell'ordine):
#   - tutti i pixel connessi al pixel di coordinate (x,y) nell'immagine vanno
#     ricolorati col colore c1;
#   - tutti i pixel del perimetro (che si trovano sul 'bordo') della zona che si
#     è appena colorata devono essere ricolorati col colore c2.
# Il perimetro della zona colorata è l'insieme dei pixel che non hanno tutti e 4
# i vicini che fanno parte della zona ricolorata (ovvero almeno uno è di un
# colore diverso da quello che si sta ricolorando oppure almeno uno non esiste
# perchè sarebbe fuori dall'immagine).
#
# Si consideri ad esempio l'immagine 'I1.png', l'invocazione di
# ricolora('I1.png',[(10,10,(255,0,0), (0,0,255))],’OUT1.png') produrrà
# l'immagine 'OUT1.png' identica all'immagine di partenza se non per il fatto
# che, tutti i pixel adiacenti al pixel di coordinate (10,10) (e di colore
# verde), verranno ricolorati di rosso (255,0,0), mentre i pixel sul bordo della
# zona inizialmente verde vengono ricolorati di blu.
#
# Per ciascuna area ricolorata bisogna inoltre calcolare area interna e
# perimetro, che sono definite come segue:
#   - l'area interna è il numero di pixel ricolorati con il colore c1;
#   - il perimetro è il numero di pixel ricolorati con il colore c2;
#
# La funzone deve tornare la lista di coppie (area interna, perimetro) nello
# stesso ordine in cui sono state colorate le aree.
#
# Per altri  esempi vedere il file grade03.txt.
#
# Svolto da Emanuele Petriglia.

from immagini import load, save

from collections import deque

ROW = 0
COLUMN = 1

def paint_region(img, pixels, color):
    '''Colora i pixel contenuti in 'pixels' con il colore 'color' sulla
    immagine 'img'. Ritorna il numero di pixel colorati.
    '''
    counter = 0

    for row, column in pixels:
        img[row][column] = color
        counter += 1

    return counter

def stop_scan_line(img, row, column, color, flag):
    '''Restituisce il valore False se il pixel considerato non è uguale al
    colore 'color', altrimenti restituisce il valore di 'flag'.
    '''
    if flag and img[row][column] != color:
        return False

    return flag

def scan_pixel(img, point, color, points, pixels, flag, step):
    '''Scansione un singolo pixel, ritornando il valore aggiornato di 'flag'.
    Il pixel è identificato da 'point', il pixel controllato è quello
    superiore (step = -1) o inferiore (step = -1) ed aggiunge il pixel in
    'points' se è l'inizio di una nuova riga.
    '''
    row = point[ROW] + step
    column = point[COLUMN]

    if not flag and img[row][column] == color and \
       (row, column) not in pixels:
       points.append((row, column))
       return True

    return stop_scan_line(img, row, column, color, flag)

def scan_lines(img, row, interval, color, points, pixels):
    '''Scansiona la parte superiore ed inferiore della linea, aggiungento a
    'points' i punti iniziali di nuove linee da controllare, stando però attenti
    che non siano già presenti in 'pixels'.
    Per scansionare la linea si prendere l'immagine, la riga 'row' e
    l'intervallo 'interval', ossia la colonna di partenza e di arrivo.
    '''
    above = under = False

    column, stop_column = interval
    stop_column += 1

    last_column = len(img) - 1

    for column in range(column, stop_column): # Scorre la linea.
        point = (row, column)

        if row > 0: # Controlla il pixel superiore.
            above = scan_pixel(img, point, color, points, pixels, above, -1)

        if row < last_column: # Controlla il pixel inferiore.
            under = scan_pixel(img, point, color, points, pixels, under, +1)

        # Il punto in questio viene comunque aggiunto nei pixel da colorare.
        pixels.add(point)

def get_half_border(img, point, color, exact, step):
    '''Restituisce il punto 'point' se nel punto superiore od inferiore
    (indicato da 'step') il colore è diverso da 'color', oppure se il punto si
    trova nella riga 'exact'.
    Restituisce in caso negativo la stringa '1'.
    '''
    row, column = point

    if row == exact or img[row + step][column] != color:
        return point

    return "1"

def get_border(img, row, interval, color, border_pixels):
    '''Aggiunge a 'border_pixels' i punti della riga 'row' con intervallo
    'interval' (ossia la colonna di partenza e finale) di colore 'color'
    considerati come bordo.
    '''
    start_column, stop_column = interval

    last_column = len(img) - 1

    for column in range(start_column + 1, stop_column):
        point = (row, column)

        border_pixels.add(get_half_border(img, point, color, 0, -1))
        border_pixels.add(get_half_border(img, point, color, last_column, +1))

def get_column(img, point, color, step):
    '''Ritorna la colonna iniziale o finale (-1 o +1 per step) di una linea con
    pixel di stesso colore.
    '''
    row, column = point

    while 0 <= column < len(img[0]) and img[row][column] == color:
        column += step

    return column - step

def fill(img, point, area_clr, border_clr):
    '''Colora i pixel connessi al punto 'point' nell'immagine 'img' con il
    colore 'area_clr' e il bordo con 'border_clr'.
    '''
    # L'algoritmo base è lo scanline flood fill, ottimizzato ed adattato per le
    # esigente dell'esercizio.

    old_clr = img[point[ROW]][point[COLUMN]]

    # Si salvano tutti i punti da colorare in un insieme, per poi colorare alla
    # fine.
    border_pixels = set()
    area_pixels = set()

    # Deque è ottimizzato per le operazioni in coda ed in testa. Questo stack
    # serve per processare ogni linea della figura, identificata dal punto
    # iniziale.
    points = deque()
    points.append(point)
    while points:
        point = points.popleft()

        start_column = get_column(img, point, old_clr, -1)
        stop_column = get_column(img, point, old_clr, +1)

        interval = (start_column, stop_column)

        row = point[ROW]

        # Bordi laterali, di facile calcolo.
        border_pixels.add((row, start_column))
        border_pixels.add((row, stop_column))

        # Bordi superiori ed inferiori, di complessità maggiore.
        get_border(img, row, interval, old_clr, border_pixels)

        # Viene scansionata la linea superiore ed inferiore.
        scan_lines(img, row, interval, old_clr, points, area_pixels)

    border_pixels.discard("1") # Placeholder messo per utilità.

    # L'ordine delle due istruzioni è importante perchè il secondo dipinge
    # sopra il primo.
    area_counter = paint_region(img, area_pixels, area_clr)
    border_counter = paint_region(img, border_pixels, border_clr)

    return area_counter - border_counter, border_counter

def apply_fill(img, values):
    start_column, start_row, dest_color, side_color = values

    return fill(img, (start_row, start_column), dest_color, side_color)

def ricolora(fname, lista, fnameout):
    img = load(fname)
    retval = []

    retval = list(map(lambda element: apply_fill(img, element), lista))

    save(img, fnameout)

    return retval
