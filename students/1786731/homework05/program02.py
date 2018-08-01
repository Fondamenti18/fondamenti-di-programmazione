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

from random     import randint
from random     import random
import math
import json


# v02   deals successfully with 1 hole barriers  
# v03   implemented double barrier strategy
# v04   improvements on dealing with randomly displaced holes
#       completes rome   (tested over 100 laps)
# v05   implemented 8dir strategy - heuristics to increase velocity from gaussian distribution

# TODO:
# • as soon as we're out of a strategy, ensure we're forwarding in the right direction (set lastDir when we finish a strategy)


lastDir = -999
newDir  = -999
# currentStrategy[0] = -1: no current strategy
# currentStrategy[0] = 0:  horizontal, single barrier strategy
# currentStrategy[0] = 1:  vertical, single barrier
# currentStrategy[0] = 2:  horizontal, double barrier strategy
# currentStrategy[0] = 3:  vertical, double barrier strategy
currentStrategy = (-1, 0, 0)
strategyStep = 0
step    = 1
maximallyExpandedHempisphere = False


# 8 possible directions, 8 possible velocities 
directionVelocities = [ (1,0),  (1,1),  (0,1),  (-1,1),  (-1,0),  (-1,-1),  (0,-1),  (1,-1) ]

def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty, laps):
    global lastDir
    global newDir
    global currentStrategy
    global step
    global maximallyExpandedHempisphere

    # reset state happens in modifyCurrentVelocity(), which is always going to be called last.
    # subsequent calls to the function would already be on reset state afterwards, if laps is > 0
    if lastDir == -999:
        if verso == -1:
            lastDir = 4
        else:
            lastDir = 0


    
    if currentStrategy[0] != -1:
        # result[0]   does it collapse ? if so, delay the strategy
        # result[1]   tuple (vel, vel) strategy delta velocity to return
        result = advanceStrategy(x, y, vx, vy, griglia_corrente)
        if result[0] != 0:
            return result[1]




    # eventually modifies current strategy
    bestRayDir, bestRaySteps, barrierStrategy = bestRaycastPrediction(x, y, griglia_corrente, lastDir) 

    if bestRaySteps > 0:
        # try to follow the bestRayDir
        lastDir = bestRayDir
    else:
        # try to follow previous direction
        bestRayDir = lastDir


    newDir = bestRayDir


    # if we're currently following the direction proposed by BestDir
    if followingCurrentVelocity(vx, vy, bestRayDir):
        # if we can safely increase velocity...
        tvi = testVelocityIncrease(x, y, vx, vy, griglia_corrente)
        if tvi[0]: # if we can
            return tvi[1] # tuple of new delta velocity
    



    # new proposed velocity x
    # in range [-1 ... +1]      will be compared to current velocity to see what we can do
    # this velocity was tested from crashes
    npvx, npvy = nextUnitVelocity(bestRayDir, griglia_corrente, x, y, vx, vy)
    newvx, newvy = modifyCurrentVelocity(x,y, vx, vy, npvx, npvy, griglia_corrente, laps)




    step += 1

    return (newvx, newvy)


# dir is expressed in radians
def bestRaycastPrediction(x, y, griglia, direction):
    global currentStrategy


    bestraydir   = -999
    bestraysteps = -999
    barrierstrategy = (-1, 0, 0)

    # testing the closest 3 directions in the hemisphere to see which one is best 
    for i in range(-1, 2):
        direction = (lastDir + i) % 8  # there are 8 possible directions

        # result[0] maxsteps
        # result[1] eventual barrier strategy
        result = predictRay(x, y, griglia, direction)

        if result[0] > bestraysteps:
            bestraysteps = result[0]
            bestraydir   = direction
            barrierstrategy = result[1]

    if bestraysteps < 3:

        for i in range(-2, 3):
            direction = (lastDir + i) % 8  # there are 8 possible directions

            # result[0] maxsteps
            # result[1] eventual barrier strategy
            result = predictRay(x, y, griglia, direction)

            if result[0] > bestraysteps:
                bestraysteps = result[0]
                bestraydir   = direction
                barrierstrategy = result[1]

    return (bestraydir, bestraysteps, barrierstrategy)


