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

def canMoveXC(image, riga, colonna):
    #Controlla la cella subito a destra del robot per controllare la presenza
    #di ostacoli o di celle già percorse
    if colonna<560:
        if image[riga][colonna+40]==(255,0,0) or image[riga][colonna+40]==(0,255,0):
            return False
        else:
            return True
    else:
        return False
    
    
def canMoveXD(image, riga, colonna):
    #Controlla la cella subito a sinistra del robot per controllare la presenza
    #di ostacoli o di celle già percorse
    if colonna>=40:
        if image[riga][colonna-40]==(255,0,0) or image[riga][colonna-40]==(0,255,0):
            return False
        else:
            return True
    else:
        return False    
    
    
def canMoveYC(image, riga, colonna):
    #Controlla la cella soprastante il robot per controllare la presenza
    #di ostacoli o di celle già percorse
    if riga>=40:
        if image[riga-40][colonna]==(255,0,0) or image[riga-40][colonna]==(0,255,0):
            return False
        else:
            return True
    else:
        return False    
    
def canMoveYD(image, riga, colonna):
    #Controlla la cella sottostante il robot per controllare la presenza
    #di ostacoli o di celle già percorse
    if riga<560:
        if image[riga+40][colonna]==(255,0,0) or image[riga+40][colonna]==(0,255,0):
            return False
        else:
            return True
    else:
        return False
        
def colorCell(image, indexC, indexR, c):
    #Colora la cella dal quale il robot effettua uno spostamento o sulla quale
    #si ferma
    lato=range(indexC, indexC+40)
    altezza=range(indexR, indexR+40)
    for riga in altezza:
        for colonna in lato:
            image[riga][colonna]=c


def cammino(fname, fname1):
    image=load(fname)
    AxisMovement='XC'
    Path=''
    RotationCount=0
    indexR=0
    indexC=0
    while indexC<=600:
        if RotationCount<4:
            if AxisMovement=='XC':                              #Orientamento a destra
                if canMoveXC(image, indexR, indexC):
                    colorCell(image, indexC, indexR, (0,255,0))
                    Path+='0'
                    RotationCount=0
                    indexC+=40
                else:
                    AxisMovement='YD'
                    RotationCount+=1
            
            if AxisMovement=='YD':                              #Orientamento in basso
                if canMoveYD(image, indexR, indexC):
                    colorCell(image, indexC, indexR, (0,255,0))
                    Path+='1'
                    RotationCount=0
                    indexR+=40
                else:
                    AxisMovement='XD'
                    RotationCount+=1
            
            if AxisMovement=='XD':                              #Orientamento a sinistra
                if canMoveXD(image, indexR, indexC):
                    colorCell(image, indexC, indexR, (0,255,0))
                    Path+='2'
                    RotationCount=0
                    indexC-=40
                else:
                    AxisMovement='YC'
                    RotationCount+=1
                    
            if AxisMovement=='YC':                               #Orientamento in alto
                if canMoveYC(image, indexR, indexC):
                    colorCell(image, indexC, indexR, (0,255,0))
                    Path+='3'
                    RotationCount=0
                    indexR-=40
                else:
                    AxisMovement='XC'
                    RotationCount+=1
        else:
            colorCell(image, indexC, indexR, (0,0,255))
            break
    
    save(image, fname1)
    return Path
                
                    