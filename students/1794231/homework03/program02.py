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
    percorso=load(fname)
    direzione=0
    pos=[0, 0]
    mov=''
    f=0
    while f!=4:
        if direzione==0:
            try:
                if percorso[pos[0]][pos[1]+40] == (0, 0, 0) or percorso[pos[0]][pos[1]+40] == (255, 255, 255):
                    draw_rect(percorso, pos[1], pos[0], 40, 40, (0, 255, 0))
                    pos[1]=pos[1]+40
                    f=0
                    mov=mov+'0'
                else:
                    f+=1
                    direzione=1
            except IndexError:
                f+=1
                direzione=1
        elif direzione==3:
            if (pos[0]-40)>=0:
                if percorso[pos[0]-40][pos[1]] == (0, 0, 0) or percorso[pos[0]-40][pos[1]] == (255, 255, 255):
                    draw_rect(percorso, pos[1], pos[0], 40, 40, (0, 255, 0))
                    pos[0]=pos[0]-40
                    f=0
                    mov=mov+'3'
                else:
                    f+=1
                    direzione=0
            else:
                f+=1
                direzione=0
        elif direzione==2:
            if (pos[1]-40)>=0:
                if percorso[pos[0]][pos[1]-40] == (0, 0, 0) or percorso[pos[0]][pos[1]-40] == (255, 255, 255):
                    draw_rect(percorso, pos[1], pos[0], 40, 40, (0, 255, 0))
                    pos[1]=pos[1]-40
                    f=0
                    mov=mov+'2'
                else:
                    f+=1
                    direzione=3
            else:
                f+=1
                direzione=3
        elif direzione==1:
            try:
                if percorso[pos[0]+40][pos[1]] == (0, 0, 0) or percorso[pos[0]+40][pos[1]] == (255, 255, 255):
                    draw_rect(percorso, pos[1], pos[0], 40, 40, (0, 255, 0))
                    pos[0]=pos[0]+40
                    f=0
                    mov=mov+'1'
                else:
                    f+=1
                    direzione=2
            except IndexError:
                f+=1
                direzione=2
    draw_rect(percorso, pos[1], pos[0], 40, 40, (0, 0, 255))
    save(percorso, fname1)
    return mov
def draw_rect(img, x, y, w, h, color):
    for px in range(x, x+w):
        for py in range(y, y+h):
            try:
                 img[py][px] = color
            except IndexError:
                pass
    return (img)

