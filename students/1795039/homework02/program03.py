'''
Abbiamo una stringa i cui elementi sono cifre tra '0' e '9' (comprese) che rappresenta la struttura di una word.
La word contiene al piu' 10 lettere diverse (ma puo' essere piu' lunga di 10 lettere se alcune sono ripetute), 
e la struttura si ottiene dalla word sostituendo ciascuna lettera con una cifra, secondo le regole:
- a lettera uguale corrisponde cifra uguale
- a lettere diverse corrispondono cifre diverse

Esempio: 'cappello' -> '93447228'
Esempio: 'cappello' -> '12334556'

Sia data una "struttura" ed un insieme di parole. 
Vogliamo ottenere il sottoinsieme delle parole date compatibili con la struttura data.

Esempio: se la struttura e' '1234' e le parole sono { 'cane', 'gatto', 'nasa', 'oca', 'pino'}
le parole dell'insieme che sono compatibili con la struttura sono {'pino', 'cane'}

Scrivere una funzione decod( pfile, struttura) che prende in input:
- il percorso di un file (pfile), contenente testo organizzato in righe ciascuna composta da una sola word
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
 
    newCode = code_converter(codice)
    file = open(pfile, 'r', encoding = 'utf-8')
    matchingWords = set()
    sameLenght = lenght_checker(file,newCode)
    matchingWords = words_finder(sameLenght,newCode,matchingWords)
    
          
    return matchingWords


def code_converter(codice):

    code = ''.join(list(codice)) 
    newCode = ''
    function = {}
    count = 1
    
    for digit in code:
        if digit in function:
            newCode += function[digit]
        else:
            function[digit] = str(count)
            count += 1
            newCode += function[digit]

    return newCode


def lenght_checker(file,newCode):

    sameLenght = []
    for line in file:
        if len(line) == len(str(newCode))+1:
            sameLenght.append(line.strip())

    return sameLenght


def words_finder(sameLenght,newCode,matchingWords):

    index = -1
    while index != len(sameLenght)-1:
        function = {}
        index += 1
        convertedWord = ''
        count = 1
        word = sameLenght[index]
        for digit in word:
            if digit in function:
                convertedWord += function[digit]
            else:
                function[digit] = str(count)
                count += 1
                convertedWord += function[digit]
            if convertedWord == newCode:
                matchingWords.add(word)

    return matchingWords

    



    

    

       


  
                
    
        
                
    
    
        
    

    

                        
                                                        



