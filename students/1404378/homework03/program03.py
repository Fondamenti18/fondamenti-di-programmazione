'''

Definiamo adiacenti di un pixel p di un immagine i pixel adiacenti a p in  orizzontale o in  verticale.
Se un pixel e' sul bordo dell'immagine il suo vicinato non comprende i pixel non contenuti nell'immagine.
Il pixel dell'immagine con coordinate(x,y) ha dunque come adiacenti i pixel   
con coordinate (x-1,y),(x+1,y),(x,y-1),(x,y+1) appartenenti all'immagine. 
 
Definiamo connessi due pixel se e' possibile dall'uno raggiungere l'altro spostandosi solo su   
pixel adiacenti e dello stesso colore (ovviamente perche' cio' sia possobile e' necessario 
che i due pixel abbiano lo stesso colore).

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una funzione ricolora(fname, lista,  fnameout) che presi:
- il percorso di un file che contiene un'immagine in formato PNG
- una lista di quadruple del tipo (x,y,c1,c2) dove  x e y sono coordinate di un pixel dell'immagine e c1 e c2 due triple colore RGB
- il percorso di un file (fnameout) da creare
legge l'immagine in fname, esegue un'operazione di ricolorazione di alcuni pixel dell'immagine e 
registra l'immagine ricolorata nel file fnameout.

L'operazione di ricolorazione e' la seguente. Per ciascuna delle quadruple (x,y,c1,c2) della lista (nell'ordine), 
- tutti i pixel connessi al pixel  di coordinate (x,y) nell'immagine vanno ricolorati col colore c1, 
- tutti i pixel del perimetro (che si trovano sul 'bordo') della zona che si e' appena colorata devono essere ricolorati col colore c2.
Il perimetro della zona colorata è l'insieme dei pixel che non hanno tutti e 4 i vicini che fanno parte della zona ricolorata 
(ovvero almeno uno è di un colore diverso da quello che si sta ricolorando oppure almeno uno non esiste perchè sarebbe fuori dall'immagine)

Si consideri ad esempio l'immagine 'I1.png', l'invocazione di ricolora('I1.png',[(10,10,(255,0,0), (0,0,255))],’OUT1.png')
produrra' l'immagine 'OUT1.png' identica all'immagine di partenza se non per il fatto che,
 tutti i pixel adiacenti al pixel di coordinate (10,10) (e di colore verde), verranno ricolorati 
 di rosso ((255,0,0)), mentre i pixel sul bordo della zona inizialmente verde vengono ricolorati di blu.

Per ciascuna area ricolorata bisogna inoltre calcolare area interna e perimetro, che sono definite come segue:
- l'area interna e' il numero di pixel ricolorati con il colore c1
- il perimetro è il numero di pixel ricolorati con il colore c2

La funzone deve tornare la lista di coppie (area interna, perimetro) nello stesso ordine in cui sono state colorate le aree.
 
Per altri  esempi vedere il file grade03.txt 
'''

from immagini import *
from collections import deque


def width(img):
    return len(img[0])

def height(img):
    return len(img)

def is_inside(col, riga, im):
    return 0 <= col < width(im) and 0 <= riga < height(im)

def check_right(x, y, img):
    return is_inside(x+1, y, img) and img[y][x+1] == img[y][x] 

def check_left(x, y, img):
    return is_inside(x-1, y, img) and img[y][x-1] == img[y][x] 

def check_up(x, y, img):
    return is_inside(x, y-1, img) and img[y-1][x] == img[y][x]  

def check_down(x, y, img):
    return is_inside(x, y+1, img) and img[y+1][x] == img[y][x] 

def check_dirs(x, y, img):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in dirs:
        if not ((is_inside(x+dx, y+dy, img) and img[y+dy][x+dx] == img[y][x])):
            return False
    return True

def colora(img, coord, c):
    for x, y in coord:
        img[y][x] = c  
        
def scan(x, y, c1, c2, img):
    queue = deque([])
    queue.append((x, y))
    temp = set()
    temp_conn = set()
    while queue:
        col, riga = queue.popleft()
        if not check_dirs(col, riga, img):
            temp_conn.add((col, riga))
        if check_right(col, riga, img) and (col+1, riga) not in temp:
            queue.append((col+1, riga))
            temp.add((col+1, riga))
        if check_left(col, riga, img) and (col-1, riga) not in temp:
            queue.append((col-1, riga))
            temp.add((col-1, riga))
        if check_down(col, riga, img) and (col, riga+1) not in temp:
            queue.append((col, riga+1))
            temp.add((col, riga+1))
        if check_up(col, riga, img) and (col, riga-1) not in temp:
            queue.append((col, riga-1))
            temp.add((col, riga-1)) 
    return temp, temp_conn
                
def ricolora(fname, lista, fnameout):
    img = load(fname)
    #queue = deque([])
    visited = []
    not_conn = []
    ret = []    
    for x, y, c1, c2 in lista:
        temp, temp_conn = scan(x, y, c1, c2, img)
        colora(img, temp, c1)
        colora(img, temp_conn, c2)
        visited.extend(temp)
        not_conn.extend(temp_conn)    
        ret.append((len(temp) - len(temp_conn) \
                        if len(temp) > len(temp_conn) else 0, \
                        len(temp_conn)))
    save(img, fnameout)
    return ret


