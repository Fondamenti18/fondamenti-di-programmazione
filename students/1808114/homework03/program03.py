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

def adiacenti(imma, y, x, base):
    if imma[y][x] == base: return True
    else: return False

def check(imma, y, x, base, altezza, lunghezza):
    lista = []
    if y < altezza-1:
        if adiacenti(imma, y+1, x, base): lista.append((y+1, x))
    if x < lunghezza-1:
        if adiacenti(imma, y, x+1, base): lista.append((y, x+1))
    if y > 0:
        if adiacenti(imma, y-1, x, base): lista.append((y-1, x))
    if x > 0:
        if adiacenti(imma, y, x-1, base): lista.append((y, x-1))
    return lista

def colora_area(imma, area, cola):
    c = 0
    while c < len(area):
        imma[area[c][0]][area[c][1]] = cola
        c += 1
    return

def colora_perimetro(imma, perimetro, colp):
    c = 0
    while c < len(perimetro):
        imma[perimetro[c][0]][perimetro[c][1]] = colp
        c += 1
    return

def controlla(imma, y, x, base, cola, colp):
    listaccia = [(y, x)]
    area = []
    perimetro = []
    h = len(imma)
    l = len(imma[0])
    cont = 0
    while cont < len(listaccia):
        y = listaccia[cont][0]
        x = listaccia[cont][1]
        provvi = check(imma, y, x, base, h, l)
        if len(provvi) == 4:
            area.append((y, x))
        else:
            perimetro.append((y, x))
        co = 0
        while co < len(provvi):
            if provvi[co] not in listaccia: listaccia.append(provvi[co])
            co += 1
        cont += 1
    are = len(area)
    per = len(perimetro)
    colora_area(imma, area, cola)
    colora_perimetro(imma, perimetro, colp)
    global prearea
    global preperimetro
    prearea = area[:]
    preperimetro = perimetro[:]
    return (are, per)


def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    imma = load(fname)
    listona = []
    for c in range(len(lista)):
        y = lista[c][1]
        x = lista[c][0]
        base = imma[y][x]
        dati = controlla(imma, y, x, base, lista[c][2], lista[c][3])
        listona.append(dati)
    save(imma, fnameout)
    return listona