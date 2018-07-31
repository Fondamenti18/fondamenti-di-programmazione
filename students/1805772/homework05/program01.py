'''
Obiettivo dell'esercizio e' sviluppare la strategia di gioco per il gioco del Mastermind. 

Nel gioco del Mastermind un giocatore (il "decodificatore"), deve indovinare un codice segreto.
Il codice segreto e' di N cifre decimali distinte (NO RIPETIZIONI, solo 10 possibili simboli per ciascuna posizione).
Il decodificatore cerca di indovinare il codice per tentativi. Strategicamente nel tentativo 
possono essere presenti anche cifre ripetute pur sapendo che nel codice non sono presenti ripetizioni. 
In risposta ad ogni tentativo viene fornito un aiuto producendo una coppia di interi (a,b) dove:

- a e' il numero di cifre giuste al posto giusto,
cioe' le cifre del codice da indovinare che sono effettivamente presenti nel tentativo al posto giusto.
- b e' il numero di cifre giuste ma al posto sbagliato,
cioe' le cifre del codice da indovinare che sono effettivamente presenti nel tentativo solo al posto sbagliato.

Ad esempio per il codice
    34670915 e il tentativo
    93375948
la risposta deve essere la coppia (2,3).
Il 2 viene fuori dal contributo delle cifre 7 e 9 del codice da indovinare in quarta e sesta posizione,
il numero 3 e' dovuto alle cifre 3,4,5 che compaiono tra le cifre del tentativo ma mai al posto giusto.

Nella nostra versione di Mastermind il valore di N (lunghezza del codice) puo' essere 6, 7 o 8 e nella coppia data
in risposta ai tentativi non si vuole rivelare quale delle due cifre rappresenta il numero di cifre giuste al posto giusto 
di conseguenza nella coppia di risposta i valori di a e b possono risultare invertiti.
Ad esempio per il codice 34670915 e il tentativo 93375948 le risposte (2,3) e (3,2) sono entrambe possibili.


Una configurazione del gioco viene rappresentata come lista di liste (L). 
Il primo elemento di L e' un intero N rappresentante la lunghezza del codice.
Ciascuno degli eventuali altri elementi di L rappresenta un tentativo fin qui
effettuato dal decodificatore e la relativa risposta.
Piu' precisamente  L[i] con i>0, se presente, conterra' una tupla composta da due elementi:
- la lista di N cifre con il tentativo effettuato dal decodificatore in un qualche passo precedente
- la tupla di interi (a,b) ricevuta in risposta.


Il programma che dovete realizzare contiene la seguente funzione:
 
    decodificatore(configurazione)

che e' l'AI che guida il gioco. La funzione riceve come input la configurazione attuale del gioco e produce un tentativo
(lista di caratteri in '0-9').

Per questo esercizio la valutazione avverra' nel seguente modo: 
avete 150 tentativi e 30 secondi di tempo per indovinare quanti piu' codici possibile.
Il punteggio ottenuto e' dato dal numero di codici che riuscite ad indovinare.

Tutti i vostri elaborati al termine verranno valutati su di uno stesso set di codici,
questa operazione determinera' una classifica dei vostri elaborati.
Per entrare in classifica bisogna indovinare almeno cinque codici.
La classifica viene suddivisa in 14 fasce che corrispondono ai voti da 18 a 31 ed a 
ciascun programma viene assegnato il voto corrispondente.
Se il numero di valori diversi e' minore di 14 il voto sara' proporzionale alla posizione
nella graduatoria (con il primo che prende 31 e l'ultimo 18)

In allegato vi viene fornito un simulatore di gioco (simulatore1.py) che vi permettera' di 
autovalutare la vostra strategia. Il simulatore genera codici casuali e invoca il vostro 
programma per ottenere i vari tentativi. Appena un codice viene indovinato ne viene 
proposto uno nuovo. Il processo termina quando avete esaurito i vostri 150 tentativi
o sono passati i 30 secondi.

ATTENZIONE: NON usate lettere accentate ne' nel codice ne' nei commenti
'''

import random

