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
    file=open(pfile)
    listacodice=list(codice)
    d=len(str(codice))
    parole=[]
    lettere=[]
    numeri=[]
    c=0
    insieme=set()
    for a in file:
        b=len(a)
        b=b-1
        if b==d:
            a=a.replace("\n","")
            parole.append(a)
    listac=[]
    l=""
    for x in codice:
        controllo=""
        listab=[]
        while listacodice.count(x)>1:
                controllo+=str(listacodice.index(x))
                listacodice[listacodice.index(x)]=""
                if listacodice.count(x)==1:
                    controllo+=str(listacodice.index(x))
                if len(controllo)>1:
                    listab+=controllo
                    l+=controllo
        if len(listab)>0:
            listac+=[listab]
    totc=0
    for j in codice:
        totc+=codice.count(j)
    totv=0
    for v in parole:
        conta=0
        totv=0
        for y in v:
            totv+=v.count(y)
        for g in listac:
            i=0
            if len(g)%2==0:
                while i<len(g):
                    if v[int(g[i])]==v[int(g[i+1])]:
                        conta+=2
                    i+=2
                if conta==len(l) and totc==totv:
                    insieme.add(v)
            if len(g)%2==1:
                i=0
                while i<len(g):
                    if i<len(g)-1:
                        if v[int(g[i])]==v[int(g[i+1])]:
                            conta+=1
                            if i==1:
                                conta+=1
                    i+=1
                if conta==len(g) and totc==totv:
                    insieme.add(v)
    return insieme
            
            
            
                
                

                
                
        
    



