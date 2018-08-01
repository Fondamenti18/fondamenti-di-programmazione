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
    '''inserire qui il codice'''
    p = len(codice)
    strutturaParoleVere = []
    
    
    paroleVere, paroleGenerali = parole(pfile, codice, p)
    
    strutturaParoleVere += [''.join(paroleVere[i*p:i*p+p]) for i in range(len(paroleVere[::p]))]
    
    dizionario = creaDizionario(strutturaParoleVere, paroleGenerali)
    
    a = trasforma(codice)
    
    risultato = trova(dizionario, a)
    
    return set(risultato)
    
def parole(pfile, codice, p):
    paroleVere = []
    paroleGenerali = []
    
    with open(pfile, encoding = 'UTF-8') as fin:
        parole = fin.read()
        parole = parole.split()
    for parola in parole:
        parola.strip('\\n')
        if len(parola) == p:
            paroleGenerali += [parola]
            paroleVere += [str(parola.find(c)) for c in parola]
    return paroleVere, paroleGenerali


def creaDizionario(lista1, lista2):
    dizionario = {}
    for k,v in zip(lista1, lista2):
        if k in dizionario:
            dizionario[k] += [v]
        else:
            dizionario[k] = [v]
    return dizionario  


def trasforma(codice):
    a = ''.join(str(codice.find(c)) for c in codice)
    return a

def trova(dizionario, codice):
    risultato = []
    if codice in dizionario:
        risultato = dizionario[codice]
    return risultato
