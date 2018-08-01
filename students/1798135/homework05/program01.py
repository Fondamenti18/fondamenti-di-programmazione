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
n=0
lista_indici=[]
last=0
base=0
controllo=True
trovato=False
temp=0

def decodificatore(configurazione):
    global last,lista_indici,base,n,trovato,controllo,temp
    #prima parte di inizializzazione
    
    configurazione2=configurazione.copy()   
        
    if len(configurazione2)==1:
        n=0
        lista_indici=[]
        last=0
        base=0
        controllo=True
        trovato=False
        temp=0
        n=n+1 
        trovato=True 
        return configurazione2[0]*[0]
    else:
        if max(configurazione2[-1][1])==0:
            last=n
            base=n
            n=n+1
            trovato=True            
            return configurazione2[0]*[n-1]
        #applico il core della strategia
        
        
        
        
        else:
            
            #mossa precendente e risultato
            
            ris=configurazione2[-1][0].copy()
            aiuti=configurazione2[-1][1]
            progresso=aiuti[0]+aiuti[1]  
           
            if len(configurazione2)>2:
                aiuti0=configurazione2[-2][1]
                progresso0=aiuti0[0]+aiuti0[1]
                
                
                
                
                if controllo:
                    #un casino per controllare il secondo valore
                    if temp>0:
                        if temp==22:
                            aiuti0=[2]
                            controllo=False
                        elif max(aiuti)==2:
                            aiuti=[2]
                            aiuti0=[0]
                            controllo=False                                                                                
                            #print("trovato un valore subito dopo ")
                        else:
                            controllo=False
                            
                    elif max(aiuti)==2 and last==n:                        
                        ris[ris.index(last)] =last+1
                        last=last+1
                        return ris
                    
                    elif max(aiuti)==2 and last>n:                         
                        lista_indici.append(ris.index(last))                        
                        ris[ris.index(last)+1] =n
                        ris[ris.index(last)] =base
                        temp=last
                        last=n
                        #controllo=False
                        trovato=False
                        #print(" \n  attento \n ")                        
                        return ris
                    
                    elif progresso==2 and last>n:
                        #caso in cui la posizione va bene
                        lista_indici.append(ris.index(last))                        
                        ris[ris.index(last)] =n                       
                        #controllo=False                        
                        n=last
                        trovato=True
                        if ris[0] == base:
                            ris[0]=n                            
                        else:
                            ris[1]=n
                        temp=22
                        return ris                            
                            
                    elif last>n:
                        ris[ris.index(last)] =last+1
                        last=last+1
                        return ris
                        
                    
                    
                    
                    
                #print("ci sono  n",n," indici",lista_indici," trovato ",trovato," aiuti",aiuti,"  ",aiuti0," last ",last)    
                #decisione da prendere    
                if max(aiuti)>max(aiuti0) and n in ris:    
                     if  max(aiuti)>len(lista_indici):                         
                         #quando trovo un valore 
                         #print("salvo il valore")
                         lista_indici.append(ris.index(n))
                         trovato=True
                         #controllo=True
                         n=n+1
                    
                elif trovato and progresso==progresso0 and n in ris:
                    #quando cerco un valore ma non c e
                    #print("ho codificato dall if")
                    if max(aiuti)<max(aiuti0):
                        print(min(aiuti))
                        if min(aiuti)==2:
                            trovato=False
                        lista_indici.append(ris.index(n))
                        ris[ris.index(n)] =base
                        #return ris                    
                    else:
                        ris[ris.index(n)] =n+1                    
                        n=n+1
                        last=n
                        return ris
                    
                elif max(aiuti)<max(aiuti0) and n in ris and max(aiuti0)!=2:
                    if min(aiuti)==2:
                            trovato=False
                    lista_indici.append(ris.index(n))
                    if ris.index(n)+1 in lista_indici:
                        ris[ris.index(n)+2] =n
                    else:
                        ris[ris.index(n)+1]=n
                    ris[ris.index(n)] =base
                    return ris                    
                elif last>base:
                    #tutto in regola                    
                    trovato=False
                    #controllo=False                    
            
            
            
            
            
            for x in range(configurazione2[0]):
                if trovato and x not in lista_indici:
                    #print("sono sempre in quel maledetto for")
                    ris[x]=n
                    last=n
                    break
                elif not trovato and x>ris.index(last) and x not in lista_indici:
                    #print("secondo for baby")
                    ris[x]=n
                    ris[ris.index(last)]=base
                    last=n                    
                    break
            return ris
                
                
                                            
                
                    
                    
            
     
