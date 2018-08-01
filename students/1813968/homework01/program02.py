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


Scrivere una funzione conv(n) che prende in input un intero n, con 0<n<1.000.000.000.000, 
e restituisce in output una stringa con il numero espresso in lettere

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''


def conv(n):
	lista_1_19=["uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove", "dieci", "undici", "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette", "diciotto", "diciannove"]
	lista_decine=["venti", "trenta", "quaranta", "cinquanta", "sessanta", "settanta", "ottanta", "novanta"]
	if n==0:
		n2=""
	elif n<=19:
		n2=lista_1_19[n-1]
	elif n<=99:
		numero=lista_decine[int((n/10)-2)]
		if n%10==1 or n%10==8:
			numero=numero[0:-1]
		n2=numero+conv(n%10)
	elif n<=999:
		numero=""
		if n>=199:
			numero=conv(n//100)
		numero+="cento"
		if n%100 in range(80,90):
			numero=numero[0:-1]
		n2=numero+conv(n%100)
	elif n<=999999:
		numero=""
		if n>=1999:
			numero=conv(n//1000)
		numero+="mille"
		if n//1000>1:
			numero=numero[0:-3]
			numero+="la"
		n2=numero+conv(n%1000)
	elif n<=999999999:
		numero=""
		if n>=1999999:
			numero=conv(n//1000000)
		numero+="milione"
		if n//1000000>1:
			numero=numero[0:-1]
			numero+="i"
		n2=numero+conv(n%1000000)
	elif n<=999999999999:
		numero="un"
		if n>=1999999999:
			numero=conv(n//1000000000)
		numero+="miliardo"
		if n//1000000000>1:
			numero=numero[0:-1]
			numero+="i"
		n2=numero+conv(n%1000000000)
	return n2
	
	
	
	
	
	
	