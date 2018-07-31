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
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero.'''


def decod(pfile, codice):
    '''inserire qui il codice'''
    p=open(pfile,"r").read().split("\n")
    possibili=[]
    for parola in p:
        if len(parola)==len(codice):
                possibili+=[parola]
    cod=list(eliminaRicorrenze(codice))
    l=[]
    for el in possibili:
        el=eliminaRicorrenze(el)
        l+=[el]
    lp=[]#["ada","afa","aia"...]
    lc=[]#["ad","af",...]
    for i in range(len(l)):
        if len(l[i])==len(cod):
            lp.append(possibili[i])
            lc.append(l[i])
    codex=""#"01"
    for elem in cod:
        codex+=elem
    lf=[]
    for i in range(len(lc)):
        for i2 in range(len(lp)):
            if i==i2:
                ordinata=lc[i]
                chiave=codex
                testo=lp[i2]
                testo_codificato=""
                for x in testo:
                    if not (x.isalpha() or x.islower()):
                        testo_codificato+=x
                    elif not x in ordinata:
                        testo_codificato+=x
                    else:
                        for y in range(len(ordinata)):
                            if x==ordinata[y]:
                                testo_codificato+=chiave[y]
                lf.append(testo_codificato)
    giuste=[]
    for i3 in range(len(lf)):
        if lf[i3]==codice:
            giuste.append(lp[i3])
    return set(giuste)
    
    
    
    



def eliminaRicorrenze(x):
    x=invertiParole(x)
    lista=list(x)
    for j in x:
        if lista.count(j)>1:
            lista.remove(j)
    no_occorrenze=''
    for i in lista:
        no_occorrenze+=i
    parola=invertiParole(no_occorrenze)
    return parola


def invertiParole(x):
    if len(x)==1:
        return x
    if len(x)>1:
        return invertiParole(x[1:])+x[0]
    
        
    
    
            
    
                
    
