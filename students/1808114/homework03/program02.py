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

def dim_caselle(imma):
    num = 0
    color = imma[0][0]
    while imma[num][0] == color and imma[0][num] == color:
        num +=1
    return num

def colora(imma, dim, coord, final = False):
    col = (0,255,0)
    if final == True: col = (0,0,255)
    for y in range(coord[0], coord[0]+dim):
        for x in range(coord[1], coord[1]+dim):
            imma[y][x] = col
    return

def dx(imma, passo, rob_dir, rob_pos, l, cont):
    b = (255,255,255)
    n = (0,0,0)
    if rob_pos[1] == l-passo:
        return dir_disp(imma, passo, 1, rob_pos, cont+1)
    elif imma[rob_pos[0]][rob_pos[1]+passo] == b or imma[rob_pos[0]][rob_pos[1]+passo] == n :
        colora(imma, passo, rob_pos)
        return [0, [rob_pos[0], rob_pos[1]+passo]]
    else: return dir_disp(imma, passo, 1, rob_pos, cont+1)

def dn(imma, passo, rob_dir, rob_pos, h, cont):
    b = (255,255,255)
    n = (0,0,0)
    if rob_pos[0] == h-passo:
        return dir_disp(imma, passo, 2, rob_pos, cont+1)
    elif imma[rob_pos[0]+passo][rob_pos[1]] == b or imma[rob_pos[0]+passo][rob_pos[1]] == n:
        colora(imma, passo, rob_pos)
        return [1, [rob_pos[0]+passo, rob_pos[1]]]
    else: return dir_disp(imma, passo, 2, rob_pos, cont+1)

def sx(imma, passo, rob_dir, rob_pos, l, cont):
    b = (255,255,255)
    n = (0,0,0)
    if rob_pos[1] == 0:
        return dir_disp(imma, passo, 3, rob_pos, cont+1)
    elif imma[rob_pos[0]][rob_pos[1]-passo] == b or imma[rob_pos[0]][rob_pos[1]-passo] == n:
        colora(imma, passo, rob_pos)
        return [2, [rob_pos[0], rob_pos[1]-passo]]
    else: return dir_disp(imma, passo, 3, rob_pos, cont+1)

def up(imma, passo, rob_dir, rob_pos, h, cont):
    b = (255,255,255)
    n = (0,0,0)
    if rob_pos[0] == 0:
        return dir_disp(imma, passo, 0, rob_pos, cont+1)
    elif imma[rob_pos[0]-passo][rob_pos[1]] == b or imma[rob_pos[0]-passo][rob_pos[1]] == n:
        colora(imma, passo, rob_pos)
        return [3, [rob_pos[0]-passo, rob_pos[1]]]
    else: return dir_disp(imma, passo, 0, rob_pos, cont+1)

def dir_disp(imma, passo, rob_dir, rob_pos, cont=0):
    h = len(imma)
    l = len(imma[0])
    if cont > 4: return False
    if  rob_dir == 0:
        return dx(imma, passo, rob_dir, rob_pos, l, cont)
    elif rob_dir == 1:
        return dn(imma, passo, rob_dir, rob_pos, h, cont)
    elif rob_dir == 2:
        return sx(imma, passo, rob_dir, rob_pos, l, cont)
    elif rob_dir == 3:
        return up(imma, passo, rob_dir, rob_pos, h, cont)
    else: return False

def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    imma = load(fname)
    casella = dim_caselle(imma)
    stringa = ''
    direz = 0
    coord = [0, 0]
    while True:
        lista = dir_disp(imma, casella, direz, coord, 0)
        if lista != False:
            direz = lista[0]
            coord = lista[1]
            stringa += str(direz)
        else: break
    colora(imma, casella, coord, True)
    save(imma, fname1)
    return stringa