def predictRay(x, y, griglia, direction):

    steps = 0
    holes = []

    # array bounds
    bx = len(griglia[0])
    by = len(griglia)

    while True:
        cx = x + directionVelocities[direction][0] * (steps+1)
        cy = y + directionVelocities[direction][1] * (steps+1)

        # rounded current x
        rcx = int(round(cx))
        rcy = int(round(cy))

        if rcx >= bx or rcx < 0 or rcy >= by or rcy < 0:
            break

        char = griglia[rcy][rcx] 

        if char == ' ' or char == '|' or char.isalpha():
            if char == 'O':
                holes += [(rcx, rcy)]
            steps += 1
        else:
            break


    # barrierstrategy = findHolesBarrier(holes, griglia, direction)
    barrierstrategy = None

    return (steps, barrierstrategy)


def testVelocityIncrease(x,y, vx, vy, griglia):
    
    # test to see if by incrementing the current velocity, we can 
    # safely still brake down to speed 0 

    # proposed delta velocities
    dvx = directionVelocities[lastDir][0]
    dvy = directionVelocities[lastDir][1]

    # used by while iteration, will be modified down to 0
    nvx = vx + dvx
    nvy = vy + dvy

    cx = x
    cy = y
    while nvx != 0 or nvy != 0:
        cx += nvx
        cy += nvy

        if not testGridPoint(cx, cy, griglia):
            return (False, (0, 0))

        # reduce speed by 1
        nvx -= clamp(nvx, -1, 1) 
        nvy -= clamp(nvy, -1, 1) 

    return (True, (dvx, dvy))
    

def followingCurrentVelocity(vx, vy, direction):
    # works even if the velocity is over than [-1 ... +1] range

    dvx = directionVelocities[direction][0]
    dvy = directionVelocities[direction][1]

    cvx = clamp(vx, -1, 1)
    cvy = clamp(vy, -1, 1)

    if dvx == cvx and dvy == cvy:
        return True

    return False


def advanceStrategy(x, y, vx, vy, griglia):
    # returns:
    # (0, (0, 0))    result[0] = wheter this strategy collapses,  result[1] = the delta velocity which follows this strategy

    global currentStrategy
    global strategyStep
    global lastDir
    
    # if we're not yet in the strategy point
    if (x != currentStrategy[1] or y != currentStrategy[2]) and strategyStep == 0:
        # delta position x
        dpx = clamp(currentStrategy[1] - x, -1, 1)
        dpy = clamp(currentStrategy[2] - y, -1, 1)


        dvx = clamp(dpx - vx, -1, 1)
        dvy = clamp(dpy - vy, -1, 1)

        finalvx = -999
        finalvy = -999

        if testGridPoint(x + vx + dvx, y + vy, griglia):
            finalvx = dvx
            finalvy = 0
        
        if testGridPoint(x + vx, y + vy + dvy, griglia):
            finalvx = 0
            finalvy = dvy

        # test full velocity
        if testGridPoint(x + vx + dvx, y + vy + dvy, griglia):
            finalvx = dvx
            finalvy = dvy

        
        if vx == 0 and vy == 0 and finalvx == 0 and finalvy == 0:
            return (0, (0,0)) # zero velocity is the only thing saving us, strategy failed

        if finalvx == -999 and finalvy == -999:
            # if we can't, we should follow the proposed velocity and delay the strategy
            return (0, (0,0))

        return (1, (finalvx, finalvy))



    # from here on, we're in the correct spot or in another step of the strategy



    # zero out velocity before making the first advance, for security reasons. (not doing it will crash in rome)
    if strategyStep == 0 and (vx != 0 or vy != 0):
        dvx = 0 - vx
        dvy = 0 - vy
        return (1, (dvx, dvy))



    # from here on, we're at zero velocity in the correct spot ready to make the first advance, 
    # or at another step of an already started strategy



    targetvx = 0 
    targetvy = 0 

    if currentStrategy[0] == 1 or currentStrategy[0] == 3: # vertical barrier, horizontal pass
        targetvx = clamp(lastDir * ((2 * math.pi) / 8) * 100000, -1, 1)
    if currentStrategy[0] == 0 or currentStrategy[0] == 2: # horizontal barrier, vertical pass
        targetvy = clamp(math.sin(lastDir * ((2 * math.pi) / 8)) * 100000, -1, 1)  # not negated since direction already negated!


    if strategyStep == 0: # correct spot, first advance
        deltavx = targetvx - vx
        deltavy = targetvy - vy

        strategyStep += 1

        return (1, (deltavx, deltavy))        


    if strategyStep == 1: # second advance, pass the hole and reset state
        targetvx *= 2     # to pass the hole, the passing direction needs to be 2
        targetvy *= 2
        
        deltavx = targetvx - vx
        deltavy = targetvy - vy

        strategyStep += 1

        # reset state before leaving, if strategy is for a single line barrier
        if currentStrategy[0] == 0 or currentStrategy[0] == 1:
            currentStrategy = (-1, 0, 0)
            strategyStep = 0

        return  (1, (deltavx, deltavy))  


    if strategyStep == 2: # third advance, double barrier pass
        targetvx *= 3     # to pass the hole, the passing direction needs to be 3 
        targetvy *= 3
        
        deltavx = targetvx - vx
        deltavy = targetvy - vy

        # reset state
        currentStrategy = (-1, 0, 0)
        strategyStep = 0


        return  (1, (deltavx, deltavy))  

    return (0, (0, 0))


