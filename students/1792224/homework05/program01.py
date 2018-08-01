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
    ''' inserire qui la vostra soluzione'''
    cnf = configurazione
    nlcnf = len(cnf)
    ncnf = 0
    for ip in range(1, nlcnf):
        if cnf[nlcnf-ip][1][0]+cnf[nlcnf-ip][1][1] == cnf[0]:
            ncnf += 1
            break
    nxx = presv(cnf)
    if nxx == 0:
        return [nlcnf - 1] * cnf[0]
    if nlcnf < cnf[0] + nxx - 1:
        lrisp = pres678(cnf, nxx)
        nlmc = num_manc(lrisp)
        n = (cnf[0] + nlcnf - nxx) % cnf[0]
        if lrisp[n] >= lrisp[1]:
            return [lrisp[n+1], lrisp[1]] + nlmc * (cnf[0] - 2)
        return [lrisp[n], lrisp[1]] + nlmc * (cnf[0] - 2)
    elif nlcnf == cnf[0] + nxx - 1:
        return ele1(cnf, nxx)
    elif nlcnf > cnf[0] + nxx - 1:
        lrisp = iniz_prec(cnf)
        nfiss = lrisp[0]
        nlmc = num_manc(lrisp)
        n11 = 0
        if nlcnf > cnf[0] + nxx - 1:
            for ip in range(cnf[0] + nxx, nlcnf):
                if cnf[ip][1] == (1, 1):
                    n11 += 1
        nlri = nlmc * (n11 + 1)
        nlrf = nlmc * (cnf[0] - n11 - 3)
        if cnf[nlcnf-1][1] == (1, 1):
            n = cnf[nlcnf-1][0][n11]
            lrisp.remove(n)
            lrisp.insert(n11, n)
            return lrisp
        for t1 in range(cnf[0]-1):
            n = nlcnf-1
            if cnf[n-t1][1][0] + cnf[n-t1][1][1] == cnf[0]:
                return nlri + [cnf[n-t1][0][cnf[0]-1-t1], nfiss] + nlrf


def presv(cnf):
    nlcnf = len(cnf)
    npres = nasse = 0
    if nlcnf == 1:
        return 0
    ip = 1
    while cnf[ip][0] == [cnf[ip][0][0]] * cnf[0]:
        if cnf[ip][1][0] + cnf[ip][1][1] != 0:
            npres += 1
        else:
            nasse += 1
        ip += 1
        if ip == nlcnf:
            break
    if cnf[0] == 8   and (npres == 8 or nasse == 2):
        return ip
    elif cnf[0] == 7 and (npres == 7 or nasse == 3):
        return ip
    elif cnf[0] == 6 and (npres == 6 or nasse == 4):
        return ip
    return 0


def pres678(cnf, nxx):
    lpres = []
    lasse = []
    for ip in range(1, nxx):
        if cnf[ip][1][0] + cnf[ip][1][1] != 0:
            lpres.append(cnf[ip][0][0])
        else:
            lasse.append(cnf[ip][0][0])
    if cnf[0] == 8:
        if len(lpres) == 8:
            return lpres
        elif len(lasse) == 2:
            return rpres(lasse)
    elif cnf[0] == 7:
        if len(lpres) == 7:
            return lpres
        elif len(lasse) == 3:
            return rpres(lasse)
    else:
        if len(lpres) == 6:
            return lpres
        elif len(lasse) == 4:
            return rpres(lasse)


def rpres(lasse):
    lpres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(lasse)
    for ip in range(n):
        lpres.remove(lasse[ip])
    return lpres


def ele1(cnf, nxx):
    r1 = [0, (3, 3)]
    r2 = [0, (3, 3)]
    for i1 in range(nxx, nxx+cnf[0]-1):
        n = cnf[i1][1][0]
        if n == 1:
            r1[0] += 1
            r1[1] = cnf[i1][0]
        else:
            r2[0] += 1
            r2[1] = cnf[i1][0]
    if   r2[0] == cnf[0] - 1:
        n = r2[1][1]
    elif r1[0] > r2[0]:
        n = r2[1][0]
    else:
        n = r1[1][0]
    lp = pres678(cnf, nxx)
    lp.remove(n)
    lp.insert(0, n)
    return lp


def iniz_prec(cnf):
    nlcnf = len(cnf)
    for t1 in range(1, nlcnf):
        if cnf[nlcnf-t1][1][0]+cnf[nlcnf-t1][1][1] == cnf[0]:
            return cnf[nlcnf-t1][0]


def num_manc(l1):
    for t1 in range(10):
        if t1 not in l1:
            return [t1]
