'''
Obiettivo dell'esercizio e' sviluppare la strategia di gioco di una macchinetta che gira su una pista di formula 1.

Il gioco consiste in un percorso di gara, rappresentato da una griglia di caratteri
(' '=vuoto, '#' = ostacolo, 'A....Z' = auto, '|' = traguardo 'O' = buca tutti gli altri caratteri sono ostacoli)
nella quale si trova la macchina del giocatore (un carattere 'A..Z'), che deve:
    correre attorno alla pista per un intero giro senza sbattere contro ostacoli o altre macchine
    raggiungere il traguardo
    fermarsi senza sbattere (vx=vy=0)

Il punteggio di gioco e' il numero di step che sono stati necessari a percorrere la gara e fermarsi senza sbattere.

Ad ogni istante il simulatore della macchinetta conosce:
    x, y:   la posizione della macchina sulla griglia di gioco
    vx, vy: la velocita' corrente della macchina
Ad ogni step della simulazione il giocatore puo' solo:
    incrementare di 1, decrementare di 1 o lasciare come sono i valodi vx, vy della velocita' (-1,0,+1)
corrispondentemente il simulatore:
    somma gli incrementi/decrementi alle due variabili vx,vy
    somma le velocita' vx,vy alla posizione x,y ottenendo la prossima posizione della macchina
    controlla se la nuova posizione e' vuota
        se la nuova posizione e' occupata (da un ostacolo o da un'altra macchina) il gioco termina senza completare la corsa
        se la posizione contiene una buca si slitta di un carattere a caso fino a restare sulla strada o su un ostacolo
        altrimenti si sposta la macchina sulla nuova posizione
    se il traguardo e' stato raggiunto nella direzione giusta e la macchina e' ferma (vx=vy=0) la gara termina
    altrimenti si riesegue un nuovo step (chiedendo alla funzione 'ai' del giocatore cosa fare)

Il programma che dovete realizzare e' l'AI che guida la macchina, che riceve come input:
    la griglia di gioco del passo precedente (comprese le altre macchine)
    la griglia di gioco del passo corrente (comprese le altre macchine)
    la posizione x,y della propria macchina
    la velocita' vx,vy della propria macchina
    il carattere che individua la vostra macchina
    il verso di rotazione (-1= si parte verso sinistra rispetto al traguardo, +1= si parte verso destra rispetto al traguardo)
    la posizione startx,starty di partenza della macchina
e deve produrre in output la coppia:
    ax, ay  variazione della velocita (coppia di valori -1,0,+1)
La simulazione di tutti i 3 percorsi di gara per la qualificazione (senza visualizzazione) deve impiegare al piu' 1 minuto.

In questo esercizio la valutazione avverra' in tre fasi:
    giro di qualificazione:
        la macchina gira sulla pista di gara da sola, senza altri concorrenti su 3 piste in cui non sono presenti barriere di buche
        superare questa prova da' il punteggio minimo di qualificazione (18)
    giro di premio:
        la macchina gira su una pista di gara simile (ma diversa) da quella "Roma" che contiene barriere di buche
        superare questa prova da' il punteggio di qualificazione 24

    La classifica ottenuta nella qualificazione viene usata per determinare i gironi e poi il torneo di gara della fase successiva
    chi non completa il giro di qualificazione non partecipa al successivo torneo e non e' sufficiente

    Gironi e torneo ad eliminazione:
        (per ogni scontro vengono eseguite due gare, con A a sinistra e B a destra e viceversa)
        viene organizzato un torneo in cui prima si eseguono dei gironi di 4-5 auto
            Le due auto che ottengono il miglior punteggio sul girone partecipano alle eliminatorie successive
            Per ogni gara del girone vengono assegnati:
                3 punti a chi vince la gara
                1 punto per pareggio o scontro
                0 punti a chi perde
                a parita' di punteggio vince la macchina che ha fatto meno incidenti
                a parita' di incidenti viene simulata un'altra gara con una pista con barriere di buche (tipo "roma" per intenderci)

        Le due auto qualificate di ciascun girone partecipano ad una fase eliminatoria a scontro diretto
            l'auto vincente passa il turno (in caso di patta su esegue una gara aggiuntiva con barriere di buche casuali)

    La classifica finale della fase a scontro diretto determina i voti:
        I livelli del torneo ad eliminazione individuano i voti ottenuti, a seconda del numero di partecipanti (per esempio 6 livelli -> 2.1 voti per livello circa)
        Per avere la sufficienza bisogna aver completato almeno il giro di qualificazione sulle diverse piste
        Se una macchina ha ottenuto il voto 24 nella fase di qualificazione, il voto finale dell'esercizio e' almeno 24

COMPORTAMENTO: le auto che usano comportamenti scorrette non superano la qualificazione. Es.
    - precalcolare offline la strategia e inserirla nel programma
    - andare apposta contro l'auto dell'avversario
    - ...

ATTENZIONE: NON usate lettere accentate ne' nel codice ne' nei commenti

'''
import random

