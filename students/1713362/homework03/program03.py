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

def ricolora(fname, lista, fnameout):
    immagine = load(fname)
    lista_return = []
    if len(lista) > 50:
        return
    for quadrupla in lista:
        risultato = colora(quadrupla, immagine)
        immagine = risultato[0]
        lista_return.append((risultato[1],risultato[2]))
    save(immagine,fnameout)
    return lista_return


def colora(q, immagine):
    nuovo_colore = q[2]
    colore_perimetro = q[3]
    vecchio_colore = immagine[q[1]][q[0]]
    immagine[q[1]][q[0]] = nuovo_colore
    coda = []
    coda.append((q[0],q[1]))
    area = 0
    perimetro = 0
    lista_perimetro = []
    while len(coda) != 0:
        pixel = coda[0]
        x = pixel[0]
        y = pixel[1]
        if immagine[y][x] == nuovo_colore:
            area += 1
        if len(coda) > 1:
            coda = coda[1:]
        else:
            coda = []
        if inside(immagine,x,y+1):
            if immagine[y+1][x] == vecchio_colore:
                coda.append((x,y+1))
                immagine[y+1][x] = nuovo_colore
            else:
                if not (x,y) in lista_perimetro and immagine[y+1][x] != nuovo_colore:
                    immagine[y][x] = colore_perimetro
                    perimetro += 1
                    area -= 1
                    lista_perimetro.append((x,y))
        else:
            if not (x,y) in lista_perimetro:
                immagine[y][x] = colore_perimetro
                perimetro += 1
                area -= 1
                lista_perimetro.append((x,y))
        if inside(immagine,x,y-1):
            if immagine[y-1][x] == vecchio_colore:
                coda.append((x,y-1))
                immagine[y-1][x] = nuovo_colore
            else:
                if not (x,y) in lista_perimetro and immagine[y-1][x] != nuovo_colore:
                    immagine[y][x] = colore_perimetro
                    perimetro += 1
                    area -= 1
                    lista_perimetro.append((x,y))
        else:
            if not (x,y) in lista_perimetro:
                immagine[y][x] = colore_perimetro
                perimetro += 1
                area -= 1
                lista_perimetro.append((x,y))
        if inside(immagine,x+1,y):
            if immagine[y][x+1] == vecchio_colore:
                coda.append((x+1,y))
                immagine[y][x+1] = nuovo_colore
            else:
                if not (x,y) in lista_perimetro and immagine[y][x+1] != nuovo_colore:
                    immagine[y][x] = colore_perimetro
                    perimetro += 1
                    area -= 1
                    lista_perimetro.append((x,y))
        else:
            if not (x,y) in lista_perimetro:
                immagine[y][x] = colore_perimetro
                perimetro += 1
                area -= 1
                lista_perimetro.append((x,y))
        if inside(immagine,x-1,y):
            if immagine[y][x-1] == vecchio_colore:
                coda.append((x-1,y))
                immagine[y][x-1] = nuovo_colore
            else:
                if not (x,y) in lista_perimetro and immagine[y][x-1] != nuovo_colore:
                    immagine[y][x] = colore_perimetro
                    perimetro += 1
                    area -= 1
                    lista_perimetro.append((x,y))
        else:
            if not (x,y) in lista_perimetro:
                immagine[y][x] = colore_perimetro
                perimetro += 1
                area -= 1
                lista_perimetro.append((x,y))
    return (immagine, area, perimetro)



def width(immagine):
    return len(immagine[0])

def height(immagine):
    return len(immagine)

def inside(immagine, i, j):
    iw, ih = width(immagine), height(immagine)
    return 0 <= i < iw and 0 <= j < ih