def findHolesBarrier(holes, griglia, direction):
    res = (-1, 0, 0)    # res[0]  direction of wall: -1 no wall, 0 horizontal wall, 1 vertical wall    
    
    if len(holes) == 0:
        return res

    for hole in holes:
        hx = hole[0]
        hy = hole[1]

        # check horizontal wall
        if blockedLeft(hx, hy, griglia) and blockedRight(hx, hy, griglia):
            # horizontal wall detected   
            diry = 1 if direction < 4 else -1

            # is it a double horizontal wall ?
            if blockedLeft(hx, hy + diry, griglia) and blockedRight(hx, hy + diry, griglia):
                # find point to reach to make surpassing strategy
                # result[0] = 0 single barrier, 2 = double barrier
                # result[1] = touple (x,y) of strategy point
                result = findHorizontalBarrierStrategy(hx, hy, griglia, direction)
                return (result[0], result[1][0], result[1][1])
        


        # check vertical wall
        if blockedUp(hx, hy, griglia) and blockedDown(hx, hy, griglia):
            # vertical wall detected       
            dirx = 1 if (direction < 3) or (direction > 6) else -1

            # is it a double vertical wall ?
            if blockedUp(hx + dirx, hy, griglia) and blockedDown(hx + dirx, hy, griglia):
                # find point to reach to make surpassing strategy
                # result[0] = 1 single barrier, 3 = double barrier
                # result[1] = touple (x,y) of strategy point
                result = findVerticalBarrierStrategy(hx, hy, griglia, direction)
                return (result[0], result[1][0], result[1][1])
            
    # no barrier found with provided holes
    return res

# non considera la presenza di altri player
def findHorizontalBarrierStrategy(hx, hy, griglia, direction):

    # find every horizontal hole
    holes = [(hx, hy)]
    # left holes
    li = 1
    while True:
        char = charAt(hx - li, hy, griglia)
        li += 1

        if char == 'O':
            holes += [(hx - li, hy)]
        else:
            break
    
    # right holes
    ri = 1
    while True:
        char = charAt(hx + ri, hy, griglia)
        ri += 1

        if char == 'O':
            holes += [(hx + ri, hy)]
        else:
            break


    # find current y direction 
    diry = 1
    if direction > 4:
        diry = -1
    

    for hole in holes:

        pv4 = charAt(hole[0], hole[1] - diry * 4, griglia)
        pv3 = charAt(hole[0], hole[1] - diry * 3, griglia)
        pv1 = charAt(hole[0], hole[1] - diry    , griglia)
        # next point, be sure it is a hole (we're dealing with double barriers)
        npv1 = charAt(hole[0], hole[1] + diry   , griglia)
        # next point, be sure it is free
        npv2 = charAt(hole[0], hole[1] + diry * 2, griglia)
        
        if pv4 == " " and pv3 == " " and pv1 == " " and npv1 == "O" and (npv2 == " " or npv2 == "|"):
            # return info for double barrier strategy
            return (2, (hole[0], hole[1] - diry * 4))

    return (-1, (0, 0))

def findVerticalBarrierStrategy(hx, hy, griglia, direction):

    # find every vertical hole
    holes = [(hx, hy)]
    # upper holes
    ui = 1
    while True:
        char = charAt(hx, hy - ui, griglia)
        ui += 1

        if char == 'O':
            holes += [(hx, hy - ui)]
        else:
            break
    
    # down holes
    di = 1
    while True:
        char = charAt(hx, hy + di, griglia)
        di += 1

        if char == 'O':
            holes += [(hx, hy + di)]
        else:
            break


    # find current x direction 
    dirx = 1
    if direction > 2 and direction < 6:
        dirx = -1
    

    for hole in holes:

        pv4 = charAt(hole[0] - dirx * 4, hole[1], griglia)
        pv3 = charAt(hole[0] - dirx * 3, hole[1], griglia)
        pv1 = charAt(hole[0] - dirx    , hole[1], griglia)

        npv1 = charAt(hole[0] + dirx   , hole[1], griglia)
        npv2 = charAt(hole[0] + dirx * 2, hole[1], griglia)
        
        if pv4 == " " and pv3 == " " and pv1 == " " and npv1 == "O" and (npv2 == " " or npv2 == "|"):
            # return info for double barrier strategy
            return (3, (hole[0] - dirx * 4, hole[1]))

    return (-1, (0, 0))
    


