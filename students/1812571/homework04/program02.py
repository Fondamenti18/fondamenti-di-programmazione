'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3×3 caselle.
A turno, i due giocatori scelgono una cella vuota e vi disegnano il proprio simbolo 
(un giocatore ha come simbolo una "o" e l'avversario una 'x'). 
Vince il giocatore che riesce a disporre tre dei propri simboli in linea retta 
orizzontale, verticale o diagonale. Se la griglia viene riempita 
senza che nessuno dei giocatori sia riuscito a completare una linea 
retta di tre simboli, il gioco finisce in parita'. Nel caso in cui il gioco 
finisse in parita', la partita e' detta "patta". 
Per convenzione a griglia vuota la prima mossa spetta sempre al giocatore 'o'

Una configurazione del gioco e' dunque univocamente determinata  dal contenuto della griglia.

Nel seguito assumiamo che il contenuto della griglia sia  rappresentato tramite  lista di liste.
La dimensione della lista di liste M e'  3x3 ed   M[i][j] contiene  '', 'x', o 'o'  a seconda 
che la cella della griglia appartenente all'iesima riga e j-ma colonna sia ancora libera, 
contenga il simbolo 'x' o contenga il simbolo 'o'. 

Data una configurazione C del gioco, l'albero di gioco per C e' l'albero che 
si ottiene ricorsivamente partendo dalla configurazione C e assegnando come figli le configurazioni 
che e' possibile ottenere da C con una mossa ulteriore del gioco. Ovviamente  risulteranno 
foglie dell'albero i possibili esiti della partita vale a dire le diverse configurazioni cui e' 
possibile arrivare partendo da C e che rappresentano patte, vittorie per 'o' o vittorie per 'x'.
Se veda ad esempio l'immagine albero_di_gioco.png che mostra l' albero di gioco che si ottiene a partire 
dalla configurazione rappresentata da [['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
 

Si consideri la seguente Classe di oggetti:


class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] 


Bisogna progettare le seguente  funzione 

gen_tree(griglia)
che, data la configurazione di gioco griglia,  costruisce l'albero di gioco che si ottiene a partire 
dalla configurazione griglia e ne restituisce la radice. I nodi dell'albero devono essere 
oggetti della classe NodoTris.

Per testare la correttezza della vostra implementazione di gen_tree() il grade utilizzera' quattro metodi 
della   classe NodoTris che dovete comunque implementare: 

1)
tipo(self)
che, dato un nodo NodoTris, restituisce:
 'o' se la configurazione rappresentata dal nodo e' una configurazione di vittoria per il giocatore 'o'
 'x' se la configurazione rappresentata dal nodo e' una configurazione di vittoria per il giocatore 'x'
 '-' se la configurazione rappresentata dal nodo e' una configurazione di patta
 '?' se la configurazione rappresentata dal nodo e' una configurazione di gioco non ancora terminato

2)
esiti(self)
che, dato un nodo radice di un albero di gioco, restituisce una tripla con i possibili 
esiti della partita che ha come configurazione iniziale quella rappresentata dal nodo. 
Piu' precisamente: il primo elemento della tripla  e' il numero di  patte possibili, 
il secondo e' il numero di possibili vittorie  per il giocatore 'o' mentre  il terzo elemento 
e' il numero di possibili vittorie per il giocatore 'x'.

3)
vittorie_livello(self, giocatore, h)
che, dato un nodo radice di un albero di gioco, uno dei due giocatori ed un intero h,
restituisce il numero di nodi che rappresentano una vittoria per il giocatore e si 
trovano ad altezza h nell'albero. In altri termini restituisce il numero di vittorie possibili 
per giocatore in esattamente h mosse, nella partita che ha come configurazione iniziale 
quella rappresentata dalla radice dell'albero.

4)
strategia_vincente(self,giocatore)
che, dato un nodo radice di un albero di gioco ed uno dei due giocatori, restituisce True o False. 
Restituisce True  se  giocatore ha una strategia vincente  nella partita 
che ha come configurazione iniziale quella rappresentata dal nodo radice, False altrimenti.

Nota che un giocatore ha una strategia vincente rispetto ad una certa configurazione se, 
qualunque siano le mosse dell'avversario ha sempre la possibilita' di rispondere in modo 
che la partita termini con la sua vittoria.

Potete ovviamente definire ulteriori  funzioni e altri metodi per la   Classe NodiTris 
se li  ritenete utili al fine della risoluzione del compito.

Potete assumere che le configurazioni di gioco rappresentate da griglia siano sempre configurazioni 
lecite (vale a dire ottenute dopo un certo numero di mosse a parire dalla griglia vuota).


AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate; non
importare moduli che non sono nella libreria standard.

