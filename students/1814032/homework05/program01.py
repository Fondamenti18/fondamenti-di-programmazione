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


Una conf del  gioco viene rappresentata come lista di liste (L). 
Il primo elemento di L e' un intero N rappresentante la lunghezza del codice.
Ciascuno degli eventuali altri elementi di L rappresenta un tentativo fin qui
effettuato dal decodificatore e la relativa risposta.
Piu' precisamente  L[i] con i>0, se presente, conterra' una tupla composta da due elementi:
- la lista di N cifre  con il tentativo effettuato dal decodificatore in un qualche passo precedente
- la tupla di interi (a,b) ricevuta in risposta.


Il programma che dovete realizzare contiene la seguente funzione:
 
    decodificatore(conf)

che e' l'AI che guida il gioco. La funzione  riceve come input la conf attuale del gioco e produce un tentativo (lista di caratteri in '0-9').

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
from collections import deque

#general use
digits = deque([0,1,2,3,4,5,6,7,8,9])
pool = []
n = 0
code = []

#used during first phase - pool discovering
finding_pool = True
exclude_one = False

#used during second phase - code guessing
dual_excl = []
dual_guess = []
moving = False
crucial_move = False
pos = 0
fillr = 0
sensr = 0

def decodificatore(conf):
	global pool
	#resets vars for new code guessing
	if len(conf) == 1: reset_vars(conf[0])
	#AI discovers pool
	global finding_pool
	if finding_pool: 
		g = guess_pool(conf)
		if g: return g
		else: 
			finding_pool = False
			if len(pool) < n: pool += digits
	#AI makes guesses
	global pos
	global dual_excl
	global dual_guess
	global fillr
	global sensr
	global crucial_move
	global moving
	#last move enabled to discover 2 positions
	if crucial_move:
		#sensr position was good in last guess
		good = (2 in conf[-1][1])
		i_good = dual_excl[good].index(sensr)
		i_bad = dual_excl[not good].index(sensr)
		code[dual_excl[good].index(sensr)] = sensr
		code[dual_excl[not good].index(sensr)] = fillr
		crucial_move = False
		moving = False
		#should I check if this HELL HAS FINISHED and provide the WAY TO HEAVEN?
		if (n - len(set(code) ^ set('x'))) <= 1:
			if n%2 == 1:
				code[code.index('x')] = pool.pop()
			#Bye bye!
			return code

	if not moving:
		moving = True
		pos = 0
		dual_excl = []
		fillr = pool.pop()
		sensr = pool.pop()
		dual_guess = deque([sensr]+[fillr]*(n-1))
	else:
		#dual exclusion piece found in last guess
		if 2 in conf[-1][1]:
			dual_excl.append(list(conf[-1][0]))
		#move forward
		pos += 1
		dual_guess.rotate()
		#stop moving if dual found or if there are no other possible combinations and make a guess to exclude
		if (len(dual_excl) == 2) | (pos == n-1):
			if (pos == n-1) & (len(dual_excl) == 1):
				dual_excl.append(list(dual_guess))
			#dual exec now contains 2 opposite combinations
			crucial_move = True
			if not pool:
				flood = list(set(code) ^ set('x'))[0]
			else:
				flood = pool[0]
			return [[x,flood][x == fillr] for x in dual_excl[1]]
	while code[pos] != 'x':
		pos += 1
		dual_guess.rotate()
	#if needed, cast dual_guess to list
	return dual_guess

def reset_vars(code_len):
	global finding_pool
	finding_pool = True
	global digits
	digits = deque([0,1,2,3,4,5,6,7,8,9])
	global pool
	pool = []
	global dual_excl
	dual_excl = []
	global dual_guess
	dual_guess = []
	global n
	n = code_len
	global code
	code = ['x']*n

def guess_pool(conf):
	global exclude_one
	global pool
	#absolute first guess
	if len(conf) != 1:
		#get sum of last guess' outcome
		succ = sum(conf[-1][1])
		#gotta exlude one of second to last guess
		if exclude_one:
			if succ == 1: pool.append(conf[-1][0][0])
			else: pool += list(set(conf[-2][0]) ^ set(conf[-1][0]))
			exclude_one = False
		#both in pool
		else:
			if succ == 2:
				for d in set(conf[-1][0]):
					pool.append(d)
			elif succ == 1:
				exclude_one = True
				return [conf[-1][0][0]]*n
	#pool completed
	if (len(pool) == n) | ((len(pool) + len(digits)) == n): return None
	#guess to discover pool
	return [digits.popleft()]*(n//2) + [digits.popleft()]*((n//2)+(n%2))