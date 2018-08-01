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
from io import open
from os.path import getsize
from itertools import zip_longest

def removeDuplicates(s):
    r = []
    for c in s:
       if c not in r: r += [c]
    return r
    
def loadFile(pfile, clen):
    b = bytearray(getsize(pfile))
    with open(pfile, "rb", 64000) as f: f.readinto(b)
    return { w.decode('utf-8') for w in b.splitlines() if len(w) == clen}

def decod(pfile, codice):
    '''ritorna l'insieme delle parole che rispettano la struttura del codice passato come parametro'''
    a = loadFile(pfile, len(codice))
    codice = list(codice)
    cr = removeDuplicates(codice)
    crlen = len(cr)
    def checkWordStructure(a):
        r = set()
        for word in a:
            w = removeDuplicates(word)
            if crlen != len(w): continue
            dic = dict(zip_longest(w, cr))
            if [dic[c] for c in word] == codice: r.add(word)
        return r
    
    return checkWordStructure(a)