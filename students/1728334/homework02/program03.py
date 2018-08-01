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
import collections

def decod(pfile, codice):
    '''inserire qui il codice'''
    return s(pfile, codice)

def s(file, codice):  
    k = []
    with open(file, mode='r', encoding='utf-8') as o:
        for i in o:
            i = ''.join(i.split())
            if len(i) == len(codice):
                p = sol(codice, i)
                if p is not None:
                    k.append(p)        
    return set(k)
    
def check_codice(codice):
    codice = list(codice)
    return codice

def get_index_of_duplicate(codice):
    t = collections.defaultdict(list)
    for i, item in enumerate(codice):
        t[item].append(i)
    return dict([key, value] for key, value in t.items() if len(value) > 1)

def check(dizionario):
    for el in dizionario.keys():
        return dizionario.get(el) # mi ridà una lista

def sol(codice, parola):
    x = get_index_of_duplicate(codice)
    y = get_index_of_duplicate(parola)
    count = 0
    if check_word_with_code(x, y) is None:
        return
     #   return
    if len(codice) == len(parola):
        for v in x.items():
            for k in y.items():
                if v[1] == k[1]:
                    count += 1
    if count == len(x):
        return parola
    return
   
def check_word_with_code(word, code):
    return None if len(word) != len(code) else ""
        
    
    

def check_list_element(x):
    seen = set()
    return not any(i in seen or seen.add(i) for i in x)