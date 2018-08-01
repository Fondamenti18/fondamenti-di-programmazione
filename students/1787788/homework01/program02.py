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

def eccezioni(stringa, n, ismig):
    if(n>=80 and n<=89 and ismig==True):
            stringa = stringa[:-1]
    if(ismig == False):
        if(n==1 or n==8):
            stringa = stringa[:-1]
        stringa = stringa + conv(n)
    return stringa
	    
def createstringafrommilioni(stringa, stringa2, mil, mig, ismig):
	if(mil!=1):
		stringa = conv(mil) + stringa2
	elif(ismig==False):
		stringa = conv(mil)[:-1] + stringa
	return stringa + conv(mig)

def conv(n):
	unita = ["", "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove", "dieci", "undici", "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette", "diciotto", "diciannove"]
	decine = ["venti", "trenta", "quaranta", "cinquanta","sessanta","settanta", "ottanta", "novanta"]
	if(n<=19):
		return unita[n]
	elif(n<=99):
		stringa = ''
		dec, u=divmod(n,10)
		stringa = decine[dec-2]
		return eccezioni(stringa, u, False)
	elif(n<=999):
		ismig = True
		cent,dec=divmod(n,100)
		stringa = eccezioni('cento', dec, ismig)
		return createstringafrommilioni(stringa,stringa,cent,dec,ismig)
	elif(n<=999999):
		ismig = True
		mig, cen = divmod(n,1000)
		return createstringafrommilioni('mille','mila', mig, cen,ismig)
	elif(n<=999999999):
		ismig = False
		mil, mig = divmod(n,1000000)
		return createstringafrommilioni('milione', 'milioni', mil, mig, ismig)
	elif(n<=999999999999):
		ismig = False
		mil, mig = divmod(n,1000000000)
		return createstringafrommilioni('miliardo', 'miliardi', mil, mig, ismig)

