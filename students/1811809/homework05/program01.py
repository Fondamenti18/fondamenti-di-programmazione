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

import random, itertools

'''comperm = { #dictionary of combinations and permutations for 6,7,8 elements
    #4: (list(itertools.combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4)), list(itertools.permutations([0, 1, 2, 3]))),
    6: (list(itertools.combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6)), list(itertools.permutations([0, 1, 2, 3, 4, 5]))),
    7: (list(itertools.combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7)), list(itertools.permutations([0, 1, 2, 3, 4, 5, 6]))),
    8: (list(itertools.combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8)), list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7]))),
    #9: (list(itertools.combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9)), list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8])))
}'''
comperm = {}
combLen, permLen = 0, 0

def buildDictionary(mn, mx):
    global comperm
    val = [i for i in range(10)]
    inds = [i for i in range(mn)]
    for i in range(mn, mx+1):
        comperm[i] = (list(itertools.combinations(val, i)), list(itertools.permutations(inds)))
        inds.append(i)

def getStrikesBalls(cod, atmp): #get strikes and balls (copiato dal professore)
    a=0
    ins=set(cod)
    for i in range(len(cod)):
        if cod[i]==atmp[i]:
            a+=1
    b=len(ins & set(atmp))-a
    return a, b

def isValid(configuration, newatmp): #is the new attempt valid?
    n = len(newatmp)
    for i in range(1, len(configuration)):
        f, s = configuration[i][1][0], configuration[i][1][1]
        strikes, balls = getStrikesBalls(configuration[i][0], newatmp)
        isSB = (f != n and (f, s) == (strikes, balls))
        isBS = (s != n and (s, f) == (strikes, balls))
        if (not isSB) and (not isBS):
            return False
    return True

def isValidFastCheck(configuration, newatmp): #check if the attempt is valid only considering the values (NOT PERMUTATIONS)
    atmset = set(newatmp)
    for i in range(1, len(configuration)):
        if len(set(configuration[i][0]) & atmset) != configuration[i][1][0] + configuration[i][1][1]:
            return False
    return True

def permute(values, perm): #permutes 'values' according to permutation 'perm'
    answ = []
    for i in perm:
        answ.append(values[i])
    return answ

def getRandomComb(n): #returns a random combination (of length n)
    global comperm, combLen
    ind = random.randint(0, combLen-1)
    comperm[n][0][combLen-1], comperm[n][0][ind] = comperm[n][0][ind], comperm[n][0][combLen-1]
    combLen -= 1
    return comperm[n][0][combLen]

def getRandomPerm(n): #returns a random permutation (of length n)
    global comperm, permLen
    ind = random.randint(0, permLen-1)
    comperm[n][1][permLen-1], comperm[n][1][ind] = comperm[n][1][ind], comperm[n][1][permLen-1]
    permLen -= 1
    return comperm[n][1][permLen]

def getGoodCombination(configurazione):
    global permLen
    values = []
    n = configurazione[0]
    lastIndex = len(configurazione) - 1
    if len(configurazione) == 1 or (configurazione[lastIndex][1][0] + configurazione[lastIndex][1][1] != n): #pick random numbers
        values = getRandomComb(n)
        permLen = len(comperm[n][1])
    else:
        values = sorted(configurazione[lastIndex][0]) #we already know the correct values
    return values

def getGoodPermutation(configurazione, values):
    global permLen
    answ = None
    n = configurazione[0]
    while permLen > 0 and answ == None: #find a good permutation of the values
        pval = permute(values, getRandomPerm(n))
        if isValid(configurazione, pval):
            answ = pval
    return answ

def decodificatore(configurazione):
    global combLen, permLen
    if comperm == {}:
        buildDictionary(6, 8)

    n = configurazione[0]
    if len(configurazione) == 1: #new game started, inits the lengths
        combLen = len(comperm[n][0])
        permLen = len(comperm[n][1])

    newAttempt = None
    while newAttempt == None: #while we haven't found a good attempt
        values = getGoodCombination(configurazione) #values in the attempt (sorted in ascending order)
        if not isValidFastCheck(configurazione, values): #fast check if the values could be correct
            continue
        newAttempt = getGoodPermutation(configurazione, values)

    return newAttempt
