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

img = []

img_larghezza = 0

img_altezza = 0

area = 0

perimetro = 0

colorebase = ()

colore1 = ()

colore2 = ()

pixelselezionati = set()
    
def dentroimmagine(x, y):
    
    global img_larghezza
    
    global img_altezza
    
    return x >= 0 and x < img_larghezza and y >= 0 and y < img_altezza

def quattrovicinistessocolore(pixel, colorebase):
    
    global img
    
    vicinostessocolore = 0
    
    if dentroimmagine(pixel[0] + 1, pixel[1]):
        
        if img[pixel[1]][pixel[0] + 1] == colorebase:
               
            vicinostessocolore += 1
    
    if dentroimmagine(pixel[0] - 1, pixel[1]):
        
        if img[pixel[1]][pixel[0] - 1] == colorebase:
            
            vicinostessocolore += 1

    if dentroimmagine(pixel[0], pixel[1] + 1):
        
        if img[pixel[1] + 1][pixel[0]] == colorebase:
            
            vicinostessocolore += 1
            
    if dentroimmagine(pixel[0], pixel[1] - 1):
        
        if img[pixel[1] - 1][pixel[0]] == colorebase:
            
            vicinostessocolore += 1                
                
    return vicinostessocolore
        
def terrenivicinistessocolore(listapixel, colore):
    
    global img
    
    vicinistessocolore = set()
    
    for pixel in listapixel:
        
        if dentroimmagine(pixel[0] + 1, pixel[1]):
            
            if img[pixel[1]][pixel[0] + 1] == colore:
                   
                vicinistessocolore.add((pixel[0] + 1, pixel[1]))
        
        if dentroimmagine(pixel[0] - 1, pixel[1]):
            
            if img[pixel[1]][pixel[0] - 1] == colore:
                
                vicinistessocolore.add((pixel[0] - 1, pixel[1]))
    
        if dentroimmagine(pixel[0], pixel[1] + 1):
            
            if img[pixel[1] + 1][pixel[0]] == colore:
                
                vicinistessocolore.add((pixel[0], pixel[1] + 1))
                
        if dentroimmagine(pixel[0], pixel[1] - 1):
            
            if img[pixel[1] - 1][pixel[0]] == colore:
                
                vicinistessocolore.add((pixel[0], pixel[1] - 1))                
                
    return vicinistessocolore

def sulbordo(x, y):
    
    global img_larghezza
    
    global img_altezza
    
    return (x == 0 or x == img_larghezza - 1) or (y == 0 or y == img_altezza - 1)
        
def ricolora(fname, lista, fnameout):
    
    '''Implementare qui la funzione'''
    
    global img
    
    global colorebase
    
    global colore1
    
    global colore2
    
    global colori

    global img_larghezza
    
    global img_altezza
    
    global area
    
    global perimetro
    
    global pixelselezionati
    
    listarestituita = []

    img = load(fname)
        
    img_larghezza = len(img[0])
    
    img_altezza = len(img)
           
    for test in lista:
       
        area = 0
        
        perimetro = 0
        
        sx = test[0]
        
        sy = test[1]
        
        colore1 = test[2]
        
        colore2 = test[3]
                
        colorebase = img[test[1]][test[0]]
                
        colori = []
        
        colori.append(colorebase)
        
        colori.append(colore1)
        
        colori.append(colore2)
    
        semi = set()
        
        semi.add((test[0],test[1]))
        
        terrenigiaselezionati = set()
        
        terrenigiaselezionati |= set(semi)
        
        terrenivicini = set()
        
        while True:
            
            terrenivicini = terrenivicinistessocolore(semi, colorebase)
            
            semi = terrenivicini - terrenigiaselezionati
            
            terrenigiaselezionati |= terrenivicini
                        
            if len(terrenivicini) == 0:
                
                break
        
        dicpixel = {}
        
        for pixel in terrenigiaselezionati:
        
            if quattrovicinistessocolore(pixel, colorebase) == 4:
                
                dicpixel[pixel] = colore1
                
                area += 1
                
            else:
                
                dicpixel[pixel] = colore2
                
                perimetro += 1
            
        for pixel in dicpixel:
            
            img[pixel[1]][pixel[0]] = dicpixel[pixel]
            
        save(img, fnameout) 
        
        listarestituita.append((area, perimetro))

        img = load(fnameout)
      
    #print(listarestituita)
    return listarestituita

'''
rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)


args        = ('I1.png',[(10,10,rosso,blu),(90,10,nero,verde)],'test2.png')
expected    = [(2304, 196), (2304, 196)]
explanation = "il secondo e' l'output corretto"
ret=ricolora(*args)
'''