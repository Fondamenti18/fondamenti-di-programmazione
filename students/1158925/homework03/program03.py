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


def paint_next(img, x, y, c1, c2):
    stack = [(x, y)]
    start_color = img[y][x]
    row_len = len(img)
    col_len = len(img[0])
    matrix = {}
    nbx = [-1, +1,  0, 0]
    nby = [ 0,  0, +1, -1]
    while len(stack) > 0:
        pixel = stack.pop()
        x, y = pixel

        matrix[pixel] = 0

        for i in range(4):
            dx = x + nbx[i]
            dy = y + nby[i]


            if dx >= 0 and dx < col_len and dy>=0 and dy <row_len and img[dy][dx] == start_color:
                next_pixel = (dx, dy)
                if next_pixel not in matrix:
                    stack.append(next_pixel)
            else:
                matrix[pixel] += 1

    #print([(pixel,v) for pixel,v in matrix.items() if v <4])
    area = 0
    perimetro = 0
    for pixel,v in matrix.items():
        x,y=pixel
        if v == 0:
            img[y][x] = c1
            area +=1
        else:
            img[y][x] = c2
            perimetro+=1

    return(area,perimetro)

def ricolora(fname, lista, fnameout):
    img = load(fname)

    ret = []
    for x,y,c1,c2 in lista:
        ret.append(paint_next(img, x, y, c1, c2))

    save(img, fnameout)
    return ret


if __name__ == "__main__":
    rosso = (255, 0, 0)
    blu = (0, 0, 255)
    verde = (0, 255, 0)
    nero = (0, 0, 0)
    bianco = (255, 255, 255)
    giallo = (255, 255, 0)
    cyan = (0, 255, 255)
    magenta = (255, 0, 255)
    ricolora('I1.png', [(10, 10, rosso, blu)], 'test1.png')
    ricolora('I1.png',[(10,10,rosso,blu),(90,10,nero,verde)],'test2.png')
    ricolora('I1.png',[(10,10,bianco,blu),(90,10,verde,rosso)],'test3.png')
    lista=[(i*30+1,j*30+1,bianco,verde) for i in range(10) for j in range (10)if not (i+j)%2]
    ricolora('I2.png',lista,'test4.png')
    lista0=[(i*30+1,j*30+1,nero, verde) for i in range(10) for j in range (10)if not (i+j)%2]
    lista1=[(i*30+1,j*30+1,rosso,bianco) for i in range(10) for j in range (10)if  (i+j)%2]
    ricolora('I2.png',lista0+lista1,'test5.png')
    lista=[(25,25,(0,0,0),(0,5*i,5*i)) for i in range(1,25)]
    ricolora('I1.png',lista,'test6.png')
    lista=[(0,0,(0,0,0),(0,5*i,5*i)) for i in range(1,25)]
    ricolora('I1.png',lista,'test7.png')
    lista = [(5 * i + 2, 5 * i + 2, (0, 255 - 6 * i, 0), (0, 0, 255 - 6 * i)) for i in range(40)]
    ricolora('I3.png',lista,'test8.png')
    lista = [(100, 100, (255 - x, 255, 255), (0, 0, 255 - x)) for x in range(100)]
    ricolora('I4.png', lista, 'test9.png')
    lista = [(1, 1, (255, 255, 255), (255, 255, 255)), (1, 1, (255, 0, 0), (255, 0, 0))] * 40
    ricolora('I5.png',lista,'test10.png')
    lista = [(200 + j, 200 + j, (255 - i, 255 * j, 0), (255 * j, 255 - i, 0)) for i in range(10) for j in range(2)]
    ricolora('I6.png', lista, 'test11.png')
    lista = [(204, 204, (0, 250, 0), (240, 0, 250)) for i in range(10)]
    ricolora('I7.png', lista, 'test12.png')