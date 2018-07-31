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
from math import log10

numbs = ["uno","due","tre","quattro","cinque","sei","sette","otto","nove","dieci","undici","dodici","tredici","quattordici","quindici","sedici","diciassette","diciotto","diciannove"]
dozens = ["venti","trenta","quaranta","cinquanta","sessanta","settanta","ottanta","novanta"]
m1 = ["mila","milioni","miliardi"]
m2 = ["mille","unmilione","unmiliardo"]
due = 10**2
tre = 10**3

def conv(n):
	if n < due:
		return analyzeCent(n)
	elif n < tre:
		lett = "cent" if int((n%100)/10) == 8 else "cento"
		r = int(n/due)
		return (conv(r) + lett if r != 1 else lett) + conv(n%100)
	exp = max(list(filter(lambda x: x<=log10(n),[3,6,9])))
	u = int(n/10**exp)
	m = (exp//3)-1
	return ((conv(u)+m1[m]) if u != 1 else m2[m]) + conv(n%10**exp)

def analyzeCent(n):
	if n == 0:
		return ""
	elif n < 20:
		return numbs[n-1]
	elif n < due:
		r = int(n/10)-2
		return (dozens[r][:-1] if n%10 == 8 or n%10 == 1 else dozens[r]) + conv(n%10)