'''
Obiettivo dell'esercizio e' sviluppare la strategia di gioco per il gioco del Mastermind. 

Nel gioco del Mastermind un  giocatore (il "decodificatore"), deve indovinare un  codice segreto.
Il codice segreto e' di N cifre decimali distinte (NO RIPETIZIONI, solo 10 possibili simboli per ciascuna posizione).
Il decodificatore cerca di indovinare il codice per tentativi. Strategicamente  nel tentativo 
possono essere presenti anche cifre ripetute pur  sapendo che nel codice non sono presenti ripetizioni. 
In risposta ad  ogni tentativo viene fornito un aiuto producendo una coppia di interi (a,b) dove:

- a e' il numero di cifre giuste al posto giusto,
cioe' le cifre del codice da indovinare che sono effettivamente presenti nel tentativo al posto giusto.
- b e' il numero di cifre  giuste ma al posto sbagliato,
cioe' le cifre del codice da indovinare che sono effettivamente presenti nel tentativo solo al posto sbagliato.

Ad esempio per il codice
    34670915 e il tentativo
    93375948
la risposta deve essere la coppia (2,3).
Il 2 viene fuori dal contributo delle cifre 7 e 9 del codice da indovinare in quarta e sesta posizione,
il numero 2 e' dovuto alle cifre 3,4,5 che compaiono tra le cifre del tentativo ma mai al posto giusto.

Nella nostra versione di Mastermind il valore di N (lunghezza del codice) puo' essere 6, 7 o 8 e nella coppia data
in  risposta ai tentativi non si vuole rivelare quale delle due due cifre rappresenta il numero di  cifre giuste al posto giusto 
di conseguenza nella coppia di risposta  i valori di a e b possono risultare invertiti.
Ad esempio per il codice 34670915 e il tentativo 93375948 le risposte (2,3) e (3,2) sono entrambe possibili.


Una configurazione del  gioco viene rappresentata come lista di liste (L). 
Il primo elemento di L e' un intero N rappresentante la lunghezza del codice.
Ciascuno degli eventuali altri elementi di L rappresenta un tentativo fin qui
effettuato dal decodificatore e la relativa risposta.
Piu' precisamente  L[i] con i>0, se presente, conterra' una tupla composta da due elementi:
- la lista di N cifre  con il tentativo effettuato dal decodificatore in un qualche passo precedente
- la tupla di interi (a,b) ricevuta in risposta.


Il programma che dovete realizzare contiene la seguente funzione:
 
    decodificatore(configurazione)

che e' l'AI che guida il gioco. La funzione  riceve come input la configurazione attuale del gioco e produce un tentativo (lista di caratteri in '0-9').

Per questo esercizio la valutazione avverra' nel seguente modo: 
avete 150 tentativi e 30 secondi di tempo per indovinare quanti piu' codici possibile.
Il punteggio ottenuto e' dato dal numero di codici che riuscite ad indovinare.

Tutti i vostri elaborati al termine verranno valutati su di uno stesso set di codici,
questa operazione  determinera' una classifica dei vostri elaborati.
Per entrare in classifica bisogna indovinare almeno cinque codici.
La classifica viene suddivisa in 14 fasce che corrispondono ai voti da 18 a 31 ed a 
ciascun programma viene assegnato il voto corrispondente.
Se il numero di valori diversi e' minore di 14 il voto sara' proporzionale alla posizione
nella graduatoria (con il primo che prende 31 e l'ultimo 18)

In allegato vi viene fornito un  simulatore di gioco (simulatore1.py) che vi permettera' di 
autovalutare la vostra strategia. Il simulatore genera  codici casuali e invoca il vostro 
programma per ottenere i vari tentativi. Appena un codice  viene indovinato ne viene 
proposto uno nuovo. Il processo termina quando avete esaurito i vostri 150 tentativi
o sono passati  i 30 secondi.

ATTENZIONE: NON usate lettere accentate ne' nel codice ne' nei commenti
'''

import random 
from time import time

global worldsList




def buildPermutationsTree(digitsLeft, digitsToUse, myNumber):
    myList = [myNumber]
    if (digitsLeft == 1):
        return [myNumber]
    for cnt in range(0, len(digitsToUse)):
        myList.append(buildPermutationsTree(digitsLeft-1, digitsToUse[0:cnt]+digitsToUse[cnt+1:len(digitsToUse)+1],digitsToUse[cnt]))
        myList.append(0)
    return myList

global prebuiltTrees
prebuiltTrees = list()
digitsToUse = set([0,1,2,3,4,5,6,7,8,9])
for cnt in range(0,9):
    if (cnt<6):
        prebuiltTrees.append(0)
    else:
        sublist = list()
        for cnt2 in range(0,10):            
            sublist.append(buildPermutationsTree(cnt,list(digitsToUse-set([cnt2])),cnt2))
        prebuiltTrees.append(sublist)


def calcNewCEMCHM(bet, step, nodeDigit,cEM,cHM):
    if (bet[step] == nodeDigit):
        cEM += 1
    else:
        for digit in bet:
            if (digit == nodeDigit):
                cHM += 1
                break
    return (cEM,cHM)

