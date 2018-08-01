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

curr_x = 0
curr_y = 0
it_pos = 0
passi = [0,1,2,3]
s_passi = ""
lista_bad = [(255,0,0),(0,255,0),"out"]

def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    global it_pos
    global curr_x
    global curr_y
    global s_passi

    s_passi = ""
    it_pos=0
    curr_x=0
    curr_y=0
    img_temp = []
    prev_x = 0
    prev_y = 0
    cont_stop = 0
    h = 15
    w = 15
    img = riempi_nuova(fname,600,600)
    destra(img,h,w,cont_stop)
    img[curr_y][curr_x] = (0,0,255)
    save(conv_1to4(img),fname1)
    return s_passi

    
def riempi_nuova(fname,h,w):
    img_origin = load(fname)
    nuova = crea_nuova_fast((0,0,0),15)
    for y in range(0,w,40):
        for x in range(0,h,40):
            nuova[y//40][x//40] = img_origin[y][x]
    return nuova

def giu(img, h,w,cont_stop):
    global curr_x
    global curr_y
    global s_passi
    global lista_bad
    
    for y in range(curr_y,h+1):
        img[y][curr_x] = (0,255,0)
        pixel = getPixel(img,y+1,curr_x)
        if pixel in lista_bad:
            curr_y = y
            if cont_stop >4: return img
            cont_stop+=1
            img = sinistra(img,h,w,cont_stop)
            return img
        else:
            cont_stop = 0
            s_passi+=  "1"
            
    
def su(img, h,w,cont_stop):
    global curr_x
    global curr_y
    global s_passi
    global lista_bad
    
    for y in range(curr_y,-1,-1):
        img[y][curr_x] = (0,255,0)
        pixel = getPixel(img,y-1,curr_x)
        if pixel in lista_bad:
            curr_y = y
            if cont_stop >4: return img
            cont_stop+=1
            img =destra(img,h,w,cont_stop)
            return img
        else:
            cont_stop = 0
            s_passi+=  "3"
    
def sinistra(img, h,w,cont_stop):
    global curr_x
    global curr_y
    global s_passi
    global lista_bad
    
    for x in range(curr_x,-1,-1):
        img[curr_y][x] = (0,255,0)
        pixel = getPixel(img,curr_y,x-1)
        if pixel in lista_bad:
            curr_x = x
            if cont_stop >4: return img
            cont_stop+=1
            img =su(img,h,w,cont_stop)
            return img
        else:
            cont_stop = 0
            s_passi+=  "2"
    
def destra(img, h,w,cont_stop):
    global curr_x
    global curr_y
    global s_passi
    global lista_bad
    
    for x in range(curr_x,w+1):
        img[curr_y][x] = (0,255,0)
        pixel = getPixel(img,curr_y,x+1)
        if pixel in lista_bad:
            curr_x = x
            if cont_stop >4: return img
            cont_stop+=1
            img =giu(img,h,w,cont_stop)
            return img
        else:
            cont_stop = 0
            s_passi+=  "0"

def getPixel(img,y,x):
    if 0 <= x <= 14 and 0<=y<=14:
        return img[y][x]
    return "out"


def crea_nuova_fast(color,d):
    nuova = []
    for y in range(d): 
        nuova.append([color]*d)
    return nuova  


def conv_1to4(img):
    n_img = []
    for y in range(15):
        riga = []
        for x in range(15):
            riga.extend([img[y][x]]*40)    
        n_img.extend([riga]*40)
    return n_img
        
#img = crea_nuova_fast((200,200,200),600)
#print(id(img[10][10]),"--",id(img[20][10]))
#save(crea_nuova_fast((0,0,0),600),"aaa.png")
#cammino('I1.png','t1.png')

