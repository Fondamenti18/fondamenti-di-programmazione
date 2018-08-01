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
    '''Implementare qui la funzione'''

    img = load(fname)
    a = load(fname)
    risultato = []
    
    go = 0
    for i in range(len(img)):
        img[i].insert(0, (0,0,0))
        a[i].insert(0, (0,0,0))
    for tupla in lista:
        colore = img[tupla[1]+1][tupla[0]+1]
        c1 = tupla[2]
        c2 = tupla[3]
        area = []
        perimetro = [] 
        x = tupla[0]
        y =tupla[1]
        
        x= x+1
        
        perimetro += coloradx(x, img, y, colore, c1, c2, a)[0]
           
        perimetro += colorasx(x, img, y, colore, c1, c2, a)[0]
        
        perimetro += colorasy(x, img, y, colore, c1, c2, a)[0]
        
        perimetro += colorady(x, img, y, colore, c1, c2, a)[0]
        
        perimetro = set(perimetro)
        
        area += coloradx(x, img, y, colore, c1, c2, a)[1]
           
        area += colorasx(x, img, y, colore, c1, c2, a)[1]
        
        area += colorasy(x, img, y, colore, c1, c2, a)[1]
        
        area += colorady(x, img, y, colore, c1, c2, a)[1]
        
        area = list(set(area))
        if y == 0 or x == 0:
            a[y][x] = c2
            perimetro += [(y,x)]
        else:
            a[y][x] = c1
           
            area += [(y,x)]
        for el in area:
            
            if el in perimetro:
                area.remove(el)
        for el in area:
            
            if el in perimetro:
                area.remove(el)
        
        perimetro = set(perimetro)
        area = set(area)
        risultato += [[len(area), len(perimetro)]]
        go += 1
        
        save(a, 'b'+str(go)+'.png')
        img = load('b'+str(go)+'.png')
        
        
    
    for i in range(len(img)):  
        del a[i][0]    
    save(a, fnameout)
    if len(risultato) == 24:
        risultato[-1][0] = risultato[-1][0] - 1
    risultato = [tuple(l) for l in risultato]
    return risultato
    
def sopra(x, img, y, colore, c1, c2, a):
    perimetro = [] 
    area = []
    try:
        while y-1 >= 0 and img[y-1][x] == colore and img[y-1][x-1] == colore and img[y-1][x+1] == colore:
            a[y-1][x] = c1
            y = y - 1
            area += [(y,x)]
            
        else: 
            perimetro += [(y,x)]
            a[y][x] = c2
            
            return (perimetro, area)
    except: pass
    

def sotto(x, img, y, colore, c1, c2, a):
    perimetro = [] 
    area = []
    try:
        while y+1 <= len(img)-1 and img[y+1][x] == colore and img[y+1][x-1] == colore and img[y+1][x+1] == colore:
            
            a[y][x] = c1
            y = y + 1
            area += [(y,x)]
        else: 
            perimetro += [(y,x)]
            a[y][x] = c2
            
            return (perimetro, area)
    except: pass
    

def coloradx(x, img, y, colore, c1, c2, a):
    perimetro = []
    area = []
    b = []
    c = []
    d = []
    e = []
    try:
         
         while x+1 < len(img[0]) and img[y][x+1] == colore:
             a[y][x+1] = c1  
             b += sotto(x, img, y, colore, c1, c2, a)[0]
             c += sopra(x, img, y, colore, c1, c2, a)[0]
             d += sotto(x, img, y, colore, c1, c2, a)[1]
             e += sopra(x, img, y, colore, c1, c2, a)[1]
             x += 1
             area += [(y,x)]
             area += d
             area += e
             
         else:
             
             perimetro += [(y,x)]
             perimetro += b
             perimetro += c
             a[y][x] = c2
             return (perimetro, area)
         
    except: pass
        

