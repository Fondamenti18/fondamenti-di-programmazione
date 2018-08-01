'''
Un robottino deve muoversi su di una scacchiera di 15 x 15 celle  con celle bianche e nere	ciascuna di lato 40.
Per rendere il percorso accidentato alcune delle celle della scacchiera contengono ostacoli (queste celle sono	colorate di rosso).

Un	esempio di scacchiera con ostacoli e' dato	dall'immagine 'I1.png'

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Al'inizio il robottino e' posizionato sulla prima cella in altro a sinistra della scacchiera ed e' rivolto verso destra (x crescente).
Ad ogni step tenta di ragiungere una delle celle adiacenti in orizzontale o verticale.
Le regole di movimento del robottino sono le seguenti:
- al generico step, si sposta sulla cella che ha di fronte se questa e' libera da ostacoli e non ci e' gia transitato in passato.
- se invece la cella risulta occupata o e' una cella su cui ha gia transitato, ruota di 90 gradi in senso orario ed aspetta lo step successivo.
- dopo aver ruotato	 di 360 gradi senza essere riuscito a spostarsi si ferma.

Progettare la funzione	percorso(fname, fname1) che presi in input:
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


def fill_cell(img, pos,color):
    for i in range(pos[0],pos[0]+40):
        for j in range(pos[1],pos[1]+40):
            img[i][j] = color

size = {"w":0,"h":0}

def get_east_step(img, pos):
    x,y = pos
    z = pos[1]+40
    return (False,(x,z),img[x][z]) if size["w"] > z else (True,None,None)

def get_south_step(img, pos):
    x, y = pos
    z = pos[0] + 40
    return (False,(z,y),img[z][y]) if size["w"] > z else (True,None,None)

def get_west_step(img, pos):
    x, y = pos
    z = pos[1] - 40
    return (False,(x,z),img[x][z]) if z >= 0 else (True,None,None)

def get_north_step(img, pos):
    x, y = pos
    z = pos[0] - 40
    return (False,(z,y),img[z][y]) if z >= 0 else (True,None,None)


def cammino(fname,	fname1):
    stepper = {0:get_east_step,
               1:get_south_step,
               2:get_west_step,
               3:get_north_step}

    direction =0
    turns=0
    steps=[]
    pos=(0,0)

    cell=0
    obstacle_color = (255,0,0)
    stepped_color = (0,255,0)
    done_color = (0,0,255)

    img = load(fname)
    size["w"] = len(img[0])
    size["h"] = len(img)

    while turns <4:
        for i in range(pos[0], pos[0] + 40):
            for j in range(pos[1], pos[1] + 40):
                img[i][j] = stepped_color

        out_of_bounds, new_pos, cell_color = stepper[direction](img,pos)
        if out_of_bounds or cell_color == obstacle_color or cell_color == stepped_color:
            direction=(direction+1)%4 #next_direction[direction]
            turns+=1
        else:
            turns = 0
            pos = new_pos
            steps.append(str(direction))

    for i in range(pos[0], pos[0] + 40):
        for j in range(pos[1], pos[1] + 40):
            img[i][j] = done_color
    save(img,fname1)

    return "".join(steps)#map(lambda x: str(x),steps))
