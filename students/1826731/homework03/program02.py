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

def cammino(fname, fname1):
    scacchiera = load(fname)
    codifica = ''
    x, y = 20, 20
    scacchiera = verde(scacchiera, x, y)
    lato = len(scacchiera)
    direzione = 'destra'
    rotazione = 0
    while rotazione != 360:
        if direzione == 'destra':
            while x + 40 < lato:
                if scacchiera[y][x + 40] == (255, 0, 0) or scacchiera[y][x + 40] == (0, 255, 0):
                    break
                else:
                    rotazione = 0
                    x = x + 40
                    scacchiera = verde(scacchiera, x, y)
                    codifica = codifica + '0'
            direzione = 'basso'
            rotazione = rotazione + 90
        elif direzione == 'basso':
            while y + 40 < lato:
                if scacchiera[y + 40][x] == (255, 0, 0) or scacchiera[y + 40][x] == (0, 255, 0):
                    break
                else:
                   rotazione = 0
                   y = y + 40
                   scacchiera = verde(scacchiera, x, y)
                   codifica = codifica + '1'
            direzione = 'sinistra'
            rotazione = rotazione + 90
        elif direzione == 'sinistra':
            while x - 40 > 0:
                if scacchiera[y][x - 40] == (255, 0, 0) or scacchiera[y][x - 40] == (0, 255, 0):
                    break
                else:               
                    rotazione = 0
                    x = x - 40
                    scacchiera = verde(scacchiera, x, y)
                    codifica = codifica + '2'
            direzione = 'alto'
            rotazione = rotazione + 90
        elif direzione == 'alto':
            while y - 40 > 0:
                if scacchiera[y - 40][x] == (255, 0, 0) or scacchiera[y - 40][x] == (0, 255, 0):
                    break
                else:               
                    rotazione = 0
                    y = y - 40
                    scacchiera = verde(scacchiera, x, y)
                    codifica = codifica + '3'
            direzione = 'destra'
            rotazione = rotazione + 90
        if rotazione == 360:
            scacchiera = blu(scacchiera, x, y)
    save(scacchiera, fname1)
    return codifica 
  
def verde(imm, xN, yN):
    '''stampa sull'immagine un quadrato verde
       40x40 a partire dal punto (xN, yN)'''
    xN, yN = xN - 20, yN - 20
    for p_oriz in range(xN, xN + 40):
        for p_vert in range(yN, yN + 40):
            imm[p_vert][p_oriz] = (0, 255, 0)
    return imm
   
def blu(imm, xN, yN):
    '''stampa sull'immagine un quadrato blu
       40x40 a partire dal punto (xN, yN)'''
    xN, yN = xN - 20, yN - 20
    for p_oriz in range(xN, xN + 40):
        for p_vert in range(yN, yN + 40):
            imm[p_vert][p_oriz] = (0, 0, 255)
    return imm