import sys

DOWN = "DOWN"
UP = "UP"
DX = "DX"
SX = "SX"
DX_DOWN = "DX_DOWN"
SX_DOWN = "SX_DOWN"
DX_UP = "DX_UP"
SX_UP = "SX_UP"
STOP = "STOP"

QUADRANTE_1 = "QUADRANTE_1"
QUADRANTE_2 = "QUADRANTE_2"
QUADRANTE_3 = "QUADRANTE_3"
QUADRANTE_4 = "QUADRANTE_4"
contapassi = 0

def nextCasellaLibera(griglia_corrente, x, y, vx, vy):
    return isLibera(griglia_corrente, x + vx, y + vy)






def isLibera(griglia_corrente, x, y):
    global griglia_percorsa
    try:
        if griglia_corrente[y][x] == ' ' or griglia_corrente[y][x] == '|':
            if griglia_percorsa[y][x] == ' ' or griglia_percorsa[y][x] == '|':
                return True
        else:
            return False
    except:
        return False



def getCurrentDirection(vx, vy):
    if vx > 0 and vy == 0:
        return DX
    elif vx == 0 and vy < 0:
        return UP
    elif vx == 0 and vy > 0:
        return DOWN
    elif vx < 0 and vy == 0:
        return SX

def getOppositeDirection(move):
    if move == UP:
        return DOWN
    elif move == DOWN:
        return UP
    elif move == DX:
        return SX
    elif move == SX:
        return  DX


def getQuadrante(x, y, altezza, larghezza):
    meta_x = larghezza / 2
    meta_y = altezza / 2
    if x >= meta_x and y >= meta_y:
        return QUADRANTE_4
    elif x >= meta_x and y < meta_y:
        return QUADRANTE_1
    elif x < meta_x and y >= meta_y:
        return QUADRANTE_3
    elif x < meta_x and y < meta_y:
        return QUADRANTE_2

def getPossiblePosition(x, y):
    list_moves = list()
    up = moveCar(UP, x, y)
    down = moveCar(DOWN, x, y)
    sx = moveCar(SX, x, y)
    dx = moveCar(DX, x, y)
    list_moves.append(up)
    list_moves.append(down)
    list_moves.append(sx)
    list_moves.append(dx)
    return list_moves

def returnVelocities(x, y, vx, vy, new_x, new_y):
    velx = 0
    vely = 0
    if vx > 0 or vx < 0 or vy > 0 or vy < 0:
        return stopCar(vx, vy)

    if new_x > x:
        velx = 1
    elif new_x < x:
        velx = -1

    if new_y > y:
        vely = 1
    elif new_y < y:
        vely = -1
    return (velx, vely)


def fillCellsAtIndexes(griglia, x1, y1, x2, y2, sign):
    if x1 < 0:
        x1 = 0
    if x2 < 0:
        x2 = 0
    if y1 < 0:
        y1 = 0
    if y2 < 0:
        y2 = 0
    for i in range(y1,y2 + 1):
        for j in range(x1,x2 + 1):
            try:
                griglia[i][j] = sign
            except:
                continue


