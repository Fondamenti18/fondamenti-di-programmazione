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

def paintSquare(board,coordX,coordY,color,squareWidth):
    for y in range(coordY,coordY+squareWidth):
        for x in range(coordX,coordX+squareWidth):
            board[y][x] = color
        
              
def trace(chessBoard):
    boardWidth = len(chessBoard)
    squareWidth = boardWidth//15
    roboDirections = [(squareWidth,0), (0,squareWidth), (-squareWidth,0), (0,-squareWidth)]
    roboPosX = 0
    roboPosY = 0
    currentDirection = 0
    path = ""
    numberOfFailures = 0
    
    while (True):
        direction = roboDirections[currentDirection]
        nextPositionX = roboPosX+direction[0]
        nextPositionY = roboPosY+direction[1]
        currentDirection += 1
        numberOfFailures += 1
        if ((nextPositionX >= 0) and (nextPositionY >= 0) and (nextPositionX < boardWidth) and (nextPositionY < boardWidth)):
            if ((chessBoard[nextPositionY][nextPositionX] == (255,255,255)) or (chessBoard[nextPositionY][nextPositionX] == (0,0,0))):
                currentDirection -= 1
                paintSquare(chessBoard,roboPosX,roboPosY,(0,255,0),squareWidth)
                roboPosX = nextPositionX
                roboPosY = nextPositionY
                path += str(currentDirection)
                numberOfFailures = 0
            
        currentDirection = currentDirection % 4
        if (numberOfFailures > 3):
            break
        
    paintSquare(chessBoard,roboPosX,roboPosY,(0,0,255),squareWidth)
    return path
            
                 
        

def cammino(fname,  fname1):
    chessBoardImage = load(fname)
    path = trace(chessBoardImage)
    save(chessBoardImage, fname1)
    return path

