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

def trasfnumero(n):
	#questa funzione permette di trasformare un numero in una lista con cui poterci lavorare
	#essa dividera il numero in gruppi da tre e aggiunge 0 alle posizioni vuote
	n=[int(i) for i in str(n)]
	n.reverse()
	a=len(n)
	controllo=False
	while controllo!=True:
		a=len(n)
		if a%3!=0:
			n+=[0]
		else:
			controllo=True
	return n
	
def centinaia(ln, lett, app):
	lcifra=['uno','due','tre','quattro','cinque','sei','sette','otto','nove']
	ldieci=['dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
	ldecine=['venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
	ct='cento'
	controllo=False
		
	if ln!=[]:
	#controllo sulle centinaia
		if ln[0]!=0:
			if ln[0]==1:
				if ln[1]==8:
					app+=[ct[:-1]]
				else:
					app+=[ct]
			else:
				app+=[lcifra[ln[0]-1]]
				if ln[1]==8:
					app+=[ct[:-1]]
				else:
					app+=[ct]
		#controllo sulle decine			
		if ln[1]!=0:
			if ln[1]==1:
				app+=[ldieci[ln[2]]]
				controllo=True
			else:
				if ln[2] in [1,8]:
					illide=ldecine[ln[1]-2]
					illide=illide[:-1]
					app+=illide
				else:
					app+=ldecine[ln[1]-2]
		#controllo sulle cifre			
		if ln[2]!=0 and controllo!=True:
			app+=lcifra[ln[2]-1]
	else:
		#essendo ricorsiva (la funzione conv), essa si fermerà non appena la lista dei numeri ottenuti con la funzione trasfnumero
		#sarà vuota, cioè appena ha finito di scrivere il numero completo
		numero=''.join(lett)
		del lett[:]
		return numero
	
def calcolomil(ln, i, lett, app):
	if i!=0:
		#essendo ricorsiva (la funzione conv) questo indice segna quando inserire il suffisso delle migliaia/milioni/miliardi
		if i==1:
			num=int(''.join([str(x) for x in ln]))
			if num!=0:
				if num>1:
					app+=['mila']
				else:
					if num==1:
						app[:]=[]
						app+=['mille']
				app=''.join(app)
				lett[0:0]+=app
		if i==2:
			num=int(''.join([str(x) for x in ln]))
			if num!=0:
				if num>1:
					app+=['milioni']
				else:
					if num==1:
						app[:]=[]
						app+=['milione']
				app=''.join(app)
				lett[0:0]+=app
		if i==3:
			num=int(''.join([str(x) for x in ln]))
			if num!=0:
				if num>1:
					app+=['miliardi']
				else:
					if num==1:
						app[:]=[]
						app+=['miliardo']
				app=''.join(app)
				lett[0:0]+=app
	else:
		lett+=app

def conv(n,i=0,lett=[]):
	ln=[]
	app=[]
	illide=''
	numero=''
	controllo=False
	
	if type(n)!=type([]):
		n=trasfnumero(n)
	
	if n!=[]:
		ln[:]=n[:3]
		del n[:3]
		ln.reverse()
	
	if ln!=[]:	
		centinaia(ln, lett, app)
	else:
		numero=''.join(lett)
		del lett[:]
		return numero
		
	calcolomil(ln, i, lett, app)
	
	if i<3:
		i+=1
		return conv(n,i,lett)
	else:
		numero=''.join(lett)
		del lett[:]
		return numero