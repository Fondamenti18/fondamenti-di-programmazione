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
    '''inserire qui il codice'''
    cerca = build_RE(codice)                    # trasformo il codice in una RE

    return cerca_nel_file(pfile, cerca, len(codice))

def cerca_nel_file(pfile, cerca, k):
    '''Cerco una regular expression in una riga di un file e torno il set di parole trovate'''
    risultato = set()
    k += 1
    with open(pfile) as f:
        for line in f:
            if len(line) == k:
                match = re.match(cerca, line)
                if match:
                    risultato.add(line.strip())
    return risultato

def build_RE(codice):
    '''Trasforma il codice in una regular expression unica'''
    cerca = '^'                                 # la parola inizia al primo carattere
    visti = ''                                  # numeri gia' inseriti nella RE
    for c in codice:                            # per ciascuna cifra
        if c in visti:                          # se è stata già inserita nella RE
            cerca += '(?P=c' + c + ')'          # controllo che il prossimo carattere corrisponda al pattern 'cX'
        else:                                   # altrimenti è la prima volta che definisco questo elemento
            for v in visti:                     # per ciascuno dei codici gia' inseriti
                cerca += '(?!(?P=c' + v + '))'  # il prossimo carattere deve essere diverso da tutti i pattern gia' definiti
            cerca += '(?P<c' + c + '>\w)'       # e lo definisco col nome 'cX'
            visti += c                          # e ricordo di aver usato questo digit
    cerca += '$'                                # la parola deve finire alla fine della riga

    #print(cerca)
    return re.compile(cerca)                   # compilo la RE costruita




if __name__ == '__main__':
    print(decod('file03.txt', '363'))


