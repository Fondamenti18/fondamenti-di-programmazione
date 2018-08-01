''' In determinate occasioni ci capita di dover scrivere i numeri in lettere, 
ad esempio quando dobbiamo compilare un assegno. 
Puo' capitare che alcuni numeri facciano sorgere in noi qualche dubbio.

Le perplessita' nascono soprattutto nella scrittura dei numeri composti con 1 e 8. 
Tutti i numeri come venti, trenta, quaranta, cinquanta, ecc... elidono la vocale 
finale (la "i" per 20, la "a" per tutti gli altri) fondendola con la vocale iniziale 
del numero successivo; scriveremo quindi ventuno, ventotto, trentotto, 
cinquantuno ecc...

Il numero cento, nella formazione dei numeri composti con uno e otto, non si comporta 
cosi'; il numero "cento" e tutte le centinaia (duecento, trecento, ecc...), 
infatti, non elidono la vocale finale. Dunque non scriveremo centuno,  trecentotto ma centouno, 
trecentootto, ecc...

I numeri composti dalle centinaia e dalla decina "ottanta" invece tornano ad elidere 
la vocale finale; scriveremo quindi centottanta, duecentottanta,  ecc..., 
non centoottanta, duecentoottanta, ...

Il numero "mille" non elide in nessun numero composto la vocale finale; scriveremo 
quindi milleuno,  milleotto, milleottanta, ecc...

Altri esempi sono elencati nel file grade02.txt


Scrivere una funzione conv(n) che prende in input un intero n, con 0<n<1000000000000, 
e restituisce in output una stringa con il numero espresso in lettere

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''


def conv(n):
	'''
	Questa funzione serve a convertire un numero immesso in formato intero nella corrispondente stringa
	testuale in lingua italiana. Le condizioni di imput sono:
	1) Il numero deve essere compreso tra 0 e 1000000000000;
	2) Il numero non deve essere a virgola mobile.
	'''
	if not (0<n<1000000000000 and n%1 == 0):
		raise Exception("Il numero immesso non rispetta le condizioni date.")
	stringa = ''
	try:
		prov = str(n)
	except TypeError:
		print("Il numero immesso non e' in formato intero")
	else:
		if len(prov) == 1:
			stringa += cifra(prov)
		elif len(prov) < 4:
			norm = normalizza(prov, 3)
			stringa += cifra_centinaia(norm[0], norm[1], norm[2])
		elif len(prov) < 7:
			norm = normalizza(prov, 6)
			stringa += cifra_centinaia(norm[0], norm[1], norm[2])
			if stringa == 'uno':
				stringa = 'mille'
			else:
				stringa += 'mila'
			stringa += cifra_centinaia(norm[3], norm[4], norm[5])
		elif len(prov) < 10:
			norm = normalizza(prov, 9)
			stringa += cifra_centinaia(norm[0], norm[1], norm[2])
			if stringa == 'uno':
				stringa = 'unmilione'
			else:
				stringa += 'milioni'
			stringa += cifra_centinaia(norm[3], norm[4], norm[5])
			if 'milioniuno' in stringa or 'milioneuno' in stringa:
				stringa = stringa[:-3]
				stringa += 'mille'
			else:
				stringa += 'mila'
			stringa += cifra_centinaia(norm[6], norm[7], norm[8])
		elif len(prov) < 13:
			norm = normalizza(prov, 12)
			stringa += cifra_centinaia(norm[0], norm[1], norm[2])
			if stringa == 'uno':
				stringa = 'unmiliardo'
			else:
				stringa += 'miliardi'
			stringa += cifra_centinaia(norm[3], norm[4], norm[5])
			if 'miliardiuno' in stringa or 'miliardouno' in stringa:
				stringa = stringa[:-3]
				stringa += 'unmilione'
			stringa += 'milioni'
			stringa += cifra_centinaia(norm[6], norm[7], norm[8])
			if 'milioniuno' in stringa or 'milioneuno' in stringa:
				stringa = stringa[:-3]
				stringa += 'mille'
			else:
				stringa += 'mila'
			stringa += cifra_centinaia(norm[9], norm[10], norm[11])
	return stringa

def cifra(n):
	'''
	Questa funzione prende in parametro un numero intero n a cifra singola compreso tra 0 e 9 e restituisce
	una stringa contenente la cifra in lettere, ad eccezione dell'input pari a 0. Se il parametro e' pari a 0
	la funzione restituisce una stringa vuota, in quanto lo zero funge da segnaposto.
	'''
	lista = ['', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove']
	for i in range(0, 10):
		if n == str(i):
			return lista[i]

def cifra_effettiva(a, n):
	'''
	Questa funzione prende in parametro una stringa ed un numero a cifra singola. Se
	il numero a cifra singola e' pari a 1 o 8, la funzione cancella l'ultimo carattere
	della stringa ed aggiunge la stringa delle unita', corrispondente al numero immesso
	come parametro. Altrimenti aggiunge direttamente la stringa delle unita'.
	'''
	if n == '1':
		a = a[:len(a) - 1]
		a += 'uno'
	elif n == '8':
		a = a[:len(a) - 1]
		a += 'otto'
	else:
		a += cifra(n)
	return a

def cifra_decine(a, n, m):
	'''
	Questa funzione serve a stampare le decine del numero immesso tramite una serie di condizioni. Prende come parametri
	la stringa delle centinaia e i due numeri a cifra singola che rappresentano le decine e le unita'. Se la decina
	e' pari a 0, restituisce una stringa vuota. Se e' pari a 1, procede a verificare immediatamente le unita', se e' pari a 8,
	elimina l'ultimo carattere della stringa delle centinaia, quindi aggiunge la stringa 'ottanta'. Per tutti i casi regolari 
	aggiunge alla stringa delle centinaia la corrispondente stringa delle decine e procede ad eseguire la funzione cifra_effettiva()
	per le unita', dandogli in parametro la stringa di centinaia e decine unite, e il numero a cifra singola che rappresenta le unita'.
	'''
	if n == '0':
		a += cifra(m)
		return a
	if n == '1':
		if m == '0':
			a += 'dieci'
			return a
		if m == '1':
			a += 'undici'
			return a
		if m == '2':
			a += 'dodici'
			return a
		if m == '3':
			a += 'tredici'
			return a
		if m == '4':
			a += 'quattordici'
			return a
		if m == '5':
			a += 'quindici'
			return a
		if m == '6':
			a += 'sedici'
			return a
		if m == '7':
			a += 'diciassette'
			return a
		if m == '8':
			a += 'diciotto'
			return a
		if m == '9':
			a += 'diciannove'
			return a
	if n == '2':
		a += cifra_effettiva('venti', m)
		return a
	if n == '3':
		a += cifra_effettiva('trenta', m)
		return a
	if n == '4':
		a += cifra_effettiva('quaranta', m)
		return a
	if n == '5':
		a += cifra_effettiva('cinquanta', m)
		return a
	if n == '6':
		a += cifra_effettiva('sessanta', m)
		return a
	if n == '7':
		a += cifra_effettiva('settanta', m)
		return a
	if n == '8':
		a = a[:len(a) - 1]
		a += cifra_effettiva('ottanta', m)
		return a
	if n == '9':
		a += cifra_effettiva('novanta', m)
		return a

def cifra_centinaia(n, m, o):
	'''
	Questa funzione prende in parametro tre numeri interi a cifra singola n, m e o. Se il primo parametro, ovvero quello delle centinaia,
	e' pari a 0, restituisce una stringa vuota. Se e' pari a 1 restituisce la stringa 'cento'. Procede quindi a sfruttare la
	funzione cifra_decine() per le restanti cifre, dandogli in input la stringa appena restituita, il secondo numero ed il terzo numero.
	'''
	if n == '0':
		return cifra_decine('',m, o)
	if n == '1':
		return cifra_decine('cento',m, o)
	else:
		return cifra_decine(cifra(n) + 'cento', m, o)
		
def normalizza(a, n):
	'''
	Queta funzione serve ad imporre una convenzione alle stringhe per comodita' di lavoro.
	'''
	while(len(a) < n):
		a = '0' + a
	return a
	
if __name__ == '__main__':
	print(conv(1201000))