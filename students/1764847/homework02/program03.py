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
    '''Prende in input un percorso file ed una 
    struttura e restituisce un insieme di tutte le 
    parole all'interno del file compatibili con la
    struttura'''
    insi = set()
    lstRighe = readText(pfile)
    for i in lstRighe:
        if compare(i, codice):
            insi.add(i)
    return insi
    


def readText(file):
    '''Prende in input un file e restituisce una litsa
    di righe del file senza '\n' '''
    f = open(file, 'r', encoding = 'utf-8')
    righe = f.read()
    f.close()
    lstRighe = righe.split('\n')
    return lstRighe


def compare(parola, codice):
    '''Prende in input una parola ed una struttura
    e restituisce un valore booleano, True se la parola
     e' compatibile con la struttura, False altrimenti'''
    dCodice = {}
    dParola = {}
    if len(parola) == len(codice):
        for i in range(len(parola)):
            if codice[i] in dCodice:
                dCodice[codice[i]] += [i]
            else:
                dCodice[codice[i]] = [i]
            if parola[i] in dParola:
                dParola[parola[i]] += [i]
            else:
                dParola[parola[i]] = [i]
        parola = list(dParola.values())
        codice = list(dCodice.values())
    return parola == codice
            
        
        
        
        