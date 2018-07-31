'''
Un robottino deve muoversi su di una scacchiera di 15 x 15 celle  con celle bianche e nere  ciascuna di lato 40. 
Per rendere il percorso accidentato alcune delle celle della scacchiera contengono ostacoli (queste celle sono  colorate di rosso).

Un  esempio di scacchiera con ostacoli e' dato  dall'immagine 'I1.png'

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Al'inizio il robottino e' posizionato sulla prima cella in altro a sinistra della scacchiera ed e' rivolto verso destra (x crescente). 
Ad ogni step tenta di ragiungere una delle celle adiacenti in orizzontale o verticale. 
Le regole di movimento del robottino sono le seguenti: 
- al generico step, si sposta sulla cella che ha di fronte se questa e' libera da ostacoli e non ci e' gia transitato in passato. 
- se invece la cella risulta occupata o e' una cella su cui ha gia transitato, ruota di 90 gradi in senso orario ed aspetta lo step successivo. 
- dopo aver ruotato  di 360 gradi senza essere riuscito a spostarsi si ferma. 

Progettare la funzione  percorso(fname, fname1) che presi in input:
- il percorso di un file (fname) contenente l'immagine in formato .png di una scacchiera con ostacoli
- il percorso di un file di tipo .png (fname1) da creare
legge l'immagine della scacchiera in fname, colora di verde le celle della scacchiera percorse dal robottino prima di fermarsi, 
colora di blu la cella in cui il robottino si ferma e registra l'immagine ricolorata nel file fname1. 
Inoltre restituisce una stringa dove in sequanza sono codificati i passi effettuati dal robottino prima di fermarsi. 
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

from IPython.display import Image
import png

def cammino(fname,  fname1):
    p=''    
    colonne=0#Y = COLONNE
    righe=0# X = RIGHE
    passi=0
    a=carica(fname)
    while passi<4:
        while   0<=righe<560 and (a[colonne][righe+40]==(255,255,255) or a[colonne][righe+40]==(0,0,0)):
            b = True
            passi=0
            p+='0'
            
            for c in range(colonne,colonne+40):
                for r in range(righe,righe+40):
                    if b == True:
                        a[c][r]=(0,255,0)
                    else: break
             
            righe+=40                
        b = False 
        passi+=1   
        
        
              
        while 0<=colonne<=520 and (a[colonne+40][righe]==(255,255,255) or a[colonne+40][righe]==(0,0,0)):
            passi=0
            p+='1'
            b = True
            for c in range(colonne,colonne+40):
                for r in range(righe,righe+40):
                    if b == True:
                        a[c][r]=(0,255,0)
                    else: break
            colonne+=40
            
        b = False   
        passi+=1  
        
        
            
        while 40<=righe<=600 and (a[colonne][righe-40]==(255,255,255) or a[colonne][righe-40]==(0,0,0)):
            passi=0
            p+='2'
            b = True
            for c in range(colonne,colonne+40):
                for r in range(righe,righe+40):
                    if b == True:
                        a[c][r]=(0,255,0)
                    else: break
            righe-=40
        b = False
        passi+=1 
        
        while (0<=colonne<=600 and 0<=righe<=600) and (a[colonne-40][righe]==(255,255,255) or a[colonne-40][righe]==(0,0,0)) :
            passi=0
            b = True
            p+='3'
            for c in range(colonne,colonne+40):
                for r in range(righe,righe+40):
                    if b == True:
                        a[c][r]=(0,255,0)
                    else: break
            colonne-=40
        b = False
        passi+=1
                
    blu = (0,0,255)
    for c in range(colonne,colonne+40):
        for r in range(righe,righe+40):
            a[c][r]=blu
                
    salva(a,fname1)
    return p

def carica(fname):
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
    
def salva(a, fname1):
    pngimg = png.from_array(a,'RGB')
    pngimg.save(fname1)

