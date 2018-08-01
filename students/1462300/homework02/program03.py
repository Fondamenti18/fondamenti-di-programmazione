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
    ins = set()
    codi = list(codice)
    combinazioni = []
    for num in range(len(codi)):
        codi[num] = int(codi[num])
    with open(pfile,'r') as p:
        r = p.readline()
        r = r.strip('\n')
        while r != '':
            r = r.strip('\n')
            if len(r) == len(codi):
                combinazioni = comb(r,codi)
                if codi == combinazioni:
                    ins.add(r)
            r = p.readline()
    return ins
                    
    
def comb(r, codi):

    diz = {}
    lista_base = []
    i = 0
    for car in r:
        if car not in diz:
            if codi[i] not in codi[:i]:
                diz[car] = codi[i]
                lista_base += [diz[car]]
            i += 1
        else:
            lista_base += [diz[car]]
            i += 1
    return lista_base




