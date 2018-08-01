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

def induguali(n, lis):
	stessindici = []
	for i,v in enumerate(lis):
		if v == lis[n]:
			stessindici.append(i)
	return stessindici

def getinsieme(lnumerica, lista):
	insieme = set()
	for e in lista:
		c = 0
		V = True
		while (V and c<len(lnumerica)):
			l1 = induguali(c,lnumerica)
			l2 = induguali(c,list(e))
			if l1 == l2:
				c = c + 1
				if c == len(lnumerica):
					insieme.add(e)
			else:
				V = False
	return insieme

def decod(pfile, codice):
    '''inserire qui il codice'''
    with open(pfile) as f:
        testo = f.read()
    lrighe = testo.splitlines()
    lcodice = list(codice)
    struttura = []
    lparole = []
    for n in lcodice:
        numeri = int(n)
        struttura.append(numeri)

    for parola in lrighe:
        if len(parola) == len(struttura):
            lparole.append(parola)

    insfinale = getinsieme(struttura,lparole)
    return insfinale
