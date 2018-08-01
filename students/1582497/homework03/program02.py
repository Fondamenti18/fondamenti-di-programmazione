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
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
movimenti = []

def cammino(fname,  fname1):
    movimenti = []
    pic = load(fname)
    X=39
    Y=39
    move = 0
    count = 0
    for y in range(40):
        for x in range(40):
            pic[y][x] = green
    while count < 4:
        if move == 0:
            if X+1 < 599 and pic[Y][X+1] != red and pic[Y][X+1] != green:
                X += 40
                count = 0
                movimenti.append(str(move))
                for y in range(Y-39,Y+1):
                    for x in range(X-39,X+1):
                        pic[y][x] = green
            else:
                move += 1
                count += 1
        elif move == 1:
            if Y+1 < 599 and pic[Y+1][X] != red and pic[Y+1][X] != green:
                Y += 40
                count = 0
                movimenti.append(str(move))
                for y in range(Y-39,Y+1):
                    for x in range(X-39,X+1):
                        pic[y][x] = green
            else:
                move += 1
                count += 1
        elif move == 2:
            if X-41 > 0 and pic[Y][X-41] != red and pic[Y][X-41] != green:
                X -= 40
                count = 0
                movimenti.append(str(move))
                for y in range(Y-39,Y+1):
                    for x in range(X-39,X+1):
                        pic[y][x] = green
            else:
                move += 1
                count += 1
        elif move == 3:
            if Y-41 > 0 and pic[Y-41][X] != red and pic [Y-41][X] != green:
                Y -= 40
                count = 0
                movimenti.append(str(move))
                for y in range(Y-39,Y+1):
                    for x in range(X-39,X+1):
                        pic[y][x] = green
            else:
                move = 0
                count += 1
    else:
        for y in range(Y-39,Y+1):
            for x in range(X-39,X+1):
                pic[y][x] = blue
    save(pic,fname1)
    return ''.join(movimenti)
