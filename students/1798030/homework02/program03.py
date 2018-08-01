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
    result = set()
    with open(pfile, 'r', encoding='utf-8') as f:
      
        word_list = f.readlines() # Lista delle linee = parole
  
    
        for word in word_list:
            word = word[:-1]
            
            digit_to_char = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1] # Corrispondenze tra cifra e carattere
            char_to_digit = {} # Dizionario delle corrispondenze da carattere a cifra
            
            if(len(codice) != len(word)): # Se il codice ha lunghezza diversa dalla parola, allora la parola non va bene
                continue
            
            word_is_good = True
            
            for index in range(len(word)):
                
                if(word_is_good == False):
                    break
                
                character = word[index]
                
                try:
                    if(char_to_digit[character] != codice[index]):
                        word_is_good = False
                except:
                    # e' la prima volta che si incontra la lettera nella parola
                    digit = codice[index]
                    if(digit_to_char[int(digit)] == -1):
                        digit_to_char[int(digit)] = character
                        char_to_digit[character] = digit
                        continue
                    else:
                    
                        word_is_good = False
            
            if(word_is_good):
                result.add(word)
                
            
                
    return result
