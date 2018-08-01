
from immagini import *

def cammino(fname,  fname1):
    ''' Funzione principale '''
    # leggo immmagine
    vet = load(fname)   # scacchiera
    x,y = 0,0           # coordinate robottino
    direz = 0           # direzione in cui punta
    gradi = 0           # quanti gradi ha ruotato
    mov = ''            # movimenti
    
    # finche' robottino non ha girato completamente
    while gradi < 5:
        # punta a destra
        if direz == 0:
            #print(1)
            vet, x,y, direz, gradi, mov = destra(vet,x,y,direz,gradi,mov)
        elif direz == 1:
            vet, x,y, direz, gradi, mov = giu(vet,x,y,direz,gradi,mov)
        # punta a sinistra    
        elif direz == 2:
            vet, x,y, direz, gradi, mov = sinistra(vet, x,y, direz, gradi, mov)
        # punta su
        else:
            vet, x,y, direz, gradi, mov = su(vet, x,y, direz, gradi, mov)
    
    # salvo nuova immagine
    save(vet, fname1)
    return mov
    

def colora(vet, x,y, color):
    ''' funzione che colora 40 caselle alla volta del  vettore '''
    limX, limY = x+40, y+40         # fino a dove devo colorare
    # finche' non coloro tutte le caselle
    while y < limY:
        while x < limX:
            vet[y][x] = color       # coloro pixel
            x += 1                  # incremento 
        x -= 40                     # x torna dove era all'inizio
        y += 1                      # ncremento
    return vet
    
def destra(vet, x,y, direz, gradi, mov):
    ''' robot si muove verso destra '''
    # se ha ruotato 360 gradi
    if gradi == 4:
        vet = colora(vet, x,y, (0,0,255))   # coloro di blu casella in cui si trova
        return vet, 0,0, 0, 5, mov
    # se davanti non e' ne' verde ne' rosso e non vado fuori dall'immagine
    if (x+40 < len(vet[0])) and (vet[y][x+40]!=(255,0,0) and vet[y][x+40]!=(0,255,0)):
        vet = colora(vet, x,y, (0,255,0))   # coloro di verde casella in cui si trova
        mov += '0'
        return vet, x+40,y, direz, 0, mov
    # se davanti non puo' andare
    return vet, x,y, direz+1, gradi+1, mov

def giu(vet, x,y, direz, gradi, mov):
    ''' robot prova ad andare verso il basso '''
    # se ha ruotato 360 gradi
    if gradi == 4:
        vet = colora(vet, x,y, (0,0,255))   # blu
        return vet, 0,0, 0, 5, mov
    # davanti libero
    if (y+40 < len(vet)) and (vet[y+40][x]!=(255,0,0) and vet[y+40][x]!=(0,255,0)):
        vet = colora(vet, x,y, (0,255,0))   # verde
        mov += '1'
        return vet, x,y+40, direz, 0, mov
    # davanti bloccato
    return vet, x,y, direz+1, gradi+1, mov

def sinistra(vet, x,y, direz, gradi, mov):
    ''' robot si muove verso sinistra '''
    # se ha ruotato di 360
    if gradi == 4:
        vet = colora(vet, x,y, (0,0,255))  # blu
        return vet, 0,0, 0, 5, mov
    # davanti libero
    if (x-40 >= 0) and (vet[y][x-40]!=(255,0,0) and vet[y][x-40]!=(0,255,0)):
        vet = colora(vet, x,y, (0,255,0))  # verde
        mov += '2'
        return vet, x-40,y, direz, 0, mov
    # davanti bloccato
    return vet, x,y, direz+1, gradi+1, mov

def su(vet, x,y, direz, gradi, mov):
    ''' robot si muove verso l'alto '''
    # se ha ruotato di 360
    if gradi == 4:
        vet = colora(vet, x,y, (0,0,255)) # blu
        return vet, 0,0, 0, 5, mov
    # davanti libero
    if (y-40 >= 0) and (vet[y-40][x]!=(255,0,0) and vet[y-40][x]!=(0,255,0)):
        vet = colora(vet, x,y, (0,255,0)) # verde
        mov += '3'
        return vet, x,y-40, direz, 0, mov
    # davanti bloccato
    return vet, x,y, 0, gradi+1, mov