def checkIfPruneShouldReturn(cEM,cHM,answer, step, length):
    if ((cEM > answer[0]) or (cHM > answer[1]) or (length-step < answer[0] - cEM) or (length-step < answer[1] - cHM)):
        return (True, True)
    
def checkWhatPruneShouldReturn(cEM,cHM,answer, step, length):
    if (step == length - 1):
        return (True,((cEM!=answer[0]) or (cHM!=answer[1])))
    return (False, True)
    
    

def pruneTree(node, bet, answer, step, cEM, cHM, length):
    cEM,cHM = calcNewCEMCHM(bet, step, node[0], cEM, cHM)
    if checkIfPruneShouldReturn(cEM,cHM,answer, step, length):
        return True
    shouldReturn, shouldReturnWhat = checkWhatPruneShouldReturn(cEM,cHM,answer, step, length)
    if (shouldReturn):
        return shouldReturnWhat
    
    bigPrune = True
    for cnt in range(1,len(node),2):
        pruned = pruneTree(node[cnt], bet, answer, step+1, cEM, cHM, length)
        if (pruned):
            node[cnt+1] = 0
        else:
            node[cnt+1] = 1

            bigPrune = False
    return bigPrune
                

def copyPrunedTree(node):
    size = 1
    newNode = [node[0]]
    for cnt in range(1,len(node),2):
        if node[cnt+1]:
            res = copyPrunedTree(node[cnt])
            newNode.append(res[0])
            newNode.append(1)
            size = size + res[1]
    return (newNode,size)
        
    
    
def getNumberFromNode(node):
    if (len(node)<2):
        return [node[0]]
    else:
        lst = [node[0]]
        half = (len(node) -1) // 4
        lst = lst + getNumberFromNode(node[half*2+1])
        return lst
    
def getNumberFromNodeRandom(node):
    if (len(node)<2):
        return [node[0]]
    else:
        lst = [node[0]]
        rand =random.randint(0,((len(node) - 1) // 2) - 1)
        lst = lst + getNumberFromNode(node[rand*2 + 1])
        return lst


def createNewHypothesis(hypothesis, bet, answer, length, dimensionsList, prob):
    newHypothesis = [[1,prob*hypothesis[0][1]]]
    totalSize = 0
    for cnt in range(len(hypothesis)-1,0,-1):
        if (hypothesis[cnt]):
            if (not pruneTree(hypothesis[cnt],bet,answer,0,0,0,length)):
                res = copyPrunedTree(hypothesis[cnt])
                newHypothesis.append(res[0])
                totalSize += res[1]
    
    if (len(newHypothesis)>1):
        newHypothesis[0][0] = totalSize*newHypothesis[0][1]
        dimensionsList.append(newHypothesis)

def calcProbOnFirstMove(answer,length): #wrong, but good enough, this isn't a statistics course
    digitsLeft = 10
    prob = 1.0
    for cnt in range(0,answer[0]):
        prob = prob / digitsLeft
        digitsLeft -= 1
    prob += digitsLeft*0.005
    probrev = 1.0
    digitsLeft = 10
    for cnt in range(0,answer[1]):
        probrev = probrev / digitsLeft
        digitsLeft -= 1
    probrev += digitsLeft*0.005
    return prob, probrev

def normalizeWorldsListProb(worldsList):
    totalProb = 0.0
    for el in worldsList:
        totalProb += el[0][0]
 
    for el in worldsList:
        el[0][0] /= totalProb
    
def chooseWorld(worldsList,rnd):
    partialSum = 0.0
    for cnt in range(0,len(worldsList)):
        partialSum += worldsList[cnt][0][0]
        if (partialSum>rnd):
            return cnt
    return 0

def searchNextMove(configurazione):
    global worldsList
    
    newWorldsList = list()
    right = 1.0
    reverse = 1.0

    if (len(configurazione) == 2):
        right, reverse = calcProbOnFirstMove(configurazione[1][1], configurazione[0])
    lastMove = configurazione[len(configurazione)-1]
    for hypothesis in worldsList:
        createNewHypothesis(hypothesis, lastMove[0], lastMove[1], configurazione[0], newWorldsList, right)
        reversedAnswer = (lastMove[1][1], lastMove[1][0])
        if (reversedAnswer[0] != configurazione[0]): #answer can't be a=number of digits, game would be won 
            createNewHypothesis(hypothesis, lastMove[0], reversedAnswer, configurazione[0], newWorldsList, reverse)
 
    worldsList = newWorldsList
    normalizeWorldsListProb(worldsList)
    rnd= random.random()
    worldID = chooseWorld(worldsList, rnd)
    chosenWorld = worldsList[worldID]
    nodeID = random.randint(1,len(chosenWorld) - 1)

    return getNumberFromNodeRandom(chosenWorld[nodeID])
        
def decodificatore(configurazione):
    global prebuiltTrees
    global worldsList

    if (len(configurazione) > 1):
        nextMove = searchNextMove(configurazione)
    else:
        listOfTrees = [[1.0,1.0,1.0]]
        for cnt in range(0,len(prebuiltTrees[configurazione[0]])):
            listOfTrees.append(prebuiltTrees[configurazione[0]][cnt])
            
        worldsList = list()
        worldsList.append(listOfTrees)

        nextMove = getNumberFromNodeRandom(listOfTrees[1])
    
    return nextMove
    
