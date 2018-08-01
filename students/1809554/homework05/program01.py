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
r=[]
num=[]
numeri=[]
o=0
g=0
h=-1
caso=0
m=0
c=-1
def decodificatore(configurazione):
    ''' inserire qui la vostra soluzione'''
    global r
    global num
    global numeri
    global o
    global g
    global h
    global caso
    global m
    global c
    if len(configurazione)==1:
        r=[]
        o=0
        g=0
        h=-1
        caso=0
        c=-1
        m=0
        numeri=[]
    w=0
    if m>0:
        m+=1
    d=[]
    c+=1
    n=configurazione[0]
    x='0123456789'
    risposta=[]
    a=0
    if len(numeri)<n and len(configurazione)>1:
        if 1 in configurazione[-1][-1]:
            numeri+=[configurazione[-1][0][0]]
    if len(numeri)==n:
        for i in range(0,len(numeri)):
            if int(x[i])!=numeri[i]:
                w=x[i]
                d+=[configurazione[-1][-1]]
                break
    if len(numeri)==n and d==[]:
        w=int(x[len(numeri)])
        d+=[configurazione[-1][-1]]
    num[:]=numeri
    for i in r:
        if i in num:
            num.remove(i)
    if m==0 and len(numeri)==n:
        m=11
    if len(numeri)<n:
        while a<n:
            risposta+=[int(x[c])]
            a+=1
        return risposta
    elif len(r)==0:
        if m==11:
            risposta+=[num[g]]
            risposta+=[num[h]]
            for i in range(len(risposta),n):
                risposta+=[int(w)]
            return risposta
        elif m==12:
            if d==[(2, 0)] or d==[(0, 2)]:
                caso=1
            else:
                caso=2
            risposta+=[num[g]]
            risposta+=[int(w)]
            risposta+=[num[h]]
            for i in range(len(risposta),n):
                risposta+=[int(w)]
            return risposta
        elif m==13:
            if caso==1 and d==[(1, 1)]:
                risposta+=[num[g]]
                risposta+=[int(w)]
                risposta+=[int(w)]
                risposta+=[num[h]]
                for i in range(len(risposta),n):
                    risposta+=[int(w)]
                return risposta
            elif caso==1 and (d==[(2, 0)] or d==[(0, 2)]):
                g+=1
                risposta+=[num[g]]
                risposta+=[num[h]]
                for i in range(len(risposta),n):
                    risposta+=[int(w)]
                return risposta
            elif caso==2 and d==[(1, 1)]:
                r+=[configurazione[-1][0][0]]
            elif caso==2 and (d==[(2, 0)] or d==[(0, 2)]):
                risposta+=[num[g]]
                risposta+=[int(w)]
                risposta+=[int(w)]
                risposta+=[num[h]]
                for i in range(len(risposta),n):
                    risposta+=[int(w)]
                return risposta 
        elif m==14:
            if d==[(1, 1)]:
                r+=[configurazione[-1][0][0]]
            elif caso==1 and (d==[(0, 2)] or d==[(2, 0)]):
                g+=1 
                risposta+=[num[g]]
                risposta+=[num[h]]
                for i in range(len(risposta),n):
                    risposta+=[int(w)]
                return risposta
            elif caso==2 and (d==[(0, 2)] or d==[(2, 0)]):
                g+=1
                h+=1
                risposta+=[num[g]]
                risposta+=[num[h]]
                for i in range(len(risposta),n):
                    risposta+=[int(w)]
                return risposta
        elif m>=15:
            if d==[(1, 1)]:
                r+=[configurazione[-1][0][0]]
            elif num[g+1]==num[-1]:
                r+=[num[g+1]]
            elif d==[(2, 0)] or d==[(0, 2)]:
                g+=1 
                risposta+=[num[g]]
                risposta+=[num[h]]
                for i in range(len(risposta),n):
                    risposta+=[int(w)]
                return risposta
    v=len(r)+1
    if o>0 and (d==[(v, 0)] or d==[(0, v)]):
        r+=[configurazione[-1][0][v-1]]
        o=0
    for i in r:
        if i in num:
            num.remove(i)
    if len(r)>0:
        risposta[:]=r
        risposta+=[num[o]]
        if len(risposta)<n:
            for i in range(len(risposta),n):
                risposta+=[int(w)]
        o+=1
        return risposta

