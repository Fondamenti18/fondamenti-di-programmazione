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
nodes = []
def getNode(x, y):
    for node in nodes:
        if node.x == x and node.y == y: return node
    return None

class Node:
    def __init__(self, x, y, val, arrive):
        self.x = x
        self.y = y
        self.h = abs(self.x - arrive[0]) + abs(self.y - arrive[1])
        self.g = 0
        self.val = val
        self.parent = None
        self.status = 'notchecked'
        self.nearest = []
        
    def setDistanceFromStart(self, parentDistance):
        self.g = parentDistance + 1
    
    def getNearest(self):
        for n in self.nearest:
            n.setDistanceFromStart(self.g)
        return self.nearest
    def getF(self):
        if self.val == 'O': return 99999
        else: return self.h + self.g
        
def isInside(circuit, x, y): return 0 <= x < len(circuit[0]) and 0 <= y < len(circuit)
def isCharTrue(char): return char in " AXBO"


nearest = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]

def genNodes(circuit, arrive):
    for x in range(len(circuit[0])):
        for y in range(len(circuit)):
            if isInside(circuit, x, y) and isCharTrue(circuit[y][x]):
                nodes.append(Node(x, y, circuit[y][x], arrive))

def linkNodes():
    for node in nodes:
        for p in nearest:
            near = getNode(node.x + p[0], node.y + p[1])
            if near != None:
                node.nearest.append(near)
                    
def findNodeByValue(val):
    for node in nodes:
        if node.val == val: return node
    return None


def getNodeWithBestScore(nodes):
    minV, index = 9999999, -1
    for i in range(len(nodes)-1):
        val = nodes[i].getF()
        if val < minV: 
            minV = val
            index = i
            
    return nodes.pop(index)

def findArrive(circuit, verso):
    for x in range(len(circuit[0])):
        for y in range(len(circuit)):
            if circuit[y][x] == '|' and circuit[y][x-verso] == ' ':
                return (x-verso, y)
    
def shouldExit(actualNode, arriveX, arriveY):
    return actualNode.x == arriveX and actualNode.y == arriveY

def findPathTo(startx, starty, arriveX, arriveY):
    start = getNode(startx, starty)
    start.setDistanceFromStart(0)
    start.status = 'close'
    actualNode, path = start, []
    exitL = False
    while not exitL:
        exitL = shouldExit(actualNode, arriveX, arriveY)
        neighbors = actualNode.getNearest()
        for node in neighbors:
            if node.status == 'open':
                if node.getF() + 1 < node.getF(): 
                    node.parent = actualNode
            elif node.status == 'notchecked':
                node.status = 'open'
                node.parent = actualNode        
        choices = list(filter(lambda x: x.status == 'open', sorted(nodes, key= lambda x: x.getF())))
        getNode(choices[0].x, choices[0].y).status = 'close'
        actualNode = choices[0]
    node = getNode(arriveX, arriveY)
    while node != None:
        path.append((node.x, node.y))
        node = node.parent
    return list(reversed(path))
            
            
path = []
start = False

def evaluateCoord(coord, nextpos, v):
    if coord > nextpos:
        if v != -1: return -1                
    elif coord < nextpos:
        if v != 1: return 1 
    elif v != 0: return -v
    return 0

def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty, laps):
    global path
    global start
    if laps != 0:
        start = False
        path.clear()
        nodes.clear()
        return (-vx, -vy)
    if not start:
        start = True
        genNodes(griglia_corrente, (x, y))
        linkNodes()
        arrive = findArrive(griglia_corrente, verso)
        path = findPathTo(x, y, arrive[0], arrive[1])
        path += [(arrive[0] + verso, arrive[1]),(arrive[0] + 2*verso, arrive[1])]
        return (0, 0)
    else:            
        nextPos = path.pop(0)       
        return(evaluateCoord(x, nextPos[0], vx), evaluateCoord(y, nextPos[1], vy))