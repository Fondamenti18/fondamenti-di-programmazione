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
    op_file= open(pfile,"r")
    lungc=str(codice)
    lungc=len(lungc)
    strcodice=str(codice)
    tst_file=0
    ins=[]
    while tst_file!='':
        tst_file=op_file.readline()
        parola=tst_file[0:-1]
        lengh=len(parola)
        if(lungc==lengh):
           ins+=codicecodi(parola,strcodice,lengh)
    ins=set(ins)
    return(ins)


def codicecodi(parola,strcodice,lengh):
    c=0
    al=[]
    while c<len(strcodice):
        if(strcodice[c] not in al):
            al+=strcodice[c]
        c+=1
    c=0
    k=0
    b=[]
    val=[]
    ret=[]
    retf=[]
    while c<len(parola):
        if parola[c] not in b and k<len(al):
            b+=[parola[c]]
            val+=[al[k]]
            k+=1
        c+=1
    if(len(val)<len(al)):
        return()
    for i in parola:
        c=0
        while c<len(b):
            if i==b[c]:
                ret+=val[c]
            c+=1
    ret=''.join(ret)
    if(ret==strcodice):
        retf+=[parola]
        return(retf)
    return()


