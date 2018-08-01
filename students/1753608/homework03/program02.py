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
    img = load(fname)
    passed = []
    green = (0,255,0)
    blue = (0,0,255)
    x = 0
    y = 0
    i = 0
    start_i = 0
    directions = ["right","down","left","up"]
    walk = ""
    draw_fn = draw(img,passed,y,x,green)
    img = draw_fn[0]
    passed = draw_fn[1]
    while(True):
        i = check(img,passed,y,x,directions,i,start_i)
        start_i = i
        direction = directions[i]
        if(i == -1):
            draw_fn = draw(img,passed,y,x,blue)
            img = draw_fn[0]
            passed = draw_fn[1]
            break
        up = update(y,x,direction)
        y = up[0]
        x = up[1]
        draw_fn = draw(img,passed,y,x,green)
        img = draw_fn[0]
        passed = draw_fn[1]
        walk += str(i)
    save(img,fname1)
    return walk

def draw(img,passed,y,x,color):
    start_x = x
    max_y = y+40
    max_x = x+40
    while(y < max_y):
        while(x < max_x):
            img[y][x] = color
            passed.append((y,x))
            x+=1
        y+=1
        x = start_x
    return img,passed

def get_index(i):
    return i % 4

def update(y,x,direction):
    if(direction == "right"):
        x+=40
    elif(direction == "down"):
        y+=40
    elif(direction == "left"):
        x-=40
    elif(direction == "up"):
        y-=40
    return y,x

def check(img,passed,y,x,directions,i,start_i):
    i = get_index(i)
    up = update(y,x,directions[i])
    start_x = x
    start_y = y
    y = up[0]
    x = up[1]
    try:
        if(x < 0 or y < 0):
            next_one = (255,0,0)
        else:
            next_one = img[y][x]
    except:
        next_one = (255,0,0)
        pass
    if(next_one != (255,0,0) and
       (y,x) not in passed ):
        return i
    else:
        i = get_index(i+1)
    if(get_index(i) == start_i): return -1
    return check(img,passed,start_y,start_x,directions,i,start_i)
