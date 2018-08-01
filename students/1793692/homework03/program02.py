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
from immagini import load,save

def cammino(fname,  fname1):
    img=load(fname)
    rosso=(255, 0, 0)
    verde=(0, 255, 0)
    blu=(0, 0, 255)
    bianco=(255, 255, 255)
    nero=(0, 0, 0)
    flag=0
    x=0
    y=0
    listapassi=[]
    while flag!=1:
        des=0
        while des!=1:
            if intorno(img,x,y):
                quadrato(img,x,y,40,40,blu)
                flag=1
            if destra(img,x,y):
                 quadrato(img,x,y,40,40,verde)
                 x+=40
                 listapassi.append('0')
            else:
                des=1
        bas=0
        while bas!=1:
            if intorno(img,x,y):
                quadrato(img,x,y,40,40,blu)
                flag=1
            if basso(img,x,y):
                 quadrato(img,x,y,40,40,verde)
                 y+=40
                 listapassi.append('1')
            else:
                bas=1
        sin=0
        while sin!=1:
            if intorno(img,x,y):
                quadrato(img,x,y,40,40,blu)
                flag=1
            if sinistra(img,x,y):
                 quadrato(img,x,y,40,40,verde)
                 x-=40
                 listapassi.append('2')
            else:
                sin=1
        alt=0
        while alt!=1:
            if intorno(img,x,y):
                quadrato(img,x,y,40,40,blu)
                flag=1
            if alto(img,x,y):
                 quadrato(img,x,y,40,40,verde)
                 y-=40
                 listapassi.append('3')
            else:
                alt=1
    save(img,fname1)
    return ''.join(listapassi)



def quadrato(img, x, y, w, h, c):
    for j in range(y, y+h):
        for i in range(x, x+w):
            img[j][i] = c

def inside(img, x, y):
    return 0 <= y < len(img[1]) and 0 <= x < len(img[0])

def intorno(img,x,y):
    cont=0
    rosso=(255, 0, 0)
    verde=(0, 255, 0)
    try:
        if img[y][x+40]==rosso or img[y][x+40]==verde or not inside(img,x+40,y):
            cont+=1
        if img[y+40][x]==rosso or img[y+40][x]==verde or not inside(img,x,y+40):
            cont+=1
        if img[y][x-40]==rosso or img[y][x-40]==verde or not inside(img,x-40,y):
            cont+=1
        if img[y-40][x]==rosso or img[y-40][x]==verde or not inside(img,x,y-40):
            cont+=1
        if cont==4:
            return True
        if cont!=4:
            return False
    except IndexError:
        pass
def destra(img,x,y):
    bianco=(255, 255, 255)
    nero=(0, 0, 0)
    try:
        if img[y][x+40]==bianco and inside(img,x+40,y) or img[y][x+40]==nero and inside(img,x+40,y) :
            return True
        return False
    except IndexError:
        pass
def basso(img,x,y):
    bianco=(255, 255, 255)
    nero=(0, 0, 0)
    try:
        if img[y+40][x]==bianco and inside(img,x,y+40) or img[y+40][x]==nero and inside(img,x,y+40):
            return True
        return False
    except IndexError:
        pass
def sinistra(img,x,y):
    bianco=(255, 255, 255)
    nero=(0, 0, 0)
    try:
        if img[y][x-40]==bianco and inside(img,x-40,y) or img[y][x-40]==nero and inside(img,x-40,y):
            return True
        return False
    except IndexError:
        pass   
def alto(img,x,y):
    bianco=(255, 255, 255)
    nero=(0, 0, 0)
    try:
        if img[y-40][x]==bianco and inside(img,x,y-40) or img[y-40][x]==nero and inside(img,x,y-40):
            return True
        return False
    except IndexError:
        pass
