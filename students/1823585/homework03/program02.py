'''
Un robottino deve muoversi su di una scacchiera di 15 x 15 celle  con celle bianche e nere  ciascuna di lato 40. 
Per rendere il percorso accidentato alcune delle celle della scacchiera contengono ostacoli (queste celle sono  colorate di rosso).

Un  esempio di scacchiera con ostacoli e' dato  dall'immagine 'I1.png'

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Al'inizio il robottino e' posizionato sulla prima cella in altro a sinistra della scacchiera ed e' rivolto verso destra (x crescente). 
Ad ogni step tenta di ragiungere una delle celle adiacenti in orizzontale o verticale. 
Le regole di movimento del robottino sono le seguenti: 
- al generico step, si sposta sulla cella che ha di fronte se questa e' libera da ostacoli e non ci e' gia transitato in passato. 
- se invece la cella risulta occupata o e' una cella su cui ha gia transitato, ruota di 90 gradi in senso orario ed aspetta lo step successivo. 
- dopo aver ruotato  di 360 gradi senza essere riuscito a spostarsi si ferma. 

Progettare la funzione  percorso(fname, fname1) che presi in input:
- il percorso di un file (fname) contenente l'immagine in formato .png di una scacchiera con ostacoli
- il percorso di un file di tipo .png (fname1) da creare
legge l'immagine della scacchiera in fname, colora di verde le celle della scacchiera percorse dal robottino prima di fermarsi, 
colora di blu la cella in cui il robottino si ferma e registra l'immagine ricolorata nel file fname1. 
Inoltre restituisce una stringa dove in sequanza sono codificati i passi effettuati dal robottino prima di fermarsi. 
La codifica e' a seguente: 
    '0' per un passo verso destra (x crescenti)
    '1' per un passo verso il basso (y crescenti)
    '2' per un passo verso sinistra (x decrescenti)
    '3' per un passo verso l'alto (y decrescenti)

Si puo' assumere che la cella in alto a sinistra sia priva di ostacoli. 

Per esempi di scacchiere con ostacoli e relativi cammini  vedere il file grade02.txt 

NOTA: il timeout per la esecuzione del grader e' fissato a 10*N secondi (per N test eseguiti dal grader)
'''

from immagini import *

RIGHT, DOWN, LEFT, UP = 0,1,2,3
RED, GREEN, BLUE  = (255,0,0), (0,255,0), (0,0,255)

def cammino(fname,  fname1):
    img = load(fname)
    facing = RIGHT
    degrees = 0
    p_i, p_j = 0,0  
    passi = []

    while degrees < 360:
        color_cell(p_i, p_j, GREEN, img)
        n_i, n_j = get_next_cell(p_i, p_j, facing)
        if is_passable(n_i, n_j, img):
            p_i, p_j = n_i, n_j
            degrees = 0
            passi.append(facing)
        else:
            facing += 1
            if facing > 3:
                facing = 0
            degrees += 90
            if degrees >= 360:
                color_cell(p_i, p_j, BLUE, img)
                break
    save(img, fname1)
    return "".join(str(p) for p in passi)

def get_next_cell(i,j,direction):
    if direction == RIGHT:
        return i,j+40
    if direction == DOWN:
        return i+40,j
    if direction == LEFT:
        return i,j-40
    if direction == UP:
        return i-40,j
    
def is_passable(i,j,img):
    if 0 > i or i >= len(img) or 0 > j or j >= len(img[0]):
        return False
    color = img[i][j]    
    if color == RED or color == GREEN:
        return False
    return True

def color_cell(i,j,color,img):
    for t_i in range(i,i+40):
        for t_j in range(j,j+40):
            img[t_i][t_j] = color