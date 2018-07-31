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

def pastelli(picture,longitudine,latitudine):
    for i in range(latitudine, latitudine+40):
        for c in range(longitudine, longitudine+40):
            picture[i][c]=(0,255,0)
    return picture 



def freno(picture,longitudine,latitudine,daje,contatore,ctrl=False):
    for i in range(latitudine, latitudine+40):
        for c in range(longitudine, longitudine+40):
            picture[i][c]=(0,0,255)
    mooseeca=0   
    ctrl=False
    return [picture,longitudine, latitudine, contatore, mooseeca,daje,ctrl]              





def destra(picture,longitudine,latitudine,daje,contatore,ctrl):
    if longitudine==len(picture)-40:
        contatore+=1
        mooseeca=1
        return [picture,longitudine,latitudine,contatore,mooseeca,daje,ctrl]
    elif picture[latitudine][longitudine+40]!=(0,0,0) and picture[latitudine][longitudine+40]!=(255,255,255):
        mooseeca=1
        contatore+=1
        return[picture,longitudine,latitudine,contatore,mooseeca,daje,ctrl]
    elif picture[latitudine][longitudine+40]==(0,0,0) or picture[latitudine][longitudine+40]==(255,255,255):
        mooseeca=0
        contatore=0
        picture=pastelli(picture,longitudine,latitudine)
        longitudine+=40
        daje+='0'
        return[picture,longitudine, latitudine, contatore, mooseeca,daje,ctrl]
        
        
        
def giu(picture,longitudine,latitudine,daje,contatore,ctrl):
    if latitudine==len(picture)-40:
        contatore+=1
        mooseeca=2
        return [picture,longitudine,latitudine,contatore,mooseeca,daje,ctrl]
    elif picture[latitudine+40][longitudine]!=(0,0,0) and picture[latitudine+40][longitudine]!=(255,255,255):
        mooseeca=2
        contatore+=1
        return[picture,longitudine,latitudine,contatore,mooseeca,daje,ctrl]
    elif picture[latitudine+40][longitudine]==(0,0,0) or picture[latitudine+40][longitudine]==(255,255,255):
        mooseeca=1
        contatore=0
        picture=pastelli(picture,longitudine,latitudine)
        latitudine+=40
        daje+='1'
        return[picture,longitudine, latitudine, contatore, mooseeca,daje,ctrl]   
        
        
def sinistra(picture,longitudine,latitudine,daje,contatore,ctrl):
    if longitudine==0:
        contatore+=1
        mooseeca=3
        return [picture,longitudine,latitudine,contatore,mooseeca,daje,ctrl]
    elif picture[latitudine][longitudine-40]!=(0,0,0) and picture[latitudine][longitudine-40]!=(255,255,255):
        mooseeca=3
        contatore+=1
        return [picture,longitudine,latitudine,contatore,mooseeca,daje,ctrl]
    elif picture[latitudine][longitudine-40]==(0,0,0) or picture[latitudine][longitudine-40]==(255,255,255):
        mooseeca=2
        contatore=0
        picture=pastelli(picture,longitudine,latitudine)
        longitudine-=40
        daje+='2'
        return [picture,longitudine, latitudine, contatore, mooseeca,daje,ctrl] 

           
        
def su(picture,longitudine,latitudine,daje,contatore,ctrl):
    if latitudine==0:
        contatore+=1
        mooseeca=0
        return [picture,longitudine,latitudine,contatore,mooseeca,daje,ctrl]
    elif picture[latitudine-40][longitudine]!=(0,0,0) and picture[latitudine-40][longitudine]!=(255,255,255):
        mooseeca=0
        contatore+=1
        return [picture,longitudine,latitudine,contatore,mooseeca,daje,ctrl]
    elif picture[latitudine-40][longitudine]==(0,0,0) or picture[latitudine-40][longitudine]==(255,255,255):
        mooseeca=3
        contatore=0
        picture=pastelli(picture,longitudine,latitudine)
        latitudine-=40
        daje+='3'
        return [picture,longitudine, latitudine, contatore, mooseeca,daje,ctrl]           
    
    
            
            
            
            
            
def vittoria(picture,longitudine,latitudine,contatore,mooseeca,daje,ctrl=True):
    if contatore>4:
        return freno(picture,longitudine,latitudine,daje,contatore,ctrl)
    elif mooseeca ==0:
        return destra(picture,longitudine,latitudine,daje,contatore,ctrl)
    elif mooseeca ==1:
        return giu(picture,longitudine,latitudine,daje,contatore,ctrl)
    elif mooseeca ==2:
        return sinistra(picture,longitudine,latitudine,daje,contatore,ctrl)
    elif mooseeca ==3:
        return su(picture,longitudine,latitudine,daje,contatore,ctrl)
    
        
 


def cammino(file, file1):
    '''Implementare qui la funzione'''
    picture=load(file)
    longitudine=0
    latitudine=0
    mooseeca=0
    daje=''
    contatore=0
    ctrl=True
    lista=[picture,longitudine,latitudine,contatore,mooseeca,daje,ctrl]
    while 1:
        lista=vittoria(*lista)
        if  lista[6]==False:
            break
    save(picture,file1)
    return lista[5]
            
        
            