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


def conv_unit(unita):
	if(unita=='1'):
		letteral='uno'
	elif(unita=='2'):
		letteral='due'
	elif(unita=='3'):
		letteral='tre'
	elif(unita=='4'):
		letteral='quattro'
	elif(unita=='5'):
		letteral='cinque'
	elif(unita=='6'):
		letteral='sei'
	elif(unita=='7'):
		letteral='sette'
	elif(unita=='8'):
		letteral='otto'
	elif(unita=='9'):
		letteral='nove'
	elif(unita=='0'):
		letteral=''
	return letteral

def conv_decin(unita,decina,letteral):
	if(decina=='1'):
		if(unita=='1'):
			letteral='undici'
		elif(unita=='2'):
			letteral='dodici'
		elif(unita=='3'):
			letteral='tredici'
		elif(unita=='4'):
			letteral='quattordici'
		elif(unita=='5'):
			letteral='quindici'
		elif(unita=='6'):
			letteral='sedici'
		elif(unita=='7'):
			letteral='diciassette'
		elif(unita=='8'):
			letteral='diciotto'
		elif(unita=='9'):
			letteral='diciannove'
	elif(decina=='2'):
		if(unita!='1' and unita!='8'):
			letteral='venti'+letteral
		else:
			letteral='vent'+letteral
	elif(decina=='3'):
		if(unita!='1' and unita!='8'):
			letteral='trenta'+letteral
		else:
			letteral='trent'+letteral
	elif(decina=='4'):
		if(unita!='1' and unita!='8'):
			letteral='quaranta'+letteral
		else:
			letteral='quarant'+letteral
	elif(decina=='5'):
		if(unita!='1' and unita!='8'):
			letteral='cinquanta'+letteral
		else:
			letteral='cinquant'+letteral
	elif(decina=='6'):
		if(unita!='1' and unita!='8'):
			letteral='sessanta'+letteral
		else:
			letteral='sessant'+letteral
	elif(decina=='7'):
		if(unita!='1' and unita!='8'):
			letteral='settanta'+letteral
		else:
			letteral='settant'+letteral
	elif(decina=='8'):
		if(unita!='1' and unita!='8'):
			letteral='ottanta'+letteral
		else:
			letteral='ottant'+letteral
	elif(decina=='9'):
		if(unita!='1' and unita!='8'):
			letteral='novanta'+letteral
		else:
			letteral='novant'+letteral
	elif(decina=='0'):
		letteral=''+letteral
	return letteral

def conv_centin(decina,centina,letteral):
	if(centina=='1' and decina!='8'):
		letteral='cento'+letteral
	if(centina=='1' and decina=='8'):
		letteral='cent'+letteral
	if(centina=='2' and decina!='8'):
		letteral='duecento'+letteral
	if(centina=='2' and decina=='8'):
		letteral='duecent'+letteral
	if(centina=='3' and decina!='8'):
		letteral='trecento'+letteral
	if(centina=='3' and decina=='8'):
		letteral='trecent'+letteral
	if(centina=='4' and decina!='8'):
		letteral='quattrocento'+letteral
	if(centina=='4' and decina=='8'):
		letteral='quattrocent'+letteral
	if(centina=='5' and decina!='8'):
		letteral='cinquecento'+letteral
	if(centina=='5' and decina=='8'):
		letteral='cinquecent'+letteral
	if(centina=='6' and decina!='8'):
		letteral='seicento'+letteral
	if(centina=='6' and decina=='8'):
		letteral='seicent'+letteral
	if(centina=='7' and decina!='8'):
		letteral='settecento'+letteral
	if(centina=='7' and decina=='8'):
		letteral='settecent'+letteral
	if(centina=='8' and decina!='8'):
		letteral='ottocento'+letteral
	if(centina=='8' and decina=='8'):
		letteral='ottocent'+letteral
	if(centina=='9' and decina!='8'):
		letteral='novecento'+letteral
	if(centina=='9' and decina=='8'):
		letteral='novecent'+letteral
	if(centina=='0'):
		letteral=''+letteral
	return letteral

def lavora_stringa(stringa,n):
	stringa=stringa[::-1]
	lista = []
	tmp = []
	counter = 0
	for char in stringa:
		if counter == n:
			lista.append("".join(tmp))
			tmp = [char]
			counter = 1
		else:
			tmp.append(char)
			counter += 1
	if tmp:
		lista.append("".join(tmp))
	if(len(lista)>=1):
		lista[0]=lista[0][::-1]
	if(len(lista)>=2):
		lista[1]=lista[1][::-1]
	if(len(lista)>=3):
		lista[2]=lista[2][::-1]
	if(len(lista)>=4):
		lista[3]=lista[3][::-1]
	return lista
      
def conv_base(n):
	listanum=(' '.join(str(n))).split()
	listanum=listanum[::-1]
	if(len(listanum)>=1):
		letteral=conv_unit(listanum[0])
	if(len(listanum)>=2):
		letteral=conv_decin(listanum[0],listanum[1],letteral)
	if(len(listanum)>=3):
                letteral=conv_centin(listanum[1],listanum[2],letteral)
	return letteral
      
def conv(n):
	listanum=lavora_stringa(str(n),3)
	if(len(listanum)>=1):
	      letteral=conv_base(listanum[0])
	if(len(listanum)>=2):
	      if(conv_base(listanum[1])+'mila'=='unomila'):
		      letteral='mille'+letteral
	      else:
		      letteral=conv_base(listanum[1])+'mila'+letteral
	if(len(listanum)>=3):
	      letteral=conv_base(listanum[2])+'milioni'+letteral
	if(len(listanum)>=4):
	      letteral=conv_base(listanum[3])+'miliardi'+letteral
	return letteral
