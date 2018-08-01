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
import math



global fullCoords
fullCoords = [(0,0),(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1)]

global simplifiedCoords
simplifiedCoords = [(0,0),(1,1),(1,-1),(-1,1),(-1,-1)]

global downhillTrack
downhillTrack = 0
global otherCarsMap
otherCarsMap = 0
global finishLinePosition
finishLinePosition = [0,0,0]


def exploreCoordsForDownHillTrack(nextWaveFront, track, cost, downhillTrack, startingPos, impactPoint):
    coordExpansionList = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1)]
    for coordE in coordExpansionList:
        nextCoordX = impactPoint[0] + coordE[0]
        nextCoordY = impactPoint[1] + coordE[1]
        if ((track[nextCoordY][nextCoordX] == "#") or (track[nextCoordY][nextCoordX] == "|")):
            continue
        if (cost < downhillTrack[nextCoordY][nextCoordX]):
            downhillTrack[nextCoordY][nextCoordX] = cost
            if ((nextCoordX == startingPos[0]) and (nextCoordY == startingPos[1])):
                   # return downhillTrack
                return True
            nextWaveFront.append((nextCoordX,nextCoordY))
    return False


def giveMeDownhillTrack(track, startingPos, targetPos):
    downhillTrack = [[1000000 for x in range(len(track[0]))] for y in range(len(track))]
    waveFront = [targetPos]
    
    cost = 0
    track[targetPos[1]][targetPos[0]]

    downhillTrack[targetPos[1]][targetPos[0]] = 0
    
    while (len(waveFront) > 0):
        cost += 1
        nextWaveFront = []
        for impactPoint in waveFront:
            if (exploreCoordsForDownHillTrack(nextWaveFront,track,cost,downhillTrack,startingPos,impactPoint)):
                return downhillTrack
        waveFront = nextWaveFront
                
    return downhillTrack

class node:
    def __init__(self,posX,posY,velX,velY,distance,parentNode):
        self.posX = posX
        self.posY = posY
        self.velX = velX
        self.velY = velY
        self.distance = distance
        self.parentNode = parentNode

def isOutOfMap(pX,pY,bX,bY):
    return ((pX<0) or (pY<0) or (pX>=bX) or (pY>=bY))

def exploreCoords(coordExpansionList,downhillTrack,realTrack,myNode,panickMode):
    nodesList = []
    for el in coordExpansionList:
        newPosX = myNode.posX+myNode.velX+el[0]
        newPosY = myNode.posY+myNode.velY+el[1]
        if (isOutOfMap(newPosX,newPosY,len(downhillTrack[0]),len(downhillTrack))):
            continue
#        if ((abs(myNode.velX+el[0])>5) or (abs(myNode.velY+el[1])>5)): #better safe than sorry
#            continue
        diff = downhillTrack[newPosY][newPosX] - downhillTrack[myNode.posY][myNode.posX]
        if ((diff<-60) or (diff > 0)):
            continue
        if ((realTrack[newPosY][newPosX] == "O") and not panickMode):
            continue
        
        nodesList.append(node(newPosX,newPosY,myNode.velX+el[0],myNode.velY+el[1],downhillTrack[newPosY][newPosX],myNode))
    return nodesList

def getCoordsForMoves(deepness):
    global fullCoords
    global simplifiedCoords
    
    if (deepness<2):
        coordExpansionList = fullCoords
    else:
        coordExpansionList = simplifiedCoords
    return coordExpansionList


def chooseIfLoopShouldContinueBasedOnBranchValue(bestB,thisB,velX,velY):
    if (thisB[0]<=bestB[0]):
        if (thisB[0]==bestB[0]):
            if (bestB[3]<=thisB[3]):
                return True
        bestB[0] = thisB[0]
        bestB[1] = velX
        bestB[2] = velY
        bestB[3] = thisB[3]
    return False

    
