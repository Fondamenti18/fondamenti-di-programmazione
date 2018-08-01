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
	listaUnita=['uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']	#lista unità più decine
	listaDecine=['dieci','venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']	#lista decine
	if n == 0:	#zero
		return('')
	elif n<=19:	#unita e decine
		cifra=listaUnita[n-1]
		return(cifra)
	elif n<=99:	#decine
	    stringa=funzioneDecine(n)
	    return(stringa)	
	elif n<=999:	#centinaia
		stringa=funzioneCentinaia(n)
		return(stringa)
	elif n<=9999:	#migliaia 4 cifre
		stringa=funzioneMigliaia(n)
		return(stringa)
	elif n<=99999:	#migliaia 5 cifre			
		stringa=funzioneMigliaia5cifre(n)
		return(stringa)
	elif n<=999999:	#migliaia 6 cifre
		stringa=funzioneMigliaia6cifre(n)
		return(stringa)
	elif n<=9999999:	#milioni 7 cifre
		stringa=funzioneMilioni(n)
		return(stringa)
	elif n<=99999999:	#milioni 8 cifre
		stringa=funzioneMilioni8cifre(n)
		return(stringa)
	elif n<=999999999:	#milioni 9 cifre
		stringa=funzioneMilioni9cifre(n)
		return(stringa)
	elif n<=9999999999:	#miliardi 10 cifre
		stringa=funzioneMiliardi(n)
		return(stringa)
	elif n<=99999999999:	#miliardi 11 cifre
		stringa=funzioneMiliardi11cifre(n)
		return(stringa)
	elif n<=999999999999:	#miliardi 12 cifre
		stringa=funzioneMiliardi12cifre(n)
		return(stringa)
	elif n<=1000000000000:	#un bilione 13 cifre	
		stringa=str(n)
		cifra1=conv(int(stringa[0]))
		cifra2=conv(int(stringa[1]+stringa[2]+stringa[3]+stringa[4]+stringa[5]+stringa[6]+stringa[7]+stringa[8]+stringa[9]+stringa[10]+stringa[11]))
		return(cifra1.strip(cifra1[-1])+'bilione'+cifra2)



def funzioneDecine(n):
    listaUnita=['uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']	#lista unità più decine
    listaDecine=['dieci','venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']	#lista decine
    stringa=str(n)
    cifra1=listaDecine[int(stringa[0])-1]
    cifra2=conv(int(stringa[1]))
    if(cifra2=='uno' or cifra2=='otto'):
        return(cifra1.strip(cifra1[-1])+cifra2)
    else:   
       return(cifra1+cifra2)

def funzioneCentinaia(n):
    listaUnita=['uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']	#lista unità più decine
    stringa=str(n)
    cifra1=listaUnita[int(stringa[0])-1]
    cifra2=conv(int(stringa[1]))
    cifra3=conv(int(stringa[2]))
    cifra4=conv(int(stringa[1]+stringa[2]))
    if(cifra2=='otto'):
        if(cifra1=='uno'):
            return('cent'+cifra4)
        else:
            return(cifra1+'cent'+cifra4)
    else:
        if(cifra1=='uno'):
            return('cento'+cifra4)
        else:
            return(cifra1+'cento'+cifra4)
            
            
def funzioneMigliaia(n):
    listaUnita=['uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']	#lista unità più decine

    stringa=str(n)
    cifra1=listaUnita[int(stringa[0])-1]
    cifra2=conv(int(stringa[1]+stringa[2]+stringa[3]))
    if(cifra1=='uno' and cifra2==''):
        return('mille')
    else:
        if(cifra1=='uno'):
            return('mille'+cifra2)
        else:
            return(cifra1+'mila'+cifra2)


def funzioneMigliaia5cifre(n):
    stringa=str(n)
    cifra1=conv(int(stringa[0]+stringa[1]))
    cifra2=conv(int(stringa[2]+stringa[3]+stringa[4]))	
    return(cifra1+'mila'+cifra2)
    
def funzioneMigliaia6cifre(n):
    stringa=str(n)
    cifra1=conv(int(stringa[0]+stringa[1]+stringa[2]))
    cifra2=conv(int(stringa[3]+stringa[4]+stringa[5]))	
    return(cifra1+'mila'+cifra2)
    
def funzioneMilioni(n):
    stringa=str(n)
    cifra1=conv(int(stringa[0]))
    cifra2=conv(int(stringa[1]+stringa[2]+stringa[3]+stringa[4]+stringa[5]+stringa[6]))
    if(cifra1=='uno'):
        return(cifra1.strip(cifra1[-1])+'milione'+cifra2)
    return(cifra1+'milioni'+cifra2)
    
def funzioneMilioni8cifre(n):
    stringa=str(n)
    cifra1=conv(int(stringa[0]+stringa[1]))
    cifra2=conv(int(stringa[2]+stringa[3]+stringa[4]+stringa[5]+stringa[6]+stringa[7]))
    return(cifra1+'milioni'+cifra2)	
    
def funzioneMilioni9cifre(n):
    stringa=str(n)
    cifra1=conv(int(stringa[0]+stringa[1]+stringa[2]))
    cifra2=conv(int(stringa[3]+stringa[4]+stringa[5]+stringa[6]+stringa[7]+stringa[8]))
    return(cifra1+'milioni'+cifra2)	
    
def funzioneMiliardi(n):
    stringa=str(n)
    cifra1=conv(int(stringa[0]))
    cifra2=conv(int(stringa[1]+stringa[2]+stringa[3]+stringa[4]+stringa[5]+stringa[6]+stringa[7]+stringa[8]+stringa[9]))
    if(cifra1=='uno'):
        return(cifra1.strip(cifra1[-1])+'miliardo'+cifra2)
    else:
        return(cifra1+'miliardi'+cifra2)
        
def funzioneMiliardi11cifre(n):
    stringa=str(n)
    cifra1=conv(int(stringa[0]+stringa[1]))
    cifra2=conv(int(stringa[2]+stringa[3]+stringa[4]+stringa[5]+stringa[6]+stringa[7]+stringa[8]+stringa[9]+stringa[10]))
    return(cifra1+'miliardi'+cifra2)

def funzioneMiliardi12cifre(n):
    stringa=str(n)
    cifra1=conv(int(stringa[0]+stringa[1]+stringa[2]))
    cifra2=conv(int(stringa[3]+stringa[4]+stringa[5]+stringa[6]+stringa[7]+stringa[8]+stringa[9]+stringa[10]+stringa[11]))
    return(cifra1+'miliardi'+cifra2)
    

if __name__ == '__main__':			
	print(conv(1000000000000))
	










