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
import itertools
fase_iniziale = True
fase_centrale = True
fase_finale = True
permutazioni = set()
permutazioni1 = set()
cifre_presenti = []
cifre_non_presenti = []

def decodificatore(configurazione):
	global permutazioni
	global permutazioni1
	global fase_iniziale
	global fase_centrale
	global fase_finale
	global cifre_presenti 
	global cifre_non_presenti 
	n = configurazione[0]
	if len(configurazione) == 1:
		permutazioni = set()
		cifre_presenti = []
		cifre_non_presenti = []
		fase_iniziale = True
		fase_centrale = True
		if n == 8:
			return [0 for j in range(8)]
	if fase_iniziale:
		if n == 8:
			fase_inziale = False
			if len(cifre_presenti) < n and len(cifre_non_presenti) < 10 - n :
				if 1 in configurazione[len(configurazione) - 1][1]:
					cifre_presenti  += [len(configurazione) - 2]
				else :
					cifre_non_presenti += [len(configurazione) - 2]
				return [len(configurazione) - 1 for j in range(n)]
			if len(cifre_presenti) == n :
				cifre_non_presenti = [j for j in range(10) if j not in cifre_presenti]
			if len(cifre_non_presenti) == 10 - n :
				cifre_presenti = [j for j in range(10) if j not in cifre_non_presenti]
		else:
			permutazioni = set(itertools.permutations([0,1,2,3,4,5,6,7,8,9],n))
			codice_estratto = permutazioni.pop()
			fase_iniziale = False
			return codice_estratto
	if n == 8  :
		if fase_centrale:
			permutazioni1 = set(itertools.permutations(cifre_presenti))
			codice_estratto = permutazioni1.pop()
			fase_centrale = False
			return codice_estratto
		if fase_finale:
			temp_permutazioni = set()
			for s in permutazioni1:
				l = len(configurazione)
				tupla1 = configurazione[l - 1][1]
				if risposta(configurazione[l - 1][0], s) == tupla1 or risposta(configurazione[l - 1][0], s) == tupla1[:: -1]:
					temp_permutazioni.add(s)
				permutazioni1 = temp_permutazioni
			return permutazioni1.pop()
	else:
		temp_permutazioni = set()
		for p in permutazioni:
			l = len(configurazione)
			tupla = configurazione[l - 1][1]
			if risposta(configurazione[l - 1][0], p) == tupla or risposta(configurazione[l - 1][0], p) == tupla[:: -1]:
				temp_permutazioni.add(p)
			permutazioni = temp_permutazioni
		return permutazioni.pop()
			
def risposta(codice, proposta):
    a=0
    ins=set(codice)
    for i in range(len(codice)):
        if codice[i]==proposta[i]: a+=1
    b=len(ins & set(proposta))-a    # cifre del codice in comune con il tentativo, meno quelle azzeccate esattamente
    return a,b
			