def findNextMoveRec(downhillTrack, myNode, deepness, realTrack, otherCarsTrack, panickMode):
    
    coordExpansionList = getCoordsForMoves(deepness)
    
    if (deepness > 8):
        return [myNode.distance,0,0,myNode.distance]
    
    if (myNode.distance <= -1):
        return [myNode.distance+deepness-20+abs(myNode.velX)*2+abs(myNode.velY),0,0,myNode.distance+deepness-20+abs(myNode.velX)*2+abs(myNode.velY)]
 
#    if (otherCarsTrack[myNode.posY][myNode.posX]>0):
 #       return [1000000,0,0,100000]
    
    nodesList = exploreCoords(coordExpansionList,downhillTrack,realTrack,myNode,panickMode)

    
    best = [1000000,0,0,100000]   
    for el in nodesList:
        branchValue = findNextMoveRec(downhillTrack, el, deepness+1, realTrack, otherCarsTrack, panickMode)
        if (chooseIfLoopShouldContinueBasedOnBranchValue(best,branchValue, el.velX, el.velY)):
            continue
    best[3] = myNode.distance
    if (deepness==1):
        best[0] += otherCarsTrack[myNode.posY][myNode.posX]
    return best
 

def findFinishLineYBound(grid, position, direction):
    shift = -1
    for cnt in range(0,5):
        if (grid[position[1] + cnt*direction][position[0]] != "|"):
            shift = cnt - 1
            break
    if (shift < 0):
        return 0
    else: 
        return shift
    
def findFinishLineSquaresList(grid, finishLineStart, finishLineLength, xDirection):
    finishLineList = list()
    for cnt in range(finishLineStart[1], finishLineStart[1]+finishLineLength):
        if (grid[cnt][finishLineStart[0]] == "|"):
            finishLineList.append((finishLineStart[0],cnt))
    xPos = finishLineStart[0] + xDirection
    playersLineList = list()
    for cnt in range(finishLineStart[1], finishLineStart[1]+finishLineLength):
        if (grid[cnt][xPos] != "#"):
            playersLineList.append((xPos,cnt))
    return (finishLineList,playersLineList)

    

def findFinishLinePosition(grid, startingPosition, direction):
#    print("verso",direction,grid[startingPosition[1]][startingPosition[0]])
    shift = -1
    for cnt in range(0,10):
        if (grid[startingPosition[1]][startingPosition[0] - cnt*direction] == "|"):
            shift = cnt
            break
    fallbackFinishLineC = [startingPosition[0] - direction, startingPosition[1]]
    fallbackPlayerLineC = [startingPosition[0] , startingPosition[1]]
    
    fallbackReturn = [[fallbackFinishLineC],[fallbackPlayerLineC]]    
    if (shift < 0):
        return fallbackReturn
    xPos = startingPosition[0] - shift*direction
    
    northernStretch = findFinishLineYBound(grid, [xPos,startingPosition[1]], -1)
    southernStretch = findFinishLineYBound(grid, [xPos,startingPosition[1]],  1)
    return findFinishLineSquaresList(grid, [xPos,startingPosition[1] - northernStretch], northernStretch+southernStretch + 1, direction)
    

global finishLineData
finishLineData = 0    

global otherCarsData
otherCarsData = 0
    
def normalizeIntoRange(n):
    if (n > 1):
        n = 1
    elif (n < -1):
        n= -1
    return n

def braking(vX,vY):
    x = 0
    y = 0
    if (vX>0):
        x = -1
    if (vX<0):
        x = 1
    if (vY>0):
        y = -1
    if (vY<0):
        y = 1
    return (x,y)    

def findOtherCarsPosition(grid, myCar):
    carsDict = dict()
    gW = len(grid[0])
    gH = len(grid)
    for rowC in range(0,gH):
        for elC in range(0,gW):
            el = grid[rowC][elC]
            if ((el >= "A") and (el <= "Z") and el!=myCar and el!="O"):
                carsDict[el] = (elC,rowC)
    return carsDict
    

