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

from  random import choice, randint
from itertools import permutations

# ESEMPIO di strategia che tira a caso una combinazione di N valori anche ripetuti

step = 0
target = 0
soluzione = []
subchecking = False
totali = 0
indovinati = 0
todomundo = []
initialcombo = []
initialsteps = 5
secondphase = []
sp_counter = -1
second_phase_check_point = 0
rightFixed = False
mergedData = []
sfighe = 0
allComboLeft = []
allComboRight = []
lastCombo = []
cifre = []
cifre2 = []
greedy = True

def generateLastCombo():
	global lastCombo, allComboLeft, allComboRight
	if lastCombo == []:
		for left in allComboLeft:
			for right in allComboRight:
				combo = [-1]*8
				combo[0] = left[0]
				combo[1] = left[1]
				combo[2] = left[2]
				combo[3] = left[3]
				combo[4] = right[0]
				combo[5] = right[1]
				combo[6] = right[2]
				combo[7] = right[3]
				lastCombo.append(combo)
			

def isAllSame(lista):
	first = lista[0]
	for l in lista:
		if l != first:
			return False
	return True

def merge(combo1, combo2,n):
	x = [-1]*n
	#if n==6:
	'''
	for i in range(0,3):
		x[i] = combo1[i]
	for i in range(3,6):
		x[i] = combo2[i]
	'''
	x[0] = combo2[3]+1
	x[1] = combo1[0]
	return x

def isMergeIndex(i):
	global mergedData
	for md in mergedData:
		index = md[3]+initialsteps+1
		if i == index:
			return True
	return False

def generateTodoMundo(n):
	global todomundo
	for i in range(n):
		todomundo.append([])
	#('TODO MUNDO = ',todomundo)

def isAvailable(cifra,todo):
	for t in todo:
		if cifra == t:
			return False
	return True

def generateInitialCombo(n):
	global initialcombo
	if n == 7:
		initialcombo.append((0,0,0,0,1,1,1))
		initialcombo.append((2,2,2,2,3,3,3))
		initialcombo.append((4,4,4,4,5,5,5))
		initialcombo.append((6,6,6,6,7,7,7))
		initialcombo.append((8,8,8,8,9,9,9))
	if n == 6:
		initialcombo.append((0,0,0,1,1,1))
		initialcombo.append((2,2,2,3,3,3))
		initialcombo.append((4,4,4,5,5,5))
		initialcombo.append((6,6,6,7,7,7))
		initialcombo.append((8,8,8,9,9,9))
	if n == 8:
		initialcombo.append((0,0,0,0,1,1,1,1))
		initialcombo.append((2,2,2,2,3,3,3,3))
		initialcombo.append((4,4,4,4,5,5,5,5))
		initialcombo.append((6,6,6,6,7,7,7,7))
		initialcombo.append((8,8,8,8,9,9,9,9))

def nextTryLeftWithDistance(n,old,d):
	next = [-1]*n
	if n == 6:
		if d == 3:
			next[0] = old[2]
			next[1] = old[0]
			next[2] = old[1]
			if isTryTollerable(next):
				return next
			else:
				next[0] = old[1]
				next[1] = old[2]
				next[2] = old[0]
				return next
		if d==2:
			next[0] = old[0]
			next[1] = old[2]
			next[2] = old[1]
			if isTryTollerable(next):
				return next
			else:
				next[0] = old[2]
				next[1] = old[1]
				next[2] = old[0]
				if isTryTollerable(next):
					return next
				else:
					next[0] = old[1]
					next[1] = old[0]
					next[2] = old[2]
					return next
			
		
def nextTryRightWithDistance(n,old,d):
	next = [-1]*n
	k = 0
	if n == 7:
		k = 1
	if n == 8:
		k = 2
		
	if d == 3:
		next[3+k] = old[5+k]
		next[4+k] = old[3+k]
		next[5+k] = old[4+k]
		if isTryTollerable(next):
			return next
		else:
			next[3+k] = old[4+k]
			next[4+k] = old[5+k]
			next[5+k] = old[3+k]
			return next
	if d==2:
		next[3+k] = old[3+k]
		next[4+k] = old[5+k]
		next[5+k] = old[4+k]
		if isTryTollerable(next):
			return next
		else:
			next[3+k] = old[5+k]
			next[4+k] = old[4+k]
			next[5+k] = old[3+k]
			if isTryTollerable(next):
				return next
			else:
				next[3+k] = old[4+k]
				next[4+k] = old[3+k]
				next[5+k] = old[5+k]
				return next
				
			
