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
import png

rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)

def Passi(img, x, y, lato, c):
    for px in range(x, x+lato):
        for py in range(y, y+lato):
            img[py][px] = c

def cammino(fname,  fname1):
    img=load(fname)
    direzione='0'
    percorso=''
    x_robot=0
    y_robot=0
    controllo=0
    while controllo<5:
            while direzione=='0':
                try:
                    if img[y_robot][x_robot+40]!=rosso and img[y_robot][x_robot+40]!=verde:
                        Passi(img, x_robot, y_robot, 40, verde)
                        x_robot=x_robot+40
                        percorso+='0'
                        controllo=0
                    else:
                        direzione='1'
                        controllo+=1
                except IndexError:
                    direzione='1'
                    controllo+=1
        
            while direzione=='1':
                try:
                    if img[y_robot+40][x_robot]!=rosso and img[y_robot+40][x_robot]!=verde:
                        Passi(img, x_robot, y_robot, 40, verde)
                        y_robot=y_robot+40
                        percorso+='1'
                        controllo=0
                    else:
                        direzione='2'
                        controllo+=1
                except IndexError:
                    direzione='2'
                    controllo+=1
                    
            while direzione=='2':
                try:
                    if img[y_robot][x_robot-40]!=rosso and img[y_robot][x_robot-40]!=verde and x_robot-40>=0:
                        Passi(img, x_robot, y_robot, 40, verde)
                        x_robot=x_robot-40
                        percorso+='2'
                        controllo=0
                    else:
                        direzione='3'
                        controllo+=1
                except IndexError:
                    direzione='3'
                    controllo+=1
                    
            while direzione=='3':
                try:
                    if img[y_robot-40][x_robot]!=rosso and img[y_robot-40][x_robot]!=verde and y_robot-40>=0:
                        Passi(img, x_robot, y_robot, 40, verde)
                        y_robot=y_robot-40
                        percorso+='3'
                        controllo=0
                    else:
                        direzione='0'
                        controllo+=1
                except IndexError:
                    direzione='0'
                    controllo+=1
    if controllo>4:
        Passi(img, x_robot, y_robot, 40, blu)
    save(img, fname1)
    return percorso

