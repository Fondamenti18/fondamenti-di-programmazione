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

import sys
sys.setrecursionlimit(25000)

from immagini import *
    
def ricolora(fname, lista, fnameout):
    import immagini
    img = immagini.load(fname)
    h = len(img)
    l = len(img[0])
    out = clone_image(img, h, l) # inizializzo out con una copia dell'immagine
    npoints = len(lista)
    ret = []
    for i in range(npoints): # loop su tutti i punti in lista
        pair = []
        pair += [0] # inizializzo area a 0
        pair += [0] # inizializzo perimetro a 0
        mask = empty_mask(h, l) # creo una maschera vuota per salvare i pixel già ispezionati dalla funzione colora, per non passare più volte dallo stesso pixel
        x,y,c1,c2 = lista[i]
        colora(img, out, mask, h, l, x, y, img[y][x], c1, c2, pair) # coloro i pixel connessi al pixel x,y
        ret += [(pair[0], pair[1])] # aggiungo area e perimetro ai risultati
        img = clone_image(out, h, l) # assegno all'immagine attuale quella in output dalla colorazione
    immagini.save(out, fnameout)
    return ret

def empty_mask(h, l):
    mask = []
    for i in range(h):
        maskrow = []
        for j in range(l):
            maskrow+=[0]
        mask+=[maskrow]
    return mask

def clone_image(img, h, l):
    out = []
    for i in range(h):
        outrow = []
        for j in range(l):
            outrow+=[img[i][j]]
        out+=[outrow]
    return out


def colora(img, out, mask, h, l, x, y, c, c1, c2, pair): # funzione ricorsiva che controlla i punti vicini e aggiorna il colore del pixel
    if x >= l or x < 0 or y >= h or y < 0: # sono fuori dall'immagine
        return 0
    if img[y][x] != c: # il colore non è quello cercato
        return 0
    if mask[y][x] != 0: # la maschera indica che ho già ispezionato questo pixel
        return 1
    mask[y][x] = 1 # imposto questo pixel nella maschera come già ispezionato per non tornarci
    # controllo i pixel vicini nelle 4 direzioni
    cl = colora(img, out, mask, h, l, x-1, y, c, c1, c2, pair)
    cr = colora(img, out, mask, h, l, x+1, y, c, c1, c2, pair)
    cu = colora(img, out, mask, h, l, x, y-1, c, c1, c2, pair)
    cd = colora(img, out, mask, h, l, x, y+1, c, c1, c2, pair)
    cnt = cl + cr + cu + cd
    if cnt == 4: # tutti e 4 i pixel vicini sono dello stesso colore cercato
        out[y][x] = c1
        pair[0] += 1
    else: # non tutti i vicini sono dello stesso colore, o sono fuori dall'immagine, quindi questo pixel è sul perimetro
        out[y][x] = c2
        pair[1] += 1
    if img[y][x] == c:
        return 1
    else:
        return 0
    

                

        
