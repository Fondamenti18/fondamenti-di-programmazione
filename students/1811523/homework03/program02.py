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
    def quad(x, y, s, color):
        for px in range(x, x+s):
            for py in range(y, y+s):
                try:
                    sca[py][px] = color
                except IndexError:
                    pass
    sca=load(fname)
    p=''
    c=''
    x=0
    y=0
    b=0
    w,h=len(sca[0]),len(sca)
    quad(0,0,40,(0,255,0))
    while sca[y][x]!=(0,0,255):
        x+=40
        if c=='' or c=='y2':
            while 0 <= x < w and 0 <= y < h and (sca[y][x]==(255,255,255) or sca[y][x]==(0,0,0)):
                quad(x,y,40,(0,255,0))
                p+='0'
                x+=40
                b=0
            if (x>=w and 0 <= y < h) or sca[y][x]==(255,0,0) or sca[y][x]==(0,255,0):
                x-=40
                c='x1'
                b+=1
        y+=40
        if c=='' or c=='x1':
            while 0 <= x < w and 0 <= y < h and (sca[y][x]==(255,255,255) or sca[y][x]==(0,0,0)):
                quad(x,y,40,(0,255,0))
                p+='1'
                y+=40
                b=0
            if (y>=h and 0 <= x < w) or sca[y][x]==(255,0,0) or sca[y][x]==(0,255,0):
                y-=40
                c='y1'
                b+=1
        x-=40
        if c=='' or c=='y1':
            while 0 <= x < w and 0 <= y < h and (sca[y][x]==(255,255,255) or sca[y][x]==(0,0,0)):
                quad(x,y,40,(0,255,0))
                p+='2'
                x-=40
                b=0
            if (x<0 and 0 <= y < h) or sca[y][x]==(255,0,0) or sca[y][x]==(0,255,0):
                x+=40
                c='x2'
                b+=1
        y-=40
        if c=='' or c=='x2':
            while 0 <= x < w and 0 <= y < h and (sca[y][x]==(255,255,255) or sca[y][x]==(0,0,0)):
                quad(x,y,40,(0,255,0))
                p+='3'
                y-=40
                b=0
            if (y<0 and 0 <= x < w) or sca[y][x]==(255,0,0) or sca[y][x]==(0,255,0):
                y+=40
                c='y2'
                b+=1
        if b>=4 or b==0:
            quad(x,y,40,(0,0,255))
    save(sca,fname1)
    return p