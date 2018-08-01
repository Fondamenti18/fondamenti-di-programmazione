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

def colora(img, x, y, w, h, c):
     for j in range(y, y+h):      # Per ogni riga j del rettangolo
         for i in range(x, x+w):  # per ogni colonna i della riga j
             img[j][i] = c        # imposta il colore del pixel a c

def cammino(fname,  fname1):
    immagine = load(fname)
    blocco = (255,0,0)
    percorso = (0,255,0)
    fermata = (0,0,255)
    dire = 0
    vel = 40
    contatore = 0 # SE E' QUATTRO E' FINITO IL PERCORSO
    x = 0
    y = 0
    iterazioni = 0
    stringa = ''
    print (contatore)
    while contatore < 4:
        #print (contatore,dire,stringa)
        colora(immagine,x,y,40,40,percorso)
        iterazioni += 1
        
        
        
        if dire == 0:
           
           if x + vel >= len(immagine[0]) or immagine[y][x+vel] == blocco or immagine[y][x+vel] == percorso :
               contatore += 1 
               if dire+1 > 3 :
                  dire = 0
               else :
                  dire += 1
               
               continue
           else:
               x = x + vel
               contatore = 0
               stringa += str(dire)
               continue
        if dire == 1 :
           
           if y + vel >= len(immagine[0]) or immagine[y+vel][x] == blocco or immagine[y+vel][x] == percorso :
               contatore += 1
               if dire+1 > 3 :
                  dire = 0
               else :
                  dire += 1
               continue
           else:
               y = y + vel
               contatore = 0
               stringa += str(dire)
               continue
        if dire == 2 :
           
           if x -vel < 0 or immagine[y][x-vel] == blocco or immagine[y][x-vel] == percorso:
               contatore += 1
               if dire+1 > 3 :
                  dire = 0
               else :
                  dire += 1 
               continue
           else:
               x = x - vel
               contatore = 0
               stringa += str(dire)
               continue
        if dire == 3 :
           
           if y - vel < 0 or immagine[y-vel][x] == blocco or immagine[y-vel][x] == percorso:
               contatore += 1
               if dire+1 > 3 :
                  dire = 0
               else :
                  dire += 1 
               continue
           else:
               y = y - vel
               contatore = 0
               stringa += str(dire)
               continue
        
        
        
    else :
        
        colora(immagine,x,y,40,40,fermata)
        save(immagine,fname1)
        #print('diocane')
    return stringa
    
        
    


    
    
    
    
    
    
    
    
    
    
    
    
cammino('I2.png','t1.png')