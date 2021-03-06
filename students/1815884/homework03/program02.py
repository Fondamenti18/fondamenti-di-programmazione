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

def map_board(img):
    obstacle = (255, 0, 0)
    obstacle_map = list()
    for x in [i*40 for i in range(15)]:
        for y in [i*40 for i in range(15)]:
            if img[x][y] == obstacle:
                obstacle_map.append((y//40, x//40))
    return obstacle_map

def color_route(img, route):
    step = (0, 255, 0)
    final_pos = (0, 0, 255)
    for pos in route[:-1]:
        for x in range(40):
            for y in range(40):
                img[pos[1]*40+x][pos[0]*40+y] = step
    for x in range(40):
        for y in range(40):
            img[route[-1][1]*40+x][route[-1][0]*40+y] = final_pos
    return img


def cammino(fname,  fname1):
    board = load(fname)
    pos = [0, 0]
    direction = 0
    steps = 0
    obstacle_map = map_board(board)
    route = [(0, 0)]
    encoded_route = str()
    while steps < 5:
        if direction == 0:
            pos[0] += 1
            if tuple(pos) not in obstacle_map + route and pos[0] < 15:
                route.append(tuple(pos))
                encoded_route += str(direction)
                steps = 0
                continue
            else:
                pos[0] -= 1
                direction = 1
                steps += 1
                continue

        elif direction == 1:
            pos[1] += 1
            if tuple(pos) not in obstacle_map + route and pos[1] < 15:
                route.append(tuple(pos))
                encoded_route += str(direction)
                steps = 0
                continue
            else:
                pos[1] -= 1
                direction = 2
                steps += 1
                continue

        elif direction == 2:
            pos[0] -= 1
            if tuple(pos) not in obstacle_map + route and pos[0] > -1:
                route.append(tuple(pos))
                encoded_route += str(direction)
                steps = 0
                continue
            else:
                pos[0] += 1
                direction = 3
                steps += 1
                continue

        elif direction == 3:
            pos[1] -= 1
            if tuple(pos) not in obstacle_map + route and pos[1] > -1:
                route.append(tuple(pos))
                encoded_route += str(direction)
                steps = 0
                continue
            else:
                pos[1] += 1
                direction = 0
                steps += 1
                continue

    save(color_route(board, route), fname1)
    return encoded_route
