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
#RAGIONAMENTO:
#Leggo con un ciclo tutte le righe del file
#Se parole sono compatibili con LUNGHEZZA di struttura e LUNGHEZZA di set(struttura) allora le salvo in una lista
#Creo una funzione che codifica le parole compatibili rispettando le posizioni di CODICE
#Comparo ListaCodificata con il Codice nel caso di uguaglianza il valore relativo alla parola iniziale inserisco in una lista 

def decod(pfile, codice):
	finalList = []
	listCoded, listNormal = leggiCodifica(pfile, codice)
	for i, w in enumerate(listCoded):
		if w == codice:																	#controllo se le parole codificate sono uguali a CODICE, nel caso aggiungo ad una lista
			finalList.append(listNormal[i])
	return set(finalList)
	
def leggiCodifica(file, codice):
	wList = []
	wCoded = []
	with open(file, encoding='utf8') as file:
		for line in file:
			word = line.rstrip()
			if ((len(set(word))) == len(set(codice))) and (len(word) == len(codice)):     #leggo con un ciclo tutte le righe una ad una, nel caso siano compatibili 
				wList += [word]															  #con la lunghezza totale e la lunghezza di un set(struttura) le salvo in una lista
				wCoded += [codifica(word, codice)]										  #in questa lista salvo le parole compatibili CODIFICATE
	return wCoded, wList
	
def codifica(word, codice):
	giaCambiate = ''
	for i, let in enumerate(word):										#percorro indice e lettere della parola, sostituisco le prime occorrenze delle lettere utilizzando lo stesso indice su CODICE
		if let in giaCambiate:											#in questo modo rispetto le posizioni della struttura
			continue
		else:
			giaCambiate += let
			word = word.replace(let,codice[i])
	return word
