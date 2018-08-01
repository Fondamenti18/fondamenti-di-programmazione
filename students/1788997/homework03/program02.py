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
from immagini import load, save

def isInside(x, y):
    '''controlla e ritorna true se la coordinata è nel range consentito'''
    return 0 <= x < 15 and 0 <= y < 15
def cammino(fname,  fname1):
    '''inseriti il nome del percorso da caricare e da salvare la funzione ritorna il percorso del robottino colorato all'interno della scacchiera'''
    img = load(fname)
    def drawSquare(tx, ty, c):
        '''disegna un quadrato di colore c nel range richiesto'''
        for y in range(ty*40, ty*40+40):
            for x in range(tx*40, tx*40+40):
                img[y][x] = c
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    robotDir, s, x, y, rotationsDone, count = directions[0], "", 0, 0, 0, 0
    while rotationsDone != 4:
        if isInside(x + robotDir[1], y + robotDir[0]):
            p = img[(y + robotDir[0])*40][(x + robotDir[1])*40]
            if p != (255,0,0) and p != (0,255,0):
                s += str(count % 4)
                drawSquare(x, y, (0,255,0))
                x, y, rotationsDone = x + robotDir[1], y + robotDir[0], 0
                continue
        count += 1
        robotDir = directions[count % 4]
        rotationsDone += 1
    drawSquare(x, y, (0,0,255))
    save(img, fname1)
    return s