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
from itertools import *


def decodificatore(configurazione):      #random del prof dal quale tiro fuori il primo tentativo
    ''' inserire qui la vostra soluzione'''
    n=configurazione[0]
    risposta=[]   
    lista1=[]
    lista11=[]
    x='0123456789'
    if len(configurazione)==1: 
        for _ in range(n):
            y=random.choice(x)
            risposta+=[int(y)]
            x=x.replace(y,'')
        return risposta
    if len(configurazione)==2:
        lista_perm=genera_risposta(configurazione[-1][0],lista11,lista1,configurazione[-1][1],configurazione[1:len(configurazione)])
        risposta1=genera_tentativo(configurazione[1:len(configurazione)])
        return risposta1
    else:
        risposta2=genera_tentativo(configurazione[1:len(configurazione)])
        return risposta2
    

def genera_risposta(codice,lista11,lista1,tupla,conf):
    nn=len(codice)
    lista=[0,1,2,3,4,5,6,7,8,9]
    l=[]
    es=[]
    div=[]
    global lista_permutazioni
    lista_permutazioni=[]
    a,b=tupla
    lun=a+b
    nuova=lista_nuova(lista,codice)
    esatti=combinations(codice,lun)
    for i in esatti:
        es.append(list(i))
    rimasti=nn-lun                   
    diversi=combinations(nuova,rimasti)
    for j in diversi:
        div.append(list(j))
    lista_giocati=lista_gioc(lista1,conf)
    for i in es:
        for j in div:
            l.append(i+j)
    for ii in l:
        finale=permutations(ii)
        for jj in finale:
            lista_permutazioni.append(list(jj))
    return lista_permutazioni
    

def genera_tentativo(confi):
    listap=[]
    global lista_permutazioni
    for el in lista_permutazioni:
        if confi[-1][1]==risp(confi[-1][0],el) or tuple(reversed(confi[-1][1]))==risp(confi[-1][0],el):
            listap.append(el)
    lista_permutazioni=listap
    ttt=random.choice(lista_permutazioni)
    return ttt 


def lista_gioc(lista,con):
    for i in con:
        lista.append(list(i[0]))
    return lista


def risp(cod, proposta):  #questa la utilizzo per ricevere la risposta al mio tentativo
    a=0
    ins=set(cod)
    for i in range(len(cod)):
        if cod[i]==proposta[i]: a+=1
    b=len(ins & set(proposta))-a    # cifre del codice in comune con il tentativo, meno quelle azzeccate esattamente
    return a,b

    
def lista_nuova(lista,decod):  #con questa funzione creo una lista contenente i numeri mancanti nel tentativo
    k=[]
    for i in lista:
        if i not in decod:
            k.append(i)
    return k
        
