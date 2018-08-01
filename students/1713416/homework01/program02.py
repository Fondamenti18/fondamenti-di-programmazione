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
	while n <= 0 or n >= (10**12):
		print ('Il numero inserito non è accettabile')
		return None
	nomi = []	
	num = scomposizione(n, 10**3)
	for i in num:
		if i != 0:
			if i // 100 == 0:
				nomi += [UnitaeDecine(scomposizione(i, 10))]
			else: 
				nomi += [cifre3(scomposizione(i, 10))]
		else:
			nomi += ['']
	return scrivi(nomi)

def scomposizione(n, divisore):
    l = []
    while n != 0:
      l.append(n % divisore)
      n = n // divisore
    return l 
    
def cifre3(n):
	nome = ''
	centinaia = ['cento', 'duecento', 'trecento', 'quattrocento', 'cinquecento', 'seicento', 'settecento', 'ottocento', 'novecento']
	if n[1] == 8:
		nome += (centinaia[n[2] - 1][:-1] + UnitaeDecine(n[:-1]))
	else:
		nome += (centinaia[n[2] - 1] + UnitaeDecine(n[:-1]))
	return nome
	
def UnitaeDecine(n):
	nome = ''
	lun = len(n)
	unita = ['uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove']
	dieciventi = ['dieci', 'undici', 'dodici', 'tredici', 'quattordici', 'quindici', 'sedici', 'diciassette', 'diciotto', 'diciannove']
	decine = ['venti', 'trenta', 'quaranta', 'cinquanta', 'sessanta', 'settanta', 'ottanta', 'novanta']
	if n[0] == 0 and n[1] == 0:
		pass
	else:
		if lun == 1 or n[1] == 0:
			nome += unita[n[0]-1]
		else:
			if n[1] == 1:
				nome += dieciventi[n[0]]
			elif n[0] == 1 or n[0] == 8:
				nome += (decine[n[1]-2][:-1] + unita[n[0]-1])  
			elif n[0] == 0:
				nome += decine[n[1]-2]
			else:
				nome += (decine[n[1]-2] + unita[n[0]-1])
	return nome

	
def scrivi(nomi):
	stringa = ''
	numeri = [['uno', ''], ['mille', 'mila'], ['unmilione', 'milioni'], ['unmiliardo', 'miliardi']]
	for i in range(len(nomi)):
		if nomi[i] == '':
			pass
		elif nomi[i] == 'uno':
			stringa = numeri[i][0] + stringa
		else:
			stringa = nomi[i] + numeri[i][1] + stringa
	return stringa	