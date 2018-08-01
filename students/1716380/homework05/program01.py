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
from itertools import permutations,repeat
x=[0,1,2,3,4,5,6,7,8,9]
source=[]
ss=[]
count=0
ls=[]
find=False
def decodificatore(configurazione):
    global x,source,ss,count,ls,find
    primo=configurazione[0]
    lun=len(configurazione)
    risposta=[]
    if lun==1:                 # first guess
        for _ in range(primo): risposta.append(0)
        x=[0,1,2,3,4,5,6,7,8,9]
        ss=[]
        count=0
        ls=[]
        find=False
        return risposta
    if 2<=lun<=11 and len(x)>primo:
        a,b=configurazione[-1][-1]
        tentativop=configurazione[-1][0]
        if a==0 and b==0:
            x.remove(tentativop[0])
            ss.append(tentativop[0])
            if tentativop[0]<9 and primo!=len(x): return rep(tentativop[0]+1,primo)
            else:
                source=permutation(x)
                return random.choice(source)
        else:
            if tentativop[0]<9: return rep(tentativop[0]+1,primo)
    
    else:
        coppia=configurazione[-1][-1]
        t=configurazione[-1][0]
        tp=configurazione[-2][0]
        if coppia==(0,primo) or coppia==(primo,0):
            eli(primo,source,t)
            return random.choice(source)
        if check(coppia,primo) and not find:
            ls+=t
            t0=[i for i in t]
            t0[0]=ss[0]
            return t0
        if (coppia==(1,primo-2) or coppia==(primo-2,1)) and cn(t,primo,ss[0]):
            unknown(source,count,tp[count])
            t1=[i for i in ls]
            count+=1
            if count<primo:
                t1[count]=ss[0]
                return t1
        if c(coppia,primo) and cn(t,primo,ss[0]):
            known(source,count,tp[count])
            find=True
            eli(primo,source,t)
            return random.choice(source)
        if check(coppia,primo):
            t0=[i for i in t]
            t0[count]=ss[0]
            eli(primo,source,t0)
            return random.choice(source)
        else:
            source.remove(t) # cancell the guess already used
            return random.choice(source)
def eli(n,source,lis):
    if n==6:
        for i in source[:]:
            if i[0]==lis[0] or i[1]==lis[1] or i[2]==lis[2] or i[3]==lis[3] or i[4]==lis[4] or i[5]==lis[5]: source.remove(i)
    if n==7:
        for i in source[:]:
            if i[0]==lis[0] or i[1]==lis[1] or i[2]==lis[2] or i[3]==lis[3] or i[4]==lis[4] or i[5]==lis[5] or i[6]==lis[6]: source.remove(i)
    if n==8:
        for i in source[:]:
            if i[0]==lis[0] or i[1]==lis[1] or i[2]==lis[2] or i[3]==lis[3] or i[4]==lis[4] or i[5]==lis[5] or i[6]==lis[6] or i[7]==lis[7]: source.remove(i)
def unknown(source,position,number):
    for i in source[:]:
        if i[position]==number: source.remove(i)
def known(source,position,number):
    for i in source[:]:
        if i[position]!=number: source.remove(i)
def permutation(ln):
    a=permutations(ln)
    li=[list(i) for i in a]
    return li
def rep(x,n):
    r=repeat(x,n)
    return [i for i in r]
def check(coppia,n):
    if coppia==(n-1,1) or coppia==(1,n-1): return True
def c(coppia,n):
    if coppia==(0,n-1) or coppia==(n-1,0):return True
def cn(t,l,n):
    if l==6:
        if t[0]==n or t[1]==n or t[2]==n or t[3]==n or t[4]==n or t[5]==n: return True
    if l==7:
        if t[0]==n or t[1]==n or t[2]==n or t[3]==n or t[4]==n or t[5]==n or t[6]==n: return True
    if l==8:
        if t[0]==n or t[1]==n or t[2]==n or t[3]==n or t[4]==n or t[5]==n or t[6]==n or t[7]==n: return True

def check_source(t,l):
    if l==6:
        if t[0][0]==t[-1][0] or t[0][1]==t[-1][1] or t[0][2]==t[-1][2] or t[0][3]==t[-1][3] or t[0][4]==t[-1][4] or t[0][5]==t[-1][5]: return True
    if l==7:
        if t[0][0]==t[-1][0] or t[0][1]==t[-1][1] or t[0][2]==t[-1][2] or t[0][3]==t[-1][3] or t[0][4]==t[-1][4] or t[0][5]==t[-1][5] or t[0][6]==t[-1][6]: return True
    if l==8:
        if t[0][0]==t[-1][0] or t[0][1]==t[-1][1] or t[0][2]==t[-1][2] or t[0][3]==t[-1][3] or t[0][4]==t[-1][4] or t[0][5]==t[-1][5] or t[0][6]==t[-1][6] or t[0][7]==t[-1][7]: return True


                