def fillOldCells(griglia_percorsa, x, y, vx, vy, quadrante, verso):
    global contapassi
    contapassi += 1

    opposite_direction = getOppositeDirection(getCurrentDirection(vx, vy))
    thr = 6
    distance_from_car = 1
    if verso > 0:
        if opposite_direction == UP and (quadrante == QUADRANTE_2 or quadrante == QUADRANTE_3):
            x1 = x - (thr / 2)
            x2 = x1 + thr
            y2 = y - (distance_from_car + 1)
            y1 = y2 - thr
            fillCellsAtIndexes(griglia_percorsa, int(x1), int(y1), int(x2), int(y2), '#')
        elif opposite_direction == DOWN and (quadrante == QUADRANTE_4 or quadrante == QUADRANTE_1):
            x1 = x - (thr / 2)
            x2 = x1 + thr
            y1 = y + (distance_from_car + 1)
            y2 = y1 + thr

            fillCellsAtIndexes(griglia_percorsa, int(x1), int(y1), int(x2), int(y2), '#')
        elif opposite_direction == DX and (quadrante == QUADRANTE_1 or quadrante == QUADRANTE_2):
            x1 = x + distance_from_car
            x2 = x1 + thr
            y1 = y - (thr / 2)
            y2 = y1 + thr
            fillCellsAtIndexes(griglia_percorsa, int(x1), int(y1), int(x2), int(y2), '#')
        elif opposite_direction == SX and (quadrante == QUADRANTE_3 or quadrante == QUADRANTE_4):
            x2 = x - distance_from_car
            x1 = x2 - thr
            y1 = y - (thr / 2)
            y2 = y1 + thr
            if contapassi > thr + 1:
                fillCellsAtIndexes(griglia_percorsa, int(x1), int(y1), int(x2), int(y2), '#')
    else:
        thr = 20
        if opposite_direction == UP and (quadrante == QUADRANTE_4 or quadrante == QUADRANTE_1):
            x1 = x - (thr / 2)
            x2 = x1 + thr
            y2 = y - (distance_from_car + 1)
            y1 = y2 - thr
            fillCellsAtIndexes(griglia_percorsa, int(x1), int(y1), int(x2), int(y2), '#')
        elif opposite_direction == DOWN and (quadrante == QUADRANTE_2) and x < 20:
            x1 = x - (thr / 2)
            x2 = x1 + thr
            y1 = y + (distance_from_car + 1)
            y2 = y1 + thr
            fillCellsAtIndexes(griglia_percorsa, int(x1), int(y1), int(x2), int(y2), '#')
        elif opposite_direction == DX and (quadrante == QUADRANTE_3 or quadrante == QUADRANTE_4):
            x1 = x + distance_from_car
            x2 = x1 + thr
            y1 = y - (thr / 2)
            y2 = y1 + thr
            fillCellsAtIndexes(griglia_percorsa, int(x1), int(y1), int(x2), int(y2), '#')
        elif opposite_direction == SX and (quadrante == QUADRANTE_1 or quadrante == QUADRANTE_2 or (quadrante == QUADRANTE_3 and x < 20)):
            x2 = x - distance_from_car
            x1 = x2 - thr
            y1 = y - (thr / 2)
            y2 = y1 + thr
            if contapassi > thr + 1:
                fillCellsAtIndexes(griglia_percorsa, int(x1), int(y1), int(x2), int(y2), '#')


def moveCar(move, x, y):
    up = (x, y - 1)
    down = (x, y + 1)
    sx = (x - 1, y)
    dx = (x + 1, y)
    if move == UP:
        return up
    elif move == DOWN:
        return down
    elif move == DX:
        return dx
    elif move == SX:
        return sx

def stopCar(vx, vy):
    ret_x = 0
    ret_y = 0
    if vx > 0:
        ret_x = -1
    if vx < 0:
        ret_x = 1
    if vy > 0:
        ret_y = -1
    if vy < 0:
        ret_y = 1
    return (ret_x, ret_y)

def getNextPosition(verso, griglia_corrente, x, y, vx, vy):
    global griglia_percorsa
    if griglia_corrente[y + 1][x] == '|' or griglia_corrente[y - 1][x] == '|':
        return stopCar(vx, vy)
    ret_x = 0
    ret_y = 0
    if not nextCasellaLibera(griglia_corrente, x, y, vx, vy):
        set_position = getPossiblePosition(x, y)
        random_choise = random.choice(set_position)
        #set_position.remove(random_choise)
        new_x = random_choise[0]
        new_y = random_choise[1]
        countIt = 0
        while not isLibera(griglia_corrente, new_x, new_y):
            countIt += 1
            random_choise = random.choice(set_position)
            if countIt > 10:
                griglia_percorsa = griglia_corrente.copy()
            #set_position.remove(random_choise)
            new_x = random_choise[0]
            new_y = random_choise[1]

        ret_x, ret_y = returnVelocities(x, y, vx, vy, new_x, new_y)
    return (ret_x, ret_y)


first = True

griglia_percorsa = None
countGriglia = dict()
car_initial_position = (0,0)

def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty):
    global first
    global griglia_percorsa
    global car_initial_position
    global countGriglia
    car_initial_position = (startx, starty)
    if first and verso > 0:
        first = False
        griglia_percorsa = griglia_corrente.copy()
        return (1, 0)
    if first and verso < 0:
        first = False
        griglia_percorsa = griglia_corrente.copy()
        return (-1, 0)

    mossa = getNextPosition(verso, griglia_corrente, x, y, vx, vy)
    altezza = len(griglia_corrente)
    larghezza = len(griglia_corrente[0])
    if (x,y) in countGriglia:
        countGriglia[(x,y)] += 1
        if countGriglia[(x,y)] > 10:
            griglia_percorsa = griglia_corrente.copy()
    else:
        countGriglia[(x, y)] = 0

    fillOldCells(griglia_percorsa, x, y, vx, vy, getQuadrante(x, y, altezza, larghezza), verso)
    #for row in range(len(griglia_percorsa)):
        #print(griglia_percorsa[row])

    global  contapassi


    return mossa