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

def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    immagine = load(fname)
    immagine2 = load(fname)
    blu = (0,0,255)
    verde = (0,255,0)
    rosso = (255, 0, 0)
    direzione = "destra"
    robot_x = 0
    robot_y = 0
    contatore = 0
    stringa = ''
    while True:
        t = ostacolo(immagine2,robot_x,robot_y,direzione)
        if t[0]:
            direzione = t[1]
            contatore += 1
            if contatore == 4:
                coloraBlu(immagine2, robot_x, robot_y)
                break
        else:
            contatore = 0
            if direzione == "destra":
                stringa += "0"
                for riga in range(40):
                    for colonna in range(40):
                        x = robot_x+colonna
                        y = robot_y+riga
                        immagine2[y][x] = verde
                robot_x += 40
            if direzione == "basso":
                stringa += "1"
                for riga in range(40):
                    for colonna in range(40):
                        x = robot_x+colonna
                        y = robot_y+riga
                        immagine2[y][x] = verde
                robot_y += 40
            if direzione == "sinistra":
                stringa += "2"
                for riga in range(40):
                    for colonna in range(40):
                        x = robot_x+colonna
                        y = robot_y+riga
                        immagine2[y][x] = verde
                robot_x -= 40
            if direzione == "alto":
                stringa += "3"
                for riga in range(40):
                    for colonna in range(40):
                        x = robot_x+colonna
                        y = robot_y+riga
                        immagine2[y][x] = verde
                robot_y -= 40
    save(immagine2, fname1)
    return stringa


def coloraBlu(immagine, x, y):
    for riga in range(40):
        for colonna in range(40):
            xt = x+colonna
            yt = y+riga
            immagine[yt][xt] = (0, 0, 255)
    return None


def width(immagine):
    return len(immagine[0])

def height(immagine):
    return len(immagine)

def ostacolo(immagine, x, y, direzione):
    if direzione == "destra":
        if x+40 <= width(immagine)-1:
            if immagine[y][x+40] == (255, 0, 0) or immagine[y][x+40] == (0, 255, 0):
                return (True, "basso")
            return (False, "destra")
        return (True, "basso")
    if direzione == "sinistra":
        if x-40 >= 0:
            if immagine[y][x-40] == (255, 0, 0) or immagine[y][x-40] == (0, 255, 0):
                return (True, "alto")
            return (False, "sinistra")
        return (True, "alto")
    if direzione == "alto":
        if y-40 >= 0:
            if immagine[y-40][x] == (255, 0, 0) or immagine[y-40][x] == (0, 255, 0):
                return (True, "destra")
            return (False, "alto")
        return (True, "destra")
    if direzione == "basso":
        if y+40 <= height(immagine)-1:
            if immagine[y+40][x] == (255, 0, 0) or immagine[y+40][x] == (0, 255, 0):
                return (True, "sinistra")
            return (False, "basso")
        return (True, "sinistra")
    return ()