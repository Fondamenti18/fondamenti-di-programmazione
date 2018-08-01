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
    img=load(fname)
    passi=''
    verso,y,x=0,0,0
    stop=False
    while stop==False:
        img=colora(img,y,x,(0,255,0))
        if verso==0:
            y,x,passi,verso,stop=dx(img,y,x,passi)
        elif verso==1:
            y,x,passi,verso,stop=down(img,y,x,passi)
        elif verso==2:
            y,x,passi,verso,stop=sx(img,y,x,passi)
        elif verso==3:
            y,x,passi,verso,stop=up(img,y,x,passi)
    img=colora(img,y,x,(0,0,255))
    save(img, fname1)
    return passi

def inside(img,y,x):
    return 0<=y<len(img) and 0<=x<len(img[0])

def colora(img,y,x,c):
    for py in range(y*40,(y+1)*40):
            for px in range(x*40,(x+1)*40):
                img[py][px]=c
    return img

def dx(img,y,x,passi,verso=0,stop=False):
    if inside(img,y*40,(x+1)*40) and img[y*40][(x+1)*40]!=(255,0,0) and img[y*40][(x+1)*40]!=(0,255,0):
        x+=1
        passi+='0'
    elif inside(img,(y+1)*40,x*40) and img[(y+1)*40][x*40]!=(255,0,0) and img[(y+1)*40][x*40]!=(0,255,0):
        y+=1
        passi+='1'
        verso=1
    elif inside(img,y*40,(x-1)*40) and img[y*40][(x-1)*40]!=(255,0,0) and img[y*40][(x-1)*40]!=(0,255,0):
        x-=1
        passi+='2'
        verso=2
    elif inside(img,(y-1)*40,x*40) and img[(y-1)*40][x*40]!=(255,0,0) and img[(y-1)*40][x*40]!=(0,255,0):
        y-=1
        passi+='3'
        verso=3
    else: stop=True
    return y,x,passi,verso,stop

def down(img,y,x,passi,verso=1,stop=False):
    if inside(img,(y+1)*40,x*40) and img[(y+1)*40][x*40]!=(255,0,0) and img[(y+1)*40][x*40]!=(0,255,0):
        y+=1
        passi+='1'
    elif inside(img,y*40,(x-1)*40) and img[y*40][(x-1)*40]!=(255,0,0) and img[y*40][(x-1)*40]!=(0,255,0):
        x-=1
        passi+='2'
        verso=2
    elif inside(img,(y-1)*40,x*40) and img[(y-1)*40][x*40]!=(255,0,0) and img[(y-1)*40][x*40]!=(0,255,0):
        y-=1
        passi+='3'
        verso=3
    elif inside(img,y*40,(x+1)*40) and img[y*40][(x+1)*40]!=(255,0,0) and img[y*40][(x+1)*40]!=(0,255,0):
        x+=1
        passi+='0'
        verso=0
    else: stop=True
    return y,x,passi,verso,stop

def sx(img,y,x,passi,verso=2,stop=False):
    if inside(img,y*40,(x-1)*40) and img[y*40][(x-1)*40]!=(255,0,0) and img[y*40][(x-1)*40]!=(0,255,0):
        x-=1
        passi+='2'
    elif inside(img,(y-1)*40,x*40) and img[(y-1)*40][x*40]!=(255,0,0) and img[(y-1)*40][x*40]!=(0,255,0):
        y-=1
        passi+='3'
        verso=3
    elif inside(img,y*40,(x+1)*40) and img[y*40][(x+1)*40]!=(255,0,0) and img[y*40][(x+1)*40]!=(0,255,0):
        x+=1
        passi+='0'
        verso=0
    elif inside(img,(y+1)*40,x*40) and img[(y+1)*40][x*40]!=(255,0,0) and img[(y+1)*40][x*40]!=(0,255,0):
        y+=1
        passi+='1'
        verso=1
    else: stop=True
    return y,x,passi,verso,stop

def up(img,y,x,passi,verso=3,stop=False):
    if inside(img,(y-1)*40,x*40) and img[(y-1)*40][x*40]!=(255,0,0) and img[(y-1)*40][x*40]!=(0,255,0):
        y-=1
        passi+='3'
    elif inside(img,y*40,(x+1)*40) and img[y*40][(x+1)*40]!=(255,0,0) and img[y*40][(x+1)*40]!=(0,255,0):
        x+=1
        passi+='0'
        verso=0
    elif inside(img,(y+1)*40,x*40) and img[(y+1)*40][x*40]!=(255,0,0) and img[(y+1)*40][x*40]!=(0,255,0):
        y+=1
        passi+='1'
        verso=1
    elif inside(img,y*40,(x-1)*40) and img[y*40][(x-1)*40]!=(255,0,0) and img[y*40][(x-1)*40]!=(0,255,0):
        x-=1
        passi+='2'
        verso=2
    else: stop=True
    return y,x,passi,verso,stop
