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
def colora_sqr(img,x,y,l,c):
    for cy in range(y,y+l):
        for cx in range(x,x+l):
            img[cy][cx] = c 

def cammino(fname,  fname1):
    file= load(fname)
    ultimopasso = 0
    string= ''
    x,y = 0,0
    rosso,verde,blu = (255,0,0),(0,255,0),(0,0,255)
    xymax=len(file)-1
    l=40
    counter=0
    while True:
        counter=0
        if ultimopasso == 0:
            if x+40 > xymax or (file[y][x+40] == rosso or file[y][x+40] == verde) :
                ultimopasso += 1
                ultimopasso %= 4
                counter += 1
            else:
                colora_sqr(file,x,y,l,verde)
                x += 40
                string += str(ultimopasso)
                continue


        if ultimopasso == 1:
            if y + 40 >= xymax or (file[y+40][x] == rosso or file[y+40][x] == verde) :
                    ultimopasso += 1
                    ultimopasso %= 4
                    counter += 1
            else:
                colora_sqr(file,x,y,l,verde)
                y += 40
                string += str(ultimopasso)
                continue

        if ultimopasso == 2:
            if x-40 < 0 or (file[y][x-40] == rosso or file[y][x-40] == verde):
                    ultimopasso += 1
                    ultimopasso %= 4
                    counter += 1
            else:
                colora_sqr(file,x,y,l,verde)
                x -= 40
                string += str(ultimopasso)
                continue
       
        if ultimopasso == 3:
            if y-40 < 0 or (file[y-40][x] == rosso or file[y-40][x] == verde):
                    ultimopasso += 1
                    ultimopasso %= 4
                    counter += 1
            else:
                colora_sqr(file,x,y,l,verde)
                y -= 40
                string += str(ultimopasso)
                continue
        if counter == 4:
            colora_sqr(file,x,y,l,blu)
            break
    save(file,fname1)
    return string


