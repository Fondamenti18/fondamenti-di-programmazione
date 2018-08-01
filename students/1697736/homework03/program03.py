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
import png

def load(fname):
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

def save(img, filename):
    pngimg = png.from_array(img,'RGB')
    pngimg.save(filename)
    
def inside(img, i, j):
    '''Ritorna True se il pixel (i, j) e' dentro l'immagine img, False
    altrimenti'''
    w, h = len(img[0]), len(img)
    return 0 <= i < w and 0 <= j < h
            

    
def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    immagine = load(fname)
    
    lis_adiac = set()
    listafinale = []
    
    
    
    
    for quad in lista:
        x = quad[0]
        y = quad[1]
        c1 = quad[2]
        c2 = quad[3]
        
        colorati = set()
        area = 0
        perimetro = 0
        
        col_pix = immagine[y][x]
        
        lis_adiac.add((x,y))
        
        while len(lis_adiac) != 0:
            newlist = set()
            for pix in lis_adiac:
                contapix = 0
                if inside(immagine, pix[0]+1, pix[1]):
                    if (pix[0]+1,pix[1]) in colorati or immagine[pix[1]][pix[0]+1] == col_pix:
                        contapix += 1
                        if immagine[pix[1]][pix[0]+1] == col_pix:
                            newlist.add((pix[0]+1,pix[1]))
                            
                if inside(immagine, pix[0]-1, pix[1]):
                    if immagine[pix[1]][pix[0]-1] == col_pix or (pix[0]-1,pix[1]) in colorati:
                        contapix += 1
                        if immagine[pix[1]][pix[0]-1] == col_pix:
                            newlist.add((pix[0]-1,pix[1]))
                            
                if inside(immagine, pix[0], pix[1]+1):
                    if immagine[pix[1]+1][pix[0]] == col_pix or (pix[0],pix[1]+1) in colorati:
                        contapix += 1
                        if immagine[pix[1]+1][pix[0]] == col_pix:
                            newlist.add((pix[0],pix[1]+1))
                            
                if inside(immagine, pix[0], pix[1]-1):
                    if immagine[pix[1]-1][pix[0]] == col_pix or (pix[0],pix[1]-1) in colorati:
                        contapix += 1
                        if immagine[pix[1]-1][pix[0]] == col_pix:
                            newlist.add((pix[0],pix[1]-1))
                    
                if contapix == 4:
                    immagine[pix[1]][pix[0]] = c1
                    area += 1
                else:
                    immagine[pix[1]][pix[0]] = c2
                    perimetro += 1
                
                colorati.add((pix[0],pix[1]))
                    
            lis_adiac = newlist
        listafinale.append((area,perimetro))
                    
    save(immagine, fnameout)
    
    return listafinale
        
    
    
if __name__ == '__main__':
    rosso = (255,   0,   0)
    blu   = (  0,   0, 255)
    verde = (  0, 255,   0)
    nero  = (  0,   0,   0)
    bianco= (255, 255, 255)
    print(ricolora('I1.png',[(10,10,rosso,blu),(90,10,nero,verde)],'test2.png'))