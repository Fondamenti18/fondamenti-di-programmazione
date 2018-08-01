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

unita ={0:"",1:"uno",2:"due",3:"tre",4:"quattro",5:"cinque",6:"sei",7:"sette",8:"otto",9:"nove",10:"dieci",11:"undici",12:"dodici",13:"tredici",14:"quattordici",15:"quindici",16:"sedici",17:"diciassette",18:"diciotto",19:"diciannove"}
decine ={0:"", 1:"dieci",2:"venti",3:"trenta",4:"quaranta",5:"cinquanta",6:"sessanta", 7:"settanta",8:"ottanta", 9:"novanta"}

def converti_gruppo(gruppo):

	if len(gruppo) == 0 or gruppo=="000":
		return []
	
	result =[]
	int_gruppo = int(gruppo)
	
	g0=int(gruppo[-1])
	
	if int_gruppo > 9:
		g1=int(gruppo[-2])
		if g1 == 1:
			result.append(unita[g1*10+g0])
		else:
			d = decine[g1] if g0 not in (1, 8) else decine[g1][:-1]
			u = unita[g0]
			result.extend([u,d])

		if int_gruppo > 99:
			g2 =int(gruppo[0])
			result.append("cento" if g1 != 8 else "cent")
			if g2 != 1:
				#la prima centinaia non ha prefissi, altrimenti si ripetono i prefissi delle unità 1-9
				result.append(unita[g2])
			#aggiungo cento 
	else:
		result.append(unita[int_gruppo])
	
	return result
	
	
def conv(n):
	'Scrivete qui il codice della funzione'
	assert(0<n and n<1000000000000)
	result = []
	str_n = str(n)
	
	result.extend(converti_gruppo(str_n[-3:]))
	if 999<n<=1999:
		result.append("mille")
	else:
		res = converti_gruppo(str_n[-6:-3])
		if len(res)>0:
			result.append("mila")
			result.extend(res)
			
	if 999999<n<=1999999:
		result.append("unmilione")
	else:
		res = converti_gruppo(str_n[-9:-6])
		if len(res)>0:
			result.append("milioni")
			result.extend(res)
		
	if 999999999 <n<=1999999999:
		result.append("unmiliardo")
	else:
		res=converti_gruppo(str_n[-12:-9])
		if len(res)>0:
			result.append("miliardi")
			result.extend(res)
	
	
	return "".join(reversed(result))
	
