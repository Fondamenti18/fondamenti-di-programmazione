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
def elabora(codpar):
	cod=[str(i) for i in codpar]
	cor1=[]
	cor2=[]

	c=0
	#per trovare le parole che hanno la stessa struttura del codice io mi baserò sulle posizioni
	#ove si ripetono i caratteri. ES: 121 ha la posizione 0 e 2 correlate, quindi tutte le parole
	#che hanno 3 come lunghezza e le posizioni 0 e 2 correlate saranno proprio le parole che ci interessano
	while c<len(cod):
		for j in range(c+1, len(cod)):
			if cod[c]==cod[j]:
				cor1+=[c]
				cor2+=[j]
		c+=1

	rel=list(zip(cor1,cor2))
	return rel

def decod(pfile, codice):
	f=open(pfile,'r')
	parola=set()
	dim=len(codice)
	
	c=f.readline().strip('\n')
	rel=elabora(codice)
	while c!='':
		par=elabora(c)
		if rel==par and len(c)==dim:
			parola.add(c)
		c=f.readline().strip('\n')

	f.close()
	return parola