# DA_ESAMINARE sono i numeri da sistemare
DA_ESAMINARE = []
# ESAMINATI sono i numeri sistemati
ESAMINATI = []
# CODICE_BASE sono i numeri che mi porto appresso durante l'esecuzione, e che aggiorno con i gpg e gps
CODICE_BASE = []
# PROBABILI contiene i numeri probabili del CODICE_BASE
PROBABILI = []
# BANDIERA e' una variabile che mi dice se fare o meno un'istruzione
BANDIERA = True
# TROVATO e' una variabile che mi dice se fare o meno un'istruzione
TROVATO = True
# PROCEDERE e' una variabile che mi dice se fare o meno un'istruzione
PROCEDERE = False
# OK e' una variabile che mi dice se fare o meno un'istruzione
OK = True

def tentativoCasuale(numeri):
    ''' Questa funzone mi genera un tetativo casuale data una lista di numeri. '''
    lunghezza = len(numeri)
    x = ''.join([str(numero) for numero in numeri])
    risposta = []
    for _ in range(lunghezza):
        estratto = random.randint( 0 , len(x) - 1)
        risposta.append( int( x[estratto] )  )
        x = x.replace(x[estratto] , '')
    return risposta

def scambia(lista , n1):
    ''' Questa funzione serve a spostare indietro il numero "n1" (il piu' piccolo di "DA_ESAMINARE"). '''
    indice_n1 = lista.index(n1)
    indice_n2 = indice_n1 - 1
    # finquando il numero che esce fuori da lista[indice_n2] si trova nei numeri esaminati, mi sottrai uno (spostando l'indice)
    while lista[indice_n2] in ESAMINATI: indice_n2 -= 1
    n2 = lista[indice_n2]
    lista[indice_n1] = n2
    lista[indice_n2] = n1
    return lista

def esaminando(tentativo):
    ''' Questa funzione serve a capire con chi ho scambiato il numero che sto' esaminando. '''
    # esaminando1 e' il numero che sto' esaminando
    esaminando1 = min(DA_ESAMINARE)
    indice1 = tentativo.index(esaminando1)
    indice2 = indice1 + 1
    try: esaminando2 = tentativo[indice2]
    except IndexError: indice2 = 0
    while tentativo[indice2] in ESAMINATI:
        if indice2 == (len(tentativo) - 1):
            indice2 = 0
        else:
            indice2 += 1
    # esaminando2 e' il numero che scambio con esaminando1
    esaminando2 = tentativo[indice2]
    return esaminando1 , esaminando2

def scopri(codice , n1 , n2):
    ''' Questa funzione compie un primo passo per scoprire quale numero e' gpg.
    Se il risultato e' (1,1) "n1" e' gps, e "n2" e' gpg.
    Se il risultato e' (0,2) "n1" e' gpg. '''
    risposta = []
    for conta , valore in enumerate(codice):
        if codice[conta] != n1: risposta.append(n2)
        else: risposta.append(n1)
    return risposta

def ultimoPenultimo(ultimo , penultimo):
    ''' Questa funzione mi restituisce gli indizi e i tentativi di configurazione[-1] e configurazione[-2].
    ultimo e' l'ultimo elemento di configurazione ovvero l'ultimo tentativo + indizi.
    penultimo e' il penultimo elemento di configurazione ovvero il penultimo tentativo + indizi. '''
    ultimo_tentativo = ultimo[0].copy()
    ultimo_indizio = ultimo[1]
    penultimo_tentativo = penultimo[0].copy()
    penultimo_indizio = penultimo[1]
    return ultimo_tentativo , ultimo_indizio , penultimo_tentativo , penultimo_indizio

