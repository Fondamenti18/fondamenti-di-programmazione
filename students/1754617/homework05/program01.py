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

In allegato vi viene fornito un  simulatore di gioco (simulatore1.py) che vi permettera' di 
autovalutare la vostra strategia. Il simulatore genera  codici casuali e invoca il vostro 
programma per ottenere i vari tentativi. Appena un codice  viene indovinato ne viene 
proposto uno nuovo. Il processo termina quando avete esaurito i vostri 150 tentativi
o sono passati  i 30 secondi.

ATTENZIONE: NON usate lettere accentate ne' nel codice ne' nei commenti
'''

import collections

def check(valore_iniziale, valore_nuovo, prefix_is_correct):
    a, b = valore_iniziale
    c, d = valore_nuovo

    if a > b:
        a, b = b, a

    if c > d:
        c, d = d, c

    if prefix_is_correct is not None:
        if prefix_is_correct:
            return (c, d) == (0, 3)
        else:
            return (c, d) == (1, 2)

    if (a, b) == (0, 2):
        if (c, d) == (1, 2) or (c, d) == (1, 1):
            return True

    if (a, b) == (1, 1):
        if (c, d) ==(0, 2):
            return True
    return False

def decodificatore(configurazione):
    ''' inserire qui la vostra soluzione'''
    n, *configurazione = configurazione   #prendo n il primo elem di conf
    
    missing=set()
    ctr=0
    while(configurazione and len(missing)<10-n and ctr < 9):
        ctr+=1
        (x, (a, b)), *configurazione = configurazione
        if(a==0 and b==0):
            missing.add(x[0])

    if(len(missing)<10-n):
        if(ctr==9):
            missing.add(9)
        else:
            return [ctr]*n
        
    numeri=[n for n in range(10) if n not in missing]
    
    valore_iniziale = None
    swap = False
    posizioni = {}
    contatore = collections.defaultdict(list)
    candidati_prefisso = set()
    candidati_precedenti = []
    prefix_is_correct = None

    spurious_cfgs = {}
    
    while configurazione:
        (x, (a, b)), *configurazione = configurazione
        if a > b:
            a, b = b, a

        if valore_iniziale is None or valore_iniziale == (1, 1):
            valore_iniziale = (a, b)
            if (a, b) == (1, 1):
                swap = True
            continue            

        idx_max = max(range(2, n), key=lambda i: x[i])
        elem_max = x[idx_max]
        candidati_precedenti.append(elem_max)
        contatore[elem_max].append(idx_max)

        if set(candidati_prefisso) == set(numeri[:2]) and len(set(candidati_precedenti)) == 3:
            spurious_cfgs[tuple(x)] = (a, b)
            if len(spurious_cfgs) == n - 2:
                ctr = collections.Counter(spurious_cfgs.values())
                (common, _), _ = ctr.most_common()
                for k, v in spurious_cfgs.items():
                    if v != common:
                        idx_max = max(range(2, n), key=lambda i: k[i])
                        elem_max = k[idx_max]
                        posizioni[elem_max] = idx_max
                        prefix_is_correct = common == (1, 2)
        elif check(valore_iniziale, (a, b), prefix_is_correct):
            #print('Elemento {} in posizione {}'.format(elem_max, idx_max))
            assert elem_max not in posizioni
            posizioni[elem_max] = idx_max
        elif elem_max not in posizioni and len(contatore[elem_max]) == n - 2:
            #print('Elemento {} candidato prefisso'.format(elem_max))
            candidati_prefisso.add(elem_max) 
            assert len(candidati_prefisso) <= 2

        if len(posizioni) == n - 2:
            if len(candidati_prefisso) != 2:
                candidati_prefisso = set(numeri).difference(set(posizioni.keys()))
            i, j = list(candidati_prefisso)
            if i > j:
                i, j = j, i
            x = [-1] * n
            for k, v in posizioni.items():
                x[v] = k

            if configurazione:
                x[0:2] = j, i
            else:
                x[0:2] = i, j 
            return x
        
    i, j = numeri[:2]
    x = [-1] * n

    if not swap:
        x[0:2] = i, j
    else:
        x[0:2] = j, i
        
    if valore_iniziale is None:
        return x

    if not len(candidati_precedenti):
        candidato = i
    else:
        candidato = candidati_precedenti[-1]

    if len(contatore[candidato]) == n - 2 or candidato in posizioni:
        idx = numeri.index(candidato)
        candidato = numeri[idx + 1]

    while True:
        indici = [idx
                  for idx in range(2, n)
                  if idx not in set(contatore[candidato])
                  and idx not in set(posizioni.values())]
        if not indici:
            idx = numeri.index(candidato)
            candidato = numeri[idx + 1]
            continue
        idx = indici.pop(0)    
        x[idx] = candidato
        return x
                        
