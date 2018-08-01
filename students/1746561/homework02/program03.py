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

import collections, itertools

def parole(pfile):
    '''Restituisce una lista di set di parole'''
    with open(pfile, 'r') as f:
        return [l.strip() for l in f]
    
def light(pfile, codice): return [w for w in parole(pfile) if len(w) == len(str(codice))] #Alleggerisce lista

def conteggio(ls): 
    c = collections.defaultdict(list)
    for i,j in enumerate(ls):
        c[j].append(i)
    return ((key,locs) for key,locs in c.items() if len(locs)>1)

def occorrenze(ls): return [el for el in sorted(conteggio(ls))] #Restituisce il numero di occorrenze a elemento

def lista(ls): return [list(reversed(list(itertools.chain(*l)))) for l in ls] #Unisce in un'unica lista

def rem_str(ls): return [i for i in ls if isinstance(i, int)] #Elimina caratteri non int

def decod(pfile, codice):
    ls = light(pfile, codice)
    code = str(codice)
    l = []
    for w in ls: 
        if occorrenze(w) and len(occorrenze(code)) == len(occorrenze(w))\
        and len(list(itertools.chain(*lista(occorrenze(code))))) == len(list(itertools.chain(*lista(occorrenze(w))))):
                lc = rem_str(list(itertools.chain(*lista(occorrenze(code)))))
                lf = rem_str(list(itertools.chain(*lista(list(reversed(occorrenze(w)))))))
                if lc == lf: l.append(w)
    return set(l)