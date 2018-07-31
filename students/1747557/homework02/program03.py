'''
Abbiamo una stringa i cui elementi sono cifre tra '0' e '9' (comprese) che rappresenta la struttura di una parola.
La parola contiene al piu' 10 lettere diverse (ma puo' essere piu' lunga di 10 lettere se alcune sono ripetute), 
e la struttura si ottiene dalla parola sostituendo ciascuna lettera con una cifra, secondo le regole:
- a lettera uguale corrisponde cifra uguale
- a lettere diverse corrispondono cifre diverse

Esempio: 'cappello' -> '93447228'
Esempio: 'cappello' -> '12334556'

Sia data una "struttura" ed un insieme di parole. 
Vogliamo ottenere il sottoinsieme delle parole date compatibili con la struttura data.

Esempio: se la struttura e' '1234' e le parole sono { 'cane', 'gatto', 'nasa', 'oca', 'pino'}
le parole dell'insieme che sono compatibili con la struttura sono {'pino', 'cane'}

Scrivere una funzione decod( pfile, struttura) che prende in input:
- il percorso di un file (pfile), contenente testo organizzato in righe ciascuna composta da una sola parola
- una stringa di almeno 1 carattere, composta solo da cifre (la struttura delle parole da cercare)

La funzione  deve restituire l'insieme delle parole di pfile che sono compatibili con la struttura data.

Per gli esempi vedere il file grade03.txt

AVVERTENZE: 
	non usare caratteri non ASCII, come le lettere accentate;
	non usare moduli che non sono nella libreria standard.
NOTA: l'encoding del file e' 'utf-8'
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero.
'''


def decod(pfile, codice):
	ritorno= set()
	lenuguale=[]
	appoggio=[]
	with open(pfile,'r') as f:
		F= f.readlines()
	for s in F:
		s=s.strip()
		#print(s)
		if len(codice)== len(s):
			lenuguale.append(s)
	#print(lenuguale)
	lritorno= analisi(codice, lenuguale)
	#print('lritorno:   ',lritorno)
	for el in lritorno:
		appoggio.append(el)
		
	for el in appoggio:
		ritorno.add(el)
	return ritorno
			
			#return lenuguale
	#for e in lenuguale:
		
			
	'''inserire qui il codice'''
	
def analisi(codice, lenuguale):
	appoggio=[]
	lritorno=[]
	#print(lenuguale)
	for el in lenuguale:
		#print('el :  ',el)
		for e in el:
			x=el.count(e)
			#print('x   :  ',x)
		for c in codice:
			y=codice.count(c)
			#print('y :  ',y)
		if el.index(e)==codice.index(c) :
			appoggio.append(el)
		#	print('appoggio:   ', appoggio)
			
	for el in appoggio:
		lritorno.append(el)
	return lritorno
				
	

codice='121'
print(decod('file03.txt',codice))


