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

'''in conv trasformo l input in str e lo divido nelle sue componenti con li indici, poi chiamo le funzioni sugli indici corrispondenti e ritorno una concatenazioone'''
def conv(n):
	N=str(n)
	if len(N)==1:
		return unita(n)
	elif len(N)==2:
		return decine(n)
	elif len(N)==3:
		return centinaia(n)
	elif len(N)==4:
		return migliaia(n)
	elif len(N)==5:
		return decine_migliaia(n)
	elif len(N)==6:
		return cent_migliaia(n)
	elif 7<=len(N)<=9:
		return milioni(n)
	
'Scrivete qui il codice della funzione'

	
	
def unita(n):
	unitaint=['1','2','3','4','5','6','7','8','9']
	unitastr=['uno','due','tre','quattro','cinque','sei','sette','otto','nove']
	y= str(n)
	if y in unitaint:
	    x= unitaint.index(y)
	    return unitastr[x]
	
	    
#def Checknumeri(n):
#	y=str(n)
#	if len(y)==3:
#		decimale=y[1]+y[2]
#		if y[1]='8' and y[0]='1':
#			return ('cent'+ decine(decimale))
		
		
		
def decine(n):
	decinaint=['10','11','12','13','14','15','16','17','18','19']
	decinastr=['dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
	#ALL INIZIO DI OGNI CONTROLLO CHIAMARE LA F CHECK PER VEDERE SE CI SONO O 1 O 8
	#return('n: ',n)
	y=str(n)
	#return('y: ',y)
	if y in decinaint:
		x= decinaint.index(y)
		return decinastr[x]
	if n==20:
		return 'venti'
	elif n==21:
		return('ventuno')
	elif n==28:
		return('ventotto')
	elif 22<=n<=29:
		return('venti'+unita(y[1]))
	if n==30:
		return('trenta')
	elif n==31:
		return('trentuno')
	elif n==38:
		return('trentotto')
	elif 32<=n<=39:
		return('trenta'+unita(y[1]))
	if n==40:
		return('quaranta')
	elif n==41:
		return('quarantuno')
	elif n==48:
		return('quarantotto')
	elif 42<=n<=49:
		return('quaranta'+unita(y[1]))
	if n==50:
		return('cinquanta')
	elif n==51:
		return('cinquantuno')
	elif n==58:
		return('cinquantotto')
	elif 52<=n<=59:
		return('cinquanta'+unita(y[1]))
	if n==60:
		return('sessanta')
	elif n==61:
		return('sessantuno')
	elif n==68:
		return('sessantotto')
	elif 62<=n<=69:
		return('sessanta'+unita(y[1]))
	if n==70:
		return('settanta')
	elif n==71:
		return('settantuno')
	elif n==78:
		return('settantotto')
	elif 72<=n<=79:
		return('settanta'+unita(y[1]))
	if n==80:
		return('ottanta')
	elif n==81:
		return('ottantuno')
	elif n==88:
		return('ottantotto')
	elif 82<=n<=89:
		return('ottanta'+unita(y[1]))
	if n==90:
		return('novanta')
	elif n==91:
		return('novantuno')
	elif n==98:
		return('novantotto')
	elif 92<=n<=99:
		return('novanta'+unita(y[1]))
		
def centinaia(n):
	#Checknumeri(n)
	y=str(n)
	decimale=int(y[1]+y[2])
	if n==100:
		return('cento')
	elif 101<=n<=109:
		return('cento'+unita(y[2]))
	elif 110<=n<=199:
		if 180<=n<=189:
			return ('cent'+str(decine(decimale)))
		return('cento'+str(decine(decimale)))
	if n==200:
		return('duecento')
	elif 201<=n<=209:
		return('duecento'+unita(y[2]))
	elif 210<=n<=299:
		if 280<=n<=289:
			return ('duecent'+str(decine(decimale)))
		return('duecento'+str(decine(decimale)))
	if n==300:
		return 'trecento'
	elif 301<=n<=309:
		return('trecento'+unita(y[2]))
	elif 310<=n<=399:
		if 380<=n<=389:
			return ('trecent'+str(decine(decimale)))
		return('trecento'+str(decine(decimale)))
	if n==400:
		return 'quattrocento'
	elif 401<=n<=409:
		return('quattrocento'+unita(y[2]))
	elif 410<=n<=499:
		if 480<=n<=489:
			return ('quattrocent'+str(decine(decimale)))
		return('quattrocento'+str(decine(decimale)))
	if n==500:
		return 'cinquecento'
	elif 501<=n<=509:
		return('cinquecento'+unita(y[2]))
	elif 510<=n<=599:
		if 580<=n<=589:
			return ('cinquecent'+str(decine(decimale)))
		return('cinquecento'+str(decine(decimale)))
	if n==600:
		return 'seicento'
	elif 601<=n<=609:
		return('seicento'+unita(y[2]))
	elif 610<=n<=699:
		if 680<=n<=689:
			return ('seicent'+str(decine(decimale)))
		return('seicento'+str(decine(decimale)))
	if n==700:
		return 'settecento'
	elif 701<=n<=709:
		return('settecento'+unita(y[2]))
	elif 710<=n<=799:
		if 780<=n<=789:
			return ('settecent'+str(decine(decimale)))
		return('settecento'+str(decine(decimale)))
	if n==800:
		return 'ottocento'
	elif 801<=n<=809:
		return('ottocento'+unita(y[2]))
	elif 810<=n<=899:
		if 880<=n<=889:
			return ('ottocent'+str(decine(decimale)))
		return('ottocento'+str(decine(decimale)))
	if n==900:
		return 'novecento'
	elif 901<=n<=909:
		return('novecento'+unita(y[2]))
	elif 910<=n<=999:
		if 980<=n<=989:
			return ('novecent'+str(decine(decimale)))
		return('novecento'+str(decine(decimale)))
		

def migliaia(n):
	y=str(n)
	decimale=int(y[2]+y[3])
	centesimi=int(y[1]+y[2]+y[3])
	if n==1000:
		return('mille')
	if 1000<n<=1009:
		return ('mille'+unita(y[3]))
	elif 1010<=n<=1099:
		return ('mille'+str(decine(decimale)))
	elif 1100<=n<=1999:
		return ('mille'+str(centinaia(centesimi)))
	if n==2000:
		return 'duemila'
	if 2000<n<=2009:
		return ('duemila'+unita(y[3]))
	elif 2010<=n<=2099:
		return ('duemila'+str(decine(decimale)))
	elif 2100<=n<=2999:
		return ('duemila'+str(centinaia(centesimi)))
	if n==3000:
		return 'tremila'
	if 3000<n<=3009:
		return ('tremila'+unita(y[3]))
	elif 3010<=n<=3099:
		return ('tremila'+str(decine(decimale)))
	elif 3100<=n<=3999:
		return ('tremila'+str(centinaia(centesimi)))
	if n==4000:
		return 'quattromila'
	if 4000<n<=4009:
		return ('quattromila'+unita(y[3]))
	elif 4010<=n<=4099:
		return ('quattromila'+str(decine(decimale)))
	elif 4100<=n<=4999:
		return ('quattromila'+str(centinaia(centesimi)))
	if n==5000:
		return 'cinquemila'
	if 5000<n<=5009:
		return ('cinquemila'+unita(y[3]))
	elif 5010<=n<=5099:
		return ('cinquemila'+str(decine(decimale)))
	elif 5100<=n<=5999:
		return ('cinquemila'+str(centinaia(centesimi)))
	if n==6000:
		return 'seimila'
	if 6000<n<=6009:
		return ('seimila'+unita(y[3]))
	elif 6010<=n<=6099:
		return ('seimila'+str(decine(decimale)))
	elif 6100<=n<=6999:
		return ('seimila'+str(centinaia(centesimi)))
	if n==7000:
		return 'settemila'
	if 7000<n<=7009:
		return ('settemila'+unita(y[3]))
	elif 7010<=n<=7099:
		return ('settemila'+str(decine(decimale)))
	elif 7100<=n<=7999:
		return ('settemila'+str(centinaia(centesimi)))
	if n==8000:
		return 'ottomila'
	if 8000<n<=8009:
		return ('ottomila'+unita(y[3]))
	elif 8010<=n<=8099:
		return ('ottomila'+str(decine(decimale)))
	elif 8100<=n<=8999:
		return ('ottomila'+str(centinaia(centesimi)))
	if n==9000:
		return 'novemila'
	if 9000<n<=9009:
		return ('novemila'+unita(y[3]))
	elif 9010<=n<=9099:
		return ('novemila'+str(decine(decimale)))
	elif 9100<=n<=9999:
		return ('novemila'+str(centinaia(centesimi)))
		
def decine_migliaia(n):
	y=str(n)
	inizio=int(y[:2])
	centesimi=int(y[2:])
	decimale=int(y[3:])
	u=int(y[4])
	if y[2:]=='000':
		return str(decine(inizio))+'mila'
	if y[2:4]=='00' and y[4]!='0':
		return str(decine(inizio))+'mila'+unita(u)
	elif y[3]!='0':
		return str(decine(inizio))+'mila'+str(decine(decimale))
	elif y[2]!='0':
		return str(decine(inizio))+'mila'+str(centinaia(centesimi))
		
def cent_migliaia(n):
	y=str(n)
	inizio=int(y[:3])
	u=int(y[5])
	decimale=int(y[4:])
	centesimi=int(y[3:])
	if y[3:]=='000':
		return str(centinaia(inizio))+'mila'
	if y[3:5]=='00' and y[5]!='0':
		return str(centinaia(inizio))+'mila'+unita(u)
	if y[4]!='0':
		return str(centinaia(inizio))+'mila'+str(decine(decimale))
	if y[3]!='0':
		return str(centinaia(inizio))+'mila'+str(centinaia(centesimi))
		
def milioni(n):
	y=str(n)
	if len(y)==7:
		m=int(y[0])
		u=int(y[6])
		decimale=int(y[5:])
		centesimi=int(y[4:])
		mill=int(y[3:])
		decmill=int(y[2:])
		centmill=int(y[1:])
		if y[1:]=='000000':
			return unita(m)+'milioni'
		elif y[1:6]=='00000' and y[6]!='0':
			return unita(m)+'milioni'+unita(u)
		elif y[1:5]!='0000' and y[5]!='0':
			return unita(m)+'milioni'+str(decine(decimale))
		elif y[1:4]=='000' and y[4]!='0':
			return unita(m)+'milioni'+str(centinaia(centesimi))
		elif y[1:3]=='00' and y[3]!='0':
			return unita(m)+'milioni'+str(migliaia(mill))
		elif y[1]=='0' and y[2]!='0':
			return unita(m)+'milioni'+ str(decine_migliaia(decmill))
		elif y[1]!='0':
			return unita(m)+'milioni'+str(cent_migliaia(centmill))
		
	if len(y)==8:
		m=int(y[:2])
		u=int(y[7])
		decimale=int(y[6:])
		centesimi=int(y[5:])
		mill=int(y[4:])
		decimill=int(y[3:])
		centmill=int(y[2:])
		if y[2:]=='000000':
			return str(decine(m))+'milioni'
		elif y[2:7]=='00000' and y[7]!='0':
			return str(decine(m))+'milioni'+unita(u)
		elif y[2:6]!='0000' and y[6]!='0':
			return str(decine(m))+'milioni'+str(decine(decimale))
		elif y[2:5]=='000' and y[5]!='0':
			return str(decine(m))+'milioni'+str(centinaia(centesimi))
		elif y[2:4]=='00' and y[4]!='0':
			return str(decine(m))+'milioni'+str(migliaia(mill))
		elif y[2]=='0' and y[3]!='0':
			return str(decine(m))+'milioni'+ str(decine_migliaia(decimill))
		elif y[2]!='0':
			return str(decine(m))+'milioni'+str(cent_migliaia(centmill)) 
	if len(y)==9:
		m=int(y[:3])
		u=int(y[8])
		decimale=int(y[7:])
		centesimi=int(y[6:])
		mill=int(y[5:])
		decimill=int(y[4:])
		centmill=int(y[3:])
		
		if y[3:]=='000000':
			return str(centinaia(m))+'milioni'
		elif y[3:8]=='00000' and y[8]!='0':
			return str(centinaia(m))+'milioni'+unita(u)
		elif y[3:7]!='0000' and y[7]!='0':
			return str(centinaia(m))+'milioni'+str(decine(decimale))
		elif y[3:6]=='000' and y[6]!='0':
			return str(centinaia(m))+'milioni'+str(centinaia(centesimi))
		elif y[3:5]=='00' and y[5]!='0':
			return str(centinaia(m))+'milioni'+str(migliaia(mill))
		elif y[3]=='0' and y[4]!='0':
			return str(centinaia(m))+'milioni'+ str(decine_migliaia(decimill))
		elif y[3]!='0':
			return str(decine(m))+'milioni'+str(cent_migliaia(centmill)) 
		
		
	
	
	
	
	
	
	
			
	    
	
# main
print(conv(6482937))
#return(result)