def blockedUp(x, y, griglia):
    i = 0
    while True:
        char = charAt(x, y-i, griglia)  # inverted coordinates since we're computing over array
        i += 1
        if char == 'O':
            continue
        if char == ' ':
            return False
        if char == '#' or char == "":  # in teoria char == "" non dovrebbe mai capitare
            return True     
        

def blockedDown(x, y, griglia):
    i = 0
    while True:
        char = charAt(x, y+i, griglia)  # inverted coordinates since we're computing over array
        i += 1
        if char == 'O':
            continue
        if char == ' ':
            return False
        if char == '#' or char == "":  # in teoria char == "" non dovrebbe mai capitare
            return True     
        

def blockedLeft(x, y, griglia):
    i = 0
    while True:
        char = charAt(x - i, y, griglia)
        i += 1

        if char == 'O':
            continue
        if char == ' ':
            return False
        if char == '#' or char == "":  # in teoria char == "" non dovrebbe mai capitare
            return True     
        
        

def blockedRight(x, y, griglia):
    i = 0
    while True:
        char = charAt(x + i, y, griglia)
        i += 1
        if char == 'O':
            continue
        if char == ' ':
            return False
        if char == '#' or char == "":  # in teoria char == "" non dovrebbe mai capitare
            return True     
        

def nextUnitVelocity(direction, griglia, x, y, cvx, cvy):
    global currentStrategy

    # original vx, we don't want this one modified
    ovx = directionVelocities[direction][0]
    ovy = directionVelocities[direction][1]

    vx = directionVelocities[direction][0]
    vy = directionVelocities[direction][1]

    gx = x + vx
    gy = y + vy

    res = testGridPoint(gx, gy, griglia)
    
    if res == False:

        noxvelocity = testGridPoint(x, gy, griglia)
        noyvelocity = testGridPoint(gx, y, griglia)

        if noxvelocity:
            vx = 0
        if noyvelocity:
            vy = 0

        if noxvelocity and noyvelocity and (vx != 0 or vy != 0):    # they can't be both zero
            # randomly choose one of the two
            if random() < 0.5:
                return (0, vy)
            else:
                return (vx, 0)
        
        if ((not noxvelocity) and (not noyvelocity)) or (vx == 0 and vy == 0):

            gx = x + clamp(ovx, -1, 1)
            gy = y + clamp(ovy, -1, 1)

            # check if blocked by double barrier
            holes = set()
            if charAt(gx, gy, griglia) == 'O':
                holes.add((gx, gy))
            if charAt(gx, y, griglia) == 'O':
                holes.add((gx, y))
            if charAt(x, gy, griglia) == 'O':
                holes.add((x, gy))
            
            barrierstrat = findHolesBarrier(holes, griglia, direction)
            # if we are, make a new strategy for it
            if barrierstrat[0] != -1:

                # if we can jump over this barrier with the next step, don't set a strategy
                if (math.fabs(cvx) > 1 or math.fabs(cvy) > 1) and (testGridPoint(x + cvx, y + cvy, griglia)): 
                    # we can jump over this barrier without making a strategy for it
                    return (vx, vy)

                currentStrategy = barrierstrat
                # skip this step
                return (0, 0)



            # just pick a random working direction
            return pickRandomFreeDirectionVelocity(x, y, griglia)
            
            # pickRandomWorkingVelocity will try instead of us
            # return (0, 0)
    

    return (vx, vy)

