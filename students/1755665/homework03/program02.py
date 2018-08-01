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

from immagini import load
from immagini import save


bianco=(255,255,255)
nero=(0,0,0)
rosso=(255,0,0)
blu=(0,0,255)
verde=(0,255,0)

dx=True
sx=True
dw=True
up=True

l=40


def width(img):
    '''larghezza immagine'''
    return len(img[0])

def height(img):
    '''Altezza immagine'''
    return len(img)

def inside(img, x, y):
    '''True se il pixel è
        nell'immagine'''
    iw, ih = width(img), height(img)
    return 0<=x<iw and 0<=y<ih

def draw_quad(img, x, y, w, h, c):
    '''Disegna un quadrato delle dimensioni
        e colore indicato nell posizione indicata'''
    for i in range(y,y+h):
        for j in range(x,x+w):
            if inside(img, j, i):
                img[i][j]=c

def is_color(img, x, y, c):
    '''controlla il colore'''
    return img[y][x]==c

def todx(img, x, y):
    '''cambia le variabili dx'''
    global dx
    if not(inside(img, x+l, y) and (is_color(img,x+l,y,bianco) or is_color(img,x+l,y,nero))):
        dx=False
    else:
        dx=True
    
def tosx(img, x, y):
    '''cambia le variabili sx'''
    global sx
    if not(inside(img, x-l, y) and (is_color(img,x-l,y,bianco) or is_color(img,x-l,y,nero))):
        sx=False
    else:
        sx=True

def todw(img, x, y):
    '''cambia le variabili dw'''
    global dw
    if not(inside(img, x, y+l) and (is_color(img,x,y+l,bianco) or is_color(img,x,y+l,nero))):
        dw=False
    else:
        dw=True

def toup(img, x, y):
    '''cambia le variabili up'''
    global up
    if not(inside(img, x, y-l) and (is_color(img,x,y-l,bianco) or is_color(img,x,y-l,nero))):
        up=False
    else:
        up=True
        
def draw_v(img, x, y):
    '''crea un quadrato vedre'''
    draw_quad(img, x, y, l, l, verde)

def draw_b(img, x, y):
    '''crea un quadrato blu'''
    draw_quad(img, x, y, l, l, blu)



def robot(img):
    r=0
    ret=''
    spost=0
    x=0
    y=0
    while r<4:
        if spost==0:
            todx(img,x,y)
            if dx:
                draw_v(img,x,y)
                x+=l
                r=0
                ret+=str(spost)
            else:
                spost+=1
                r+=1
        elif spost==1:
            todw(img,x,y)
            if dw:
                draw_v(img,x,y)
                y+=l
                r=0
                ret+=str(spost)
            else:
                spost+=1
                r+=1
        elif spost==2:
            tosx(img,x,y)
            if sx:
                draw_v(img,x,y)
                x-=l
                r=0
                ret+=str(spost)
            else:
                spost+=1
                r+=1
        else:
            toup(img,x,y)
            if up:
                draw_v(img,x,y)
                y-=l
                r=0
                ret+=str(spost)
            else:
                spost=0
                r+=1
    draw_b(img,x,y)
    return ret

def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    img = load(fname)
    s=robot(img)
    save(img, fname1)
    return s