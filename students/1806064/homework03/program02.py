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

def cammino(fname,fname1):
    percorso=""
    matrice=load(fname)
    percorso,matrice=controlla_ostacoli(matrice)
    save(matrice,fname1)
    return percorso

def colora_quad(output,y,x,c):
    for j in range(y,y+40):
        for i in range(x,x+40):
            output[j][i]=c
    return output
            
def destra(y,x,matrice,larghezza):
    contapassi=""
    x+=40
    while x<larghezza:
        valore=matrice[y][x]
        if valore!=(255,0,0) and valore!=(0,255,0):
            matrice=colora_quad(matrice,y,x,(0,255,0))
            contapassi+="0"
            x+=40
        else:
            return y,x-40,matrice,contapassi
    x-=40
    return y,x,matrice,contapassi

def basso(y,x,matrice,altezza):
    contapassi=""
    y+=40
    while y<altezza:
        valore=matrice[y][x]
        if valore!=(255,0,0) and valore!=(0,255,0):
            matrice=colora_quad(matrice,y,x,(0,255,0))
            contapassi+="1"
            y+=40
        else:
            return y-40,x,matrice,contapassi
    y-=40
    return y,x,matrice,contapassi

def sinistra(y,x,matrice,larghezza):
    contapassi=""
    x-=40
    while x>=0:
        valore=matrice[y][x]
        if valore!=(255,0,0) and valore!=(0,255,0):
            matrice=colora_quad(matrice,y,x,(0,255,0))
            contapassi+="2"
            x-=40
        else:
            return y,x+40,matrice,contapassi
    x+=40
    return y,x,matrice,contapassi

def alto(y,x,matrice,altezza):
    contapassi=""
    y-=40
    while y>=0:
        valore=matrice[y][x]
        if valore!=(255,0,0) and valore!=(0,255,0):
            matrice=colora_quad(matrice,y,x,(0,255,0))
            contapassi+="3"
            y-=40
        else:
            return y+40,x,matrice,contapassi
    y+=40
    return y,x,matrice,contapassi

def controlla_ostacoli(matrice):
    cammino=""
    contapassi=""
    bloccato=1
    altezza=len(matrice)
    larghezza=len(matrice[0])
    y=0
    x=0
    test1=1
    test2=1
    test3=1
    test4=1
    matrice=colora_quad(matrice,0,0,(0,255,0))
    while (test1 or test2 or test3 or test4)!= 0:
        y,x,matrice,contapassi=destra(y,x,matrice,larghezza)
        test1=verifica_passi(contapassi,test1)
        cammino+=contapassi
        y,x,matrice,contapassi=basso(y,x,matrice,altezza)
        test2=verifica_passi(contapassi,test2)
        cammino+=contapassi
        y,x,matrice,contapassi=sinistra(y,x,matrice,larghezza)
        test3=verifica_passi(contapassi,test3)
        cammino+=contapassi
        y,x,matrice,contapassi=alto(y,x,matrice,altezza)
        test4=verifica_passi(contapassi,test4)
        cammino+=contapassi
    matrice=colora_quad(matrice,y,x,(0,0,255))
    return cammino,matrice

def verifica_passi(contapassi,test):
    if contapassi=="":
        test=0
    else:
        test=1
    return test

        
        
        
        
        
            
                
                
            
        

            
            
            
        
        
    
    




        
        
        
        
    
    
    






