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

La funzione	 deve restituire l'insieme delle parole di pfile che sono compatibili con la struttura data.

Per gli esempi vedere il file grade03.txt

AVVERTENZE: 
	non usare caratteri non ASCII, come le lettere accentate;
	non usare moduli che non sono nella libreria standard.
NOTA: l'encoding del file e' 'utf-8'
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero.
'''


def decod(pfile, codice):
	'''inserire qui il codice'''
	words = set()
	matrice_dizionario = {c:None for c in set(codice)}
	len_codice = len(codice)
	buffer = []
	print(codice, matrice_dizionario)
	with open(pfile, "r") as f:
		
		for l in f.readlines():
			
			dizionario = matrice_dizionario.copy()
			buffer.clear()
			correct = True
			if len_codice != len(l)-1:
				correct=False
			else:
				for k in range(0,len_codice):
					char = l[k]
					codice_k = codice[k]
					char_map = dizionario[codice_k]
					if char_map == None and char not in buffer:
						dizionario[codice_k] = char
						buffer.append(char)
					elif dizionario[codice_k] != char:
						correct = False
					
			if correct:
				words.add(l.strip("\n"))
			
			
	return words
	
if __name__ == "__main__":
	import time
	start = time.time()
	print(decod('all.txt','2091555'))
	end = time.time()
	print((end-start)*1000)



