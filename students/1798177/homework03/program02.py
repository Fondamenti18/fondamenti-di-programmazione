# Un robottino deve muoversi su di una scacchiera di 15 x 15 celle con celle
# bianche e nere ciascuna di lato 40. Per rendere il percorso accidentato
# alcune delle celle della scacchiera contengono ostacoli (queste celle sono

#
# Un  esempio di scacchiera con ostacoli è dato dall'immagine 'I1.png'.
#
# Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo
# preparato nel modulo immagini.py.
#
# All'inizio il robottino è posizionato sulla prima cella in altro a sinistra
# della scacchiera ed è rivolto verso destra (x crescente).
# Ad ogni step tenta di ragiungere una delle celle adiacenti in orizzontale o
# verticale.
# Le regole di movimento del robottino sono le seguenti:
# - al generico step, si sposta sulla cella che ha di fronte se questa è libera
#   da ostacoli e non ci è gia transitato in passato.
# - se invece la cella risulta occupata o è una cella su cui ha gia transitato,
#   ruota di 90 gradi in senso orario ed aspetta lo step successivo.
# - dopo aver ruotato di 360 gradi senza essere riuscito a spostarsi si ferma.
#
# Progettare la funzione  percorso(fname, fname1) che presi in input:
# - il percorso di un file (fname) contenente l'immagine in formato .png di una
#   scacchiera con ostacoli
# - il percorso di un file di tipo .png (fname1) da creare legge l'immagine
#   della scacchiera in fname, colora di verde le celle della scacchiera
#   percorse dal robottino prima di fermarsi, colora di blu la cella in cui il
#   robottino si ferma e registra l'immagine ricolorata nel file fname1.
#
# Inoltre restituisce una stringa dove in sequenza sono codificati i passi
#  effettuati dal robottino prima di fermarsi.
#
# La codifica è a seguente:
#    '0' per un passo verso destra (x crescenti)
#    '1' per un passo verso il basso (y crescenti)
#    '2' per un passo verso sinistra (x decrescenti)
#    '3' per un passo verso l'alto (y decrescenti)
#
# Si puo' assumere che la cella in alto a sinistra sia priva di ostacoli.
#
# Per esempi di scacchiere con ostacoli e relativi cammini  vedere il file
# grade02.txt.
#
# NOTA: il timeout per la esecuzione del grader è fissato a 10*N secondi (per N
# test eseguiti dal grader)
#
# Svolto da Emanuele Petriglia.

from immagini import load, save

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

ROW = 0
COLUMN = 1

def is_inside(point):
    '''Ritorna True se il punto si trova nella scacchiera, altrimenti False.'''
    return 0 <= point[ROW] < 600 and 0 <= point[COLUMN] < 600

def check_colors(img, point):
    '''Controlla che il punto 'point' nella scacchiera 'img' non sia di colore
    rosso o verde, ritornando True altrimenti False.
    '''
    row, column = point

    return img[row][column] != RED and img[row][column] != GREEN

def can_move(img, point):
    '''Ritorna True se il robot si può muovere nel punto 'point' della
    scacchiera 'img', altrimenti False.
    '''
    return is_inside(point) and check_colors(img, point)

def get_move(img, point, direction = 0):
    '''Ritorna il punto successivo che indica la mossa del robot, assieme ad un
    codice di codifica numero per la direzione. In caso non sa possibile
    effettuare alcun movimento ritorna il punto originale ed il codice -1.
    '''
    directions = { # Indica l'offset da calcolare per ogni direzione.
        0 : (0, 40),
        1 : (40, 0),
        2 : (0, -40),
        3 : (-40, 0)
    }

    column, row = point

    for _ in range(0, 4):
        direction %= 4 # La direzione iniziale può variare.
        offset = directions[direction]

        row = point[ROW] + offset[ROW]
        column = point[COLUMN] + offset[COLUMN]

        if can_move(img, (row, column)):
            return (row, column), direction

        direction += 1

    return (point[ROW], point[COLUMN]), -1

def paint_cell(img, point, color):
    '''Dipinge una cella di lato 40 col colore 'color' indicata dal punto
    'point' dell'angolo in alto a sinistra sulla scacchiera 'img'.
    '''
    start_row, start_column = point

    for row in range(start_row, start_row + 40):
        for column in range(start_column, start_column + 40):
            img[row][column] = color

def move_robot(img):
    '''Dipinge sulla scacchiera 'img' il percorso che effettua il robot,
    ritornando una stringa con i movimenti codificati in numero.
    '''
    moves = '' # Passi codificati.

    point = (0, 0)
    paint_cell(img, point, GREEN) # Cella di partenza.

    point, move = get_move(img, point)
    while move != -1:
        moves += str(move)
        paint_cell(img, point, GREEN)

        point, move = get_move(img, point, move)

    paint_cell(img, point, BLUE) # Cella di arrivo.

    return moves

def cammino(fname, fname1):
    img = load(fname)

    moves = move_robot(img)

    save(img, fname1)

    return moves
