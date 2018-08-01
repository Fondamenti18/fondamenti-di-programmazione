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
	diz = open(pfile, 'r')
	dizionario = diz.readlines()
	diz.close()
	compatibili = []
	doppie = ''
	dizionario.sort(key = lambda x: len(x) == len(codice)+1, reverse = True)
	for y in codice:
		if y*2 in codice:
			doppie += y
	for i in dizionario:
		if len(i) == len(codice)+1 and doppie == '' and len(set(i))==len(set(codice))+1:
			i = i.replace('\n','')
			setparolaord = sorted(set(i),key = lambda x: i.index(x))
			setcodiceord = sorted(set(codice),key = lambda x: codice.index(x))
			d = dict(zip(setcodiceord, setparolaord))
			b = ''
			for boh in codice:
				y=str(boh)
				b+=d[y]
			if b == i:
				compatibili += [i]
		elif len(i) == len(codice)+1 and len(set(i))==len(set(codice))+1:
			doppie2 = ''
			for x in i:
				if x*2 in i:
					doppie2 += x
			if len(doppie2) == len(doppie):
				i=i.replace('\n','')
				setparolaord = sorted(set(i),key = lambda x: i.index(x))
				setcodiceord = sorted(set(codice),key = lambda x: codice.index(x))
				d = dict(zip(setcodiceord, setparolaord))
				b = ''
				for h in codice:
					y=str(h)
					b+=d[y]
				if b == i:
					compatibili += [i]	
		elif len(i) != len(codice)+1:
			break
	return set(compatibili)
