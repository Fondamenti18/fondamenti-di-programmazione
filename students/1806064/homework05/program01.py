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

from random import choice
from random import shuffle
import copy

condizione_sicura=False
codice=[]
y=0
x=0
main=[]
Max=0
lista_tentativi=[]
alpha=[]
d=0
lista_risposta=[]
e=0

def decodificatore(configurazione):
    global codice,condizione_sicura,y,x,main,Max,lista_tentativi,alpha,d,lista_risposta,e
    lunghezza=configurazione[0]
    if len(configurazione)==1:
        condizione_sicura=False
        x=0
        y=0
        d=0
        e=0
        lista_tentativi=[]
        lista_risposta=["" for i in range(lunghezza)]
        main= [i for i in range(lunghezza)]
        return main
    lista_precedente=copy.deepcopy(configurazione[-1][0])
    tupla_precedente=configurazione[-1][1]
    if set(tupla_precedente)==set((0,lunghezza)) and condizione_sicura==False:
        condizione_sicura=True
        alpha=copy.deepcopy(lista_precedente)
    if len(configurazione)==2:
        tupla=configurazione[-1][1]
        a,b=tupla
        if a+b==lunghezza:
            return configurazione[-1][0]
        y=lunghezza
        lista_temp=copy.deepcopy(lista_precedente)
        lista_temp[x]=y
        a,b=tupla_precedente
        Max=a+b
        return lista_temp
    lista_precedentex2=copy.deepcopy(configurazione[-2][0])
    tupla_precedentex2=configurazione[-2][1]
    a2,b2=tupla_precedentex2
    a1,b1=tupla_precedente
    if not condizione_sicura:
        if a1+b1==lunghezza:
            x=copy.deepcopy(lista_precedente)
            while x in lista_tentativi:
                shuffle(x)
            lista_tentativi.append(x)
            return x
        if x+1==lunghezza:
            if a1+b1>Max and y!=9:
                main[x]=y
                y=y+1
            x=0
            p=copy.deepcopy(main)
            p[0]=y
            return p
        if (a1+b1)>(a2+b2) and a1+b1>Max and y!=9:
            Max=(a1+b1)
            x=x+1
            y=y+1
            main=lista_precedente
            p=copy.deepcopy(main)
            p[x]=y
            return p
        elif (a1+b1)<(a2+b2) or a1+b1<Max and y!=9:
            x=x+1
            y=y+1
            p=copy.deepcopy(main)
            p[x]=y
            return p
        elif (a1+b1)==(a2+b2) or a1+b1==Max:
            x=x+1
            p=copy.deepcopy(main)
            p[x]=y
            return p
        elif y==9:
            x=x+1
            if lista_precedente[-1]==9:
                x=0
            p=copy.deepcopy(main)
            p[x]=y
            return p
    if condizione_sicura:
        if "" not in lista_risposta:
            return lista_risposta
        beta=copy.deepcopy(lista_precedente)
        var=alpha[d]
        if 1 in tupla_precedente:
            lista_risposta[e]=var
            d=d+1
            beta=copy.deepcopy(alpha)
            if lista_risposta.count("")==1:
                var=alpha[d]
                for i in range(lunghezza):
                    if lista_risposta[i]=="":
                        lista_risposta[i]=var
                return lista_risposta
        elif beta.count(var)==lunghezza-1:
            o=0
            for i in range(lunghezza):
                if beta[i]!=var:break
                o+=1
            lista_risposta[o]=var
            d=d+1
            beta=copy.deepcopy(alpha)
            if lista_risposta.count("")==1:
                var=alpha[d]
                for i in range(lunghezza):
                    if lista_risposta[i]=="":
                        lista_risposta[i]=var
                return lista_risposta
        var=alpha[d]
        e=0
        for i in range(lunghezza):
            if lista_risposta[i]!="":
                beta[i]=var
        for i in range(lunghezza):
            if beta[i]!=var:
                beta[i]=var
                break
            e=e+1
        return beta
        
        
            
    
        
                
        
        
            
            
            
