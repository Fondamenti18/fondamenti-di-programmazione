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

from heapq import heappush, heappop
import random, pprint

INF = 99999999
HOLE_PENALTY = 100
nodes = {}
speedLimits = {}
endings = set()

def onEdge(table, x, y): #check if a cell is on the margin of the road
    w = len(table[0])
    h = len(table)
    for vy in range(-1, 2):
        for vx in range(-1, 2):
            if not(0 <= x + vx < w and 0 <= y + vy < h) or table[y+vy][x+vx] not in ' OABX':
                return True
    return False

def getBadNeighs(table, x, y): #number of "bad neighbors" of a node
    w = len(table[0])
    h = len(table)
    c = 0
    for vx, vy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if (0 <= x + vx < w and 0 <= y + vy < h):
            if table[y+vy][x+vx] == 'O':
                c+=1
            elif table[y+vy][x+vx] == ' ':
                c-=1
    for vy in range(-1, 2):
        for vx in range(-1, 2):
            if not(0 <= x + vx < w and 0 <= y + vy < h) or table[y+vy][x+vx] not in ' OABX':
                c+=1
    return max(c, 0)

def getCost(table, x, y): #we assign to each cell a cost
    edge = onEdge(table, x, y)
    if table[y][x] == 'O':
        c = getBadNeighs(table, x, y)
        return HOLE_PENALTY*(c+1) #hole
    if edge: return 1 #on the edge
    return 1

def getDistance(table, x, y): #get distance from the end (without considering the kind of cell)
    return nodes[(x, y)] - (getCost(table, x, y)-1)

def buildMinxLimits(table, x, y, sx, verso):
    global speedLimits
    if (x, y) not in speedLimits: speedLimits[(x, y)] = {}
    if 0 in speedLimits[(x,y)]:
        return None
    ac = getDistance(table, x, y)
    if (verso == -1 or x != sx) and (x-1, y) in nodes and getDistance(table, x-1, y) <= ac:
        buildMinxLimits(table, x-1, y, sx, verso)
        s = speedLimits[(x-1, y)][0]
        if (x+s-1, y) in speedLimits and 0 not in speedLimits[(x+s-1, y)]: buildMinxLimits(table, x+s-1, y, sx, verso)
        good = ((x+s-1, y) in speedLimits and speedLimits[(x+s-1, y)][0] <= s and getDistance(table, x+s-1, y) <= ac)
        speedLimits[(x, y)][0] = s-1 if good else s
    else:
        speedLimits[(x, y)][0] = -1

def buildMaxxLimits(table, x, y, sx, verso):
    global speedLimits
    if (x, y) not in speedLimits: speedLimits[(x, y)] = {}
    if 1 in speedLimits[(x,y)]:
        return None
    ac = getDistance(table, x, y)
    if (verso == 1 or x != sx) and (x+1, y) in nodes and getDistance(table, x+1, y) <= ac:
        buildMaxxLimits(table, x+1, y, sx, verso)
        s = speedLimits[(x+1, y)][1]
        if (x+s+1, y) in speedLimits and 1 not in speedLimits[(x+s+1, y)]: buildMaxxLimits(table, x+s+1, y, sx, verso)
        good = ((x+s+1, y) in speedLimits and speedLimits[(x+s+1, y)][1] >= s and getDistance(table, x+s+1, y) <= ac)
        speedLimits[(x, y)][1] = s+1 if good else s
    else:
        speedLimits[(x, y)][1] = 1

def buildMinyLimits(table, x, y):
    global speedLimits
    if (x, y) not in speedLimits: speedLimits[(x, y)] = {}
    if 2 in speedLimits[(x,y)]:
        return None
    ac = getDistance(table, x, y)
    if (x, y-1) in nodes and getDistance(table, x, y-1) <= ac:
        buildMinyLimits(table, x, y-1)
        s = speedLimits[(x, y-1)][2]
        if (x, y+s-1) in speedLimits and 2 not in speedLimits[(x, y+s-1)]: buildMinyLimits(table, x, y+s-1)
        good = ((x, y+s-1) in speedLimits and speedLimits[(x, y+s-1)][2] <= s and getDistance(table, x, y+s-1) <= ac)
        speedLimits[(x, y)][2] = s-1 if good else s
    else:
        speedLimits[(x, y)][2] = -1

def buildMaxyLimits(table, x, y):
    global speedLimits
    if (x, y) not in speedLimits: speedLimits[(x, y)] = {}
    if 3 in speedLimits[(x,y)]:
        return None
    ac = getDistance(table, x, y)
    if (x, y+1) in nodes and getDistance(table, x, y+1) <= ac:
        buildMaxyLimits(table, x, y+1)
        s = speedLimits[(x, y+1)][3]
        if (x, y+s+1) in speedLimits and 3 not in speedLimits[(x, y+s+1)]: buildMaxyLimits(table, x, y+s+1)
        good = ((x, y+s+1) in speedLimits and speedLimits[(x, y+s+1)][3] >= s and getDistance(table, x, y+s+1) <= ac)
        speedLimits[(x, y)][3] = s+1 if good else s
    else:
        speedLimits[(x, y)][3] = 1

