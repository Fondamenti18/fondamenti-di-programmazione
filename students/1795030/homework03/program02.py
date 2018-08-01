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

Libero = 0
Ostacolo = 1
Visitato = 2
Ultimo = 3

Destra = 0
Basso = 1
Sinistra = 2
Alto = 3

def cammino(fname, fname1):
    img = load(fname)
    matrix = [[0 for x in range(15)] for y in range(15)]
    for y in range(0, 15):
        for x in range(0, 15):
            px = img[y*40][x*40];
            matrix[y][x] = Libero if px == (0, 0, 0) or px == (255, 255, 255) else Ostacolo
    stato= {'x' : 0, 'y' : 0, 'dir' : Destra}
    matrix[0][0] = Visitato
    dirs = ''
    while movimento(matrix, stato, ferma_ricorsione = -1):
        matrix[stato['y']][stato['x']] = Visitato
        dirs += str(stato['dir'])
    matrix[stato['y']][stato['x']] = Ultimo
    imout = [[0 for x in range(600)] for y in range(600)]
    for y in range(0, 600):
        for x in range(0, 600):
            m = matrix[int(y / 40)][int(x / 40)]
            if m == Libero or m == Ostacolo:
                imout[y][x] = img[y][x]
            elif m == Visitato:
                imout[y][x] = (0, 255, 0)
            elif m == Ultimo:
                imout[y][x] = (0, 0, 255)
    save(imout, fname1)
    return dirs

def movimento(matrix, stato, ferma_ricorsione = -1):
    if ferma_ricorsione == -1:
        ferma_ricorsione = stato['dir']
    elif ferma_ricorsione == stato['dir']:
        return False
    x = stato['x']
    y = stato['y']
    #verso destra
    if stato['dir'] == Destra:
        if x<14 and matrix[y][x+1] == Libero:
            stato['x'] = x+1
            return True
        stato['dir'] = Basso
    #verso il basso
    elif stato['dir'] == Basso:
        if y < 14 and matrix[y+1][x] == Libero:
            stato['y'] = y+1
            return True
        stato['dir'] = Sinistra
    #verso sinistra
    elif stato['dir'] == Sinistra:
        if x > 0 and matrix[y][x-1] == Libero:
            stato['x'] = x - 1
            return True
        stato['dir'] = Alto
    #verso alto
    elif stato['dir'] == Alto:
        if y > 0 and matrix[y-1][x] == Libero:
            stato['y'] = y - 1
            return True
        stato['dir'] = Destra
    return movimento(matrix, stato, ferma_ricorsione)

if __name__ == '__main__':
    cammino('I1.png', 'risI1.png')
    cammino('I2.png', 'risI2.png')
    cammino('I3.png', 'risI3.png')
    cammino('I4.png', 'risI4.png')
    cammino('I5.png', 'risI5.png')
