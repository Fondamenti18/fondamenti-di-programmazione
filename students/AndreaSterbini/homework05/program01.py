
'''
Obiettivo dell'esercizio e' sviluppare la strategia di gioco per il gioco del Mastermind. 

Nel gioco del Mastermind un  giocatore (il "decodificatore"), deve indovinare un  codice segreto.
Il codice segreto e' di n cifre decimali distinte. 
Il decodificatore cerca di indovinare il codice per tentativi. Strategicamente  nel tentativo 
possono essere presenti anche cifre ripetute pur  sapendo che nel codice non sono presenti ripetizioni. 
In risposta ad  ogni tentativo viene fornito un aiuto producento una coppia di interi (a,b) dove:

- a e' il numero di cifre   giuste  al posto giusto, cioè le cifre   del tentativo che sono 
effettivamente presenti nel codice al posto tentato.
- b e' il numero di cifre  giuste ma presenti nei posti sbagliati, cioè le cifre  del tentativo che 
sono effettivamente presenti nel codice, ma non al posto tentato.

ad esempio per il codice 34670915 e il tentativo '93379948' la risposta deve essere 
la coppia (2,1). Il 2 viene fuori dal contributo delle cifre 7 e 9 in quarta e sesta posizione, il numero 1 
e' dovuto al 3 che compre tra le cifre del tentativo ma mai al posto giusto. 

Nella nostra versione di Mastermind il valore di n (lunghezza del codice) puo' essere 7 o 8 e nella coppia data 
in  risposta ai tentativi non si vuole rivelare quale delle due due cifre rappresenta il numero di  cifre giuste al posto giusto 
di conseguenza nella coppia di risposta  i valori di a e b possono risultare invertiti.
Ad esempio per il codice 34670915 e il tentativo '93379948' le risposte (2,1) e (1,2) sono entrambe possibili.



Una configurazione del  gioco viene rappresentata come lista di liste (L). 
Il primo elemento di L e' un intero n rappresentante la lunghezza del codice.
Ciascuno degli eventuali altri elementi di L rappresenta i tentativi fin qui 
effettuati dal decodificatore e la relativa risposta. Piu' precisamente  L[i] con i>0, se presente,  
conterra' una tupla composta da due elementi:
- la lista di n cifre  con il tentativo effettuato dal decodificatore
- la  tupla di interi (a,b) ricevuta in risposta.


Il programma che dovete realizzare la seguente funzione:
 
decodificatore(configurazione)

che e' l'AI che guida il gioco. La funzione  riceve come input la configurazione attuale del gioco e produce un tentativo. 

Per questo esercizio la valutazione avverra' nel seguente modo: 
avete 150 tentativi e 30 secondi di tempo per indovinare quanti piu' codici possibile. 
Il punteggio ottenuto e' dato dai codici che si riesce ad indovinare. 

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
proposto uno nuovo. Il processo termina quando avete esaurito i vostri 200 tentativi 
o sono passati  i 30 secondi. 

ATTENZIONE: NON usate lettere accentate ne' nel codice ne' nei commenti
'''




import random

combi = {}

def decodificatore(configurazione):
    n, *tentativi = configurazione
    K = 6
    if len(tentativi)<K:
        print("Random per i primi K={} tentativi".format(K))
        prova = random.choice(combinazioni(n))
        while any( map( lambda x: prova == x[0], tentativi) ):
            prova = random.choice(combinazioni(n))
        return prova
    combi[n].reverse()
    for combinazione in combinazioni(n):
        coerente = True
        for tentativo, risp in tentativi:
            a, b = risposta(tentativo, combinazione)
            if (a, b) == risp or (b, a) == risp:
                next
            else:
                coerente = False
                break
        if coerente:
            if a == n or b == n and 50 > random.randint(0,100):
                print("Random nel 50% dei casi se N,0 o 0,N")
                prova = random.choice(combinazioni(n))
                while any( map( lambda x: prova == x[0], tentativi) ):
                    prova = random.choice(combinazioni(n))
                return prova
            else:
                return combinazione
    assert False, "Le combinazioni sono finite!!!"

def combinazioni(n):
    if n in combi:
        return combi[n]
    if n:
        cifre = range(10)
        res = [ comb + [c]  for c in cifre
                            for comb in combinazioni(n-1)
                            if c not in comb
              ]
    else:
        res = [[]]
    random.shuffle(res) # randomizzate
    combi[n] = res
    return res

def risposta(codice, proposta):
    ''' restituisce per ogni proposta quanti indovinati al posto giusto (a) e quanti al posto sbagliato (b)'''
    a=0
    ins=set(codice)
    for i in range(len(codice)):
        if codice[i]==proposta[i]: a+=1
    b=len(ins & set(proposta))-a    # cifre del codice in comune con il tentativo, meno quelle azzeccate esattamente
    return a,b
       

combinazioni(8) # precalcolo le combinazioni

