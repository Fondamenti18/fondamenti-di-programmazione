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
    (NUOVO) il numero di attraversamenti del traguardo fatti dalla macchina (contromano se negativo)
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

import copy


'''

    CONSTANTS

'''

ROAD = ' '
WALL = '#'
HOLE = 'O'
GOAL = '|'
CARS = ['A', 'B', 'C']
CAR = 'X'

'''

    VARIABLES

'''

finalPath = []
matrixCopy = None

'''

    CLASSES

'''

# MATRIX
class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.xMax = len(matrix[0])
        self.yMax = len(matrix)

    def inBounds (self, x, y):
        return 0 <= x < self.xMax and 0 <= y < self.yMax

    def getMatrix (self):
        return self.matrix

# NODE
class Node:
    
    # COMMONS BASE ATTRIBUTES
    
    matrixObj = None
    visitedNodes = None
    
    # INIT

    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.value = Node.matrixObj.getMatrix()[y][x]
        self.cost = cost
        self.id = str(x)+'-'+str(y)
        self.neighborsCords = []
        self.goalsCords = []
        self.holesCords = []
        self.roadCords = []
        self.wallsCords = []
        self.carCords = []
        self.neighborsNodes = []
        self.goalsNodes = []
        self.holesNodes = []
        self.roadNodes = []
        self.wallsNodes = []
        self.carNodes = []
        self.checkNeighborsCords() #set my cords arrs

    # GETTERS

    def getCords (self):
        return (self.x, self.y)

    def getCost (self):
        return self.cost

    def getId (self):
        return self.id

    def getNeighborsCords (self):
        return self.neighborsCords

    def getGoalsCords (self):
        return self.goalsCords

    def getHolesCords (self):
        return self.holesCords

    def getRoadCords (self):
        return self.roadCords

    def getCarCords (self):
        return self.carCords

    def getNeighborsNodes (self):
        return self.neighborsNodes

    def getGoalsNodes (self):
        return self.goalsNodes

    def getHolesNodes (self):
        return self.holesNodes

    def getRoadNodes (self):
        return self.roadNodes

    def getCarNodes (self):
        return self.carNodes

    def getPreviousNode(self):
        
        for cords in (self.getRoadCords() + self.getCarCords()):
            
            id = str(cords[0])+'-'+str(cords[1])
            
            node = Node.visitedNodes.get(id, None)
            
            if node != None:
                if (self.cost - node.getCost()) == 1:
                    
                    return node
                    break
    
    # SETTERS

    def checkNeighborsCords (self):
        
        neighborsCords = [(self.x+1, self.y),(self.x+1, self.y+1), (self.x, self.y+1), (self.x-1, self.y+1), (self.x-1, self.y), (self.x-1, self.y-1), (self.x, self.y-1), (self.x+1, self.y-1)]
        
        mtr = Node.matrixObj.getMatrix()

        for cords in neighborsCords:
            
            x = cords[0]
            y = cords[1]
            
            # check cords are in matrix
            if Node.matrixObj.inBounds(x, y):
                # save neighbor
                self.neighborsCords.append(cords)
                
                # check road node
                if mtr[y][x] == ROAD:
                    
                    self.roadCords.append(cords)
                
                # check wall node
                elif mtr[y][x] == WALL:
                    
                    self.wallsCords.append(cords)
                
                # check hole node
                elif mtr[y][x] == HOLE:
                    
                    self.holesCords.append(cords)
                
                # check goal node
                elif mtr[y][x] == GOAL:
                    
                    self.goalsCords.append(cords)
                
                # check car node
                elif mtr[y][x] == CAR:
                    
                    self.carCords.append(cords)

'''

    FUNCTIONS

'''

#check if cords refers to goal node
def isGoalNode (x, y, nodes):
    
    for node in nodes:
        cords = node.getCords()
        if cords[0] == x and cords[1] == y:
            return True
            break
    return False

# return all nodes with GOAL value
def getGoalsNodes (circuit, start):

    # array of not visited nodes
    nodes = [start]

    # array with lines nodes
    lines = []

    # create dictionary with visited nodes
    visited = { start.getId(): start }

    # iterate all nodes
    while len(nodes)>0:
        
        # save first node
        currentNode = nodes[0]
        
        # cicle goals neighbors cords of current node
        for cords in currentNode.getGoalsCords():
            
            x = cords[0]
            y = cords[1]

            # create id like this because create node is useless, it's a waste of memory
            idBox = str(x)+'-'+str(y)
            
            # check box isn't visited
            if visited.get(idBox, None) == None:

                # create line node
                node = Node(x, y, -1)

                #save node
                nodes.append(node)
                lines.append(node)
                
                #set visited
                visited[idBox] = node

        # remove visited node
        nodes.pop(0)

    return lines        