def isTryTollerable(next):
	global todomundo
	for i in range(len(todomundo)):
		if next[i] == -1:
			continue
		if not isAvailable(next[i],todomundo[i]):
			return False
	return True
	
def findSafeSpot(n):
	global todomundo
	if n==6:
		spot = -1
		for i in range(0,10):
			howmany = 0
			#print('searching for ',i)
			ti = 0
			for t in todomundo:
				#print('			looking in todomundo  ', t)
				if i not in t:
					#print(' -------- vero, ',i,'  non e in todomundo: ',t)
					if howmany == 1:
						spot = -1
						break
					else:
						howmany = 1
						spot = ti
				ti+=1
				if ti == 3:
					break
			if howmany == 1 and spot != -1:
				return (i,spot)
	return None
			
	
def generateAllCombo(cifre):
	return list(permutations(cifre))
	

def getRightCifre(n):
	global todomundo,greedy
	if n == 8 and  greedy:
		cifre = [-1]*4
		cifre2 = [-1]*4
		used = []
		for i in range(0,4):
			guess = 0
			while(True):
				if isAvailable(guess, todomundo[i]) and isAvailable(guess,used):
					cifre[i]=guess
					print('                           GUESS = ',guess)
					used.append(guess)
					break
				guess+=1
				if guess == 10:
					return None
		for i in range(4,8):
			guess = 0
			while(True):
				if isAvailable(guess, todomundo[i]) and isAvailable(guess,used):
					cifre2[i-4]=guess
					print('                           GUESS = ',guess)
					used.append(guess)
					break
				guess+=1
				if guess == 10:
					return None
		return (cifre,cifre2)
		
	if n == 8 and not greedy:
		cifre = [-1]*4
		used = []
		for i in range(0,4):
			guess = 0
			while(True):
				if isAvailable(guess, todomundo[i+4]) and isAvailable(guess,used):
					cifre[i]=guess
					print('                           GUESS = ',guess)
					used.append(guess)
					break
				guess+=1
				if guess == 10:
					return None
		return cifre	

def getLeftCifre(n):
	global todomundo
	
	if n == 7:
		cifre = [-1]*4
		used = []
		for i in range(0,4):
			guess = 0
			while(True):
				if isAvailable(guess, todomundo[i]) and isAvailable(guess,used):
					cifre[i]=guess
					print('                           GUESS = ',guess)
					used.append(guess)
					break
				guess+=1
				if guess == 10:
					return None
		return cifre
		
		
