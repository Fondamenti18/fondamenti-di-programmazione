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

def load(filename):
    with open(filename,mode='rb') as f:
        r=png.Reader(file=f)
        iw,ih,png_img,_=r.asRGB8()
        img=[]
        for png_row in png_img:
            row=[]
            for i in range(0,len(png_row),3):
                row.append((png_row[i+0],
                            png_row[i+1],
                            png_row[i+2]))
            img.append(row)
    return img,iw,ih

def create(iw,ih,fname):
    img=[]
    for i in range(ih):
        row=[]
        for j in range(iw):
            row.append(fname[i][j])
        img.append(row)
    return img

def save(filename,img):
    pngimg=png.from_array(img,'RGB')
    pngimg.save(filename)

def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    fname,iw,ih=load(fname)
    img=create(iw,ih,fname)
    cont2=0
    x=0
    y=0
    cmdl=[(0,40),(40,0),(0,-40),(-40,0)]
    cmd=0
    stringa=''
    while cont2<=4:
        h,k=cmdl[cmd]
        if x+h>len(img)-1 or x+h<0 or y+k>len(img[0])-1 or y+k<0 or img[x+h][y+k]==(255,0,0) or img[x+h][y+k]==(0,255,0):
            cont2+=1
            cmd+=1
            if cmd==4:
                cmd=0
            if cont2==4:
                for i in range(x,x+40):
                    for j in range(y,y+40):
                        img[i][j]=(0,0,255)
                cont2+=1
        elif img[x+h][y+k]!=(255,0,0) or img[x+h][y+k]!=(0,255,0):
            stringa+=str(cmd)
            for i in range(x,x+40):
                for j in range(y,y+40):
                    img[i][j]=(0,255,0)
            x=x+h
            y=y+k
            cont2=0
    save(fname1,img)
    return stringa