def buildSpeedLimits(table, x, y, sx, verso): #for each node, compute its speed limits
    global speedLimits
    #0 = min_x ; 1 = max_x ; 2 = min_y ; 3 = max_y
    buildMinxLimits(table, x, y, sx, verso)
    buildMaxxLimits(table, x, y, sx, verso)
    buildMinyLimits(table, x, y)
    buildMaxyLimits(table, x, y)
    #speedLimits[(x, y)] = {0:-1, 1:1, 2:-1, 3:1}

def handleHolesOnEndings(table, dr): #change speed limits to handle holes in front of the ending line
    global speedLimits
    dr = -dr
    for end in endings:
        size = 0
        i = end[0] + dr
        inHole = True
        while (i, end[1]) in nodes and inHole:
            if table[end[1]][i] == 'O' and inHole:
                size+=1
            else:
                inHole = False
                if dr == -1: #verso = 1
                    speedLimits[(i, end[1])][1] = max(speedLimits[(i, end[1])][1], size)
                    speedLimits[(end[0], end[1])][1] = max(speedLimits[(end[0], end[1])][1], size+1)
                else: #verso = -1
                    speedLimits[(i, end[1])][0] = min(speedLimits[(i, end[1])][0], -size)
                    speedLimits[(end[0], end[1])][0] = min(speedLimits[(end[0], end[1])][0], -size-1)
            i += dr

def buildGraph(table, verso): #builds the graph from the map
    global nodes, speedLimits, endings
    endings = set()
    h = len(table)
    w = len(table[0])
    Q = [] #priority queue for dijkstra
    for i in range(h):
        for j in range(w):
            if table[i][j] == '|':
                endings.add((j, i))
                speedLimits[(j,i)] = {0:-1, 1:1, 2:-1, 3:1}
                heappush(Q, (0, j, i))
                nodes[(j, i)] = 0
    while len(Q) != 0: #Dijkstra
        act = heappop(Q)
        x, y = act[1], act[2]
        for vy in range(-1, 2):
            for vx in range(-1, 2):
                if (vy != 0 or vx != 0) and (act[0] != 0 or vx != verso):
                    if 0 <= x + vx < w and 0 <= y + vy < h and ((x+vx, y+vy) not in nodes) and table[y+vy][x+vx] in ' OABX':
                        cost = getCost(table, x+vx, y+vy)
                        nodes[(x+vx, y+vy)] = min(nodes.get((x+vx, y+vy), INF), cost + act[0])
                        heappush(Q, (cost + act[0], x+vx, y+vy))

def myPos(table, you): #get position from map
    for r in range(len(table)):
        for c in range(len(table[0])):
            if table[r][c] == you:
                return (c, r)
    return -INF, -INF

def enemyPos(table, you): #returns position of the enemy
    for r in range(len(table)):
        for c in range(len(table[0])):
            if 'A' <= table[r][c] <= 'Z' and 'O' != table[r][c] != you:
                return (c, r)
    return -INF, -INF

def findEnemyStatus(prevTable, actTable, you): #returns actual position of the enemy and his velocity
    x1, y1 = enemyPos(prevTable, you)
    x2, y2 = enemyPos(actTable, you)
    return x2, y2, x2-x1, y2-y1

def isReachable(dx, dy, sx, sy, svx, svy): #is possible to reach (dx, dy) from (sx, sy) with velocity (svx, svy) ?
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (sx+svx+i, sy+svy+j) == (dx, dy):
                return True
    return False

def getExtraCost(table, x, y, ex, ey, evx, evy): #get an extra cost based on possible future positions of the enemy
    if ex < 0 or ey < 0 or (ex, ey) not in nodes:
        return 0
    if isReachable(x, y, ex, ey, evx, evy) and getDistance(table, x, y) <= getDistance(table, ex, ey): #if the cell is reachable from the enemy, gets 50 extra penalty
        dist = abs(x-ex) + abs(y-ey)
        return max(0, 1000 - dist)
    return 0

def brake(vx, vy):
    ax = 0 if vx == 0 else (1 if vx < 0 else -1)
    ay = 0 if vy == 0 else (1 if vy < 0 else -1)
    return ax, ay

def speedPenalty(table, x, y, vx, vy): #speed penalty used in stop function
    if (x, y) not in nodes: return INF
    c = 0 if table[y][x] != 'O' else HOLE_PENALTY
    return max(abs(vx), abs(vy)) + c

def stop(table, x, y, vx, vy): #stop the car: to call if the ending has been passed
    bax, bay = brake(vx, vy)
    nx, ny = x+vx+bax, y+vy+bay
    if (nx, ny) in nodes and table[ny][nx] != 'O':
        return bax, bay
    ret = (bax, bay)
    best = INF
    for ax in range(-1, 2):
        for ay in range(-1, 2):
            nx, ny = x+vx+ax, y+vy+ay
            sp = speedPenalty(table, nx, ny, vx+ax, vy+ay)
            if sp < best or (sp == best and random.choice([0, 1])):
                best = sp
                ret = (ax, ay)
    return ret

