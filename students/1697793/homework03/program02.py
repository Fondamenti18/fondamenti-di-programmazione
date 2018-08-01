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
    
def checkMove (chessboard, robot, ir, ic):
    
    ir1 = ir
    ic1 = ic
    
    orien = robot['orientation']
    
    if orien == 0:
        ic1+=40
    elif orien == 1:
        ir1+=40
    elif orien == 2:
        ic1-=40
    else:       
        ir1-=40
        
    return [ir1, ic1]

def checkCasella (chessboard, rows, cols, robot, ir, ic):
    
    if ir < rows and ir >= 0 and ic < cols and ic >= 0:
    
        casella = chessboard[ir][ic]
    
        if casella == (0,255,0) or casella == (255,0,0):
            return False
        else:
            return True
    else:
        return False
 
def changeOrientation (robot):
    
    orien = robot['orientation']
    
    if orien == 3:
        orien = -1
        
    robot['orientation'] = orien+1
    robot['totalRotate']+=1
    
def colorCasella (chessboard, ir, ic, color):
    
    for ir1 in range(ir,ir+40):
        for ic1 in range(ic,ic+40):
            chessboard[ir1][ic1] = color

def getRobot ():
    return { 'orientation': 0, 'totalRotate': 0, 'steps': '' }

def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    
    chessboard = load(fname)
    rows = len(chessboard)
    cols = len(chessboard[0])
    
    ir = 0
    ic = 0
    
    robot = getRobot()
        
    while (robot['totalRotate'] < 4):
    
        nextCasella = checkMove(chessboard, robot, ir, ic)
    
        if checkCasella(chessboard, rows, cols, robot, nextCasella[0], nextCasella[1]):
            
            colorCasella(chessboard, ir, ic, (0,255,0))
            ir = nextCasella[0]
            ic = nextCasella[1]
            robot['totalRotate'] = 0
            robot['steps']+=str(robot['orientation'])
            
        else:
            
            changeOrientation(robot)
     
    colorCasella(chessboard, ir, ic, (0,0,255))
            
    save(chessboard, fname1)
    
    return robot['steps']
