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
    image=load(fname)
    cammino=path(image)
    save(cammino[0],fname1)
    return cammino[1]

def path(image):
    direction='0'
    path=''
    square=0
    line=0
    changeColor(image,(0, 255, 0),0,40,0)
    flag=True
    while flag:
        find_path=findPath(image,square,line,direction)
        if not(find_path):
            flag=False
            image=changeColor(image,(0, 0, 255),square,square+40,line)
        else:
            square=find_path[0]
            line=find_path[1]
            direction=find_path[2]
            path+=direction
            image=changeColor(image,(0, 255, 0),square,square+40,line)
    return (image,path)

def findPath(image,square,line,direction):
    directionsOrig=['0','1','2','3']
    directions=directionsOrig[int(direction):]
    directions.extend(directionsOrig[:int(direction)])
    counter=0
    while counter<=3:
        free=searchFreeSquare(image,square,line,directions[0])
        if free:
            free.append(directions[0])
            return free
        directions=directions[1:]
        counter+=1
    return 0
    

def searchFreeSquare(image,square,line,direction):
    wrong=[(0, 255, 0),(255, 0, 0)]
    if isIn(square,line,direction):
        if direction=='0' and image[line][square+40] not in wrong:
            return [square+40,line]
        if direction=='2' and image[line][square-40] not in wrong:
            return [square-40,line]
        if direction=='1'  and image[line+40][square] not in wrong:
            return [square,line+40]
        if direction=='3'  and image[line-40][square] not in wrong:
            return [square,line-40] 
    return 0

        
def isIn(square,line,direction):
    if direction=='0':
        return square<560
    if direction=='2':
        return square>0
    if direction=='1':
        return line<560
    if direction=='3':
        return line>0

    
def changeColor(image,c,start,end,line):
    for i in range(line,line+40):
        for x in range (start,end):
            image[i][x]=c
    return image
    
