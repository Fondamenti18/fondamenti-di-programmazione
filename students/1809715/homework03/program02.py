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

COLOR_WHITE=(0, 0, 0)
COLOR_BLACK=(255, 255, 255)
COLOR_RED=(255, 0, 0)
COLOR_GREEN=(0, 255, 0)
COLOR_BLUE=(0, 0, 255)
    
def color(img, color, position, cell_pixel):
    for x in range(0, cell_pixel):
        for y in range(0, cell_pixel):
            img[ y + position[0]][x + position[1]]=color
    return img
    
def cammino(fname, fname1):
    
    CELL_NUMBER=15
    CELL_PIXEL=40

    cell_current_position = [0, 0] # y, x
    cell_next_position = [0, 0] # y, x
    cell_next_color = False
    
    rotation=0
    direction=0
    movements=''
    img = load(fname)
                
    img = color(img, COLOR_GREEN, cell_current_position, CELL_PIXEL)
    
    while (rotation < 4):
        cell_next_position = cell_current_position[:]
        if direction==0:
            cell_next_position[1] = cell_next_position[1] + CELL_PIXEL
        elif direction==1:
            cell_next_position[0] = cell_next_position[0] + CELL_PIXEL
        elif direction==2:
            cell_next_position[1] = cell_next_position[1] - CELL_PIXEL
        elif direction==3:
            cell_next_position[0] = cell_next_position[0] - CELL_PIXEL
       
        try:
           cell_next_color = img[cell_next_position[0]][cell_next_position[1]]
           if (cell_next_position[0] < 0) or (cell_next_position[1] < 0):
               cell_next_color = False
        except IndexError:
            cell_next_color = False
       
        if (cell_next_color == False) or (cell_next_color == COLOR_RED) or (cell_next_color == COLOR_GREEN):
            rotation = rotation + 1
            direction = direction + 1
            if direction > 3:
                direction = 0
            continue
        rotation = 0

        movements = movements + str(direction)
        cell_current_position = cell_next_position
        img = color(img, COLOR_GREEN, cell_current_position, CELL_PIXEL)

    img = color(img, COLOR_BLUE, cell_current_position, CELL_PIXEL)
    save(img, fname1)
    
    return movements





                
                

