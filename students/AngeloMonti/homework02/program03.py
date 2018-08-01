'''
Abbiamo una stringa i cui elementi sono cifre tra '0' e '9' che rappresenta la struttura di una parola.
La parola contiene al più 10 lettere diverse, e la struttura si ottiene dalla parola 
sostituendo ciascuna lettera con una cifra, secondo le regole:
- a lettera uguale corrisponde cifra uguale
- a lettere diverse corrispondono cifre diverse

Esempio: 'cappello' -> '93447228'

Sia data una "struttura" ed un insieme di parole. 
Vogliamo ottenere il sottoinsieme delle parole date compatibili con la struttura data.

Esempio: se la struttura è '1234' e le parole sono [ 'cane', 'gatto', 'nasa', 'oca', 'pino']
le parole della lista che sono compatibili con la struttura sono {'pino', 'cane'}

Scrivere una funzione decod( pfile, struttura) che prende in input:
- il percorso di un file (pfile), contenente testo organizzato in righe ciascuna composta da una sola parola
- una stringa composta solo da cifre di almeno 1 carattere (la struttura delle parole da cercare)

La funzione  deve restituire l'insieme delle parole di pfile che sono compatibili con la struttura data.

Per gli esempi vedere il file grade03.txt

AVVERTENZE: 
	non usare caratteri non ASCII, come le lettere accentate;
	non usare moduli che non sono nella libreria standard.
NOTA: l'encoding del file è 'utf-8'
===================================
ATTENZIONE: Se il grader non termina entro 5 minuti il punteggio dell'esercizio e' zero.
					   ========
'''




def leggi_file(ftesto,k,t):
    '''legge il file di testo contenente stringhe di caratteri e restituisce la lista di quelle di 
    lunghezza k e con t caratteri distinti'''
    f = open(ftesto,'r', encoding='utf8')
    lista = f.readlines()
    f.close()
    lista1=[]
    for x in lista:
        x=x[:-1] 
        if len(x)==k and len(set(x))==t: lista1+=[x]
    return lista1


def calcola_dizio(x):
    '''crea un dizionario contenete come chiavi le cifre del codice e per attributo l'insieme 
    delle posizioni in cui la cifra compare'''
    d=dict()
    for i in range(len(x)):
        if x[i] not in d: 
            d[x[i]]=set([i])
        else:
            d[x[i]].add(i)
    return d

def uguali(parola,posi):
    '''controlla se i caratteri della stringa parola nell'insieme di posizioni posi sono uguali tra loro'''
    t=posi.pop()
    posi.add(t)
    c=parola[t]
    for i in posi:
        if parola[i]!=c: return 0
    return 1

def coerente(parola,d):
    '''controlla che la parola sia coerente con le posizioni del codice riportate dal dizionario'''
    for x in d:
        if not uguali(parola,d[x]): return 0
    return 1

def decod(pfile, codice):
    '''inserire qui il codice'''
    d=calcola_dizio(codice)
    lista=leggi_file(pfile,len(codice),len(d))
    soluzione=set()
    for parola in lista:
        if coerente(parola,d): soluzione.add(parola)
    return soluzione






