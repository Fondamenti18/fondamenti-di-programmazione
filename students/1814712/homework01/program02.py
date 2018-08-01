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
	''' converte un intero nella stringa di lettere corrispondente'''
	s = str(n)
	for i in range( 12 - len(s)):
		s = '0' + s
	l = dividi_in_tuple(s)
	s =''
	m = ['miliardi', 'milioni', 'mila', '']
	for i in range(4):
		if l[i] != "000":
			if l[i] == '001':
				s = s + casi('1' + (3 - i) * 3 * '0')
			else:
				s = s + triplette(l[i]) + m[i]
	s = s.replace('iu', 'u')
	s = s.replace('antau', 'antu')
	s = s.replace('oottanta', 'ottant')
	s = s.replace('oottant','ottant')
	s = s.replace('sessanta','sessant')
	s = s.replace('cinquanta','cinquant')
	s = s.replace('quaranta','quarant')
	s = s.replace('trenta','trent')
	s = s.replace('ventio', 'vento')
	s = s.replace('novantao','novanto')
	
	return s
	
def dividi_in_tuple(s):
    ''' divide il numero in stringhe di tre cifre'''
    l = []
    for i in range(4):
        l.append(s[3 * i : 3 * (i + 1)])  	
    return l    

def triplette(x) :
	''' converte ogni singola tripletta di cifre in una stringa che rappresenta il numero in lettere'''
	s = ''	
	if x[0] != "0":
		if x[0] == '1':
			s = "cento"
		else:
			s = casi(x[0]) + "cento"
	
	if x[1:] < '19':
		if x[1] != '0':
			s = s + casi(x[1:])
		else:
			s = s + casi(x[2])
		return s
	s = s + casi(x[1] + "0") + casi(x[2])
	return s

def casi(n):
	if n == '0':
		return('')
	if n == "1":
		return('uno')
	if n == "2":
		return('due')
	if n == "3":
		return('tre')
	if n == "4":
		return('quattro')
	if n == "5":
		return('cinque')
	if n == "6":
		return('sei')
	if n == "7":
		return('sette')
	if n == "8":
		return('otto')
	if n == "9":
		return('nove')
	if n == "10":
		return('dieci')
	if n == "11":
		return('undici')
	if n == "12":
		return('dodici')
	if n == "13":
		return('tredici')
	if n == "14":
		return('quattordici')
	if n == "15":
		return('quindici')
	if n == "16":
		return('sedici')
	if n == "17":
		return('diciassette')
	if n == "18":
		return('diciotto')
	if n == "19":
		return('diciannove')
	if n == "20":
		return('venti')
	if n == "30":
		return('trenta')
	if n == "40":
		return('quaranta')
	if n == "50":
		return('cinquanta')
	if n == "60":
		return('sessanta')
	if n == "70":
		return('settanta')
	if n == "80":
		return('ottanta')
	if n == "90":
		return('novanta')
	if n == "1000":
		return('mille')
	if n == "1000000":
		return('unmilione')
	if n == "1000000000":
		return('unmiliardo')
	
	