def codiceIniziale(ultimo_tentativo , ultimo_indizio , lunghezza , tentativi):
    ''' Questa funzione mi scopre i numeri giusti. '''
    global CODICE_BASE , PROBABILI
    risposta = []
    
    if tentativi > 6:
        if len(PROBABILI) == 0:
            return True , CODICE_BASE
            
        if 1 in ultimo_indizio:
            CODICE_BASE.append(ultimo_tentativo[0])
            PROBABILI[0:1] = []
        else:
            CODICE_BASE.append(PROBABILI[0][1])
            PROBABILI[0:1] = []
            
        if len(PROBABILI) == 0:
            return True , CODICE_BASE
        
        risposta = [PROBABILI[0][0]] * lunghezza
        return False , risposta
    else:
        if sum(ultimo_indizio) == 2:
            CODICE_BASE.append(ultimo_tentativo[0])
            CODICE_BASE.append(ultimo_tentativo[-1])
        elif 1 in ultimo_indizio:
            PROBABILI.append( [ultimo_tentativo[0] , ultimo_tentativo[-1]] )

        # if tentativi == 6 and PROBABILI != []: allora mi ritorni False, e il primo elemento della prima lista di PROBABILI
        if tentativi == 6 and PROBABILI != []: return False , [PROBABILI[0][0]] * lunghezza
        # elif tentativi == 6 and PROBABILI == []: allora mi ritorni True e il CODICE_BASE (non risposta, che senno' mi farebbe 10 e 11)
        elif tentativi == 6 and PROBABILI == []: return True , CODICE_BASE
        
        risposta = [ultimo_tentativo[0] + 2] * (lunghezza // 2) + [ultimo_tentativo[-1] + 2] * (lunghezza - (lunghezza // 2))
        return False ,  risposta

# === FUNZIONI HOMEWORK ===

def decodificatore(configurazione):
    global DA_ESAMINARE , ESAMINATI , CODICE_BASE , BANDIERA , TROVATO , PROCEDERE , OK
    # lunghezza del codice da decodificare
    lunghezza = configurazione[0]
    risposta = []
    # numero di tentativi + lunghezza
    tentativi = len(configurazione)
    
    if tentativi == 1:
        # inizializzazione
        DA_ESAMINARE = []
        ESAMINATI = []
        CODICE_BASE = []
        BANDIERA = True
        TROVATO = False
        PROCEDERE = False
        risposta = [0] * (lunghezza // 2) + [1] * (lunghezza - (lunghezza // 2))
        return risposta
    
    if PROCEDERE == False:
        # ricerca dei numeri del codice
        ultimo = configurazione[-1]
        ultimo_tentativo = ultimo[0].copy()
        ultimo_indizio = ultimo[1]
        PROCEDERE , risposta = codiceIniziale(ultimo_tentativo , ultimo_indizio , lunghezza , tentativi)
        if PROCEDERE == False:
            return risposta
        else:
            DA_ESAMINARE = risposta.copy()
            return DA_ESAMINARE

    if TROVATO == False:
        # questa if mi mischia i numeri finquando non ho una sequenza dove non c'e' neanche un gpg
        ultimo_tentativo , ultimo_indizio ,\
        penultimo_tentativo , penultimo_indizio = ultimoPenultimo(configurazione[-1] , configurazione[-2])
        if lunghezza in ultimo_indizio:
            TROVATO = True
            OK = False
        else:
            risposta = tentativoCasuale(ultimo_tentativo.copy())
            return risposta   
    else:
        ultimo_tentativo , ultimo_indizio ,\
        penultimo_tentativo , penultimo_indizio = ultimoPenultimo(configurazione[-1] , configurazione[-2])
        # se il max(penultimo_indizio) != max(ultimo_indizio), allora c'e' stato un cambiamento.
        # BANDIERA == True solo se il mio ultimo tentativo non proviene da scopri()
        if max(penultimo_indizio) != max(ultimo_indizio) and BANDIERA == True:
            OK = True
            if ultimo_tentativo == CODICE_BASE and max(penultimo_indizio) - max(ultimo_indizio) in (2 , -2):
                n1 , n2 = esaminando(ultimo_tentativo.copy())
                DA_ESAMINARE.remove(n1)
                ESAMINATI.append(n1)
                DA_ESAMINARE.remove(n2)
                ESAMINATI.append(n2)
            elif ultimo_tentativo == CODICE_BASE:    
                n1 , n2 = esaminando(ultimo_tentativo.copy())
                risposta = scopri(ultimo_tentativo.copy() , n1 , n2)
                return risposta
            # ultimo_tentativo != CODICE_BASE se il mio ultimo tentativo proviene da scopri()
            else:
                if max(ultimo_indizio) == 2:
                    DA_ESAMINARE.remove(min(ultimo_tentativo))
                    ESAMINATI.append(min(ultimo_tentativo))
                else:
                    DA_ESAMINARE.remove(max(ultimo_tentativo))
                    ESAMINATI.append(max(ultimo_tentativo))
                # BANDIERA = False serve per non far scattare l'if di riga 225
                BANDIERA = False
                return CODICE_BASE
        elif ultimo_tentativo == penultimo_tentativo and OK == True:
            DA_ESAMINARE = ultimo_tentativo
            ESAMINATI = []
            TROVATO = False
            return ultimo_tentativo
            
    risposta = scambia( ultimo_tentativo , min(DA_ESAMINARE) )
    CODICE_BASE = risposta.copy()
    BANDIERA = True
    return risposta
