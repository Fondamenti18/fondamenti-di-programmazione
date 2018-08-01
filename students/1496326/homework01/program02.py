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
	
	unita = ('uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove', 'dieci', 'undici', "dodici", 'tredici', 'quattordici', 'quindici', 'sedici', 'diciassette', 'diciotto', 'diciannove')
	decine = ('venti', 'trenta', 'quaranta','cinquanta', 'sessanta', 'settanta', 'ottanta', 'novanta')
	cento = 'cento'
	
	#lo zero in lettere è esluso dal range quindi lo mappo solo come stringa vuota
	if(n == 0):
		return '';
		
	#restituisco il valore in posizione n-1 (la lista inizia da 0)
	elif (n < 20):
		return unita[n-1]
		
	elif (n < 100):
		#divido il numero per 10 per ottenere la posizione nella lista delle decine (traslata di -2 per l'assenza di dieci e cento nella lista)
		decinaLetterale = decine[int(n/10)-2]
		
		#ottengo le unita di n dal resto del modulo 10
		unit = n%10
		unitLetterale = conv(unit)
		
		#se le unita sono 1 o 8 tronco le decine di una lettera
		if (unit == 1 or unit == 8):
			decinaLetterale = decinaLetterale[:-1]
		return decinaLetterale + unitLetterale
		
	elif (n < 200):
	
		decinaLetterale = conv(n%100)
		decina = int((n%100)/10)
		
		#controllo se si tratta di un numero della decina ottanta e in quel caso tronco una lettera sul cento
		if(decina == 8):
			return cento[:-1] + decinaLetterale
		else:
			return cento + decinaLetterale
		
	elif (n < 1000):
		centinaia = unita[int(n/100)-1]
		decina = int((n%100)/10)
		
		#controllo se si tratta di un numero della decina ottanta e in quel caso tronco una lettera sul cento
		if(decina == 8):
			centinaia += cento[:-1] + conv(n%100)
			return centinaia
		else:
			centinaia += cento + conv(n%100)
			return centinaia
	
	#sfrutto la ricorsione quasi senza aggiungere logica
	elif (n < 2000):
		return 'mille' + conv(n%1000)
		
	elif (n < 1000000):
		return conv(int(n/1000)) + 'mila' + conv(n%1000)
		
	elif n < 2000000:
		return 'unmilione' + conv(n%1000000)
			
	elif n < 1000000000:
		return conv(int(n/1000000))+ 'milioni' + conv(n%1000000)
		
	elif n < 2000000000:
		return 'unmiliardo' + conv(n%1000000000)
		
	else:
		return conv(int(n/1000000000)) + 'miliardi' + conv(n%1000000000)

print(conv(188))				
#for number in range(10000000, (1000000000000-1)):
	#conv1Res = conv(number)
	#conv2Res = conv2(number)
	#if (conv1Res != conv2Res):
	#	print(conv1Res);