def nextTryLeft(n,configurazione):
	global todomundo,allComboLeft,cifre
	next = [-1]*n
	used = []
	if n==6:
		coppia = findSafeSpot(n)
		if coppia != None:
			valore = coppia[0]
			spot = coppia[1]
			next[spot] = valore
			used.append(valore)
			print('COPPIA = ',coppia)
			#input('coppia')
		
		for i in range(0,3):
			if coppia != None:
				if i == coppia[1]:
					continue
			guess = 0
			while(True):
				if isAvailable(guess, todomundo[i]) and isAvailable(guess,used):
					next[i]=guess
					print('                           GUESS = ',guess)
					used.append(guess)
					break
				guess+=1
				if guess == 10:
					return None
	if n == 7:
		if allComboLeft == []:
			cifre = getLeftCifre(7)
			allComboLeft = generateAllCombo(cifre)
			for p in allComboLeft:
				print(p)
			#input('wait')
			next[0] = cifre[0]
			next[1] = cifre[0]
			next[2] = cifre[1]
			next[3] = cifre[1]
		else:
			lastRisposta = configurazione[len(configurazione)-1][1]
			print('LAST RESULT = ',lastRisposta)
			if lastRisposta == (4,1):
				next[0] = cifre[0]
				next[1] = cifre[1]
				next[2] = -1
				next[3] = -1
			if lastRisposta == (3,2):
				next[0] = cifre[1]
				next[1] = cifre[2]
				next[2] = cifre[0]
				next[3] = cifre[3]
			if lastRisposta == (5,0):
				next[0] = cifre[0]
				next[1] = cifre[2]
				next[2] = cifre[1]
				next[3] = cifre[3]
			if len(allComboLeft) <=3:
				next[0] = allComboLeft[0][0]
				next[1] = allComboLeft[0][1]
				next[2] = allComboLeft[0][2]
				next[3] = allComboLeft[0][3]
			print('next = ',next)
			#input('mo vediamo')
	if n == 8:
		if allComboLeft == []:			
			allComboLeft = generateAllCombo(cifre)
			for p in allComboLeft:
				print(p)
			#input('wait')
			next[0] = cifre[0]
			next[1] = cifre[1]
			next[2] = cifre[2]
			next[3] = cifre[3]
			next[4] = cifre[4]
			next[5] = cifre[5]
			next[6] = cifre[6]
			next[7] = cifre[7]
			
		else:
			lastRisposta = configurazione[len(configurazione)-1][1]
			print('LAST RESULT = ',lastRisposta)
			if lastRisposta == (4,1):
				next[0] = cifre[0]
				next[1] = cifre[1]
				next[2] = -1
				next[3] = -1
			if lastRisposta == (3,2):
				next[0] = cifre[1]
				next[1] = cifre[2]
				next[2] = cifre[0]
				next[3] = cifre[3]
			if lastRisposta == (5,0):
				next[0] = cifre[0]
				next[1] = cifre[2]
				next[2] = cifre[1]
				next[3] = cifre[3]
			if len(allComboLeft) <=3:
				next[0] = allComboLeft[0][0]
				next[1] = allComboLeft[0][1]
				next[2] = allComboLeft[0][2]
				next[3] = allComboLeft[0][3]
			print('next = ',next)
			#input('mo vediamo')
				
			
		

		
	return next
	
	
def nextTryRight(n,configurazione):
	global allComboRight,cifre,allComboLeft
	next = [-1]*n
	used = []
	if n==6:
		for i in range(3,6):
			guess = 0
			while(True):
				if isAvailable(guess, todomundo[i]) and isAvailable(guess,used):
					next[i]=guess
					print('                           GUESS = ',guess)
					used.append(guess)
					break
				guess+=1
				if guess == 10:
					return None
	if n==7:
		for i in range(4,7):
			guess = 0
			while(True):
				if isAvailable(guess, todomundo[i]) and isAvailable(guess,used):
					next[i]=guess
					print('                           GUESS = ',guess)
					used.append(guess)
					break
				guess+=1
				if guess == 10:
					return None
	if n == 8 and not greedy:
		if allComboRight == []:
			cifre = getRightCifre(8)
			allComboRight = generateAllCombo(cifre)
			for p in allComboRight:
				print(p)
			next[4] = cifre[0]
			next[5] = cifre[1]
			next[6] = cifre[2]
			next[7] = cifre[3]
		else:
		
			lastRisposta = configurazione[len(configurazione)-1][1]
			tentativo = configurazione[len(configurazione)-1][0]
			print('LAST RESULT = ',lastRisposta)
			print('LAST TENTATIVO = ',tentativo)
			
			if lastRisposta == (1,3):
				next[4] = cifre[0]
				next[5] = cifre[1]
				next[6] = -1
				next[7] = -1
			if lastRisposta == (0,4):
				next[4] = tentativo[5]
				next[5] = tentativo[4]
				next[6] = tentativo[7]
				next[7] = tentativo[6]
			if lastRisposta == (2,2):
				next[4] = cifre[0]
				next[5] = cifre[3]
				next[6] = cifre[2]
				next[7] = cifre[1]
			if len(allComboRight) <=4:
				next[4] = allComboRight[0][0]
				next[5] = allComboRight[0][1]
				next[6] = allComboRight[0][2]
				next[7] = allComboRight[0][3]
			print('next = ',next)
			#input('mo vediamo')
	if n == 8 and greedy:
		if allComboRight == []:
			coppiaCifre = getRightCifre(8)
			
			cifreDestre = coppiaCifre[1]
			cifreSinistre = coppiaCifre[0]
			
			allComboRight = generateAllCombo(cifreDestre)
			allComboLeft = generateAllCombo(cifreSinistre)
			print('ALL COMBO RIGHT')
			for p in allComboRight:
				print(p)
			print('ALL COMBO LEFT')
			for p in allComboLeft:
				print(p)
			print('************************************************************')
			
			next[0] = cifreSinistre[0]
			next[1] = cifreSinistre[1]
			next[2] = cifreSinistre[2]
			next[3] = cifreSinistre[3]
			next[4] = cifreDestre[0]
			next[5] = cifreDestre[1]
			next[6] = cifreDestre[2]
			next[7] = cifreDestre[3]
			print('NEXT -> ',next)
			
		else:
		
			lastRisposta = configurazione[len(configurazione)-1][1]
			tentativo = configurazione[len(configurazione)-1][0]
			print('LAST RESULT = ',lastRisposta)
			print('LAST TENTATIVO = ',tentativo)
			#input('ten last right')
			if lastCombo == []:
				next[0] = allComboLeft[0][0]
				next[1] = allComboLeft[0][1]
				next[2] = allComboLeft[0][2]
				next[3] = allComboLeft[0][3]
				next[4] = allComboRight[0][0]
				next[5] = allComboRight[0][1]
				next[6] = allComboRight[0][2]
				next[7] = allComboRight[0][3]
			else:
				next = lastCombo[0]
			print('next = ',next)
			#input('mo vediamo')
	return next
			
