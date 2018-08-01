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
    lstImg = load(fname)
    x,y=0,0
    lbEnd=False
    lstMov=[[x,y]]
    direz='E'
    acc=0
    string = ''
    while(lbEnd==False):
        ver,acc=checkT(lstMov,lstImg,[x,y],direz,acc)
        if ver=='yes':
            x,y,lstMov,lstImg,string=move(direz,[x,y],lstMov,lstImg,string)
        elif ver =='no':
            blue(lstImg,x,y)
            lbEnd=True
        else:
            direz=ver        
    save(lstImg,fname1)
    return string
def checkT(lst,img,lstCoord,direzione,accDir):
    if accDir > 3:
        return 'no',0
    x=lstCoord[0]
    y=lstCoord[1]
    red = (255,0,0)
    if direzione =='E':
        #inside
        if insideImg(img,x+40,y)and [y,x+40] not in lst and img[y][x+40] != red:
            return 'yes',0
        else:
            return change(direzione),accDir+1
    elif direzione =='S':
        #inside
        if insideImg(img,x,y+40) and [y+40,x] not in lst and img[y+40][x] != red:
            return 'yes',0
        else:
            return change(direzione),accDir+1
    elif direzione =='W':
        #inside
        if insideImg(img,x-40,y) and [y,x-40] not in lst and img[y][x-40] != red:
            return 'yes',0
        else:
            return change(direzione),accDir+1
    elif direzione =='N':
        #inside
        if insideImg(img,x,y-40) and [y-40,x] not in lst and img[y-40][x] != red:
            return 'yes',0
        else:
            return change(direzione),accDir+1
        
def move(direzione,lstCoord,lstMov,img,string):
    x,y=lstCoord[0],lstCoord[1]
    if direzione == 'E':
        for h in range(0,40):
            for j in range(0,40):
                img[y+h][x+j]=(0,255,0)
        lstMov.append([y,x+40])
        return x+40,y,lstMov,img,string+'0'
    elif direzione == 'S':
        for h in range(0,40):
            for j in range(0,40):
                img[y+h][x+j]=(0,255,0)
        lstMov.append([y+40,x])
        return x,y+40,lstMov,img,string+'1'
    elif direzione == 'W':
        for h in range(0,40):
            for j in range(0,40):
                img[y+h][x+j]=(0,255,0)
        lstMov.append([y,x-40])
        return x-40,y,lstMov,img,string+'2'
    elif direzione == 'N':
        for h in range(0,40):
            for j in range(0,40):
                img[y+h][x+j]=(0,255,0)
        lstMov.append([y-40,x])
        return x,y-40,lstMov,img,string+'3'
    
def change(direzione):
    if direzione == 'E':
        return 'S'
    elif direzione == 'S':
        return 'W'
    elif direzione =='W':
        return 'N'
    elif direzione == 'N':
        return 'E'
    
def blue(img,x,y):
    blu=[0,0,255]
    for h in range(0,40):
        for j in range(0,40):
            img[y+h][x+j]=blu
    return img

def insideImg(img,x,y):
    return 0 <= y < rows(img) and 0<=x<columns(img)

def rows(img):
    return len(img)

def columns(img):
    return len(img[0])