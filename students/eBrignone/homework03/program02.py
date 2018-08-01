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
from enum import Enum

WIDTH = 600
HEIGHT = 600
BLOCK_WIDTH = 40
BLOCK_HEIGHT = 40

class Color(Enum):
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)

class Move(Enum):
    TOP = (-1,0)
    RIGHT = (0,1)
    BOTTOM = (1,0)
    LEFT = (0,-1)

def tupleSum(t1,t2):
    return(t1[0]+t2[0],t1[1]+t2[1])
    
def tupleToColor(rgb):
    if rgb==(255,255,255):
        return Color.WHITE
    elif rgb==(0,0,0):
        return Color.BLACK
    elif rgb==(255,0,0):
        return Color.RED
    elif rgb==(0,255,0):
        return Color.GREEN
    else:
        return Color.BLUE
def nextTry(move):
    if move==Move.RIGHT:
        return Move.BOTTOM
    elif move==Move.BOTTOM:
        return Move.LEFT
    elif move==Move.LEFT:
        return Move.TOP
    else:
        return Move.RIGHT
def moveToString(move):
    if move==Move.RIGHT:
        return "0"
    elif move==Move.BOTTOM:
        return "1"
    elif move==Move.LEFT:
        return "2"
    else:
        return "3"
def caricaScacchiera(img):
    matrix = []
    for j in range(0,int(HEIGHT/BLOCK_HEIGHT)):
        row = []
        for i in range(0,int(WIDTH/BLOCK_WIDTH)):
            row.append(tupleToColor(img[j*BLOCK_HEIGHT][i*BLOCK_WIDTH]))
        matrix.append(row)
    return matrix

def salvaScacchiera(matrix):
    img = []
    for y in range(0,len(matrix)):
        row = []
        for x in range(0,len(matrix[y])):
            for i in range(0,BLOCK_WIDTH):
                row.append(matrix[y][x].value)
        for j in range(0,BLOCK_HEIGHT):
            img.append(row)
    return img

def inBound(h,w,y,x):
    return y>=0 and y<h and x>=0 and x<w

def nextMove(matrix,currentPosition,prevMove):
    y = currentPosition[0]
    x = currentPosition[1]
    
    nextY = y + prevMove.value[0]
    nextX = x + prevMove.value[1]
    
    tryCount = 0
    while tryCount < 4:
        #dentro la matrice (non sforo)
        if inBound(len(matrix),len(matrix[0]),nextY,nextX):
            #controllo se il blocco nella prossima mossa è valido per muoversi
            if matrix[nextY][nextX]==Color.WHITE or matrix[nextY][nextX]==Color.BLACK:
                return ((nextY,nextX),prevMove)
            else:
                prevMove = nextTry(prevMove)
        else:
            prevMove = nextTry(prevMove)
        nextY = y + prevMove.value[0]
        nextX = x + prevMove.value[1]
        tryCount += 1
        
    return ((-1,-1),prevMove)
         
def cammino(fname,  fname1):
    img = load(fname)
    matrix = caricaScacchiera(img)
    moves = ""
    position = (0,0)
    move = Move.RIGHT
    while(position[0]<len(matrix) and position[1]<len(matrix[position[0]])):
        matrix[position[0]][position[1]] = Color.GREEN
        moves += moveToString(move)
        t = nextMove(matrix,position,move)
        nextPosition = t[0]
        
        if(nextPosition==(-1,-1)):
            matrix[position[0]][position[1]] = Color.BLUE

            break
        move = t[1]
        position = nextPosition
    
    toSave = salvaScacchiera(matrix)
    save(toSave,fname1)
    return moves[1:]

    