def isSolutionReady():
	global soluzione
	for s in soluzione:
		if s == -1:
			return False
	return True
		
	

def debug(codice, proposta):
	''' restituisce per ogni proposta quanti indovinati al posto giusto (a) e quanti al posto sbagliato (b)'''
	#print('CODICE   = ',codice)
	#print('PROPOSTA = ',proposta)
	a=0
	ins=set(codice)
	for i in range(len(codice)):
		if codice[i]==proposta[i]: a+=1
	b=len(ins & set(proposta))-a    # cifre del codice in comune con il tentativo, meno quelle azzeccate esattamente
	#print('RISPOSTA = (',a,', ',b,')')
	coppia = a,b
	if choice([0,1]): coppia=b,a
	#print('COPPIA = ',coppia)
	#input('bozz')
	return coppia
	
def nextFirstCombo(n,ci):
	global step
	proposta = [-1]*n

	if n == 6:
		for i in range(0,3):
			proposta[i] = ci
		for i in range(3,6):
			proposta[i] = ci+1
	if n == 7:
		for i in range(0,4):
			proposta[i] = ci
		for i in range(4,7):
			proposta[i] = ci+1
	if n == 8:
		for i in range(0,4):
			proposta[i] = ci
		for i in range(4,8):
			proposta[i] = ci+1
	return proposta
			
			
	
cifreTotali = [0,1,2,3,4,5,6,7,8,9]
cifreTrovate = False
checkingQ = False
cifraChecking =0
	
