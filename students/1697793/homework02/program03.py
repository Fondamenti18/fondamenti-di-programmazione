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

def createCodeMap (code) :
    
    newCodeMap = {}
    
    for i in range(0, len(code)):
        currentCode = code[i]
        if(newCodeMap.get(currentCode, None) == None):
            newCodeMap[currentCode] = [i]
        else:
            newCodeMap[currentCode].append(i)
        
    result = []
    
    for key, value in newCodeMap.items():
        result.append(value)
        
    return result

def checkCorrectWord (word, codeMap) :
    
    wordMap = createCodeMap(word)
    
    for i in range(0, len(codeMap)):
        if i < len(wordMap):
            for j in range(0, len(codeMap[i])):
                if j < len(wordMap[i]):
                    if codeMap[i][j] != wordMap[i][j]:
                        return False
                else:
                    return False
        else:
            return False
            
    return True
    
def decod(pfile, codice):
    '''inserire qui il codice'''
    
    inFile = open(pfile, 'r', encoding='utf8')
    lines = inFile.readlines()
    inFile.close()
    
    codeMap = createCodeMap(codice)
    correctWords = set()
    
    for word in lines:
        currentWord = word.strip()
        if(len(currentWord) == len(codice)):
            if checkCorrectWord(currentWord, codeMap):
                correctWords.add(currentWord)
    
    return correctWords
        