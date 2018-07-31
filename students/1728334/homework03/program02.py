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
from PIL import Image
import itertools
import json


def isObstacle(diz, coordinates):
    if diz.get(coordinates) == "rosso":
        return True
    return False

def convert_to_word(colore):
    if colore == (255, 255, 255):
        return "bianco"
    elif colore == (255, 0, 0):
        return "rosso"
    elif colore == (0, 0, 0):
        return "nero"
    else:
        return "undefined"


def quadrati(file):
    img = Image.open(file)
    width, height = img.size
    lista = []
    for x in range(0, width, 40):
        for y in range(0, height, 40):
            r,g,b = img.getpixel((x,y))
            colore = r, g, b
            lista.append(colore)
    return lista


def create_cartesian():
    coordinates = list(itertools.product(range(15), range(15)))
    return coordinates


def cartesian_dict(file):
    cartesio = create_cartesian()
    lista_quadrati = quadrati(file)
    diz = {}
    for k, v in enumerate(cartesio):
        diz[v] = convert_to_word(lista_quadrati[k])
    return diz

        

def spiral(n, diz):
    dx, dy = 1, 0 # il mio incremento
    x, y = 0, 0 # la mia posizione di partenza
    matrix = [[None]* n for j in range(n+1)]
    moves = 0 # la mia direzione è verso destra
    passato = []
    cammino = ''
    obstacles2 = obstacles(diz)
    for i in range(n**2):
        matrix[x][y] = i
        nx, ny = x+dx, y+dy # incremento
        passato.append((x, y))
        #if (nx, ny) in passato and len(obstacles2) != 0:
         #   return cammino, passato
        obstacle = isObstacle(diz, (nx, ny))
        #if obstacle is True:           
        if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == None and obstacle is False: # controlliamo che non sia ai bordi della mappa, quindi entro e incremento! 
            x, y = nx, ny    
            cammino += str(moves)
        else: # o bordi od ostacolo
            celle_adj = celle_adiacenti(moves)   
            for el in celle_adj: # per tutte le coordinate vicino alla mia, in base alla mia direzione
                 # cella vicino alla mia: la prima sarà quella sottt, la seconda quella a sx, la terza quella su.
                 coordinate_aggiornate = x+el[0], y+el[1] 
                 if canWalk(diz, coordinate_aggiornate) is True and coordinate_aggiornate not in passato:
                     x, y = coordinate_aggiornate # modifico le mie x ed y
                     dx, dy = el[0], el[1] # modifico il mio incremento
                     # infine devo modificare la mia camminata
                     moves = moves_change((dx, dy)) # ecco che la modifico
                     cammino += str(moves)
                     break  
                 else:
                     continue
                     
                     
    return cammino, passato

    
def ricolora_porzioni(lista_quadrati, file, name):
    img = Image.open(file)
    pixels = img.load() # this is not a list, nor is it list()'able
    width, height = img.size
    for quadrato in lista_quadrati:
        qX = quadrato[0]
        qY = quadrato[1]
        for x in range(qX * 40, (qX + 1) * 40):
            for y in range(qY * 40, (qY + 1) * 40):
                if quadrato != lista_quadrati[-1]:
                    pixels[x, y] = (0, 255, 0)
                else:
                    pixels[x, y] = (0, 0, 255)   
    list_of_pixels = list(img.getdata())
    im2 = Image.new(img.mode, img.size)
    im2.putdata(list_of_pixels)
    im2.save(name)

def jsontest():
    img = load("t4.png")
    with open("outson.json", mode="w") as out:
        json.dump(img, out)

def get_range_to_recolor(n, width, height):
    width = (n - 1) * 40
    height = n*40
    return width, height

def canWalk(diz, coord):
    x, y = coord
    if isObstacle(diz, coord) is False and 0 <= x <= 14 and 0 <= y <= 14:
        return True
    return False


def change_moves(case):
    if case == 0:
        return 1
    if case == 1:
        return 2
    if case == 2:
        return 3
    if case == 3:
        return 0

def moves_change(coord):
    if coord == (1, 0):
        return 0
    elif coord == (0, 1):
        return 1
    elif coord == (-1, 0):
        return 2
    else:
        return 3

def celle_adiacenti(moves):
    if moves == 0: # sto arrivando da destra
        adiacenti = [(0, 1), (-1, 0), (0, -1)] # controllo sotto, sinistra, e sopra
    if moves == 1: # arrivo da giù
        adiacenti = [(-1, 0), (0, -1), (1, 0)] # prima controllo a sinistra, poi su, poi destra
    if moves == 2: # arrivo da sinistra
        adiacenti = [(0, -1), (1, 0), (0, 1)] # prima controllo su, poi destra poi giù
    if moves == 3: # 3 vuol dire che vado su
        adiacenti = [(1, 0), (0, 1), (-1, 0)] # controllo dx, giù, sx
    return adiacenti
        

def obstacles(diz):
    return [k for k, v in diz.items() if v == "rosso"]


def change_increment(moves):
    if moves == 0:
        dx, dy = 0, 1
    if moves == 1:
        dx, dy = -1, 0
    if moves == 2:
        dx, dy = 0, -1
    if moves == 3:
        dx, dy = 1, 0
    return dx, dy


def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    cartesiano = cartesian_dict(fname)
    spirale = spiral(15, cartesiano)
    ricolora_porzioni(spirale[1], fname, fname1)
    return spirale[0]
    



    