# deprecated function
# deprecated function
# deprecated function
def checkHolesWall(x,y, vx, vy, griglia):
    hx = -1
    hy = -1

    if charAt(x+vx, y, griglia) == "O":
        hx = x+vx
        hy = y

    if charAt(x+vx, y+vy, griglia) == "O":
        hx = x+vx
        hy = y+vy

    if charAt(x, y+vy, griglia) == "O":
        hx = x
        hy = y+vy

    bx = len(griglia[0])
    by = len(griglia)
    
    # holes wall can be either horizontal or vertical
    # check surrounding spots
    # for i in range(-1, 2):
    #     for j in range(-1, 2):
    #         # bounds check
    #         if (x+j) >= bx or (x+j) < 0 or (y+i) >= by or (y+i) < 0:
    #             continue

    #         char = griglia[y+i][x+j]

    #         if char == 'O':
    #             hx = x+j
    #             hy = y+i
    #             break

    if hx != -1 and hy != -1:
        holes = 0
        # possible central hole x/y     
        pchx = -1
        pchy = -1

        # horizontal wall check            
        for j in range(-3, 4):
            if (hx+j) < 0 or (hx+j) >= bx:
                continue

            char = griglia[hy][hx+j]
            if char == 'O':
                holes += 1
                # second hole found in this line, possible central one
                if holes > 1:
                    pchx = hx+j
                    pchy = hy

        if holes >= 3:
            return (1, pchx, pchy)


        # reset counter
        holes = 0
        # vertical wall check            
        for i in range(-3, 4):
            if (hy+i) < 0 or (hy+i) >= by:
                continue

            char = griglia[hy+i][hx]
            if char == 'O':
                holes += 1

                # second hole found in this line, possible central one
                if holes > 1:
                    pchx = hx
                    pchy = hy+i
        
        if holes >= 3:
            return (1, pchx, pchy)

    # else return no present wall
    return (0, -1, -1)
    
def charAt(x, y, griglia):
    bx = len(griglia[0])
    by = len(griglia)

    if x >= bx or x < 0 or y >= by or y < 0:
        return ""

    return griglia[y][x]


def pickRandomFreeDirectionVelocity(x, y, griglia):
    randomStartRad = (randint(0, 8) / 8) * 2 * math.pi
    anglestep      = (2 * math.pi) / 8 
    for i in range(8):
        angle = randomStartRad + i * anglestep
        rvx = int(round(math.cos(angle)))
        rvy = int(round(math.sin(angle)))
        if testGridPoint(x + rvx, y + rvy, griglia):
            return (rvx, rvy)

def pickRandomWorkingVelocity(x, y, vx, vy, griglia):
    global newDir

    # prefers the 3 directions closer to what we're forwarding
    tried = 0
    forwrdir = [(newDir + 1) % 8, newDir, (newDir + 7) % 8]
    while True:
        if newDir < 0 or newDir > 7:
            # will try randomly at this point
            break

        randdir = forwrdir[randint(0,2)]
        nrvx = directionVelocities[randdir][0] 
        nrvy = directionVelocities[randdir][1]
        
        if testGridPoint(x + vx + nrvx, y + vy + nrvy, griglia):
            # found a working velocity, j and i will be summed to the current velocity
            return (nrvx, nrvy)

        tried += 1

        if tried > 100:
            break


    # tries against any possible direction
    tried = 0
    while True:
        rndx = randint(-1, 1)
        rndy = randint(-1, 1)
        
        tried += 1

        if testGridPoint(x + vx + rndx, y + vy + rndy, griglia):
            # found a working velocity, j and i will be summed to the current velocity
            return (rndx, rndy)

        if tried > 100:
            # try to hit the best hole as a last resort?
            return (0, 0)


def modifyCurrentVelocity(x,y, vx, vy, nvx, nvy, griglia, laps):
    global lastDir
    global newDir
    global currentStrategy
    global strategyStep
    global step
    global maximallyExpandedHempisphere

    # finishline, reduce velocity, reset state
    if laps > 0:
        nvx = 0
        nvy = 0
        lastDir = -999
        newDir  = -999
        currentStrategy = (-1, 0, 0)
        strategyStep = 0
        step    = 1
        maximallyExpandedHempisphere = False
    
    # if new proposed velocity is zero, something is wrong
    if nvx == 0 and nvy == 0 and laps == 0:
        return pickRandomWorkingVelocity(x, y, vx, vy, griglia)
    
    fvx = 0
    fvy = 0


    deltax = nvx - vx
    deltay = nvy - vy

    deltax = min(max(deltax, -1), 1)    # clamp -1 ... +1
    deltay = min(max(deltay, -1), 1)    # clamp -1 ... +1

    # test where we finish with proposed velocity
    if not testGridPoint(x + vx + deltax, y + vy + deltay, griglia):
        deltax, deltay = pickRandomWorkingVelocity(x, y, vx, vy, griglia)


    return (deltax, deltay)
    


# if out of bounds, returns false
# if not a ' ' or 'O' returns false
# otherwise true
def testGridPoint(px, py, griglia):
    bx = len(griglia[0])
    by = len(griglia)

    if px >= bx or px < 0 or py >= by or py < 0:
        return False

    char = griglia[py][px] 
    if char != ' ' and char != '|' and char != 'X': # and char != 'O':
        return False

    return True

def clamp(t, rangemin, rangemax):
    return min(max(t, rangemin), rangemax)