def isForward(table, x, y, x2, y2):
    if (x, y) not in nodes or (x2, y2) not in nodes: return False
    return getDistance(table, x2, y2) <= getDistance(table, x, y) and (x2, y2) != (x, y)

def inSpLimits(table, x, y, vx, vy, level=0, MAX_LEVEL=2): #MAX_LEVEL=3 works better but slower
    if (x, y) not in nodes or getCost(table, x, y) > HOLE_PENALTY*2: return False
    if (speedLimits[(x, y)][0] <= vx <= speedLimits[(x, y)][1] and speedLimits[(x, y)][2] <= vy <= speedLimits[(x, y)][3]):
        return True
    if level == MAX_LEVEL:
        return False
    for ax in range(-1, 2):
        for ay in range(-1, 2):
            nx, ny = x+vx+ax, y+vy+ay
            if (nx, ny) in nodes and getCost(table, x, y) <= HOLE_PENALTY*2 and isForward(table, x, y, nx, ny) and inSpLimits(table, nx, ny, vx+ax, vy+ay, level+1):
                return True
    return False

def getRandomMove(table, x, y, vx, vy): #make a random (not stupid) move for the opponent
    ret = (0, 0)
    for ay in range(-1, 2):
        for ax in range(-1, 2):
            nx, ny = x+vx+ax, y+vy+ay
            if isForward(table, x, y, nx, ny) and random.choice([0, 1]):
                ret = (ax, ay)
    return ret

def getTotalCost(table, x, y, ex, ey, evx, evy):
    return getCost(table, x, y) + getExtraCost(table, x, y, ex, ey, evx, evy)

def getBestForChoice(table, x, y, sx, sy, verso, vx, vy, ex, ey, evx, evy, level=1, MAX_LEVEL=4): #  get the best i can do (minimize penalty) ad this coordinate
    if (x, y) in nodes and nodes[(x, y)] == 0:
        return 0 if (vx == 0 or vx // abs(vx) == verso) else INF
    if level == MAX_LEVEL:
        return nodes[(x, y)]
    minCost = INF
    eax, eay = getRandomMove(table, ex, ey, evx, evy)
    for ay in range(-1, 2):
        for ax in range(-1, 2):
            nx, ny = x+vx+ax, y+vy+ay
            if (x != sx or ax != -verso) and isForward(table, x, y, nx, ny) and inSpLimits(table, nx, ny, vx+ax, vy+ay):
                cost = getTotalCost(table, nx, ny, ex, ey, evx, evy)
                if cost < minCost: cost += getBestForChoice(table, nx, ny, sx, sy, verso, vx+ax, vy+ay, ex+evx+eax, ey+evy+eay, evx+eax, evy+eay, level+1)
                minCost = min(minCost, cost)
    return minCost
    #return nodes[(x, y)] + getExtraCost(table, x, y, ex, ey, evx, evy) #basic heuristics (works fine without holes)

def followGraph(ptable, atable, x, y, sx, sy, verso, myvx, myvy): #move following the shortest path on the graph
    if nodes[(x, y)] == 0:
        return brake(myvx, myvy)
    ex, ey, evx, evy = findEnemyStatus(ptable, atable, atable[y][x])
    eax, eay = getRandomMove(atable, ex, ey, evx, evy)
    best, bind = INF, getRandomMove(atable, x, y, myvx, myvy)
    for ay in range(-1, 2):
        for ax in range(-1, 2):
            nx, ny = x+myvx+ax, y+myvy+ay
            if (x != sx or y != sy or ax != -verso) and isForward(atable, x, y, nx, ny) and inSpLimits(atable, nx, ny, myvx+ax, myvy+ay):
                cost = getTotalCost(atable, nx, ny, ex, ey, evx, evy) + getBestForChoice(atable, nx, ny, sx, sy, verso, myvx+ax, myvy+ay, ex+evx+eax, ey+evy+eay, evx+eax, evy+eay)
                if cost < best or (cost == best and random.choice([0,1])):
                    best = cost
                    bind = (ax, ay)
    return bind[0], bind[1]

def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty, laps):
    global nodes, speedLimits, hasFinished
    if x == startx and y == starty and vx == 0 and vy == 0:
        nodes = {}
        speedLimits = {}
        buildGraph(griglia_corrente, verso)
        for i in range(len(griglia_corrente)):
            for j in range(len(griglia_corrente[0])):
                if (j, i) in nodes:
                    buildSpeedLimits(griglia_corrente, j, i, startx, verso)
        handleHolesOnEndings(griglia_corrente, verso)
        #pprint.pprint(speedLimits)

    if laps > 0:
        return stop(griglia_corrente, x, y, vx, vy)
    return followGraph(griglia_precedente, griglia_corrente, x, y, startx, starty, verso, vx, vy)
