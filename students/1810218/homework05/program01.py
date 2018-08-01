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


import itertools


def answer(codice, proposta):
    
    a=0
    ins=set(codice)
    
    for i in range(len(codice)):
     
        try:
            if codice[i]==proposta[i]: a+=1
        except:
            break
       
    b=len(ins & set(proposta))-a    
    return (a,b)




soluz=set()





def decodificatore(configurazione):
    global soluz
  
    
    
    
    if len(configurazione)==1:
        a=set()
        a.update(itertools.permutations(['0','1','2','3','4','5','6','7','8','9'],configurazione[0]))
        soluz.update([''.join(x) for x in a])
        
        if configurazione[0]==6:
            return [0,1,2,3,4,5]
        elif configurazione[0]==7:
            return [0,1,2,3,4,5,6]
        else:
            return [0,1,2,3,4,5,6,7]
    
    elif len(configurazione)==2:
        
        tent=tuple(configurazione[1][0])
        risp=configurazione[1][1]
        
        
        ins2=soluz.copy()
        
        for guess in soluz:
            g=tuple(int(x) for x in guess)
            ans=answer(g,tent)
            
            if ans!=risp and (ans[1],ans[0])!=risp:
                
                ins2.remove(guess)
            
            
        soluz=ins2
        return [int(x) for x in soluz.pop()]
    else:
        
        tent=tuple(configurazione[-1][0])
        risp=configurazione[-1][1]
        ins_2=soluz.copy()
        for guess in soluz:
            g=tuple(int(x) for x in guess)
            ans=answer(g,tent)
            
            if ans!=risp and (ans[1],ans[0])!=risp:
                
                ins_2.remove(guess)
            
        soluz=ins_2
       
        return [int(x) for x in soluz.pop()]
    