def calcOtherCarsData(currentGrid, previousGrid, myCar):
    carsP = findOtherCarsPosition(previousGrid, myCar)
    carsN = findOtherCarsPosition(currentGrid, myCar)
    fullDict = dict()
    for k in carsP:
        if (k in carsN):
            carKNPos = carsN[k]
            carkPPos = carsP[k]
            velX = carKNPos[0] - carkPPos[0]
            velY = carKNPos[1] - carkPPos[1]
            fullDict[k] = [carKNPos[0], carKNPos[1], velX, velY]
    return fullDict
            
def modifyDownHillTrackWorker(downhillTrack, carsData, revertingFactor):
    global fullCoords
    bX = len(downhillTrack[0])
    bY = len(downhillTrack)
    if (carsData):
        for k in carsData:
            carPos = carsData[k]
           # print("modifying track",carPos)
            for el in fullCoords:
                x=carPos[0]+carPos[2]+el[0]
                y=carPos[1]+carPos[3]+el[1]
                if (not isOutOfMap(x,y,bX,bY)):
                    downhillTrack[y][x] += revertingFactor*2
                   # print("x,y,rf",x,y,revertingFactor)
            downhillTrack[carPos[1]][carPos[0]] += revertingFactor*1
    

def modifyOtherCarsTrack(downhillTrack, currentCarsData, formerCarsData):
    if (downhillTrack):
        modifyDownHillTrackWorker(downhillTrack, formerCarsData, -1)
        modifyDownHillTrackWorker(downhillTrack, currentCarsData, 1)            
    
def initAllTheStuff(griglia_corrente, startx, starty, verso, x, y):
    fLD = findFinishLinePosition(griglia_corrente, (startx, starty), verso)
    dT = giveMeDownhillTrack(griglia_corrente, (x,y),(fLD[0][0][0]-(verso),starty))
    oCM = [[0 for x in range(len(griglia_corrente[0]))] for y in range(len(griglia_corrente))]
    return fLD,dT,oCM


def modifyTrackOnFinishLine(finishLineData,downhillTrack):
 #   for el in finishLineData[1]:
  #      downhillTrack[el[1]][el[0]] = -4
    for el in finishLineData[0]:
        downhillTrack[el[1]][el[0]] = -3


def decideNextStep(griglia_corrente, griglia_precedente, car, otherCarsMap, otherCarsData, downhillTrack,x,y,vx,vy):
    newOtherCarsData = calcOtherCarsData(griglia_corrente, griglia_precedente,car)
    modifyOtherCarsTrack(otherCarsMap, newOtherCarsData, otherCarsData)
    otherCarsData = newOtherCarsData
        
    v = findNextMoveRec(downhillTrack, node(x,y,vx,vy,downhillTrack[y][x],0),0,griglia_corrente, otherCarsMap, False)
    if (v[0]>10000):
        v=findNextMoveRec(downhillTrack, node(x,y,vx,vy,downhillTrack[y][x],0),0,griglia_corrente, otherCarsMap, True)
    aX = v[1] - vx
    aY = v[2] - vy
    aX = normalizeIntoRange(aX)
    aY = normalizeIntoRange(aY)
    return (aX,aY)    

def needReset(isLapDone, x, startx, y, starty):
    return (isLapDone or ((x==startx) and (y==starty)))
    
def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty, isLapDone):
    global downhillTrack
    global finishLineData
    global otherCarsData
    global otherCarsMap
    if needReset(isLapDone, x, startx, y, starty):
        downhillTrack = 0
        otherCarsMap = 0
        finishLineData = 0
        otherCarsData = 0
        
    if (isLapDone):
        return braking(vx,vy)
    
    
    if (not downhillTrack):
        finishLineData, downhillTrack,otherCarsMap = initAllTheStuff(griglia_corrente, startx, starty, verso, x, y)

    if ((x!=startx) or (y!=starty)):
        modifyTrackOnFinishLine(finishLineData,downhillTrack)
    
    return decideNextStep(griglia_corrente, griglia_precedente, car, otherCarsMap, otherCarsData, downhillTrack,x,y,vx,vy)

    
