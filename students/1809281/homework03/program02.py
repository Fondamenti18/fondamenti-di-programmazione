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

def cammino(fname,  fname1):
    image = load(fname)
    x = 0
    y = 0
    next_x = 0
    next_y = 0
    tile_size = 40
    direction = 0 # 0 = right, 1 = down, 2 = right, 3 = up
    direction_steps = ''
    
    while (True):
        paint_tile(image, x, y)
        next_x, next_y = increment_coordinates(x, y, direction)
        
        
        # Say hello to Mr. Clusterflip
        # 2 main conditions to check: next tile is green or red (obstacles), and next tile is NOT within bounds of the image. If true, it changes rotation and checks in that direction.
        # The loops variable makes sure it only tries to rotate a finite number of times before giving up.
        loops = 0
        while ((next_x < 0) or (next_x > 14)) or ((next_y < 0) or (next_y > 14)) or ((image[next_y * tile_size][next_x * tile_size] == (0, 255, 0)) or (image[next_y * tile_size][next_x * tile_size] == (255, 0, 0))):
            direction += 1
            if direction >= 4: direction = 0
            
            next_x, next_y = increment_coordinates(x, y, direction)
            
            loops += 1
            if loops > 3: break
 

        else:
            # print('X: {} -> {}        Y: {} -> {}        Direction: {}'.format(x,next_x,y,next_y,direction))*
            
            x = next_x
            y = next_y        
            direction_steps += str(direction)

            continue
        break

    
    paint_tile(image, x, y, color=(0,0,255))
        
    save(image, fname1)    
    return direction_steps
    

    
def increment_coordinates(x, y, direction):
    next_x, next_y = x, y
    
    direction_dict = {
    '0' : (1, 0),
    '1' : (0, 1),
    '2' : (-1, 0),
    '3' : (0, -1) }
    
    next_x += direction_dict[str(direction)][0]
    next_y += direction_dict[str(direction)][1]
    
    return next_x, next_y

    
def paint_tile(image, x, y, tile_size=40, color=(0, 255, 0)):
    for y_current in range(y * tile_size, (y + 1) * tile_size):
        for x_current in range(x * tile_size, (x + 1) * tile_size):
            image[y_current][x_current] = color

    
if __name__ == '__main__':
    print(cammino('I3.png', 'solotest.png'))