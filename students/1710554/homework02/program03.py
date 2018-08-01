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

import re

def decod(pfile, codice):
    pfile = open(pfile, mode = 'rt', encoding = 'utf-8')
    lista_compatibili = []
    for linea in pfile:
        linea = re.sub('[^a-z]', '', linea)
        if len(codice) == len(linea):
            lista_compatibili.append(linea)
            if scarta(linea, codice) == False:
                lista_compatibili.remove(linea)
                
    lista_compatibili = set(lista_compatibili)
    return lista_compatibili


def scarta(linea, codice):
    linea = list(linea)
    codice = list(codice)
    for a,b in zip(linea, codice):
        for l,c in zip(linea, codice):
            if a == l:
                if b == c:
                    continue
                else:
                    return False
            else:
                if b != c:
                    continue
                else:
                    return False
    return True


