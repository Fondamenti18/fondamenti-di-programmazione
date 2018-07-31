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



def controllo_valori(diz_num, diz_car, codice, x):
    '''controllo se i valori sono giusti.'''
    for y in range(0, len(x)):
        if codice[y] not in diz_num and x[y] not in diz_car:
            diz_num[codice[y]] = x[y]
            diz_car[x[y]] = codice[y]
        elif controllo_not_valori(diz_num, diz_car, codice, x, y) == False: return False
    return x

def controllo_not_valori(diz_num, diz_car, codice, x, y):
    '''controllo se i valori sono sbagliati.'''
    if (x[y] in diz_car and diz_car[x[y]] != codice[y]) or (codice[y] in diz_num and diz_num[codice[y]] != x[y]): return False
    return True

def controllo_formato(codice, x):
    '''controllare se il formato corrisponde.'''
    diz_num = {}
    diz_car = {}
    return controllo_valori(diz_num, diz_car, codice, x)

def trova_parole(lista_testo, codice):
    '''aggiungere gli elementi alla lista risultato.'''
    return [x for x in lista_testo if len(x) == len(codice) and controllo_formato(codice, x)]

def decod(pfile, codice):
    '''dato un formato numerico in ingresso restituire le parole nel file pfile che soddisfano tale formato.'''
    return set(trova_parole(open(pfile, 'r').read().split(), codice))