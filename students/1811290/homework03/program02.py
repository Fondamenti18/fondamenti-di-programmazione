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
import png

def cammino(fname,fname1):
    '''Implementare qui la funzione'''
    img=load(fname)
    stringa_azioni=''
    riga_iniziale=0
    col_iniziale=0
    img1=img
    direzione=0
    rotazioni_fatte=0
    while rotazioni_fatte < 4:
        rotazioni_fatte=0
        for rotazioni_fatte in range (0,4):
            #capisco dove dovrei andare
            nuove_coordinate = prossima_casella (riga_iniziale,col_iniziale,direzione)
            riga_possibile = nuove_coordinate[0]
            col_possibile = nuove_coordinate[1]
            #controllo se e' cella valida
            if cella_ok (riga_possibile,col_possibile,img1):
                #coloro di verde la casella
                colora_casella_verde (riga_iniziale,col_iniziale,img1)
                #mi riposiziono sulla cella dove posso andare
                riga_iniziale=riga_possibile
                col_iniziale=col_possibile
                #aggiorno la stringa del movimento
                stringa_azioni=stringa_azioni+str(direzione)
                break
            else:
                #ruoto di 90 gradi
                if direzione > 2:
                    direzione = -1
                direzione += 1
                rotazioni_fatte +=1           
    colora_casella_blue (riga_iniziale,col_iniziale,img1)
    save(img1,fname1)
    return stringa_azioni

def colora_casella_verde (riga_iniziale,col_iniziale,img1):
    for k in range (riga_iniziale,riga_iniziale+40):
        for k1 in range (col_iniziale,col_iniziale+40):
            img1[k][k1]=(0,255,0)
    return img1

def colora_casella_blue (riga_iniziale,col_iniziale,img1):
    for k in range (riga_iniziale,riga_iniziale+40):
        for k1 in range (col_iniziale,col_iniziale+40):
            img1[k][k1]=(0,0,255)
    return img1

def prossima_casella (riga_iniziale,col_iniziale,direzione):
    nuove_coordinate = [0,0]
    if direzione == 0:
        col_iniziale+=40
    if direzione == 1:
        riga_iniziale+=40
    if direzione == 2:
        col_iniziale-=40
    if direzione == 3:
        riga_iniziale-=40
    nuove_coordinate[0] = riga_iniziale
    nuove_coordinate[1] = col_iniziale
    return nuove_coordinate

def cella_ok (riga_possibile,col_possibile,img1):
    if riga_possibile < 0 or riga_possibile > 599:
        #ascisse fuori dalla scacchiera
        return False
    if col_possibile < 0 or col_possibile > 599:
        #ordinate fuori dalla scacchiera
        return False
    if img1[riga_possibile][col_possibile]==(0,255,0):
        #cella verde
        return False
    if img1[riga_possibile][col_possibile]==(255,0,0):
        #cella rossa
        return False
    return True
 
def load(fname):
    """ Carica la immagine PNG dal file fname.
        Torna una lista di liste di pixel.
        Ogni pixel è una tupla (R, G, B) dei 3 colori.
        Ciascun colore è un intero tra 0 e 255 compresi.
    """
    with open(fname, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            l = []
            for i in range(0, len(line), 3):
                l+=[(line[i], line[i+1], line[i+2])]
            img+=[l]
        return img

def save(img,fname1):
    """ Salva la immagine img  nel file filename in formato PNG8.
        Img e' una lista di liste di pixel.
        Ogni pixel è una tupla (R, G, B) dei 3 colori.
        Ciascun colore è un intero tra 0 e 255 compresi.
    """
    pngimg = png.from_array(img,'RGB')
    pngimg.save(fname1)


#cammino('I1.png','prova1.png')
