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


Scrivere una funzione conv(n) che prende in input un intero n, con 0<n<1 000 000 000 000, 
e restituisce in output una stringa con il numero espresso in lettere

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

def edit_one_eight(s):
	app = ""
	for i in range(len(s)-1):
		app += s[i]
	return app

def number_conversion(s,d,m):
	c = ""

	if int(s) == 1 and (m == 2 or m == 3 or m == 4):
		s = "1"
		if m == 2:
			s = s +"000"
		if m == 3:
			s = s + "000000"
		if m == 4:
			s = s + "000000000"

	for i in d:
		if d[i] == int(s):
			if int(s)>1000:
				c += edit_one_eight('uno')
			c += i

	if (c == ""):

		for pos, i in enumerate(s):
			for j in d:

				if pos == 0:
					if int(i) == d[j]:
						if int(i)==1:
							c += "cento"
						else:
							c += j + "cento"

				if pos == 1:
					
					if i == "1":
						if (int(i+s[pos+1]) == d[j]):
							c += j
					elif (int(i+"0") == d[j] and (s[pos+1] != "1" and s[pos+1] != "8" and int(i+"0") != "80")):
						c += j
					elif (int(i+"0") == d[j] and (s[pos+1] == "1" or s[pos+1] == "8" or int(i+"0") == "80")):
						if (i == "1" or i == "8"):
							c = edit_one_eight(c)
						if(s[pos+1] == "1" or s[pos+1] == "8"):
							c += edit_one_eight(j)

				if pos == 2:
					if(int(i) == d[j] and s[pos-1] != "1"):
						c += j
	
	if(int(s) != 1000 and int(s) != 1000000 and int(s) != 1000000000 and int(s) != 000 ):
		if m == 2:
			c += "mila"
		elif m == 3:
			c += "milioni"
		elif m == 4:
			c += "miliardi"

	return c

def check_value(d, n):
	s = ""
	app = str(n)
	app2 = ""
	cont =len(app)
	i = 0

	if (cont + 2) % 3 == 0:
		app2 = "00" + app
	elif (cont + 1) % 3 == 0:
		app2 = "0" + app
	else:
		app2 = app

	cont = len(app2)

	while cont > 0:
		m = 0

		if (cont == 3):
			m = 1
		if cont == 6:
			m = 2
		if cont == 9:
			m = 3
		if cont == 12:
			m = 4

		s += number_conversion(app2[i:i+3],d,m)

		i += 3
		cont -= 3

	return s
	

def conv(n):
    dict = {'uno':1,
    		'due':2,
    		'tre':3,
    		'quattro':4,
    		'cinque':5,
    		'sei':6,
    		'sette':7,
    		'otto':8,
    		'nove':9,
    		'dieci':10,
    		'undici':11,
    		'dodici':12,
    		'tredici':13,
    		'quattordici':14,
    		'quindici':15,
    		'sedici':16,
    		'diciassette':17,
    		'diciotto':18,
    		'diciannove':19,
    		'venti':20,
    		'trenta':30,
    		'quaranta':40,
    		'cinquanta':50,
    		'sessanta':60,
    		'settanta':70,
    		'ottanta':80,
    		'novanta':90,
    		'cento':100,
    		'mille':1000,
    		'millione':1000000,
    		'miliardo':1000000000,
    	   }

    s = ""

    s = check_value(dict,n)

    return s