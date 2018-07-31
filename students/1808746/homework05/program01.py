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

from itertools import permutations

numTentativo = 0
cifreGiuste = 0
posizione = 0
permutazioni = list()

def decodificatore(configurazione):
    lun=configurazione[0] #si ricava la lunghezza del codice da indovinare
    #si richiamano le variabili globali che indicano il numero del tentativo (e anche il numero che andrò a provare nella lista), le cifregiuste del tentativo precedente, la posizione nella lista che si sta scorrendo e la lista che conterrà le permutazioni
    global numTentativo; global cifreGiuste; global posizione; global permutazioni

    if len(configurazione)==1:
        '''PRIMO TENTATIVO'''
        #creo una possibile lista con lo 0 ripetuto per lun
        risposta = [0]*lun
        
        #azzero le variabili (nel caso sia un nuovo codice da indovinare)
        numTentativo, cifreGiuste, posizione = 0,0,0
        permutazioni = list()
        
        return risposta
            
    else:
        '''TENTATIVI SUCCESSIVI'''
        #lavoro con l'ultimo tentativo fatto (ovvero configurazione[:-1]): ricavo la lista dell'ultima risposta data e le NUOVE a,b
        rispostaPre = configurazione[-1][0]
        a, b = configurazione[-1][1]
        
        #si verifica se nell'ultimo tentativo sono state trovate tutte le cifre corrette (nel posto giusto o sbagliato)
        if a+b==lun and permutazioni==[]:
            '''TROVATI I NUMERI PRESENTI (prima volta)'''
            #rispostaPre contiene tutti i numeri corretti ma in posizione sbagliata; procedo alla creazione di tutte le permutazioni di questi numeri inserendoli nella lista permutazioni
            for el in permutations(rispostaPre, len(rispostaPre)):
                permutazioni.append(list(el))

            return permutazioni[0]
        
        if a+b==lun:
            '''TROVATI I NUMERI PRESENTI (questo if è soddisfatto anche dalla seconda volta in poi)'''
            permutazioni.remove(rispostaPre) #rimuovo la risposta che non era giusta dalle possibilità
            
    
            #se a o b è uguale a 0, elimino tutti i codici che danno lo stesso risultato (perché inutili: se tutti i numeri fossero nella posizione giusta, sarebbe il codice giusto, quindi significa che sono tutti nella posizione sbagliata
            #elimino dalla lista di permutazioni, tutte quelle permutazioni che non avrebbero la stessa risposta di rispostaPre
            for perm in permutazioni:
                tupla = confronta_perm(rispostaPre, perm)
                if tupla!=(a,b) and tupla!=(b,a):
                    '''DECIDI QUALI TRA LE DUE:
                            permutazioni.remove(perm)
                            del permutazioni[permutazioni.index(perm)]
                    '''
                    del permutazioni[permutazioni.index(perm)]
            
            #ritorno sempre la prima permutazione, finché alla lista non sarà rimasto solo il codice giusto
            return permutazioni[0]
        
        numTentativo += 1
        #incremento la posizione solo se il numero aggiunto nel tentativo precedente è presente nel codice
        #altrimenti il nuovo numero (numTentativo) andrà nella posizione precedente, ovvero andrà a sostituire il numero aggiunto prima in quanto inutile
        if a+b > cifreGiuste: posizione += 1
        
        rispostaPre[posizione] = numTentativo
        cifreGiuste = a+b #aggiorno la variabile con gli a,b di questo tentativo per il prossimo
        
        return rispostaPre


def confronta_perm(codice, perm):
    '''Restituisce la compatibilità tra una permutazione e il codice del primo parametro'''
    a=0
    ins=set(codice)
    for i in range(len(codice)):
        if codice[i]==perm[i]: a+=1
    b=len(ins & set(perm))-a    # cifre del codice in comune con il tentativo, meno quelle azzeccate esattamente
    return a,b

        
        
        
        