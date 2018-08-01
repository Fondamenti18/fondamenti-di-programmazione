'''

Definiamo adiacenti di un pixel p di un immagine i pixel adiacenti a p in  orizzontale o in  verticale.
Se un pixel e' sul bordo dell'immagine il suo vicinato non comprende i pixel non contenuti nell'immagine.
Il pixel dell'immagine con coordinate(x,y) ha dunque come adiacenti i pixel   
con coordinate (x-1,y),(x+1,y),(x,y-1),(x,y+1) appartenenti all'immagine. 
 
Definiamo connessi due pixel  e' possibile  dall'uno raggiungere l'altro spostandosi solo su   
pixel adiacenti e dello stesso colore (ovviamente perche' cio' sia possobile e' necessario 
che i due pixel abbiano lo stesso colore).

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.png .

scrivere una funzione ricolora(fname, lista,  fnameout) che presi:
- il percorso di un file che contiene un'immagine in formato PNG
- una lista di quadruple del tipo (x,y,c1,c2) dove  x e y sono coordinate di pixel dell'immagine e c1 e c2 due triple colore RGB
- il percorso di un file (fnameout)
legge l'immagine in fname, esegue un'operazione di ricolorazione di alcuni pixel dell'immagine e 
registra l'immagine ricolorata nel file fnameout.
L'operazione di ricolorazione e' la seguente. Per ciascuna delle quadruple (x,y,c1,c2) della lista nell'ordine in cui sono, 
tutti i pixel connessi al pixel  di coordinate (x,y) nell'immagine vanno ricolorati col colore c1, 
tutti i pixel del perimetro (che si trovano sul 'bordo') della zona che si e' appena colorata devono essere ricolorati col colore c2.
Il perimetro della zona colorata è l'insieme dei pixel che non hanno tutti e 4 i vicini che fanno parte della zona ricolorata 
(ovvero almeno uno è di un colore diverso da quello che si sta ricolorando oppure almeno uno non esiste perchè sarebbe fuori dall'immagine)

Si consideri ad esempio l'immagine 'I1.png', l'invocazione di 
ricolora('I1.png',[(10,10,(0,255,0), (0,0,255))],’OUT1.png')
produrra' l'immagine 'OUT1.png' identica all'immagine di partenza se non per il fatto che,
 tutti i pixel adiacenti al pixel di coordinate (10,10) (e di colore verde), verranno ricolorati 
 di rosso ((255,0,0)), mentre i pixel sul bordo della zona inizialmente verde vengono ricolorati di blu.

Per ciascuna area ricolorata bisogna inoltre calcolare area e perimetro, che sono definite come segue:
- l'area è il mumero di pixel totali ricolorati (compreso il bordo)
- il perimetro è il numero di pixel ricolorati che si trovano sul bordo, 

La funzone deve tornare la lista di coppie (area, perimetro) nello stesso ordine in cui sono state colorate le aree.
 
Per altri  esempi vedere il file grade03.txt 
'''

from immagini import *
    
def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    img=load(fname)
    w=len(img[0])
    h=len(img)
    risultati = []
    for X, Y, colore1, colore2 in lista:
        img, ris = colora(img, X, Y, w, h, colore1, colore2)
        risultati.append(ris)
    save(img, fnameout)
    return risultati

def colora(img, X, Y, w, h, colore1, colore2):
    img2 = [[ rgb for rgb in linea] for linea in img]
    colorati = espandi(img, img2, X, Y, w, h, colore1)
    area = len(colorati)
    dentro = interno(colorati,w,h)
    sul_perimetro = colorati - dentro
    for x,y in sul_perimetro:
        img2[y][x] = colore2
    perimetro=len(sul_perimetro)
    return img2, ((area-perimetro), perimetro)

def espandi(img, img2, X, Y, w, h, colore1):
    orig = img[Y][X]
    colorati = set()
    da_colorare = [(X,Y)]
    while da_colorare:
        x,y = da_colorare.pop()
        img2[y][x] = colore1
        colorati.add((x,y))
        for x1, y1 in [ (x+1, y), (x-1, y), (x, y+1), (x, y-1) ]:
            if 0 <= x1 < w and 0 <= y1 < h and (x1, y1) not in colorati and img[y1][x1] == orig :
                da_colorare.append((x1, y1))
    return colorati

def interno(colorati, w, h):
    dentro = set()
    for x,y in colorati:
        ok = True
        for x1, y1 in [ (x+1, y), (x-1, y), (x, y+1), (x, y-1) ]:
            if not( 0 <= x1 < w and 0 <= y1 < h and (x1, y1) in colorati) :
                ok = False
        if ok:
            dentro.add((x,y))
    return dentro


if __name__ == '__main__':
    args        = ('I1.png',[(10,10,(255,0,0),(0,0,255))],'test1.png')
    result      = ricolora(*args)
    print(result)