# BFS Algorithm
def BFS(matrix, xStart, yStart, car):

    # create matrix object
    circuit = Matrix(matrix)
    Node.matrixObj = circuit

    # create start node with initial cost like 0
    start = Node(xStart, yStart, 0)

    # get goals nodes
    goalsNodes = getGoalsNodes(circuit, start)
    minToCheckGoal = len(goalsNodes)*8

    # create dictionary with visited nodes
    Node.visitedNodes = { start.getId(): start }

    # array of not visited nodes
    nodes = [start]

    # check when found goal
    isGoal = False
    
    # cicle all not visited boxes
    while len(nodes)>0 and (not isGoal):

        # save first node
        currentNode = nodes[0]
        
        #save cords to iterate
        neighboarsCords = currentNode.getGoalsCords() + currentNode.getRoadCords()
        
        # cicle all neighbors cords of current node
        for cords in neighboarsCords:
            
            # save current x y cords
            x = cords[0]
            y = cords[1]
            
            # create id like this because create node is useless, it's a waste of memory
            idBox = str(x)+'-'+str(y)
            
            # check if current node is a goal node
            if isGoalNode(x, y, goalsNodes):
                
                # check if is first time i visit the goal
                if Node.visitedNodes.get(idBox, None) == None:
                    Node.visitedNodes[idBox] = True
                # check i'm arrived at GOAL box
                elif len(Node.visitedNodes.keys()) > minToCheckGoal:
                    
                    # create new node
                    node = Node(x, y, currentNode.getCost()+1)
                    
                    # in next iteration will check the new node
                    nodes.append(node)
    
                    # save the node
                    Node.visitedNodes[idBox] = node
                    
                    isGoal = True
                    idGoal = idBox
                    break
            
            # check if i've already visited the node
            elif Node.visitedNodes.get(idBox, None) == None:
                
                # create new node
                node = Node(x, y, currentNode.getCost()+1)
                
                # in next iteration will check the new node
                nodes.append(node)

                # save the node
                Node.visitedNodes[idBox] = node
                

        # remove visited node
        nodes.pop(0)

    return getPath(idGoal, start)

# return the shortest path to arrive from start to goal
def getPath(idGoal, startNode):

    # save last node
    currentNode = Node.visitedNodes[idGoal]

    # array of cords (x, y) of path
    currentPath = []

    # cicle until don't arrive to start
    while currentNode.getId() != startNode.getId():

        # save cords
        currentPath.insert(0, currentNode.getCords())

        # save the new node (the node with less cost)
        currentNode = currentNode.getPreviousNode()

    return currentPath

def getNextCordsAttainable(cords, vx, vy, x, y):
        
    cs = [(1,1), (1,0), (1,-1), (0,1), (0,0), (0,-1), (-1,1), (-1,0), (-1,-1)]
    
    cases = [(vx+case[0], vy+case[1], case) for case in cs]
        
    for case in cases:
        
        if (x+case[0]) == cords[0] and (y+case[1]) == cords[1]:
            return case[2]
            break
        
'''

    MAIN FUNCTION

'''

#def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty): # vecchia versione
def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty, laps):
    '''inserite qui il vostro codice'''

    global finalPath
    global CAR
    global matrixCopy
    
    CAR = car

    # INITIALIZE
       
    if x == startx and y == starty:
        
        finalPath = BFS(griglia_corrente, x, y, car)
        
        matrixCopy = copy.deepcopy(Node.matrixObj.getMatrix())
            
    # CALCULATE NEXT MOVE
    if len(finalPath) > 0:
        nextMove = getNextCordsAttainable(finalPath.pop(0), vx, vy, x, y)
        vx = nextMove[0]
        vy = nextMove[1]
    else:
        #stop car
        if vx > 0:
            vx = -1
        elif vx < 0:
            vx = 1
        if vy > 0:
            vy = -1
        elif vy < 0:
            vy = 1

    return (vx, vy)
    