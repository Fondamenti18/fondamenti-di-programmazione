'''
Un robottino deve muoversi su di una scacchiera di 15 x 15 celle  con celle bianche e nere  ciascuna 
di lato 40. 
Per rendere il percorso accidentato alcune delle celle della scacchiera contengono ostacoli 
(queste celle sono  colorate di rosso).

Un  esempio di scacchiera con ostacoli e' dato  dall'immagine 'I1.png'

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo 
immagini.py .

Al'inizio il robottino e' posizionato sulla prima cella in altro a sinistra della scacchiera ed e' 
rivolto verso destra (x crescente). 
Ad ogni step tenta di ragiungere una delle celle adiacenti in orizzontale o verticale. 
Le regole di movimento del robottino sono le seguenti: 
- al generico step, si sposta sulla cella che ha di fronte se questa e' libera da ostacoli e non ci 
e' gia transitato in passato. 
- se invece la cella risulta occupata o e' una cella su cui ha gia transitato, ruota di 90 gradi in 
senso orario ed aspetta lo step successivo. 
- dopo aver ruotato  di 360 gradi senza essere riuscito a spostarsi si ferma. 

Progettare la funzione  percorso(fname, fname1) che presi in input:
- il percorso di un file (fname) contenente l'immagine in formato .png di una scacchiera con ostacoli
- il percorso di un file di tipo .png (fname1) da creare
legge l'immagine della scacchiera in fname, colora di verde le celle della scacchiera percorse dal 
robottino prima di fermarsi, 
colora di blu la cella in cui il robottino si ferma e registra l'immagine ricolorata nel file fname1. 
Inoltre restituisce una stringa dove in sequanza sono codificati i passi effettuati dal robottino 
prima di fermarsi. 
La codifica e' a seguente: 
    '0' per un passo verso destra (x crescenti)
    '1' per un passo verso il basso (y crescenti)
    '2' per un passo verso sinistra (x decrescenti)
    '3' per un passo verso l'alto (y decrescenti)

Si puo' assumere che la cella in alto a sinistra sia priva di ostacoli. 

Per esempi di scacchiere con ostacoli e relativi cammini  vedere il file grade02.txt 

NOTA: il timeout per la esecuzione del grader e' fissato a 10*N secondi (per N test eseguiti dal grader)
'''

from immagini import *
import png

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

def save(img, filename):
    """ Salva la immagine img  nel file filename in formato PNG8.
        Img e' una lista di liste di pixel.
        Ogni pixel è una tupla (R, G, B) dei 3 colori.
        Ciascun colore è un intero tra 0 e 255 compresi.
    """
    pngimg = png.from_array(img,'RGB')
    pngimg.save(filename)
    

def colora(img,mat,x, y,p,q):
    for t in range(x, x+40):
        for u in range(y,y+40):
            img[t][u]=mat[p][q]
    return(img)



def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    immagine=load(fname)
    

    quadrati=[]
    for x in range(0, len(immagine), 40):
        riga=[]
        for y in range(0, len(immagine[x]), 40):
            riga.append(immagine[x][y])
        quadrati.append(riga)
       
            
    #print("this is the huge matrice of sqares ", quadrati)
        
    ViaLibera=True
    direzione=0
    poX=0
    poY=0
    stringa=""
   
    while ViaLibera:
        #print("new ciclo")
        #print("direzione: ", direzione) 
        check=0
        
        #print("posizione: ", poX, poY )
        
        if direzione == 0:
            if poY < len(quadrati)-1 and quadrati[poX][poY+1]!=(0,255,0) and quadrati[poX][poY+1]!=(255,0,0):
                quadrati[poX][poY]=(0,255,0)
                poY=poY+1
                stringa=stringa+str(direzione)
            else:
                direzione=1
                check=check+1
            #print("direzione: ", direzione)        
        if direzione == 1:
            if poX < len(quadrati)-1 and quadrati[poX+1][poY]!=(0,255,0) and quadrati[poX+1][poY]!=(255,0,0):
                quadrati[poX][poY]=(0,255,0)
                poX=poX+1
                stringa=stringa+str(direzione)
            else:
                direzione=2
                check=check+1
            #print("direzione: ", direzione)        
        if direzione == 2:
            if poY>0 and quadrati[poX][poY-1]!=(0,255,0) and quadrati[poX][poY-1]!=(255,0,0):
                quadrati[poX][poY]=(0,255,0)
                poY=poY-1
                stringa=stringa+str(direzione)
            else:
                direzione=3
                check=check+1
            #print("direzione: ", direzione)
        if direzione == 3:
            if poX>0 and quadrati[poX-1][poY]!=(0,255,0) and quadrati[poX-1][poY]!=(255,0,0):
                quadrati[poX][poY]=(0,255,0)
                poX=poX-1
                stringa=stringa+str(direzione)
            else:
                direzione=0
                check=check+1
            #print("direzione: ", direzione)
        #print("check", check)
        if check == 4:
            quadrati[poX][poY]=(0,0,255)
            ViaLibera=False
        
    #print("this is the huge solution matrice of sqares ", quadrati)
            

    k=-40
    for x in range(len(quadrati)):
        k=k+40
        h=-40
        for y in range(len(quadrati[x])):
            h=h+40
            if quadrati[x][y] == (0,0,255) or quadrati[x][y] == (0,255,0):
                colora(immagine, quadrati, k, h,x,y)
    
  
            



         
    
    save(immagine, fname1)     
    #print(stringa)
    return(stringa)
    
        
        
            
            
            