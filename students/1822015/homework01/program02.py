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
infatti, non elidono la vocale finale. Dunque non scriveremo centuno,trecentotto ma centouno, 
trecentootto, ecc...

I numeri composti dalle centinaia e dalla decina "ottanta" invece tornano ad elidere 
la vocale finale; scriveremo quindi centottanta, duecentottanta,ecc..., 
non centoottanta, duecentoottanta, ...

Il numero "mille" non elide in nessun numero composto la vocale finale; scriveremo 
quindi milleuno,milleotto, milleottanta, ecc...

Altri esempi sono elencati nel file grade02.txt


Scrivere una funzione conv(n) che prende in input un intero n, con 0<n<1000000000000, 
e restituisce in output una stringa con il numero espresso in lettere

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

def conv(n):
	convString = []
	
	listaTriple = generaLista(str(n))			#chiamata al metodo per creare una lista di triple

	for tripla in listaTriple:				#percorro la lista per individuare dove fare la conversione
		if tripla == '000':					#in questo caso non e' necessario convertire, quindi ignoro
			convString += ['']
		else:
			convString += [convTripla(tripla)]		#chiamo il metodo creato per la conversione
			
	return convFinale(convString)				#restituisco il return del metodo creato per la stringa finale

def generaLista(stringa):
	tmpString = stringa
	
	while len(tmpString)<12:
		tmpString = '0' + tmpString						#aggiungo tanti zero quanti ne servono per riempire la stringa con 12 elementi
	strWork = tmpString[0:3]+' '+tmpString[3:6]+' '+tmpString[6:9]+' '+tmpString[9:] 		#aggiungo spazi alla stringa per dividere in TRIPLE
	
	return strWork.split()		#uso il metodo .split per ritornare una lista con la divisione in triple	
		
def convTripla(strTripla):
	lLetter = ['','uno','due','tre','quattro','cinque','sei','sette','otto','nove', 'dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
	mLetter = ['','','venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
	
	#ho dichiarato due liste con le stringhe per effettuare le conversioni, ogni stringa e' nella posizione per essere chiamata utilizzando l'indice, avrei potuto implementare un dizionario ma solo oggi(22/10) ho seguito la videolezione che ne parla.
	
	primoEl = strTripla[:1]			#con queste due assegnazioni divido la tripla in centinaia e decine, pronte per la conversione
	secEl = strTripla[1:3]
	tmpConv = ''
	
	if int(primoEl) > 1:
		tmpConv = lLetter[int(primoEl)] + 'cento'
	elif int(primoEl) == 1:
		tmpConv = 'cento'
		
	if (int(secEl)> 0) and (int(secEl)<20):					#insieme di if/elif per effettuare la conversione, per le condizioni e per le assegnazioni utilizzo la conversione str -> int per dividere "in corso" decine ed unita'
		endConv = tmpConv + lLetter[int(secEl)]
	elif secEl[0] == '8':								#condizione per effettuare l'elisione in caso di 'ottanta'
		if (secEl[-1] == '8') or (secEl[-1] == '1'):				#condizione per l'elisione di 'uno' e 'otto'
			endConv = tmpConv[:-1] + mLetter[int(secEl[:1])][:-1] + lLetter[int(secEl[1:])]
		else:
			endConv = tmpConv[:-1] + mLetter[int(secEl[:1])] + lLetter[int(secEl[1:])]
	elif int(secEl)>= 20:
		if (secEl[-1] == '8') or (secEl[-1] == '1'):
			endConv = tmpConv + mLetter[int(secEl[:1])][:-1] + lLetter[int(secEl[1:])]
		else:
			endConv = tmpConv + mLetter[int(secEl[:1])] + lLetter[int(secEl[1:])]
		
	return endConv	

def convFinale(listString):					#metodo per la conversione finale, un insieme di if/elif per assegnare ad ogni tripla il giusto valore nella scala
	finalString=['', '', '', '']
	
	if listString[0] == 'uno':
		finalString[0] = listString[0]+'miliardo'
	elif listString[0] != '':
		finalString[0] = listString[0]+'miliardi'
	
	if listString[1] == 'uno':
		finalString[1] = listString[1]+'milione'
	elif listString[1] != '':
		finalString[1] = listString[1]+'milioni'
		
	if listString[2] == 'uno':
		finalString[2] = 'mille'
	elif listString[2] != '':
		finalString[2] = listString[2]+'mila'
	
	finalString[3]= listString[3]
	
	return ''.join(finalString)
