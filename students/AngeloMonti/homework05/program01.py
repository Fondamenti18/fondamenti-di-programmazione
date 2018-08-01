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


def genera_parola(n,configurazione):
    lista=configurazione[len(configurazione)-1][0][:]
    preso=[0]*10
    for i in range(len(lista)):
        preso[lista[i]]=1
    i=n-1
    preso[lista[i]]=0
    while True:
        j=lista[i]+1
        while j<10 and preso[j]: j+=1
        if j==10:
            lista[i]=-1
            i=i-1 
            preso[lista[i]]=0
        else:
            lista[i]=j
            preso[j]=1
            i+=1
            if i==n:
                if compatibile(lista, configurazione): return lista
                i-=1
                preso[lista[i]]=0

def compatibile(x, partite):
    ins=set(x)
    for i in range(1,len(partite)):
        partita=partite[i][0]
        a,b=partite[i][1]
        count=0
        for j in range(len(x)):
            if x[j]==partita[j]:count+=1
        if count!=a and count!=b: return False
        if count==a: 
            if len(ins & set(partita))-count!= b: return False
        if count==b: 
            if len(ins & set(partita))-count!= a: return False
    return True


def decodificatore(configurazione):
    n=configurazione[0]
    tot= len(configurazione)
    if tot==1: 
        if n==6: return [0,1,2,3,4,5]
        if n==7: return [0,1,2,3,4,5,6]
        return [0,1,2,3,4,5,6,7]
    else: return genera_parola(n,configurazione)
    



