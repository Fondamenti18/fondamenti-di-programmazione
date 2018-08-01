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

''' date n stringhe in input, returna in un set quelle che matchano il pattern dato in input'''
def decod(pfile, codice):
	right_words = set(list())
	with open(pfile) as my_file:
		for string in my_file:
			string = string.replace("\n", "")
			if(verify(codice,string)):
				right_words.add(string)
	return right_words

'''verifica se la parola matcha il pattern'''
def verify(pat,st):
	if(wrong_size(pat,st)): return False
	n_to_c = {}
	c_to_n = {}
	num = 0
	char = ""
	for i in range(len(pat)):
		num = pat[i]
		char = st[i]
		if(num not in n_to_c):
			try:
				if(c_to_n[char] != num ): return False
			except:
				n_to_c.update({ num:char })
				c_to_n.update({ char:num })

		if(n_to_c[num] != st[i]):
			return False
	return True

''' return True se la lunghezza del pattern e' diversa da quella della parola'''
def wrong_size(pat,st):
	len_pat = len(pat)
	len_st = len(st)
	if(len_pat != len_st): return True
