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
    '''Implementare qui la funzione'''
    l=40
    immagine=load(fname)
    
    indici=trova_indice(immagine,l)     #trova la posisizione dello spigolo della casella
    listacasellerosse=analisi(immagine,indici)
    immagine2,stringa=analisiscacchiera(immagine,listacasellerosse)
    save(immagine2,fname1)  #salva il file nella posizione data
    return stringa

            
def trova_indice(immagine,l):    
    listaindici=[]
    altezza=len(immagine)
    larghezza=len(immagine[0])
    for riga in range(altezza//40):      # numero delle caselle per lato(lungo l'altezza)
        for colonna in range(larghezza//40): #numero delle caselle per lato(lungo la lunghezza)
            indicecolonna=colonna*l   #posione dello spigolo(colonna)
            indiceriga=riga*l         #posizione dello spigolo(riga)
            tupla=indiceriga,indicecolonna    #tupla:riga,colonna
            listaindici.append(tupla)
    return listaindici        #lista delle posizioni delle caselle
    
def analisi(immagine,indici):  
    listacasellerosse=[]
    for riga,c in indici:
        if immagine[riga][c+1]==(255,0,0):
            listacasellerosse.append((riga,c))       
    return listacasellerosse
def analisiscacchiera(immagine,listacasellerosse):
    listacasellepercorse=[]
    r=0
    c=0
    ris=0
    risultato=True
    stringa=''
    k=0
    g=0
    z=0
    h=0
    if c==0 and r==0:
            listacasellepercorse.append((r,c))
    while risultato:
        k=0
        g=0
        z=0
        h=0
        ris=0
        while c<14 and (r*40,(c+1)*40) not in listacasellerosse and (r*40,(c+1)*40) not in listacasellepercorse:
            listacasellepercorse.append((r*40,(c+1)*40))
            stringa=stringa+'0'                
            c=c+1 
            k='c' 
        if  k==0:
            ris+=1
            
        while r<14 and  ((r+1)*40,c*40) not in listacasellerosse and ((r+1)*40,c*40) not in listacasellepercorse:
            listacasellepercorse.append(((r+1)*40,c*40))
            stringa=stringa+'1'
            r=r+1
            z='c'
        if  z==0:
            ris+=1
        while c>0 and (r*40,(c-1)*40) not in listacasellerosse and (r*40,(c-1)*40) not in listacasellepercorse:
            listacasellepercorse.append((r*40,(c-1)*40))
            stringa=stringa+'2'
            c=c-1
            h='c'
        if h==0:
            ris+=1
            
        while r>=1 and ((r-1)*40,c*40) not in listacasellerosse and ((r-1)*40,c*40) not in listacasellepercorse:
            listacasellepercorse.append(((r-1)*40,c*40))
            stringa=stringa+'3'
            r=r-1
            g='c'
           
        if g==0:
            ris+=1
        if ris==4:
            risultato=False
            casellafinale=(r,c)
    immagine2=colora(immagine,listacasellepercorse,casellafinale)        
    return immagine2,stringa  
            
            
            
            
                
            
        
        
    
    
            
    
def colora(immagine,lista,casellafinale): 
   for el in lista:
        r,c=el
        if c<=560 and r<=560:
            for el in  range(r,r+40):
                for el1 in range(c,c+40):
                    immagine[el][el1]=(0,255,0)          
                
   riga,colonna=casellafinale
   if riga*40<=560 and colonna*40<=560:
       for riga in range((riga*40),(riga*40)+40):   
           for col in range(colonna*40,(colonna*40)+40):
               immagine[riga][col]=(0,0,255)
   
   return immagine        



