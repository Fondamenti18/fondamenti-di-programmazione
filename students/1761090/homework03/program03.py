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
'''
funzione per trovare i pixel connessi tra gli adiacenti al pixel desiderato in img
'''
def adiacenti_connessi(img, pixel):
    x,y = pixel
    adj = [(-1,0),(0,-1),(1,0),(0,1)] #scarti delle coordinate dei pixel adiacenti (sinistra, su, destra, giu)
    return [(x+xx, y+yy) for xx,yy in adj if 0<=y+yy<len(img)
            and 0<=x+xx<len(img[0]) and img[y+yy][x+xx] == img[y][x]]	#lista degli adiacenti (se le coordinate sono valide) se sono dello stesso colore di pixel
'''
ritorna i pixel connessi a un pixel_iniziale tramite una BFS sull'immagine, ritorna anche il bordo
'''
def trova_connessi(img, pixel_iniziale):
    visitati = set([pixel_iniziale])
    attivi = set([pixel_iniziale])
    bordo = set()
    while attivi:
        newattivi = set()
        while attivi:
            pixel = attivi.pop()
            " dentro connessi ho tutte le tuple(x,y) che corrispondono ai pixel connessi al pixel che sto esaminando"
            connessi = adiacenti_connessi(img, pixel)	#se ci sono dei pixel connessi al pixel corrente, li visito; se non sono 4, il pixel corrente sta nel bordo
            if connessi:
                if len(connessi) < 4:
                    bordo.add(pixel)
                for p in connessi:
                    if p not in visitati:
                        visitati.add(p)
                        newattivi.add(p)
        attivi = newattivi
    return visitati, bordo


def ricolora(fname, lista, fnameout):
    img = load(fname)
    pixel_cambiati = []

    for tupla in lista:
        x, y = tupla[0], tupla[1]
        connessi, bordo = trova_connessi(img, (x,y))
        colore_area = tupla[2]
        colore_bordo = tupla[3]
        for pixel in connessi:    #ricoloro tutti i pixel connessi
            x,y = pixel
            img[y][x] = colore_area
        for pixel in bordo:       #ricoloro il bordo
            x,y = pixel
            img[y][x] = colore_bordo

        pixel_cambiati.append((len(connessi)-len(bordo), len(bordo))) #l'informazione su quanti pixel devo cambiare sta nella lunghezza dei due set ottenuti in precedenza

    save(img, fnameout)
    return pixel_cambiati

#ricolora('I1.png', [(25,25, (0,0,0), (255,255,0)), (25,25, (0,0,0), (255,0,0))], 'prova.png')