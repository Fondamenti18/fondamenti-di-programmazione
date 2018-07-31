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
    
    img = load(fname)
    lato = len(img)/40
    scacchiera = [[0 for x in range(len(img[0]))] for y in range(len(img))]

    posizione = (0, 0)
    direzione = (0, 1)
    sequenza = ""

    for i in range(len(img)):
        for j in range(len(img[i])):
            scacchiera[i][j] = img[i][j]
    while(1):
        if(direzione[0] == 0 and direzione[1] == 0): #UP
            for i in range(posizione[0], 0, -40):
                if((img[i][posizione[1]][0] == 255 and img[i][posizione[1]][1] == 255 and img[i][posizione[1]][2] == 255) or (img[i][posizione[1]][0] == 0 and img[i][posizione[1]][1] == 0 and img[i][posizione[1]][2] == 0)):
                    scacchiera[i][posizione[1]] = (0,255,0)
                    sequenza += '3'
                else:
                    if((posizione[1] + 1 < lato) and (img[i + 1][posizione[1] + 1][0] == 255 and img[i + 1][posizione[1] + 1][1] == 255 and img[i + 1][posizione[1] + 1][2] == 255) or (img[i + 1][posizione[1] + 1][0] == 0 and img[i + 1][posizione[1] + 1][1] == 0 and img[i + 1][posizione[1] + 1][2] == 0)):
                        posizione = (i + 40, posizione[1] + 40)
                        direzione = (0, 1)
                        break
                    elif((posizione[1] - 1 > 0) and (img[i + 1][posizione[1] - 1][0] == 255 and img[i + 1][posizione[1] - 1][1] == 255 and img[i + 1][posizione[1] - 1][2] == 255) or (img[i + 1][posizione[1] - 1][0] == 0 and img[i + 1][posizione[1] - 1][1] == 0 and img[i + 1][posizione[1] - 1][2] == 0)):
                        posizione = (i + 40, posizione[1] - 40)
                        direzione = (1, 1)
                        break
                    else:
                        scacchiera[i][posizione[1]] = (0,0,255)
                        save(scacchiera, fname1)
                        return sequenza
        elif(direzione[0] == 0 and direzione[1] == 1): #Destra
            for i in range(posizione[1], len(img), 40):
                if((img[posizione[0]][i] == (255,255,255)) or (img[posizione[0]][i] == (0,0,0))):
                    scacchiera[posizione[0]][i] = (0,255,0)
                    sequenza += '0'
                else:
                    sequenza = sequenza[:-1]
                    if((posizione[0] + 1 < lato) and (img[posizione[0] + 1][i -1] == (255,255,255)) or (img[posizione[0] + 1][i - 1] == (0,0,0))):
                        posizione = (posizione[0] + 40, i - 40)
                        direzione = (1, 0)
                        break
                    elif((posizione[0] - 1 > lato) and (img[posizione[0] - 1][i - 1][0] == 255 and img[posizione[0] - 1][i - 1][1] == 255 and img[posizione[0] - 1][i - 1][2] == 255) or (img[posizione[0] - 1][i - 1][0] == 0 and img[posizione[0] - 1][i -1][1] == 0 and img[posizione[0] - 1][i - 1][2] == 0)):
                        posizione = (posizione[0] - 40, i - 40)
                        direzione = (0, 0)
                        break
                    else:
                        scacchiera[posizione[0]][i] = (0,0,255)
                        save(scacchiera, fname1)
                        return sequenza
        elif(direzione[0] == 1 and direzione[1] == 0): #DOWN
            for i in range(posizione[0], len(img), 40):
                if((img[i][posizione[1]][0] == 255 and img[i][posizione[1]][1] == 255 and img[i][posizione[1]][2] == 255) or (img[i][posizione[1]][0] == 0 and img[i][posizione[1]][1] == 0 and img[i][posizione[1]][2] == 0)):
                    scacchiera[i][posizione[1]] = (0,255,0)
                    sequenza += '1'
                else:
                    if((posizione[1] - 1 > 0) and (img[i - 1][posizione[1] -1][0] == 255 and img[i - 1][posizione[1] -1][1] == 255 and img[i - 1][posizione[1] - 1][2] == 255) or (img[i - 1][posizione[1] - 1][0] == 0 and img[i - 1][posizione[1] - 1][1] == 0 and img[i - 1][posizione[1] - 1][2] == 0)):
                        posizione = (i - 40, posizione[1] - 40)
                        direzione = (1, 1)
                        break
                    elif((posizione[1] + 1 < lato) and (img[i - 1][posizione[1] + 1][0] == 255 and img[i - 1][posizione[1] + 1][1] == 255 and img[i - 1][posizione[1] + 1][2] == 255) or (img[i - 1][posizione[1] + 1][0] == 0 and img[i - 1][posizione[1] +1][1] == 0 and img[i - 1][posizione[1] + 1][2] == 0)):
                        posizione = (i - 40, posizione[1] + 40)
                        direzione = (0, 1)
                        break
                    else:
                        scacchiera[i][posizione[1]] = (0,0,255)
                        save(scacchiera, fname1)
                        return sequenza
        else:
            for i in range(posizione[1], 0, -40):
                if(img[posizione[0]][i] == (255,255,255) or img[posizione[0]][i] == (0,0,0)):
                    scacchiera[posizione[0]][i] = (0,255,0)
                    sequenza += '2'
                    #print(sequenza)
                else:
                    if((posizione[0] - 1 > 0) and (img[posizione[0] - 1][i + 1] == (255,255,255)) or (img[posizione[0] - 1][i + 1] == (0,0,0))):
                        posizione = (posizione[0] - 40, i + 40)
                        direzione = (0, 0)
                        break
                    elif((posizione[0] + 1 < lato) and (img[posizione[0] + 1][i + 1][0] == 255 and img[posizione[0] + 1][i + 1][1] == 255 and img[posizione[0] + 1][i + 1][2] == 255) or (img[posizione[0] + 1][i + 1][0] == 0 and img[posizione[0] + 1][i + 1][1] == 0 and img[posizione[0] + 1][i + 1][2] == 0)):
                        posizione = (posizione[0] + 40, i + 40)
                        direzione = (1, 0)
                        break
                    else:
                        scacchiera[posizione[0]][i] = (0,0,255)
                        save(scacchiera, fname1)
                        return sequenza