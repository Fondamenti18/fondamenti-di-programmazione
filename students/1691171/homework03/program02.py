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

from immagini import load, save

LIBEROB = 0
LIBERON = 1
OSTACOLO = 2
PASSATO = 3
FERMATA = 4
RIGHE = 15
COLONNE = 15
LARGHEZZA_COLONNA = 40
CENTRO = LARGHEZZA_COLONNA // 2
DIR = [
    (0, 1), # destra 0
    (1, 0), # giu 1
    (0, -1), # sinistra 2
    (-1, 0) # su 3
]


def leggi_matrice(image):
    mat = []
    i = 0
    while i < RIGHE:
        r = []
        j = 0
        while j < COLONNE:
            if image[i*LARGHEZZA_COLONNA+CENTRO][j*LARGHEZZA_COLONNA+CENTRO] == (255,255,255):
                r.append(LIBEROB)
            elif image[i*LARGHEZZA_COLONNA+CENTRO][j*LARGHEZZA_COLONNA+CENTRO] == (0,0,0):
                r.append(LIBERON)
            elif image[i*LARGHEZZA_COLONNA+CENTRO][j*LARGHEZZA_COLONNA+CENTRO] == (255,0,0):
                r.append(OSTACOLO)
            j += 1
        mat.append(r)
        i += 1
    return mat


def prox_direzione(DIREZIONI, dir):
    if dir == 3:
        dir = 0
    else:
        dir += 1
    if not DIREZIONI[dir]:
        return dir
    return -1


def reset_direzioni(DIREZIONI):
    i = 0
    while i < len(DIREZIONI):
        DIREZIONI[i] = False
        i+=1


def posizione_valida(posi, posj, image):
    if posi < 0 or posi >= len(image) or posj < 0 or posj >= len(image[0]):
        return False
    return image[posi][posj] == LIBEROB or image[posi][posj] == LIBERON


def disegna_quadrato(image2, i, j, c):
    k = i * LARGHEZZA_COLONNA
    kf = k + LARGHEZZA_COLONNA
    while k < kf:
        m = j * LARGHEZZA_COLONNA
        mf = m + LARGHEZZA_COLONNA
        while m < mf:
            image2[k][m] = c
            m+=1
        k+=1

def esporta_image(mat, image, fname1):
    len_mat = len(mat)
    len_mat0 = len(mat[0])
    i = 0
    while i < len_mat:
        j = 0
        while j < len_mat0:
            if mat[i][j] == LIBEROB:
                disegna_quadrato(image, i, j, (255,255,255))
            elif mat[i][j] == LIBERON:
                disegna_quadrato(image, i, j, (0,0,0))
            elif mat[i][j] == OSTACOLO:
                disegna_quadrato(image, i, j, (255, 0, 0))
            elif mat[i][j] == PASSATO:
                disegna_quadrato(image, i, j, (0, 255, 0))
            else:
                disegna_quadrato(image, i, j, (0, 0, 255))
            j += 1
        i += 1
    save(image, fname1)

def cammino(fname,  fname1):
    ris = ''
    DIREZIONI = [False] * 4
    image = load(fname)
    mat = leggi_matrice(image)
    posi = 0
    posj = 0
    dir = 0
    mat[posi][posj] = PASSATO
    while dir != -1:
        dest_posi = posi + DIR[dir][0]
        dest_posj = posj + DIR[dir][1]
        DIREZIONI[dir] = True
        if posizione_valida(dest_posi, dest_posj, mat):
            ris = ris + str(dir)
            posi = dest_posi
            posj = dest_posj
            mat[posi][posj] = PASSATO
            reset_direzioni(DIREZIONI)
        else:
            dir = prox_direzione(DIREZIONI, dir)
    mat[posi][posj] = FERMATA
    esporta_image(mat, image, fname1)
    return ris