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



#ritorna una lista di parole con la stessa lunghezza del codice 

def size_words(pfile,codice):
	f = open(pfile,'r')
	text = f.read()
	text = text.splitlines()
	f.close()
	elenco_parole = []
	for words in text :
		if len(codice)== len(words):
			elenco_parole+=[words]
	return elenco_parole

#prende in input una stringa e ritorna una lista con il numero di occorrenze di un carattere

def count_position(s):
	newl = []
	for c in s:
		newl += ['%d' % (s.index(c))]
	return newl



def decod(pfile, codice):
	'''inserire qui il codice'''
	parole_accettabili = set()
	parole = size_words(pfile,codice)
	char_codice = count_position(codice)
	for w in parole:
		char_parola = count_position(w)
		if char_parola == char_codice:
			parole_accettabili.add(w)
	return parole_accettabili










