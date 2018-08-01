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

def cammino(fname):
    
    img=load(fname)
    
    x=0
    y=0
    dire = 0
    s = ''

    
























def view(img, x, y, dire):
    if dire == 0:
        if (img[x][y+40] != (255, 0, 0) or img[x][y+40] != (0, 255, 0)) and y+40 in range(0, len(img[x])-1):
            return True
        else:
            return False
    if dire == 1:
        if img[x+40][y] != (255, 0, 0) and x+40 in range(0, len(img[0])-1):
            return True
        else:
            return False
    if dire == 2:
        if img[x][y-40] != (255, 0, 0) and y-40 in range(0, len(img[x])-1):
            return True
        else:
            return False
    if dire == 3:
        if img[x-40][y] != (255, 0, 0) and x-40 in range(0, len(img[0])-1):
            return True
        else:
            return False
    
                 
def square(img, x, y, dire):

    img1 = img

    if dire == 0:
        for px in range(x, x+40):
            for py in range(y+40, y+80):
                img1[px][py] = (0, 255, 0)

    if dire == 1:
        for px in range(x+40, x+80):
            for py in range(y, y+40):
                img1[px][py] = (0, 255, 0)

    if dire == 2:
        for px in range(x, x+40):
            for py in range(y-40, y):
                img1[px][py] = (0, 255, 0)

    if dire == 3:
        for px in range(x-40, x):
            for py in range(y, y+40):
                img1[px][py] = (0, 255, 0)

    return img1




       





    
        
        
            

    
