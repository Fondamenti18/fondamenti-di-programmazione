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


import re

# Converts the given pattern of numbers in a regular expression we can use to actually match it to our strings.
# Explanation (mostly for myself): for each letter in the pattern it adds to our result either '(.)' (which matches any character)
# or '\n' (which matches the nth group we already identified.
# So '3533939339' becomes '(.)(.)\1\1(.)\1\3\1\1\3'

# Problema: non ho idea di come evitare che gruppi si ripetano quindi i match vengono incasinati.
# 121 -> (.)(.)\1, match di 'aba' (corretto0 ma anche di 'aaa' (errato)
def pattern_to_regex(pattern):
    regex = []
    nr = {}
    for c in pattern:
        if c not in nr:
            regex.append('(.)')
            nr[c] = len(nr) + 1
        else:
            regex.append('\\{0}'.format(nr[c]))
            # regex.append('\\%d' % nr[c])
    
    return (''.join(regex) + '$')
    
    
def decod(pfile, codice):
    result = set()
    key = re.compile(pattern_to_regex(codice))
    
    with open(pfile, mode='r', encoding='utf-8') as file:
        
        for line in file:
            match = re.match(key, line)
            if match:
                used_letters = {match.group(1)}
                for i in range(2, key.groups + 1):
                    if match.group(i) not in used_letters:
                        used_letters.add(match.group(i))
                        
                    else:
                        break
                else:
                    result.add(line[:-1])
    return result    


    
if __name__ == '__main__':
    print(decod('testfile.txt', '2091555'))