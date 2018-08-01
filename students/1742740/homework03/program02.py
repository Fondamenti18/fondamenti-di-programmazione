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

def disegna_quadrato(img,x,y,h,w,c):#angolo in alto dx (x,y),(h,w)dimensioni quadrato , c colore
    for px in range(x,x+w):
        for py in range(y,y+h):
            if inside(img,px,py):
                img[py][px]=c

def inside(img,x,y):
    return 0<=y<len(img) and 0<=x<len(img[0])

def step(img,x,y,dir): #funzione che sceglie la direzione in cui si muove e colora la casella
    nero = (0, 0, 0)
    bianco = (255, 255, 255)
    verde = (0, 255, 0)
    blu = (0, 0, 255)
    if dir==0:
        if inside(img,x+40,y) and (img[y][x+40]==bianco or img[y][x+40]==nero):
            disegna_quadrato(img,x+40,y,40,40,verde)
            return 0
        if inside(img,x,y+40) and (img[y+40][x]==bianco or img[y+40][x]==nero):
            disegna_quadrato(img,x,y+40,40,40,verde)
            return 1
        if inside(img,x-40,y) and (img[y][x-40]==bianco or img[y][x-40]==nero):
            disegna_quadrato(img,x-40,y,40,40,verde)
            return 2
        if inside(img,x,y-40) and (img[y-40][x]==bianco or img[y-40][x]==nero):
            disegna_quadrato(img,x,y-40,40,40,verde)
            return 3
        else:
            disegna_quadrato(img,x,y,40,40,blu)
            return 4
    elif dir==1:
        if inside(img,x,y+40) and (img[y+40][x]==bianco or img[y+40][x]==nero):
            disegna_quadrato(img,x,y+40,40,40,verde)
            return 1
        if inside(img,x-40,y) and (img[y][x-40]==bianco or img[y][x-40]==nero):
            disegna_quadrato(img,x-40,y,40,40,verde)
            return 2
        if inside(img,x,y-40) and (img[y-40][x]==bianco or img[y-40][x]==nero):
            disegna_quadrato(img,x,y-40,40,40,verde)
            return 3
        if inside(img,x+40,y) and (img[y][x+40]==bianco or img[y][x+40]==nero):
            disegna_quadrato(img,x+40,y,40,40,verde)
            return 0
        else:
            disegna_quadrato(img,x,y,40,40,blu)
            return 4
    elif dir==2:
        if inside(img,x-40,y) and (img[y][x-40]==bianco or img[y][x-40]==nero):
            disegna_quadrato(img,x-40,y,40,40,verde)
            return 2
        if inside(img,x,y-40) and (img[y-40][x]==bianco or img[y-40][x]==nero):
            disegna_quadrato(img,x,y-40,40,40,verde)
            return 3
        if inside(img,x+40,y) and (img[y][x+40]==bianco or img[y][x+40]==nero):
            disegna_quadrato(img,x+40,y,40,40,verde)
            return 0
        if inside(img,x,y+40) and (img[y+40][x]==bianco or img[y+40][x]==nero):
            disegna_quadrato(img,x,y+40,40,40,verde)
            return 1
        else:
            disegna_quadrato(img,x,y,40,40,blu)
            return 4
    elif dir==3:
        if inside(img,x,y-40) and (img[y-40][x]==bianco or img[y-40][x]==nero):
            disegna_quadrato(img,x,y-40,40,40,verde)
            return 3
        if inside(img,x+40,y) and (img[y][x+40]==bianco or img[y][x+40]==nero):
            disegna_quadrato(img,x+40,y,40,40,verde)
            return 0
        if inside(img,x,y+40) and (img[y+40][x]==bianco or img[y+40][x]==nero):
            disegna_quadrato(img,x,y+40,40,40,verde)
            return 1
        if inside(img, x - 40, y) and (img[y][x - 40] == bianco or img[y][x - 40] == nero):
            disegna_quadrato(img, x - 40, y, 40, 40, verde)
            return 2
        else:
            disegna_quadrato(img,x,y,40,40,blu)
            return 4

def cammino(fname,  fname1):
    img=load(fname)
    verde=(0,255,0)
    x=0
    y=0
    dir=0
    stringa=''
    disegna_quadrato(img,0,0,40,40,verde)
    while dir<4: #sposta finche puo
        dir=step(img,x,y,dir)
        if dir==0:
            x=x+40
            stringa+='0'
        elif dir==1:
            y=y+40
            stringa+='1'
        elif dir==2:
            x=x-40
            stringa+='2'
        elif dir==3:
            y=y-40
            stringa+='3'
    save(img,fname1)
    return stringa

