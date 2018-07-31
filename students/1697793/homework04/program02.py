'''
I0l tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3×3 caselle.
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

# TIPO

def checkRows (matrix, sign):

    for ir in range(len(matrix)):
        valid = True
        for ic in range(len(matrix[0])):

            if matrix[ir][ic] != sign:
                valid = False
                break

        if valid:
            return True
            break;

    return False

def checkCols (matrix, sign):

    for ir in range(len(matrix)):
        valid = True
        for ic in range(len(matrix[0])):

            if matrix[ic][ir] != sign:
                valid = False
                break

        if valid:
            return True
            break;

    return False

def checkDiagonals (matrix, sign):
    return matrix[0][0] == sign and matrix[1][1] == sign and matrix[2][2] == sign or matrix[0][2] == sign and matrix[1][1] == sign and matrix[2][0] == sign

def checkVictory (matrix, sign):
    return checkRows(matrix, sign) or checkCols(matrix, sign) or checkDiagonals(matrix, sign)

def checkStatus(matrix):

    if checkVictory(matrix, 'o'):
        return 'o'
    elif checkVictory(matrix, 'x'):
        return 'x'
    else:

        for ir in range(len(matrix)):
            for ic in range(len(matrix)):
                if matrix[ir][ic] == '':
                    return '?'
        return '-'

# ESITI

def getResults(node, info):

    if node.node_type != '?': #check is the player to search

        info[node.node_type]+=1

    for i in range(len(node.lista_figli)):
        getResults(node.lista_figli[i], info)

# VITTORIE_LIVELLO

def getLevelVictory(node, info, level):

    if node.node_type == info['player'] and level == info['moves'] : #check player to search win and moves are how much we searched for

        info['wins']+=1

    for i in range(len(node.lista_figli)):
        getLevelVictory(node.lista_figli[i], info, level+1)

# STRATEGIA_VINCENTE

def turno (player, level):

    if player == 'x':
        return level%2==1
    else:
        return level%2==0

def isWinningStrategy(node, info, level):

    if len(node.lista_figli) == 0:
        return node.node_type == info['player']
    else:
        for i in range(len(node.lista_figli)):
            if turno(info['player'], level):
                if isWinningStrategy(node.lista_figli[i], info, level+1):
                    return True
                else:
                    if i == len(node.lista_figli)-1:
                        return False

            else:
                if not isWinningStrategy(node.lista_figli[i], info, level+1):
                    return False
                else:
                    if i == len(node.lista_figli)-1:
                        return True
        return None


# GEN_TREE

def getEmptyBoxes (matrix):

    boxes = []

    for ir in range(len(matrix)):
        for ic in range(len(matrix)):
            if matrix[ir][ic] == '':
                boxes.append( { 'ir': ir,'ic': ic } )

    return boxes


def createTree (node, info, level):

    sign = ('o' if level%2 == 0 else 'x') #check sign to set

    node.node_type = node.tipo()

    if node.node_type == '?': #enter only when game isn't end

        for i in range(len(node.empty_boxes)):

            boxes = copy.deepcopy(node.empty_boxes)  #get all the empty boxes        

            newMatrix = copy.deepcopy(node.nome)

            ir = boxes[i]['ir']
            ic = boxes[i]['ic']

            newMatrix[ir][ic] = sign #insert sign in current empty box

            matrixKey = fromMatrixToString(newMatrix)

            if matrixKey not in info:

                newNode = NodoTris(newMatrix) #create new son node

                del boxes[i]

                newNode.empty_boxes = boxes

                node.lista_figli.append(newNode) #save it

                createTree(newNode, info, level+1)

                info[matrixKey] = newNode

            else:
                equalNode = info[matrixKey]
                node.lista_figli.append(equalNode)

    if level == 0:
        return node

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.empty_boxes = []
        self.node_type = ''
    
    def tipo(self):
        '''inserire qui il vostro codice'''
        return checkStatus(self.nome)
        
    def esiti(self):
        '''inserire qui il vostro codice'''
        info = { '-': 0, 'o': 0, 'x': 0 }
        results = getResults(self, info)
        return (info['-'], info['o'], info['x'])
    
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
        info = { 'player': giocatore, 'moves': h, 'wins': 0 }
        getLevelVictory(self, info, 0)
        return info['wins']

    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        info = { 'player': giocatore, 'o': 999, 'x': 999 }
        return isWinningStrategy(self, info, 0)

def gen_tree(griglia):
    '''inserire qui il vostro codice'''

    node = NodoTris(griglia) #create main node
    node.empty_boxes = getEmptyBoxes(node.nome) #get all the empty boxes
    info = {}
    return createTree(node, info, 0)

def fromMatrixToString (matrix):

    key = ''

    for ir in matrix:
        for sign in ir:
            if sign == '':
                key += '_'
            else:
                key += sign

    #print("NUOVA CHIAVE MATRICE")
    #print(key)

    return key