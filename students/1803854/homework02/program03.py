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
	'''
	Funzione che trova, dato un percorso file e una stringa di cifre in input, tutte le parole all'interno
	del file che soddisfano la struttura.
	'''
	codice_prova = list(codice).copy()
	codice_prova = ''.join(codice_prova)
	control(codice_prova)
	lista = []
	with open(pfile, mode='r', encoding = 'utf-8') as f:
		for i in f.readlines():
			if len(i.strip()) != len(codice):
				next
			elif test(i, codice):
				lista += [i.strip()]
	f.close()
	return set(lista)
	
def test(word, code):
	'''
	Questa funzione controlla se la parola e la struttura prese in input sono compatibili.
	'''
	#Ottengo gli indici in cui ci sono cifre ripetute.
	rep = {}
	for i in range(len(code)):
		if code[i] in rep:
			rep[code[i]] += [i]
		elif code[i] in code[i+1:]:
			rep[code[i]] = [i]
	#Controllo se negli indici in cui ci sono ripetizioni le lettere sono uguali. Sfrutto l'occasione per creare il vettore che contiene tutti gli indici delle ripetizioni.
	non_rep = []
	for i in rep:
		lista = []
		for m in rep[i]:
			lista += word[m]
			non_rep += [m]
		if len(set(lista)) == 1:
			next
		else:
			return False
	#Controllo se negli indici in cui non ci sono ripetizioni le lettere sono diverse		
	l2 = []
	for i in range(len(word)):
		l2 += word[i]
	if len(set(l2))-len(rep) != (len(word) - len(non_rep)):
		return False
	else:
		return True
			
def control(code):
	'''
	Sequenza di controllo per vedere se la stringa soddisfa le condizioni della struttura.
	'''
	for i in range(0, len(code), -1):
		if code[i] in code[:i]:
			code[i].remove
	if len(code) > 10:
		raise Exception('la struttura non e\' valida')

if __name__ == '__main__':
	decod('file03.txt', '121')