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
    
def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    img=load(fname) #-------------------------------------------------------------------okay
    risultato=[]
    for n in lista:
        sottolista=n
        tupla_coordinate=coordinate_origine(img,sottolista)  #-----------------------------------okay
        tupla_lunghezzadacolorare=lunghezza_da_colorare(tupla_coordinate,img)#-------------------okay
        img=colorazione_interno(sottolista,tupla_coordinate,img,tupla_lunghezzadacolorare) #-----okay
        colorazioneperimetro=colorazione_perimetro(sottolista,tupla_coordinate,img,tupla_lunghezzadacolorare)#----okay
        img=colorazioneperimetro[0]
        perimetro=colorazioneperimetro[1]
        operazione_area=(tupla_lunghezzadacolorare[0]*tupla_lunghezzadacolorare[1])-perimetro
        soluzione=(operazione_area,perimetro)
        risultato+=[soluzione]
    save(img,fnameout)
    return risultato

def coordinate_origine(img,sottolista):
    #print('\ncoordinate_origine')
    coordinate_iniziali_X=sottolista[0]
    coordinate_iniziali_Y=sottolista[1]
    coordinate_origine_X=sottolista[0]
    coordinate_origine_Y=sottolista[1]
    img1=img
    #creazione lista che va da coordinata fino a 0
    #lista_X=[]
    #for x in range(0,coordinate_iniziali_X):
    #    lista_X+=[x+1]
    #print(lista_X)
    #lista_X=list.reverse(lista_X)
    #print(lista_X)
    #
    X_pixel=coordinate_iniziali_X
    Y_pixel=coordinate_iniziali_Y
    for k1 in range(0,coordinate_iniziali_X):
        if img[coordinate_iniziali_Y][coordinate_iniziali_X]==img[Y_pixel][X_pixel]:
            # pixel dello stesso colore
            X_pixel-=1
            
        else:
            X_pixel+=1
            break
#    X_pixel=X_pixel+1
   # print('X_pixel',X_pixel)
    
    for k in range(0,coordinate_iniziali_Y):
        #print ('\nY_pixel',Y_pixel)
        if img[coordinate_iniziali_Y][coordinate_iniziali_X]==img[Y_pixel][X_pixel]:
            #print('pixel dello stesso colore')
            # pixel dello stesso colore
            Y_pixel-=1
            
        else:
            #print('ELSE pixel dello stesso colore')
            Y_pixel+=1
            break
        
#    Y_pixel=Y_pixel+1
   # print('Y_pixel',Y_pixel)
    coordinate_origine=(X_pixel,Y_pixel)
   # print(coordinate_origine)
    return coordinate_origine

def lunghezza_da_colorare(tupla_coordinate,img):
    #print('lunghezza da colorare')
    coordinate_X=tupla_coordinate[0]
    coordinate_Y=tupla_coordinate[1]
    lunghezza_X=0
    lunghezza_Y=0
    img1=img





    
    for k1 in range(coordinate_X,len(img[coordinate_X])):
        if k1+1==len(img[coordinate_Y]):
            #lunghezza_X+=1
            break
        
        if img1[coordinate_Y][k1]==img1[coordinate_Y][k1+1]:
            lunghezza_X+=1
        else:
            break
    for k in range(coordinate_Y,len(img)):
        if lunghezza_Y+1==len(img):
            #lunghezza_Y+=1
            break
        if img[k][coordinate_X]==img[k+1][coordinate_X]:
            lunghezza_Y+=1
        else:
            break
    lunghezze=(lunghezza_X+1,lunghezza_Y+1)
    #print('lunghezze',lunghezze)
    return lunghezze

def colorazione_interno(sottolista,tupla_coordinate,img,tupla_lunghezzadacolorare):
    print('colorazione_interno')
    color_to_color=sottolista[2]
    coordinate_X=tupla_coordinate[0]
    coordinate_Y=tupla_coordinate[1]
    lunghezza_X=tupla_lunghezzadacolorare[0]
    lunghezza_Y=tupla_lunghezzadacolorare[1]
    for k in range(coordinate_Y,coordinate_Y+lunghezza_Y):
        if coordinate_Y+1==0:
            coordinate_Y+=1
            break
        for k1 in range(coordinate_X,coordinate_X+lunghezza_X):
            img[k][k1]=color_to_color
    return img

def colorazione_perimetro(sottolista,tupla_coordinate,img,tupla_lunghezzadacolorare):
    coordinate_X=tupla_coordinate[0]
    coordinate_Y=tupla_coordinate[1]
    lunghezza_X=tupla_lunghezzadacolorare[0]
    lunghezza_Y=tupla_lunghezzadacolorare[1]
    color_to_color=sottolista[3]
    somma=0
    for k1 in range(coordinate_Y,coordinate_Y+lunghezza_Y):
        #print('k1=',k1)
        #colonna lato sinistro
        img[k1][coordinate_X]=color_to_color
        somma+=1
    #print('coordinate_Y,coordinate_Y+lunghezza_Y',coordinate_Y,coordinate_Y+lunghezza_Y-1)
    for k2 in range(coordinate_Y,coordinate_Y+lunghezza_Y):
        #print('k2=',k2,'\nlunghezza_X',lunghezza_X)
        #colonna lato destro
        img[k2][coordinate_X+lunghezza_X-1]=color_to_color
        somma+=1
    for k3 in range(coordinate_X,coordinate_X+lunghezza_X):
        #larghezza lato alto
        #print('k3=',k3)
        img[coordinate_Y][k3]=color_to_color
        somma+=1
    for k4 in range(coordinate_X,coordinate_X+lunghezza_X):
        #print('k4=',k4)
        #larghezza lato basso
        img[coordinate_Y+lunghezza_Y-1][k4]=color_to_color
        somma+=1
    #print('somma=',somma)
    risultato=(img,somma-4)
    return risultato
    

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

def save(img, fnameout):
    """ Salva la immagine img  nel file filename in formato PNG8.
        Img e' una lista di liste di pixel.
        Ogni pixel è una tupla (R, G, B) dei 3 colori.
        Ciascun colore è un intero tra 0 e 255 compresi.
    """
    pngimg = png.from_array(img,'RGB')
    pngimg.save(fnameout)


#ricolora('PROVA1.png',[(90,10,(0,0,0),(0,255,0))],'PROVA2.png')
