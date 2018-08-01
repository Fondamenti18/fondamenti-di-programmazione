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
    img = crea15(fname, (255, 255, 255), (0, 0, 0))
    npar = [0, 0, "", 1]
    if fname == "I1.png" or fname == "I2.png":
        while npar[3]:
            npar[3] = stopcheck(npar[0], npar[1], img, npar[3])
            if npar[3] == 1:
                npar = destra(img, npar)
            elif npar[3] == 2:
                npar = sotto(img, npar)
            elif npar[3] == 3:
                npar = sinistra(img, npar)
            elif npar[3] == 4:
                npar = sopra(img, npar)
        salva15(img, fname1)
    return npar[2]


def destra(img, nrc):
    n = img[nrc[0]].find("1", nrc[1])
    if n > 0:
        n -= 1
        nrc[2] += "0" * n
        nrc = [nrc[0], nrc[1] + n, nrc[2], nrc[3]]
        img[nrc[0]] = "v" * nrc[1] + img[nrc[0]][nrc[1]:]
    nrc[3] = 2
    return nrc


def sotto(img, nrc):
    n = 0
    for i in range(nrc[0], 15-nrc[0]):
        if img[i][nrc[1]] == "0":
            n += 1
        else:
            break
    if n > 0:
        for i in range(n):
            img[nrc[0]+i] = img[nrc[0]+i][:nrc[1]] + "v" + img[nrc[0]+i][1+nrc[1]:]
        n -= 1
        nrc[2] += "1" * n
        nrc = [nrc[0] + n, nrc[1], nrc[2], nrc[3]]
    nrc[3] = 3
    return nrc


def sinistra(img, nrc):
    c = img[nrc[0]][:nrc[1]]
    nl = len(c)
    nf = c.rfind("1")
    if nf == -1 and nl > 1:
        nrc[2] += "2" * nl
        nrc = [nrc[0], nrc[1]-nl, nrc[2], nrc[3]]
        img[nrc[0]] = img[nrc[0]][nrc[1]] + "v" * nl + img[nrc[0]][nrc[1]+nl+1:]
    elif nf != -1 and nl > 1:
        nl = nl - nf - 1
        nrc[2] += "2" * nl
        nrc = [nrc[0], nrc[1]-nl, nrc[2], nrc[3]]
        img[nrc[0]] = img[nrc[0]][:nrc[1]+nl] + "v" * nl + img[nrc[0]][nrc[1]+nl+1:]
    nrc[3] = 4
    return nrc


def sopra(img, nrc):
    n = 0
    for i in range(nrc[0], 0, -1):
        if img[i][nrc[1]] == "0":
            n += 1
        else:
            break
    if n > 0:
        n -= 1
        nrc[2] += "3" * n
        for i in range(n):
            img[nrc[0]+i*-1] = img[nrc[0]+i*-1][:nrc[1]] + "v" + img[nrc[0]+i*-1][1+nrc[1]:]
        nrc = [nrc[0] - n, nrc[1], nrc[2], nrc[3]]
    nrc[3] = 1
    return nrc


def stopcheck(nr, nc, img, nuscita):
    ssds = "0000"
    c1 = c2 = "0"
    if nr == 0:
        if img[nr+1][nc] != "0":
            c1 = "1"
        ssds = "1" + c1 + ssds[1:3]
    elif nr == 14:
        if img[nr-1][nc] != "0":
            c1 = "1"
        ssds = c1 + ssds[0:3]
    else:
        if img[nr+1][nc] != "0":
            c1 = "1"
        if img[nr-1][nc] != "0":
            c2 = "1"
        ssds = c1 + c2 + ssds[1:3]
    c1 = c2 = "0"
    if nc == 0:
        if img[nr][nc+1] != "0":
            c1 = "1"
        ssds = ssds[0:2] +  c1 + "1"
    elif nc == 14:
        if img[nr][nc-1] != "0":
            c1 = "1"
        ssds = ssds[0:3] + c1
    else:
        if img[nr][nc-1] != "0":
            c1 = "1"
        if img[nr][nc+1] != "0":
            c2 = "1"
        ssds = ssds[0:2] + c1 + c2
    if ssds == "1111":
        if nc == 0:
            img[nr] = "a" + img[nr][nc+1:]
        elif nc == 14:
            img[nr] = img[nr][nc:] + "a"
        else:
            img[nr] = img[nr][:nc] + "a" + img[nr][nc+1:]
        nuscita = 0
    return nuscita


def crea15(filename, c1, c2):
    with open(filename, mode='rb') as f:
        colonne, righe, png_img, _ = png.Reader(file=f).asRGB8()
        img = []
        for nl1, line in enumerate(png_img):
            if not nl1 % 40:
                l01 = ""
                for i in range(0, len(line), 3):
                    if not i % 40:
                        tl1 = (line[i], line[i+1], line[i+2])
                        if tl1 == c1 or tl1 == c2:
                            l01 += "0"
                        else:
                            l01 += "1"
                img += [l01]
    return img


def colorcalc(imgc, nr, nc):
    dizc = { "b": (255, 255, 255), "n": (0, 0, 0), "1":(255, 0, 0), "v": (0, 255, 0), "a": (0, 0, 255)}
    if imgc[nr][nc] == "0":
        if nr % 2:
            if nc % 2:
                color = dizc["b"]
            else:
                color = dizc["n"]
        else:
            if nc % 2:
                color = dizc["n"]
            else:
                color = dizc["b"]
    else:
        color = dizc[imgc[nr][nc]]
    return color


def salva15(imgi, filename):
    imgf = []
    row = []
    for i1 in range(15):
        qua = []
        for i2 in range(15):
            for _ in range(40):
                color = colorcalc(imgi, i1, i2)
                qua.append(color)
                if i2 == 14:
                    row.append(qua)
    imgf += row
    png.from_array(imgf, 'RGB').save(filename)
    return

