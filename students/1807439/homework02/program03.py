'''
Abbiamo una stringa i cui elementi sono cifre tra '0' e '9' (comprese) che rappresenta la struttura di una parola.
La parola contiene al piu' 10 lettere diverse (ma puo' essere piu' lunga di 10 lettere se alcune sono ripetute), 
e la struttura si ottiene dalla parola sostituendo ciascuna lettera con una cifra, secondo le regole:
- a lettera uguale corrisponde cifra uguale
- a lettere diverse corrispondono cifre diverse

Esempio: 'cappello' -> len
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

def compatibilita(struttura,stringa):
    i=0
    d={}
    verita=True
    if len(struttura)==len(stringa):
        for x in struttura:
            if x in d:
                if d[x]==stringa[i]:
                    pass
                else:
                    verita=False
            else:
                if stringa[i] in d.values():
                    verita=False
                else:
                    d[x]=stringa[i]
            i+=1
    else:
        verita=False
    return verita
def lista_comp(struttura,insieme):
    lista_c=[]
    for x in insieme:
        if compatibilita(struttura,x)==True:
            lista_c+=[x]
    return set(lista_c)
def decod(pfile, codice):
    f=open(pfile,'r')
    var=set()
    for x in f:
        var.add(x[:-1])
    return lista_comp(codice,var)
                     
    

