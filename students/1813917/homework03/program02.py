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

def cammino(fname, fname1):
    img = load(fname)
    new_img, passi= check_cella(rimpicciolire(img))
    big_img = ingrandire(new_img)
    save(big_img, fname1)
    return passi
    
    
def rimpicciolire(img):
    new_img = []
    new_riga = []
    for riga in range(0,600, 40):
        for pixel in range(0,600 ,40):
            new_pixel = img[riga][pixel]
            new_riga.append(new_pixel)
        new_img.append(new_riga)
        new_riga = []
    return new_img

def check_cella(img):
    riga = 0
    pixel = 0
    rosso = (255,0,0)
    verde = (0,255,0)
    passi = ''
    
    while img[riga][pixel] != (0,0,255):
    # Provo Dx
        if len(passi) == 0 or passi[-1] == '0':
            try:
                if img[riga][pixel + 1] == rosso or img[riga][pixel + 1] == verde or pixel > 14:
                    raise DxOccupato
                else:
                    colora_cella(img, riga, pixel)
                    pixel += 1
                    passi += '0'
                
            except (DxOccupato, IndexError):
                try:
                    if img[riga + 1][pixel] == rosso or img[riga + 1][pixel] == verde or riga > 14:
                        raise GiuOccupato
                    else:
                        colora_cella(img, riga, pixel)
                        riga += 1
                        passi += '1'
                    
                except (GiuOccupato, IndexError):
                    try:
                        if img[riga - 1][pixel] == rosso or img[riga - 1][pixel] == verde or (riga - 1) < 0:
                            raise SuOccupato
                        else:
                            colora_cella(img, riga, pixel)
                            riga -= 1
                            passi += '3'
                        
                    except SuOccupato:
                        img[riga][pixel] = (0,0,255)
        # Provo giu               
        elif passi[-1] == '1':
            try:
                if img[riga + 1][pixel] == rosso or img[riga + 1][pixel] == verde or riga > 14:
                    raise GiuOccupato
                else:
                    colora_cella(img, riga, pixel)
                    riga += 1
                    passi += '1'
                
            except (GiuOccupato, IndexError):
                try:
                    if img[riga][pixel - 1] == rosso or img[riga][pixel - 1] == verde or (pixel - 1) < 0:
                        raise SxOccupato
                    else:
                        colora_cella(img, riga, pixel)
                        pixel -= 1
                        passi += '2'
                    
                except SxOccupato:
                    try:
                        if img[riga][pixel + 1] == rosso or img[riga][pixel + 1] == verde or pixel > 14:
                            raise DxOccupato
                        else:
                            colora_cella(img, riga, pixel)
                            pixel += 1
                            passi += '0'
                        
                    except DxOccupato:
                        img[riga][pixel] = (0,0,255)
        
        # Provo sx
        elif passi[-1] == '2':
            try:
                if img[riga][pixel - 1] == rosso or img[riga][pixel - 1] == verde or (pixel - 1) < 0:
                    raise SxOccupato
                else:
                    colora_cella(img, riga, pixel)
                    pixel -= 1
                    passi += '2'
                
            except SxOccupato:
                try:
                    if img[riga - 1][pixel] == rosso or img[riga - 1][pixel] == verde or (riga - 1) < 0:
                        raise SuOccupato
                    else:
                        colora_cella(img, riga, pixel)
                        riga -= 1
                        passi += '3'
                    
                except SuOccupato:
                    try:
                        if img[riga + 1][pixel] == rosso or img[riga + 1][pixel] == verde or riga > 14:
                            raise GiuOccupato
                        else:
                            colora_cella(img, riga, pixel)
                            riga += 1
                            passi += '1'
                        
                    except GiuOccupato:
                        img[riga][pixel] = (0,0,255)
                        
        # Provo su
        elif passi[-1] == '3':
            try:
                if img[riga - 1][pixel] == rosso or img[riga - 1][pixel] == verde or (riga - 1) < 0:
                    raise SuOccupato
                else:
                    colora_cella(img, riga, pixel)
                    riga -= 1
                    passi += '3'
                
            except SuOccupato:
                try:
                    if img[riga][pixel + 1] == rosso or img[riga][pixel + 1] == verde or pixel > 14:
                        raise DxOccupato
                    else:
                        colora_cella(img, riga, pixel)
                        pixel += 1
                        passi += '0'
                    
                except (DxOccupato, IndexError):
                    try:
                        if img[riga][pixel - 1] == rosso or img[riga][pixel - 1] == verde or (pixel - 1) < 0:
                            raise SxOccupato
                        else:
                            colora_cella(img, riga, pixel)
                            pixel -= 1
                            passi += '2'
                        
                    except SxOccupato:
                        img[riga][pixel] = (0,0,255)
            
            
    return img,passi

def ingrandire(img):
    new_img = []
    new_riga = []
    for riga in img:
        for pixel in riga:
            new_riga += [pixel] * 40
        new_img += [new_riga] * 40
        new_riga = []
    return new_img

def colora_cella(img, riga, pixel):
    img[riga][pixel] = (0,255,0)
    

class DxOccupato(Exception):
    pass
class SxOccupato(Exception):
    pass
class GiuOccupato(Exception):
    pass
class SuOccupato(Exception):
    pass
