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
from random import randint
from copy import copy
from itertools import combinations


class State:
    def __init__(self):
        self.joinedTurn = 0
    def backWork(self, params):
        pass
    def work(self, params):
        pass
    def next(self, params):
        pass
    def setJoinedTurn(self, turn):
        self.joinedTurn = turn

comb = []

def genCombination(lst, res, length):
    global comb
    if len(res) == length:
        comb += [res]
        return
    else:
        for x in lst:
            rc = copy(res)
            rc += [x]
            lc = copy(lst)
            lc.remove(x)
            genCombination(lc, rc, length)

def fromStringToInt(possible):
    comb = []
    for x in possible:
        comb.append(int(x))
    return comb

def risposta(codice, proposta):
    ins, a = set(codice), 0
    for i in range(len(codice)):
        if codice[i] == proposta[i]: 
            a+=1
    return a, len(ins & set(proposta)) - a


class findDigits(State):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.generate = False
        self.possible = []
        self.change = False
        
    def backWork(self, params):
        super().backWork(self)   
        
        if len(params) - 1 - self.joinedTurn > 0:
            lastC = params[len(params) - 1][0]
            lastT = params[len(params) - 1][1]
            
            if lastT[0] + lastT[1] == params[0]:
                self.change = True
                return self.next(params)
            
            for i in range(len(self.possible)-1, -1, -1):
                comb = []
                for x in self.possible[i]:
                    comb.append(int(x))
                    
                a = risposta(lastC, comb)
                r = a[0] + a[1]
                r1 = lastT[1] + lastT[0]
                if r1 != r:
                    self.possible.pop(i)
        
        return self.next(params)
    
    def work(self, params):
        super().work(self)

        if not self.generate:
            self.generate = True
            self.possible = [list(p) for p in combinations('0123456789', params[0])]
            
        return fromStringToInt(self.possible[0])

    def next(self, params):
        super().next(self)
        
        if self.change:
            self.possible.clear()
            self.change = False
            self.generate = False
            comb.clear()
            genCombination(params[len(params) - 1][0], [], params[0])
            States["findCombination"].lastSearch = True
            return "findCombination"
        
class findCombination(State):
    def __init__(self):
        super().__init__()
        self.win = False
        self.lastSearch = True
    def backWork(self, params):
        super().backWork(self)
        if len(params) == 1: 
            self.win = True
        elif not len(params) == 1 or self.lastSearch: 
            self.lastSearch = False
            lastC = params[len(params) - 1][0]
            lastT = params[len(params) - 1][1]        
            
            for i in range(len(comb)-1, -1, -1):
                    
                a = risposta(lastC, comb[i])
                if not((lastT[0] == a[0] and lastT[1] == a[1]) or (lastT[0] == a[1] and lastT[1] == a[0])):
                    comb.pop(i)

        return self.next(params)
    
    def work(self, params):
        super().work(self)
        return comb[randint(0, len(comb) - 1)]
    
    def next(self, params):
        super().next(self) 
        if self.win:
            self.win = False
            States["findDigits"].counter = 0
            return "findDigits"
               

States = {"findDigits": findDigits(), "findCombination": findCombination()}

class StateMachine:
    def __init__(self, initialState):
        self.currentStateName = initialState
        self.currentState = States[initialState]
        
    def nextState(self, stateName):
        self.currentStateName = stateName
        self.currentState = States[stateName]
        
    def run(self, params):
        state = self.currentState.backWork(params)
        if type(state) is str:   
            self.nextState(state)
            States[state].setJoinedTurn(len(params) - 1)
        return self.currentState.work(params)

stateMachine = StateMachine("findDigits")

def decodificatore(configurazione): 
    return stateMachine.run(configurazione)