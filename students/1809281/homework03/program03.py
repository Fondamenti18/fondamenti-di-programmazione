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
    
import sys
sys.setrecursionlimit(10000)
    
area = set()
perimeter = set()

def ricolora(fname, lista, fnameout):
    global area
    global perimeter
    image = load(fname)
    result = []
    
    for recolor in lista:
        area = set()
        perimeter = set()
        x = recolor[0]
        y = recolor[1]
        base_color = image[y][x]
        area_color = recolor[2]
        peri_color = recolor[3]
        
        
        adjacents(image, x, y, base_color, area_color, peri_color)
        
        result.append((len(area), len(perimeter)))
        
    save(image, fnameout)
    return result

def adjacents(image, x, y, base_c, area_c, peri_c):  
    adj = []
    corner = False
    if x-1 >= 0 and image[y][x-1] == base_c:
        adj.append((x-1, y))
    elif x-1 >= 0 and image[y][x-1] != area_c and image[y][x-1] != peri_c:
        corner = True
        
    if x+1 < len(image[0]) and image[y][x+1] == base_c:
        adj.append((x+1, y))
    elif x+1 < len(image[0]) and image[y][x+1] != area_c and image[y][x+1] != peri_c:
        corner = True
        
    if y-1 >= 0 and image[y-1][x] == base_c:
        adj.append((x, y-1))
    elif y-1 >= 0 and image[y-1][x] != area_c and image[y-1][x] != peri_c:
        corner = True
        
    if y+1 <= len(image) and image[y+1][x] == base_c:
        adj.append((x, y+1))
    elif y+1 < len(image) and image[y+1][x] != area_c and image[y+1][x] != peri_c:
        corner = True

        
    if x == 0 or y == 0 or corner:
        image[y][x] = peri_c
        perimeter.add((x, y))
    else:
        image[y][x] = area_c
        area.add((x,y))

    
    all_equal = True
    for a in adj:
        if image[a[1]][a[0]] != base_c:
            all_equal = False
            break
    
    if all_equal == True:
        for a in adj:
            if a[0] == 0 or a[1] == 0:
                image[a[1]][a[0]] = peri_c
            else:
                image[a[1]][a[0]] = area_c
                
            if adj != []:
                adjacents(image, a[0], a[1], base_c, area_c, peri_c)
                
    
if __name__  == '__main__':
    print(ricolora('I1.png',[(10,10,(255, 0, 0),(0, 0, 255))],'test_self.png'))
    print(ricolora('I1.png',[(10,10,(255, 0, 0),(0, 0, 255)),(90,10,(0, 0, 0),(0, 255, 0))],'test_self_second.png'))
    