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
	unita=('','uno', 'due', 'tre', 'quattro', 'cinque','sei', 'sette', 'otto', 'nove', 'dieci','undici', 'dodici', 'tredici','quattordici', 'quindici', 'sedici','diciassette', 'diciotto', 'diciannove')
	decine=('venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta')
	if n<=19:
		return unita[n]
	elif n<=99:
		d=n//10
		u=n-d*10
		b=decine[d-2]
		if u==1 or u==8:
			b=b[:-1]
		return b + unita[u]
	elif n<=999:
		c=n//100
		d=(n-c*100)//10
		u=n-c*100-d*10
		e=decine[c-2]
		d2=n-c*100
		if c==1:
			e='cento'
		else:
			e=unita[c]+'cento'
		if d==8:
			e=e[:-1]
		return e + conv(d2)
	elif n<=999999:
		m=n//1000
		c=n-m*1000
		if m==1:
			return 'mille'+conv(c)
		else:
			return conv(m)+'mila'+conv(c)
	elif n<=999999999:
		milio=n//1000000
		m=n-milio*1000000
		if milio==1:
			return 'un'+'milione'+conv(m)
		else:
			return conv(milio)+'milioni'+conv(m)
	elif n<=999999999999:
		miliardi=n//1000000000
		milio=n-miliardi*1000000000
		if miliardi==1:
			return'un'+'miliardo'+conv(milio)
		else:
			return conv(miliardi)+'miliardi'+conv(milio)