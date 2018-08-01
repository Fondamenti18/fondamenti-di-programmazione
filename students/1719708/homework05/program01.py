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

############################################ CONFIGURAZIONE BASE DI LUNGHEZZA N E RESET VARIABILI GLOBALI

def configurazione_base(n):
	global cifre, posti_vacanti, posizione, verifica, migliore, risposta, cancellazione
	cifre = '0123456789'
	temp = len(cifre)
	verifica = 0
	posti_vacanti = [x for x in range(n)]
	migliore = [0 for x in range(n)]
	posizione = posti_vacanti[0]                         #SELEZIONO LA POSIZIONE DEL CODICE IN CUI CAMBIARE CIFRA
	risposta = migliore[:]
	cancellazione = 0

	
def decodificatore(configurazione):
	
	global cifre, cancellazione, posizione, verifica, posti_vacanti, risposta, indizio, indizio_p, indizio_p_r, migliore, indizio_verifica, indizio_cancellazione
	
	n = configurazione[0]                                    #LUNGHEZZA CODICE
	
	if len(configurazione) == 1:
		configurazione_base(n)                    #CODICE DI PARTENZA E AZZERAMENTO VARIABILI
	
	elif len(posti_vacanti) == 2 and len(cifre) == 1:
				temp = risposta[posti_vacanti[0]]
				risposta[posti_vacanti[0]] = risposta[posti_vacanti[1]]
				risposta[posti_vacanti[1]] = temp
	
	else:
	
		indizio = configurazione[-1][1]                      #ULTIMO INDIZIO
		
		if len(configurazione) > 2 and verifica != 2 and cancellazione != 1:
			indizio_p = configurazione[-2][1]                #INDIZIO PRECEDENTE
			indizio_p_r = (indizio_p[1], indizio_p[0])       #INDIZIO PRECEDENTE AL CONTRARIO
		elif len(configurazione) > 2 and verifica == 2:
			indizio_p = indizio_verifica                	 #CAMBIO GLI INDIZI PRECEDENTI SE HO FATTO LA VERIFICA
			indizio_p_r = (indizio_p[1], indizio_p[0])
			verifica = 3
			#print("INDIZIO DI VERIFICA", indizio_verifica)
		elif len(configurazione) > 2 and cancellazione == 1: #CAMBIO GLI INDIZI PRECEDENTI SE HO CANCELLATO UNA CIFRA
			indizio_p = indizio_cancellazione
			indizio_p_r = (indizio_p[1], indizio_p[0])
			cancellazione = 0
			
		if len(cifre) > 1:
		
			if indizio == (0, 0):                            #SE L'INDIZIO È 0,0 CAMBIO IL CODICE DI PARTENZA AUMENTANDOLO DI 1
				cifre = cifre[1:]
				risposta = [int(cifre[0]) for x in range(n)]
				migliore = risposta[:]
			
			elif (indizio == (1, 0) or indizio == (0, 1)) and verifica == 0:
				cifre = cifre[1:]
				risposta[posizione] = int(cifre[0])
			
			#VERIFICA SE LA CIFRA CAMBIATA SI TROVA SUL POSTO DI UN'ALTRA CIFRA CORRETTA
			
			elif verifica == 0 and (indizio == (2, 0) or indizio == (0, 2)):
				risposta[posizione] = int(cifre[1])
				indizio_verifica = indizio_p
				verifica = 1
				#print("LANCIO VERIFICA")
			
			elif verifica == 1:
				if indizio == (2, 0) or indizio == (0, 2):
					posizione = posti_vacanti[posti_vacanti.index(posizione) + 1]
					risposta = migliore[:]
					risposta[posizione] = int(cifre[0])
					#print("CAMBIO CIFRA")
					verifica = 2
				elif indizio == (1, 1):
					risposta[posizione] = int(cifre[0])
					#print("CIFRA PRECEDENTE")
					verifica = 2
				else:
					risposta[posizione] = risposta[posizione] + 1
					#print("CONTINUO VERIFICA")
			
			#SE L'INDIZIO RIMANE UGUALE ALLORA LA CIFRA NON FA PARTE DEL CODICE
			
			elif (indizio == indizio_p or indizio == indizio_p_r) and 0 in indizio:
				risposta = migliore[:]
				cifre = cifre[1:]
				risposta[posizione] = int(cifre[0])
				#print("INDIZI UGUALI CON 0")
			
			#VERIFICA SE LA CIFRA INSERITA SI TROVA NEL POSTO CORRETTO
			
			elif indizio != indizio_p and indizio != indizio_p_r and 0 in indizio:
				#print("INDIZI DIVERSI CON 0")
				migliore = risposta[:]
				cifre = cifre[1:]
				del posti_vacanti[posti_vacanti.index(posizione)]
				posizione = posti_vacanti[0]
				risposta[posizione] = int(cifre[0])
			
			#VERIFICA SE LA CIFRA INSERITA FA PARTE DEL CODICE
			
			elif indizio != indizio_p and indizio != indizio_p_r and indizio[0] + indizio[1] == indizio_p[0] + indizio_p[1] and 0 in indizio_p:
				cifre = cifre[1:]
				risposta[posizione] = int(cifre[0])
				indizio_cancellazione = indizio_p
				cancellazione = 1
				
				#print("NON FA PARTE DEL CODICE")

			#ALTRIMENTI SE LA CIFRA SI TROVA NEL POSTO SBAGLIATO LA SPOSTA
			
			else:
				#print("ELSE")
				risposta = migliore[:]
				posizione = posti_vacanti[posti_vacanti.index(posizione) + 1]
				risposta[posizione] = int(cifre[0])
				
	return risposta