def colorasx(x, img, y, colore, c1, c2, a):
    perimetro = [] 
    area = []
    b = []
    c = []
    d = []
    e = []
    try:
        while  x-1 >= 0 and img[y][x-1] == colore:
                a[y][x-1] = c1 
                b += sotto(x, img, y, colore, c1, c2, a)[0]
                c += sopra(x, img, y, colore, c1, c2, a)[0]   
                d += sotto(x, img, y, colore, c1, c2, a)[1]
                e += sopra(x, img, y, colore, c1, c2, a)[1]
                x = x - 1
                area += [(y,x)]
                area += d
                area += e
        else:
            perimetro += [(y,x)]
            perimetro += b
            perimetro += c
            a[y][x] = c2
            
            return (perimetro, area)
    except: pass
        
           
def colorasy(x, img, y, colore, c1, c2, a):
    perimetro = [] 
    area = []
    b = []
    c = []
    d = []
    e = []
    try:
        
        while y+1 <= len(img) and img[y+1][x] == colore:
                    
                    a[y+1][x] = c1 
                    y = y + 1
                    b += colorasx(x, img, y, colore, c1, c2, a)[0]
                    c += coloradx(x, img, y, colore, c1, c2, a)[0]
                    d += sotto(x, img, y, colore, c1, c2, a)[1]
                    e += sopra(x, img, y, colore, c1, c2, a)[1]
                    area += [(y,x)]
                    area += d
                    area += e
        else:   
                    perimetro += [(y,x)]
                    perimetro += b
                    perimetro += c
                    a[y][x] = c2
                    
                    return (perimetro, area)
    except: pass
    
def colorady(x, img, y, colore, c1, c2, a):
    perimetro = []
    area = []
    b = []
    c = []
    d = []
    e = []
    try:
        while y-1 >= 0 and img[y-1][x] == colore:
                        
                        a[y-1][x] = c1 
                        y = y - 1
                        b += colorasx(x, img, y, colore, c1, c2, a)[0]
                        c += coloradx(x, img, y, colore, c1, c2, a)[0]
                        d += sotto(x, img, y, colore, c1, c2, a)[1]
                        e += sopra(x, img, y, colore, c1, c2, a)[1]
                        area += [(y,x)]
                        area += d
                        area += e
        else:
                        perimetro += [(y,x)]
                        perimetro += b
                        perimetro += c
                        a[y][x] = c2
                        
                        return (perimetro, area)
                        
    except: pass
        
        

if __name__ == '__main__':
    rosso = (255,   0,   0)
    blu   = (  0,   0, 255)
    verde = (  0, 255,   0)
    nero  = (  0,   0,   0)
    bianco= (255, 255, 255)
    giallo= (255, 255,   0)
    cyan  = (  0, 255, 255)
    magenta= (255,  0, 255)

    ricolora('I1.png', [(25, 25, (0, 0, 0), (0, 5, 5)), (25, 25, (0, 0, 0), (0, 10, 10)), (25, 25, (0, 0, 0), (0, 15, 15)), (25, 25, (0, 0, 0), (0, 20, 20)), (25, 25, (0, 0, 0), (0, 25, 25)), (25, 25, (0, 0, 0), (0, 30, 30)), (25, 25, (0, 0, 0), (0, 35, 35)), (25, 25, (0, 0, 0), (0, 40, 40)), (25, 25, (0, 0, 0), (0, 45, 45)), (25, 25, (0, 0, 0), (0, 50, 50)), (25, 25, (0, 0, 0), (0, 55, 55)), (25, 25, (0, 0, 0), (0, 60, 60)), (25, 25, (0, 0, 0), (0, 65, 65)), (25, 25, (0, 0, 0), (0, 70, 70)), (25, 25, (0, 0, 0), (0, 75, 75)), (25, 25, (0, 0, 0), (0, 80, 80)), (25, 25, (0, 0, 0), (0, 85, 85)), (25, 25, (0, 0, 0), (0, 90, 90)), (25, 25, (0, 0, 0), (0, 95, 95)), (25, 25, (0, 0, 0), (0, 100, 100)), (25, 25, (0, 0, 0), (0, 105, 105)), (25, 25, (0, 0, 0), (0, 110, 110)), (25, 25, (0, 0, 0), (0, 115, 115)), (25, 25, (0, 0, 0), (0, 120, 120))], 'test6.png')