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
    with open(pfile,encoding='utf-8') as f:
        x=[]
        z=[]
        l=len(codice)
        s=set(codice)
        m=len(s)
        t=f.read()
        t=t.split()
        c=0 
        while c<l:
            c1=0
            q=codice.count(codice[c])
            f=0
            while f<q:
                i=codice.index(codice[c],c1)
                z.append(i)
                c1+=1
                f+=1
            c+=1
        for k in t:
            w=[]
            u=set(k)
            v=len(u)
            if m==v:
                c=0
                j=len(k)
                while c<j:
                    c1=0
                    q=k.count(k[c])
                    f=0
                    while f<q:
                        i=k.index(k[c],c1)
                        w.append(i)
                        c1+=1
                        f+=1
                    c+=1
                if w==z:
                    x.append(k)
        return set(x)