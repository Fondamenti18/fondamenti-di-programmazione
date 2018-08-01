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

import png

def ricolora(fname, lista, fnameout):
    img=load(fname) #carico l'immagine dal percorso dato in input
    listaOut=[] #dichiaro la lista da restituire
   
    #scorro la lista per lavorare su ogni singola quadrupla
    for quad in lista:
        #coordinate del punto dato in input nella 4-pla quad
        x, y = quad[0], quad[1]
        
        #spacchetto la funzione e ricavo area e perimetro, aggiungendo le due dimensioni alla lista in output
        area, perimetro = trova_adiacenti(x, y, img)
        listaOut.append((len(area), len(perimetro)))
        
        #ricavo il colore dell'area e il colore del perimetro e procedo alla colorazione richiesta
        colA, colP = quad[2], quad[3]
        cambia_colore(img, area, perimetro, colA, colP)
    
    #salvo l'immagine (al termine delle ricolorazioni richieste) nel percorso richiesto
    save(img, fnameout)
    
    #ritorno la lista di tuple (area, perimetro)
    return listaOut
        
        

def trova_adiacenti(x, y, img):
    '''Ricava tutti i punti collegati al punto in input e ritorna la lista dei punti area e la lista dei punti perimetro'''
    #inserisco il punto in input in una lista temporanea e ricavo il colore dello stesso
    temp=[(x,y)]
    col=img[y][x]
    
    #dichiaro una lista per i punti adiacenti, una per l'area e un'altra per il perimetro
    listaAdiacenti, area, perimetro = [], [], []
    
    #dichiaro un insieme vuoto a cui aggiungerò le coordinate dei punti che ho già controllato
    controllati=set()
    
    while temp!=[]:
        #lavoro con il primo valore della lista temp, isolando le coordinate per calcolarne i tentativi
        val=temp[0]
        ics, ips = val
        
        #calcolo i possibili punti adiacenti
        tentativi=[(ics-1,ips),(ics+1,ips),(ics,ips-1),(ics,ips+1)]
        
        #ricavo i punti adiacenti a val
        listaAdiacenti+=[test for test in tentativi if inside(img, test[0], test[1]) and img[test[1]][test[0]]==col]
        
        #verifico che tipo di punto è val
        if len(listaAdiacenti)==4:
            area.append(val)
        else: perimetro.append(val)
       
        #aggiungo val all'insieme dei punti controllati e lo elimino dalla lista temp
        controllati.add(val)
        del temp[0]
        
        #aggiungo a temp tutti i punti adiacenti tranne quelli che ho già controllato finora e svuoto listaAdiacenti
        temp+=[el for el in listaAdiacenti if el not in controllati and el not in temp]
        
        listaAdiacenti[:]=[]
    
    return area, perimetro
        
def cambia_colore(img, area, perimetro, colA, colP):
    '''Modifica il colore dei pixel-area e dei pixel-perimetro'''
    for xA, yA in area:
        img[yA][xA]=colA
    for xP, yP in perimetro:
        img[yP][xP]=colP
        
def inside(img, x, y):
    '''verifica per ciascun pixel dato in input se si trova all'interno dell'immagine)'''
    return 0 <= y < len(img) and 0 <= x < len(img[0])

def load(fname):
    """ Carica la immagine PNG dal file fname.
        Torna una lista di liste di pixel.
        Ogni pixel è una tupla (R, G, B) dei 3 colori.
        Ciascun colore è un intero tra 0 e 255 compresi.
    """
    with open(fname, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            l = []
            for i in range(0, len(line), 3):
                l+=[(line[i], line[i+1], line[i+2])]
            img+=[l]
        return img

def save(img, fname1):
    """ Salva la immagine img  nel file filename in formato PNG8.
        Img e' una lista di liste di pixel.
        Ogni pixel è una tupla (R, G, B) dei 3 colori.
        Ciascun colore è un intero tra 0 e 255 compresi.
    """
    pngimg = png.from_array(img,'RGB')
    pngimg.save(fname1)

if __name__=='__main__':
    rosso = (255,   0,   0)
    blu   = (  0,   0, 255)
    verde = (  0, 255,   0)
    nero  = (  0,   0,   0)
    bianco= (255, 255, 255)
    giallo= (255, 255,   0)
    cyan  = (  0, 255, 255)
    magenta= (255,  0, 255)
    ricolora('I1.png',[(10,10,rosso,blu),(90,10,nero,verde)],'test2.png')