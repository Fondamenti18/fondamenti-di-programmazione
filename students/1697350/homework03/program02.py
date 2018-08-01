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

def getNewPosition(actual_position, move):
    if move == "right":
        return (actual_position[0], actual_position[1] + 40)
    if move == "left":
        return (actual_position[0], actual_position[1] - 40)
    if move == "up":
        return (actual_position[0] - 40, actual_position[1])
    if move == "down":
        return (actual_position[0] + 40, actual_position[1])

def rotate(actual_direction):
    if actual_direction == "right":
        return "down"
    if actual_direction == "down":
        return "left"
    if actual_direction == "left":
        return "up"
    if actual_direction == "up":
        return "right"

def checkCell(image, position):
    i = position[0]
    j = position[1]
    green_color = (0, 255, 0)
    blue_color = (0, 0, 255)
    red_color = (255, 0, 0)
    if image[i][j] != green_color and image[i][j] != blue_color and image[i][j] != red_color:
        return True
    return False

def colorCell(image, position, color):
    i = position[0]
    j = position[1]
    for r in range(40):
        for c in range(40):
            image[i + r][j + c] = color

def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    green_color = (0, 255, 0)
    blue_color = (0, 0, 255)
    path = ""
    directions = {"right" : "0", "down": "1", "left": "2", "up": "3"}
    actual_direction = "right"
    image = load(fname)
    actual_position = (0,0)
    num_rotation = 0
    limit = 15 * 40
    colorCell(image, actual_position, green_color)
    while True:
        new_pos = getNewPosition(actual_position, actual_direction)
        if new_pos[0] >= limit or new_pos[1] >= limit or new_pos[0] < 0 or new_pos[1] < 0:
            actual_direction = rotate(actual_direction)
            num_rotation += 1

        elif checkCell(image, new_pos):
            actual_position = new_pos
            colorCell(image, new_pos, green_color)
            path += directions[actual_direction]
            num_rotation = 0
        else:
            actual_direction = rotate(actual_direction)
            num_rotation += 1

        if num_rotation == 4:
            colorCell(image, actual_position, blue_color)
            save(image, fname1)
            return path




if __name__ == "__main__":
    cammino('I3.png','t3.png')