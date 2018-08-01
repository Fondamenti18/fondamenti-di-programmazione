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
    immagine = load(fname)
    direzione = 'destra'
    x=0
    y=0
    counter = 0
    percorso = ""
    while True:
        info = checkOstacolo(immagine,direzione,x,y)
        direzione = info[3]                                 #direzione nuova presa da info!
        if info[0] == False:    
            if direzione == "destra":
                percorso += "0"
            elif direzione == "giu":
                percorso += "1"
            elif direzione == "sinistra":
                percorso += "2"
            else:
                percorso += "3"
            counter = 0                                     #il counter conta quante volte cambio la mia direzione dalla posizione in cui sono !Nel momento in cui arriva a 4 vuol dire che non posso piu muovermi e il quadrato lo devo quindi colorare di blu!
            immagine = coloraDiVerde(immagine,x,y)
            x = info[1]
            y = info[2]
        else:
            counter += 1
            if counter == 4:
                immagine = coloraDiBlu(immagine,x,y)
                break
    save(immagine,fname1)
    return percorso
def checkOstacolo(immagine,direzione,x,y):
    direzione_da_ritornare = ""
    x_da_ritornare = x
    y_da_ritornare = y
    ostacolo = False                                           #all'inizio assumo che non ho ostacolo,solo nel momento in cui mi si verifica che il pixel è rosso ne avrò uno !
    if direzione=='destra':
        x_temporanea= x+40
        if inside(immagine,x+40,y):              #se il pixel del quadrato verso destra successivo è rosso allora cambio direzione e dirò che ho un ostacolo
            if immagine[y][x_temporanea]== (255,0,0) or immagine[y][x_temporanea] == (0,255,0):
                direzione_da_ritornare = "giu"
                ostacolo = True
            else:
                x_da_ritornare += 40                              #siccome non ho un ostacolo mi sposto avanti di 40 pixel nella stessa direzione in cui ho iniziato (destra)
                direzione_da_ritornare = direzione
        else:
            direzione_da_ritornare = "giu"
            ostacolo = True
    if direzione == 'giu':
        y_temporanea= y+40
        if inside(immagine,x,y+40):
            if immagine[y_temporanea][x]==(255,0,0) or immagine[y_temporanea][x] == (0,255,0):
                direzione_da_ritornare='sinistra'
                ostacolo = True
            else:
                y_da_ritornare += 40
                direzione_da_ritornare=direzione
        else:
            direzione_da_ritornare='sinistra'
            ostacolo = True
    if direzione =='sinistra':
        x_temporanea=x-40
        if inside(immagine,x-40,y):
            if immagine[y][x_temporanea]==(255,0,0) or immagine[y][x_temporanea] == (0,255,0):
                direzione_da_ritornare='su'
                ostacolo = True
            else:
                x_da_ritornare -= 40
                direzione_da_ritornare=direzione
        else:
            direzione_da_ritornare='su'
            ostacolo = True
    if direzione=='su':
        y_temporanea=y-40
        if inside(immagine,x,y-40):
            if immagine[y_temporanea][x]==(255,0,0) or immagine[y_temporanea][x] == (0,255,0):
                direzione_da_ritornare='destra'
                ostacolo = True
            else:
                y_da_ritornare -= 40
                direzione_da_ritornare=direzione
        else:
            direzione_da_ritornare='destra'
            ostacolo = True
    return (ostacolo,x_da_ritornare,y_da_ritornare,direzione_da_ritornare)        
            
            
def coloraDiBlu(immagine,x,y):
    for i in range(40):
        for j in range(40):
            immagine[i+y][j+x] = (0,0,255)
    return immagine        
            
            
def coloraDiVerde(immagine,x,y):
    for i in range(40):
        for j in range(40):
            immagine[i+y][j+x] = (0,255,0)
    return immagine      




def inside(immagine,x,y):
    if x < 0 or x >= len(immagine[0]) or y < 0 or y >= len(immagine):
        return False
    return True    
