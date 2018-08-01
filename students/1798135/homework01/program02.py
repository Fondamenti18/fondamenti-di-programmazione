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


Scrivere una funzione conv(n) che prende in input un intero n, con 0<n<1000000000000 
e restituisce in output una stringa con il numero espresso in lettere

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''


def conv(n):
    risultato=""

    conversione={0:"zero",1:"uno",2:"due",3:"tre",4:"quattro",5:"cinque",6:"sei",7:"sette",8:"otto",9:"nove",10:"dieci",11:"undici",12:"dodici",
                 13:"tredici",14:"quattordici",15:"quindici",16:"uno",17:"diciassette",18:"diciotto",19:"dicianove",20:"venti",30:"trenta",
                 40:"quaranta",50:"cinquanta",60:"sessanta",70:"settanta",80:"ottanta",90:"novanta",100:"cento",1000:"mille",1000000:"unmilione",1000000000:"unmiliardo"}
    if (n in conversione):
	    return conversione[n]
    lunghezza=len(str(n))
    blocchi=[]
    count=0
    while(lunghezza>0):
	    blocchi=blocchi+[n%1000]
	    n=n//1000
	    lunghezza=lunghezza-3
	    count=count+1
    count=count-1
    while(count>=0):
	    if blocchi[count]==1 and count ==3:
		    risultato=risultato+"unmiliardo"
	    elif blocchi[count]==1 and count==2:
		    risultato=risultato+"unmilione"
	    elif blocchi[count]==1 and count==1:
		    risultato=risultato+"mille"
	    else:
		    if count==1:
			    risultato=risultato+funzione(blocchi[count])+"mila"
		    if count==2:
			    risultato=risultato+funzione(blocchi[count])+"milioni"
		    if count==3:
			    risultato=risultato+funzione(blocchi[count])+"miliardi"
		    if count==0:
			    risultato=risultato+funzione(blocchi[count])
	    count=count-1
    return risultato


def funzione(stringa):
	conversione={0:"",1:"uno",2:"due",3:"tre",4:"quattro",5:"cinque",6:"sei",7:"sette",8:"otto",9:"nove",10:"dieci",11:"undici",12:"dodici",
                 13:"tredici",14:"quattordici",15:"quindici",16:"uno",17:"diciassette",18:"diciotto",19:"dicianove",20:"venti",30:"trenta",
                 40:"quaranta",50:"cinquanta",60:"sessanta",70:"settanta",80:"ottanta",90:"novanta",100:"cento"}
	int(stringa)

	if stringa in conversione:
		return conversione[stringa]
	a=stringa%10
	b=(stringa//10)%10
	c=(stringa//100)%10
	b=b*10
	stringa=""
	if c==1 and b!=80:
		stringa=stringa+"cento"
	if b==80 and c>=1:
		stringa=conversione[c]+"cent"
	elif c>1:
		stringa=conversione[c]+"cento"
	if (b+a) in conversione:
		return stringa+conversione[b+a]
	if a==1 or a ==8:
		k=conversione[b]
		k=k[:-1]
		stringa=stringa+k+conversione[a]
	else:
		stringa=stringa+conversione[b]+conversione[a]
	return stringa
   
