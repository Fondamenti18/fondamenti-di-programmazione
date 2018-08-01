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

# ESEMPIO di strategia che tira a caso una combinazione di N valori anche ripetuti



def decodificatore(configurazione):
    if len(configurazione) == 1:
        global searcher
        searcher = decode(configurazione[0])
    else:
        searcher.update(configurazione[-1])
    
    attempt = searcher.compute()
    
    return attempt


class decode:
    def __init__(self, nod):
        self.nod = nod            #numero di cifre del codice
        self.attempts = []      #codici provati
        self.results = []       #risultati dei codici provati
        self.results_ab = []    #risultati con (a,b) ordinati
        self.values = [0,1,2,3,4,5,6,7,8,9] #valori possibili
        self.outvalues = self.values[self.nod:] #valori che non rientrano nelle celle del codice
        self.right = 0        #numero di valori del tentativo presenti nel codice
        self.lastright = 0    #numero di valori dell'ultimo  tentativo presenti nel codice
        self.changed = []     #cifre scambiate (a,b) = a diventata b
        self.tochange = 0     #cifra da scambiare al prossimo scambio
        self.hipothesis = (0,0) #ipotesi di appartenenza (true/false -> fatta l'ipotesi, 0 -> cifra di partenza)
        self.solutions = [] #mappa delle possibili combinazioni
        self.conditions = [] #condizioni verifcate nel codice
        self.totry = []     #lista di codici da provare -> il vero codice si trova tra questi
        self.tested = []    #lista di codici provati
        
    def update(self, newattempt):  #aggiorna i tentativi e risultati con l'output del simulatore
        self.attempts.append(newattempt[0])
        self.results.append(newattempt[1])
        self.right = newattempt[1][0] + newattempt[1][1]
        
    
    def compute(self): #elabora un nuovo tentativo
        if not self.attempts:
            attempt = self.p1()
        
        elif self.right == self.nod:
            self.p3()
            if self.lastright != self.right:
                self.p4_0()
                self.lastright = self.right
            self.p4()
            attempt = self.p5()
        else:
            attempt = self.p2()
        
        return attempt
   
    def p1(self):
        attempt = self.values[:self.nod]
        return attempt
    
    def p2(self):
        attempt = self.slide(self.attempts[-1])
        if self.right < self.lastright:
            if self.hipothesis[0]:
                self.tochange = self.hipothesis[1]
            attempt = self.change(attempt,self.changed[1])
            self.erase(self.changed[0])
            attempt = self.change(attempt,self.tochange)
            self.right += 1
            
        elif self.right > self.lastright:
            if self.hipothesis[0]:
                self.hipothesis = (0,0)
            if self.changed:
                self.erase(self.changed[0])
            attempt = self.change(attempt,self.tochange)
            
        elif self.right == self.lastright:
            attempt = self.change(attempt,self.changed[1])
            if not self.hipothesis[0]:
                self.hipothesis = (1,self.tochange-1)
            attempt = self.change(attempt,self.tochange)
        
        self.lastright = self.right
        return attempt
    
    def p3(self):
        for element in self.results[len(self.results_ab):]:
            if element[0] > element[1]:
                self.results_ab.append((element[1],element[0]))
            else:
                self.results_ab.append((element[0],element[1]))
                
    def p4_0(self):
        self.values = self.attempts[-1][:]
        for _ in range(self.nod):
            self.solutions.append(self.values[:])
        self.tested.append(self.values)
                
            
    def p4(self):
        rightlist = []
        for attempt,result in enumerate(self.results_ab):
            for pos,digit in enumerate(self.attempts[attempt]):
                if digit in self.values:
                    if result[0] == 0:
                        if digit in self.solutions[pos]:
                            self.solutions[pos].remove(digit)
                    else:
                        rightlist.append((digit,pos))
            if rightlist:
                rightlist = [rightlist[:] for _ in range(len(self.values))]
                self.conditions.append(self.combinations(rightlist,0,result[0]))
                rightlist.clear()
         
         
        self.totry = self.combinations(self.solutions,self.conditions)
        
        '''
        print('to try: ', len(self.totry))
        print(self.totry)
        print('solutions:')
        print(self.solutions)
        print('conditions: ', len(self.conditions))
        print(self.conditions) 
        '''       
             
    
    def p5(self):
        while True:
            index = random.randint(0,len(self.totry)-1)
            if not self.totry[index] in self.tested:
                break
        self.tested.append(self.totry[index])
        return self.totry[index]
    
    def verify(self, code, conditions):
        for condition in conditions:
            for rules in condition:
                for rule in rules:
                    if code[rule[1]] != rule[0]: 
                        break
                else:
                    break
            else:
                return 0
        return 1
            
    
    def combinations(self, maps, rules = 0, nod = 0, code = []):
        if not nod:
            nod = len(maps)
            
        if len(code) == nod:
            if rules:
                if not self.verify(code[:], rules[:]):
                    return ''
            return [code[:]]

        
        combo = []
        for digit in maps[0]:
            if digit in code: continue
            combo.extend(self.combinations(maps[1:], rules, nod, code+[digit]))            
        return combo
        
    
    
    def slide(self, l): #esegue lo slide verso destra della lista data
        result = []
        result.append(l[-1])
        for e in l[:-1]:
            result.append(e)
        return result
    
    def change(self, l, element): #sostituisce l'elemento con il primo elemento della lista che contiene le cifre rimaste fuori dal codice
        result = l[:]
        i = result.index(element)
        result[i] = self.outvalues[0]
        self.changed = (element,self.outvalues[0])
        self.outvalues[0] = element
        if element == self.tochange:
            self.tochange += 1
        return result
    
    def erase(self, digit):
        self.outvalues.remove(digit)
        
        
        
        
        
