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
    scacchiera=matrix_init(17,17)
    immagine=load(fname)
    creaScacchieraOmbra(immagine, scacchiera)
    dir=0
    x=1
    y=1
    scacchiera[x][y]=1
    listaDirezioni=""
    draw_rect(immagine, (x-1)*40, (y-1)*40, 40, 40, (0, 255, 0))
    while True:
        xf, yf, newdir = muovi(x,y,dir,scacchiera)
        if x == xf and y==yf :
                draw_rect(immagine, (x-1)*40, (y-1)*40, 40, 40, (0, 0, 255))
                save(immagine, fname1)
                break
        else:
                listaDirezioni+=str(newdir)
                draw_rect(immagine, (xf-1)*40, (yf-1)*40, 40, 40, (0, 255, 0))
                x=xf
                y=yf
                dir=newdir
    return listaDirezioni

def matrix_init(m, n):
    return [[1] * n for i in range(m)]

def creaScacchieraOmbra(immagine, matrice):
        for r in range (0, 600, 40):
                for c in range (0,600,40):
                    if immagine[r][c] != (255, 0, 0):
                        matrice[r//40+1][c//40+1] = 0


def applicaDirezione(x0, y0, dir):
        if dir==0:
                x=x0+1
                y=y0
        else:
                if dir == 1:
                    x=x0
                    y=y0+1
                else:
                    if dir==2:
                        x=x0-1
                        y=y0
                    else:
                        x=x0
                        y=y0-1
        return (x,y)

def muovi(x0,y0,dir,matrix):
        for i in range(1,5):
            x,y=applicaDirezione(x0, y0, dir)
            if matrix[y][x] == 0:
                matrix[y][x] = 1
                break
            else:
                dir=(dir+1)%4
                x=x0
                y=y0
        return (x,y,dir)


def draw_rect(img, x, y, w, h, color):
        for px in range(x, x+w):
            for py in range(y, y+h):
                try:
                    img[py][px] = color
                except IndexError:
                    pass


