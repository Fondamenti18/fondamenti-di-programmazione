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
    setWords = txtToSet(pfile, len(codice))
    doubleInCode = doubleInString(codice)
    result = set()
    if(len(doubleInCode.keys()) > 0):
        for word in setWords:
            doubleInWord = doubleInString(word.lower())
            if(checkIfCompatible(doubleInCode, doubleInWord)):
                result.add(word)
    else:
        for word in setWords:
            doubleInWord = doubleInString(word)
            if(len(doubleInWord.keys()) == 0):
                result.add(word)
    return result


def txtToSet(filename, lenWord):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
    setWords = set()
    for line in lines:
        if(len(line[:-1]) == lenWord):
            setWords.add(line[:-1])
    return setWords


def doubleInString(string):
    double = dict()
    for char in string:
        if(string.count(char) > 1):
            double[char] = set()
            string2 = string
            pointer = 0
            index = 0
            while pointer != -1:
                pointer = string2.find(char)
                index += pointer
                double[char].add(index)
                index += 1
                string2 = string[index:]
                
    return double

def checkIfCompatible(dict1, dict2):
    dict1Keys = list(dict1.keys())
    dict2Keys = list(dict2.keys())
    check = False
    if(len(dict1Keys) == len(dict2Keys)):
        for i in range(len(dict1Keys)):
            if(dict1[dict1Keys[i]] == dict2[dict2Keys[i]]):
                check = True
            else:
                check = False
                break
    return check
