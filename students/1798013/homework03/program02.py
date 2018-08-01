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
import png
def cambia_colore(immagine,riga,colonna,colore):
    for riga_x in range(0,40):
        for colonna_x in range(0,40):
            immagine[riga*40+riga_x][colonna*40+colonna_x] = colore

            
    


def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    nostro_cammino = ""
    immagine = load(fname)
    rosso = (255,0,0)
    bianco = (255,255,255)
    nero = (0,0,0)
    verde = (0,255,0)
    blu = (0,0,255)
    riga = 0
    colonna = 0
    movimento = 1
    movimenti = 0
    while 0 == 0:
        if movimento == 1:
            incr_colonna = 1
            incr_riga = 0
        elif movimento == 2:
            incr_colonna = 0
            incr_riga = 1
        elif movimento == 3:
            incr_colonna = -1
            incr_riga = 0
        else:
            incr_colonna = 0
            incr_riga = -1
        riga_nuova = riga + incr_riga
        colonna_nuova = colonna + incr_colonna
        if riga_nuova > 14 or riga_nuova < 0 or colonna_nuova > 14 or colonna_nuova < 0:
            if movimenti == 4:
                cambia_colore(immagine,riga,colonna,blu)
                break
            else:
                movimenti = movimenti + 1
                movimento = movimento + 1
                if movimento > 4:
                    movimento = 1
        else:
            colore = immagine[riga_nuova*40][colonna_nuova*40]
            if colore == bianco or colore == nero:
                cambia_colore(immagine,riga,colonna,verde)
                riga = riga_nuova
                colonna = colonna_nuova
                nostro_cammino = nostro_cammino + str(movimento-1)
                movimenti = 0
            else:
                movimenti = movimenti + 1
                if movimenti > 4:
                    cambia_colore(immagine,riga,colonna,blu)
                    break
                movimento = movimento + 1
                if movimento > 4:
                    movimento = 1
    save(immagine,fname1)
    return nostro_cammino

    
    
   

    
    
          