def decodificatore(configurazione):
	global cifreTotali, cifreTrovate,step,cifraChecking,checkingQ,lastCombo

	print('CIFRE TOTALI = ',cifreTotali)
	print(' =============================== TENTATIVI =================')
	for a in configurazione:
			print(' a  ',a)
	print('=============================================================')
	n=configurazione[0]
	x=[]
	if len(configurazione) == 1:
		cifreTotali = [0,1,2,3,4,5,6,7,8,9]
		cifreTrovate = False
		checkingQ = False
		cifraChecking =0
		step = 0
		lastCombo = []
		x = nextFirstCombo(n,cifraChecking)		
	else:
		print('STEP = ',step)
		print('checkingQ = ',checkingQ)
		
		if not cifreTrovate:
			risposta = configurazione[len(configurazione)-1][1]
			print('RISPOSTA IF IF = ',risposta)
			if risposta == (0,0) and not checkingQ:
				print('removing = ',cifraChecking)
				print('removing = ',cifraChecking+1)
				cifreTotali.remove(cifraChecking)
				cifreTotali.remove(cifraChecking+1)
				if len(cifreTotali) == n:
					cifreTrovate = True
				else:
					cifraChecking+=2
					x = nextFirstCombo(n,cifraChecking)	
					step+=1
					return x
	
			if (risposta == (1,0) or risposta == (0,1)) and checkingQ:
				print(' UNO ++++++++++++++++++++++++++++')
				checkingQ = False
				print('							removing = ',cifraChecking+1)
				cifreTotali.remove(cifraChecking+1)
				if len(cifreTotali) == n:
					cifreTrovate = True
				else:
					cifraChecking+=2
					x = nextFirstCombo(n,cifraChecking)
					step+=1
					print(' Next x ---- > ',x)
					return x
	
			if (risposta == (1,0) or risposta == (0,1)) and not checkingQ:
				print(' 	DUE ++++++++++++++++++++++++++++')
				checkingQ = True
				x = [-1]*n
				for i in range(n):
					x[i] = cifraChecking
				print('							(1,0) o (0,1)  -> provo con x = ',x)
				step+=1
				return x
	
			if risposta == (0,0) and checkingQ:
				chekingQ = False
				print('							removing = ',cifraChecking)
				cifreTotali.remove(cifraChecking)
				if len(cifreTotali) == n:
					cifreTrovate = True
				else:
					cifraChecking+=2
					x = nextFirstCombo(n,cifraChecking)	
					step+=1
					return x
			if risposta == (2,0) or risposta == (0,2) or risposta == (1,1) and not checkingQ:
				cifraChecking+=2
				x = nextFirstCombo(n,cifraChecking)	
				return x;
			
			if x == []:
				print('e mo che facc ??')
				print('cifraChecking = ',cifraChecking)
				#input('sad')
				if cifraChecking == 8:
					if lastCombo == []:
						lastCombo = generateAllCombo(cifreTotali)
						print('dimensione combo = ',len(lastCombo))
						#input('last')
						x = choice(lastCombo)
						cifreTrovate = True  
				
	
		else:
			if lastCombo == []:
				lastCombo = generateAllCombo(cifreTotali)
				print('dimensione combo = ',len(lastCombo))
				#input('last')
				x = choice(lastCombo)
				cifreTrovate = True
			print('evvai cifre trovate ! ')
			print('CIFRE = ',cifreTotali)
			tentativo = configurazione[len(configurazione)-1][0]
			risposta = configurazione[len(configurazione)-1][1]
			rispostaInfame = (risposta[1],risposta[0])
			print('--- TENTATIVO = = = = ',tentativo)
			#input('spet')
			copia = lastCombo[:]
			for c in copia:
				deris = debug(c,tentativo)
				if deris != risposta and deris != rispostaInfame:
					lastCombo.remove(c)
			print('=============================================')
			print('dimensione combo = ',len(lastCombo))
			#input('last')
			x = choice(lastCombo)
			
	step+=1
	return x
	


print('CIAO SCHIF\n')
#codice = [4,5,6,8,2,3]
#codice = [4,5,2,6,1,3]
#codice = [3,0,7,4,8,9]
#codice = [2,0,6,5,7,8]
#codice = [5,6,8,0,1,3]
#codice = [2,6,8,4,0,7]
#codice = [2,0,6,8,7,5]
#codice = [1,3,2,4,0,8]
#codice = [5,1,2,9,0,3]
#codice = [6,9,2,3,4,1]
#codice = [0, 6, 5, 8, 7, 1]
#codice = [6,1,3,9,8,7]
#codice = [3,7,1,4,9,8]
#odice = [5,3,9,7,2,6]
#codice = [3,7,0,5,4,1]
#codice = [0,3,2,4,8,1]
#codice = [3,2,8,7,4,5,6]
#codice = [9,3,6,4,2,5,0]
#codice = [4,9,0,1,6,7,3,2]
#codice = [4,9,0,1,6,3,7,2]
codice = [5, 0, 1, 6, 8, 9, 2, 3]


configurazione = []
configurazione.append(len(codice))


for i in range(19):
	print(' C O D I C E = = = = = ',codice)
	proposta = decodificatore(configurazione)
	risposta = debug(codice,proposta)
	n = len(codice)
	if risposta == (n,0):
		print('******************************************************')
		print('******************************************************')
		print('***             Y  O  U     W  I  N                ***')
		print('******************************************************')
		print('******************************************************')
		print('CODICE   = ',codice)
		print('PROPOSTA = ',proposta)
		print('++++++++++++++++++++ HISTORY +++++++++++++++++++++++++')
		for c in configurazione:
			print(c)
		print('step = ',step)
		break
	else:
		configurazione.append((proposta,risposta))
	print('---------------------------------------------------------------------\n')

