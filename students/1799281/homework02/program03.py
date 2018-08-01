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
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero. "C:/Users/john/Desktop/homework02/es3/file03.txt"
'''


def decod(pfile, codice):
    f=open(pfile)
    d={}
    finale=set()
    for line in f:
        
        if len(codice)!=len(line)-1:
            continue

        else:
            #print(line,codice)
            d=dizio(line,codice)
            c=parola(d,line)
            if c==codice:
                finale.add(line[:-1])
    return(finale)
            




def dizio(line,codice):
    lista=list(line)
    cod=list(codice)
    d={}
    i=0
    temp=0
    while i!=len(codice):
        if lista[i] not in d.keys() and lista[i] not in d.values() and cod[i] not in d.values():
            d[lista[i]]=cod[i]
        i=i+1
    #print(d)
    return(d)
def parola(d,line):
    stringa=""
    i=0
    while i!=len(line):
        if line[i] in d.keys():
            stringa=stringa+d[line[i]]
            #print(stringa)
        i=i+1
    #print(stringa)
    return(stringa)
    
        
    
    





