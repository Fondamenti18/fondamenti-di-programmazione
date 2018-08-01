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
    parole=set()
    numeri=set(codice)
    ls=[]
    f=open(pfile)
    for i in f:
        a=i.rstrip('\n')
        controllo=set(a)
        if len(a)==len(codice) and len(controllo)==len(numeri):
            ls+=[a]
    a=len(ls)-1
    while a>=0:
        st=''
        sz=''
        for i in ls[a]:
            s=1
            for e in ls[a]:
                if e==i:
                    st+=str(s)
                    s+=1
                else:
                    st+='0'
        for i in codice:
            s=1
            for e in codice:
                if e==i:
                    sz+=str(s)
                    s+=1
                else:
                    sz+='0'
        if st!=sz:
            del ls[a]
        a=a-1
    if ls!=[]:
        for i in ls:
            parole.add(i)
    return parole






