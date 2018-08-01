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

def inside(img, x, y):
    return 0 <= y < len(img) and 0 <= x < len(img[0])

def draw_rect(img, x, y, w, h, c):
    for px in range(x, x+w):
        for py in range(y, y+h):
            img[py][px] = c

def cammino(fname,  fname1):
    img = load(fname)
    x=40
    y=0
    draw_rect(img,0,0,40,40,(0,255,0))
    passi=''
    while True:
        cont1 = True
        for i in range(0,15):         #destra
            if inside(img,x,y) and (img[y][x] == (0,0,0) or img[y][x] == (255,255,255)):
                draw_rect(img,x,y,40,40,(0,255,0))
                x += 40
                passi += '0'
                stop1 = False
                cont1 = False
            else:
                x = x-40
                y += 40
                if cont1 == True:
                    stop1 = True
                break
        cont2 = True
        for i in range(0,15):                                                         #sotto
            if inside(img,x,y) and (img[y][x] == (0,0,0) or img[y][x] == (255,255,255)):
                draw_rect(img,x,y,40,40,(0,255,0))
                y += 40
                passi += '1'
                stop2 = False
                cont2 = False
            else:
                y = y-40
                x = x-40
                if cont2 == True:
                    stop2 = True
                break
        cont3 = True
        for i in range(0,15):                                                              #sinistra
            if inside(img,x,y) and (img[y][x] == (0,0,0) or img[y][x] == (255,255,255)):
                draw_rect(img,x,y,40,40,(0,255,0))
                x = x-40
                stop3 = False
                passi += '2'
                cont3 = False
            else:
                x += 40
                y = y-40
                if cont3 == True:
                    stop3 = True
                break
        cont4 = True
        for i in range(0,15):                                                                   #sopra
            if inside(img,x,y) and (img[y][x] == (0,0,0) or img[y][x] == (255,255,255)):
                draw_rect(img,x,y,40,40,(0,255,0))
                y = y-40
                stop4 = False
                passi += '3'
                cont4 = False
            else:
                y += 40
                x += 40
                if cont4 == True:
                    stop4 = True
                break
        if stop1 == True and stop2 == True and stop3 == True and stop4 == True:
            x = x-40
            draw_rect(img,x,y,40,40,(0,0,255))
            break
    save(img,fname1)
    return passi
            

    


    
    