ATTENZIONE: i test vengono eseguiti con un timeout globale di 2*N secondi (se il grader esegue N test).
'''

import copy

def checkTris(posI, posJ, turnO, griglia):
    mask = list()
    mask.append([[posI,0],[posI,1],[posI,2]])
    mask.append([[0,posJ],[1,posJ],[2,posJ]])
    mask.append([[0,0],[1,1],[2,2]])
    mask.append([[0,2],[1,1],[2,0]])
    
    for el in mask:
        if ((griglia[el[0][0]][el[0][1]] == turnO) and (griglia[el[1][0]][el[1][1]] == turnO) and (griglia[el[2][0]][el[2][1]] == turnO)):
            return True

    return False


class NodoTris:
    
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.state = "?"
        self.hasCachedReturnValue = False
        self.hasCachedVictoriesValueForLevel = -1
        #self.lastSession = 0
        
    def chainGeneration(self, turnO, statesDict, statesHash):
        self.statesDict = statesDict
        turnItC = ["o","x"]
        
        for i in range(0,3):
            for j in range(0,3):
                if (self.nome[i][j] == ""):
                    childHash = statesHash + (3**(i*3+j))*(turnO+1)
                    updatedGrid = copy.deepcopy(self.nome)
                    updatedGrid[i][j] = turnItC[turnO]
                    newNode = NodoTris(updatedGrid)
                    newNode.statesDict = statesDict
                    newNode.statesH = childHash
                    newNode.turn = turnItC[(turnO + 1) % 2]
                    self.lista_figli.append(newNode)
                    if (childHash in statesDict):
                        continue
                    else:
                        statesDict[childHash] = newNode
                    if (checkTris(i , j, turnItC[turnO],updatedGrid)):
                        newNode.state = turnItC[turnO]
                    else:
                        newNode.chainGeneration((turnO+1) % 2, statesDict, childHash)
        
        if (len(self.lista_figli) == 0):
            self.state = "-"
        
    
    def predictFuture(self):
        childsOfWhom = self.statesDict[self.statesH]
        if (self.hasCachedReturnValue):
            return self.cachedReturnValue
        
        victStateConvDict = {"-":(1,0,0),"o":(0,1,0),"x":(0,0,1)}
        if (childsOfWhom.state != "?"):
            return victStateConvDict[childsOfWhom.state]

        oWins = 0
        xWins = 0 
        tieFighter = 0
        
        for child in childsOfWhom.lista_figli:
            dr, oW, xW = child.predictFuture()
            tieFighter += dr
            oWins += oW
            xWins += xW
         
        self.hasCachedReturnValue = True
        self.cachedReturnValue = (tieFighter, oWins, xWins)
        return self.cachedReturnValue

    
    def victories(self, player, level, playerShi):
        if (self.hasCachedVictoriesValueForLevel == level+playerShi):
            return self.cachedVictoriesValue
        
        numberOfVictories = 0
        childsOfWhom = self.statesDict[self.statesH]
        if (level == 0):
            return int(childsOfWhom.state == player)

        for child in childsOfWhom.lista_figli:
            numberOfVictories += child.victories(player, level - 1, playerShi)
        
        self.hasCachedVictoriesValueForLevel = level+playerShi
        self.cachedVictoriesValue = numberOfVictories
        return numberOfVictories
            
    def winningStrategy(self, player):
        childsOfWhom = self.statesDict[self.statesH]
        if (childsOfWhom.state != "?"):
            if (childsOfWhom.state == player):
                return True
            else:
                return False
            
        needJustOneSuccessSwitch = (self.turn == player)

        for child in childsOfWhom.lista_figli:
            if (child.winningStrategy(player) == needJustOneSuccessSwitch):
                return needJustOneSuccessSwitch
        return not needJustOneSuccessSwitch
        
                        
        
            
    def tipo(self):
        return self.state
        
    def esiti(self):
        return self.predictFuture()
    
    def vittorie_livello(self, giocatore, h):
        playerShi = 0
        if (giocatore == "x"):
            playerShi = 10
        return self.victories(giocatore, h, playerShi)
    
    def strategia_vincente(self,giocatore):
        return self.winningStrategy(giocatore)
        
def getTurn(griglia):
    #0=O 1=X
    imbalance = 0
    for i in range(0,3):
        for j in range(0,3):
            if (griglia[i][j] == "o"):
                imbalance += 1
            elif (griglia[i][j] == "x"):
                imbalance -= 1
    return imbalance

                
def gen_tree(griglia):
    rootNode = NodoTris(griglia)
    turnItC = ["o","x"]
    rootNode.statesH = 0
    rootNode.statesDict = dict()
    rootNode.statesDict[0] = rootNode
    for st in turnItC:
        for c in range(0,3):
            if (checkTris(0, c, st, rootNode.nome)):
                rootNode.state = st
                return rootNode                        
   
    turnO = getTurn(griglia)
    rootNode.turn = turnItC[turnO]
    
    rootNode.chainGeneration(turnO, rootNode.statesDict, 0)

    return rootNode