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

def cammino(fname,  fname1):    
    #-------------------
    stringa = ''
    stop = 0
    state = 0
    iadd = 0
    kadd = 40
    i = 0
    k = 0
    #-------------------
    immagine = load(fname)
    #-------------------
    
    def rotate(iadd,kadd,state):
        if state == 0:
            iadd = 40
            kadd = 0
            state = 1
            return iadd,kadd,state
        if state == 1:
            iadd = 0
            kadd = -40
            state = 2
            return iadd,kadd,state
        if state == 2:
            iadd = -40
            kadd = 0
            state = 3
            return iadd,kadd,state
        if state == 3:
            iadd = 0
            kadd = 40
            state = 0
            return iadd,kadd,state

    def move(i,k,iadd,kadd,stringa):
        green(i,k)
        i = i+iadd
        k = k+kadd
        #print('Moving...')
        stringa+=str(state)
        stop = 0
        return i,k,stop,stringa

    def search(i,k,iadd,kadd,stop,state):
        result = True
        try:
            if immagine[i+iadd][k+kadd]==(0,255,0) or immagine[i+iadd][k+kadd]==(255,0,0) or i+iadd<0 or k+kadd<0:
                #print('Red/Green tile: rotate')
                iadd,kadd,state = rotate(iadd,kadd,state)
                stop+=1
                result = False
        except IndexError:
            #print('Out of bounds: rotate')
            iadd,kadd,state = rotate(iadd,kadd,state)
            stop+=1
            result = False
        
        return result,stop,iadd,kadd,state

    def green(i,k):
        iagg = i+40
        kagg = k+40
        keep = k
        #while i < i +40
        #while k < k +40
        #print('Greening up...')
        while(i<iagg):
            k = keep
            while(k<kagg):
                immagine[i][k]=(0,255,0)
                k+=1
            i+=1
            
    def blue(i,k):
        iagg = i+40
        kagg = k+40
        keep = k
        while(i<iagg):
            k = keep
            while(k<kagg):
                immagine[i][k]=(0,0,255)
                k+=1
            i+=1

        
    while stop!=6:
        #print('i:',i,'k:',k)
        #print('stop:',stop)
        #print('state:',state)
        result,stop,iadd,kadd,state = search(i,k,iadd,kadd,stop,state)
        if result:
            i,k,stop,stringa = move(i,k,iadd,kadd,stringa)
    blue(i,k)
    
    save(immagine, fname1)
    return stringa
