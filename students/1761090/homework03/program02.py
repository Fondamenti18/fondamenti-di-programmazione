'''
Un robottino deve muoversi su di una scacchiera di 15 x 15 celle  con celle bianche e nere  ciascuna di lato 40. 
Per rendere il percorso accidentato alcune delle celle della scacchiera contengono ostacoli (queste celle sono  colorate di rosso).

Un  esempio di scacchiera con ostacoli e' dato  dall'immagine 'I1.png'

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Al'inizio il robottino e' posizionato sulla prima cella in alto a sinistra della scacchiera ed e' rivolto verso destra (x crescente). 
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
'''
Classe griglia con unico attributo una lista di liste di quadratoni della scacchiera
I metodi sono abbastanza chiari su quello che fanno
'''
class Griglia:
    def __init__(self):
        self.righe = []

    def aggiungi_riga(self, riga):
        self.righe.append(riga)

    def modifica_riga(self, x, y, tripla):
        self.righe[y][x] = tripla
'''
Crea la griglia partendo dall'immagine, prende il pixel in alto a sinistra di tutti i quadratoni
spostandosi da uno all'altro di 40 pixel (dimensioni quadrato).
Aggiunge un bordo a tutta la griglia per evitare errori di index out of range
'''
def img_to_griglia(img):
    #print('creo griglia...')
    g = Griglia()

    fuori_immagine = (128, 128, 128)

    w,h = len(img[0]), len(img)
    g.aggiungi_riga([fuori_immagine for _ in range(w//40 + 2)])
    for y in range(0, h, 40):
        riga = []
        for x in range(0, w, 40):
            riga.append(img[y][x])

        riga.insert(0, fuori_immagine)
        riga.append(fuori_immagine)
        g.aggiungi_riga(riga)

    g.aggiungi_riga([fuori_immagine for _ in range(w//40 + 2)])
    return g

'''
Cambia il colore del quadrato (x,y) della griglia e anche la corrispettiva area di img
'''

def colora_quadrato(img, griglia, x, y, colore):
    x-=1
    y-=1                    #decremento perché nella griglia c'è il bordo
    for j in range(y*40, (y+1)*40):
        for i in range(x*40, (x+1)*40):
            img[j][i] = colore

    x+=1
    y+=1                    #incremento per tornare alle (x,y) corrette
    griglia.modifica_riga(x,y, colore)

def trova_adiacenti(griglia, x, y):
    lista_adiacenti = [] #lista degli adiacenti al quadrato su cui il robot puo' andare

    adj = [(1,0), (0,1), (-1, 0), (0, -1)] #lista delle distanze dal quadrato ai suoi possibili adiacenti

    for i, j in adj:                    #per ognuno dei possibili adiacenti, controlla se il robot ci puo' andare
        xx, yy = x+i, y+j
        if controlla_quadrato(griglia, xx, yy):
            lista_adiacenti.append((i,j))

    return lista_adiacenti
'''
Controlla che il quadrato non sia ne' rosso, ne' verde, ne' fuori immagine
'''
def controlla_quadrato(griglia, x, y):
    rosso = (255, 0, 0)
    verde = (0,255,0)
    fuori_immagine = (128, 128, 128)
    if griglia.righe[y][x] == rosso:
        return False

    elif griglia.righe[y][x] == verde:
        return False

    elif griglia.righe[y][x] == fuori_immagine:
        return False

    return True



def cammino(fname, fname1):
    img = load(fname)
    g = img_to_griglia(img)
    retString = ''      #stringa delle direzioni da ritornare

    x, y = 1, 1         #posizione iniziale in alto a sinistra
    d = 0               #indice  per la direzione attuale (all'inizio e' destra)
    direzioni = [(1,0), (0,1), (-1,0), (0,-1)] #(1,0) = destra, (0,1) = giu, (-1,0) = sinsitra, (0,-1) = su

    rosso = (255, 0, 0)
    verde = (0,255,0)
    blu = (0,0,255)
    fuori_immagine = (128, 128, 128)

    while True:
        
        colora_quadrato(img, g, x, y, verde) #colora il quadrato su cui sta il robot di verde
        
        adiacenti = trova_adiacenti(g, x, y) #trova gli adiacenti al quadrato su cui il robot puo' andare
        if direzioni[d] in adiacenti:   #se la direzione attuale sta in adiacenti allora il robot puo' proseguire
            pass
        else:                           #altrimenti deve cambiare direzione
            if adiacenti:
                while direzioni[d] not in adiacenti:    #cambia direzione finche' puo', ma solo se ci sono quadrati validi
                    d = (d+1)%4
            else:                       #se non ci sono, interrompe e colora di blu
                colora_quadrato(img, g, x, y, blu)
                break

        x+=direzioni[d][0]          #cambia la posizione attuale aumentandola a seconda della direzione scelta
        y+=direzioni[d][1]
        retString+=str(d)           #aggiunge la direzione scelta alla stringa da ritornare
    save(img, fname1) 
    return retString