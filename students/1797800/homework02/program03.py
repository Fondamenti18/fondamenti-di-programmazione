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
    '''funzione  deve restituire l'insieme delle parole di pfile che sono compatibili con la struttura data'''
    codeStr = pickOneFromWord(codice)   #converto il codice in str
    originalWord= []
    compWord = set()
    lenCode_Word = len(codice)
    with open(pfile,encoding='utf8') as f:
        for line in f:
            if len(line)-1 == lenCode_Word:
                originalWord.append(line.strip('\n'))
    for x in originalWord:
        if checkComp(x,codice):
            compWord.add(x)
    return compWord




def checkComp(word,code):
    dizCodeToWord = {}
    dizWordToCode = {}
    for i in range(len(code)):
        if word[i] in dizWordToCode and dizWordToCode[word[i]] != code[i]:
            return False
        if code[i] in dizCodeToWord and dizCodeToWord[code[i]] != word[i]:
            return False
        dizWordToCode[word[i]], dizCodeToWord[code[i]] = code[i], word[i]
    stringa = ''
    for x in word:
        stringa+= dizWordToCode[x]

        # print('la parola',word,'la stringa',stringa)
    return stringa == code


def pickOneFromWord(word):
    newWord = ''
    for c in word:
        if c not in newWord:
            newWord+= c
    return newWord

