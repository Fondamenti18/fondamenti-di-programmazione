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
    cod=list(codice) #trasmormo i numeri del codice in una lista di numeri
    lista=[] #lista di ritorno
    with open(pfile) as f:
        f=f.read()
        f=f.splitlines()
        for parola in f: #per ogni parola nella lista f
            lista.append(parola) #aggiungi la parola alla lista di ritorno
            if len(parola)==len(codice): #se codice e parola hanno stessa lunghezza allora analizzo la parola
                ricerca(parola,cod,lista)         
            else: #in caso contrario rimuovo la parola dalla lista
                lista[-1:]=[]
        insieme=set(lista)
        return insieme

def ricerca(parola,cod,lista):
    par=list(parola) #trasforma la parola in una lista di caratteri
    dizionario=dict() #crea un dizionario
    i=0
    while i<len(par): #finchè i< lunghezza della lista di caratteri
        if par[i] not in dizionario.keys() and cod[i] not in dizionario.values():
             dizionario[par[i]]=cod[i] #se ne il caratere ne il numero corrispondente sono nel dizionario ve li aggiunge
             i+=1
        elif par[i] in dizionario.keys() and dizionario[par[i]]==cod[i]: #se il 
             i+=1 #se il carattere è nel dizionario e corrisponde allo stesso numro, sia all'indice di cod sia nel dizionario passa al char successivo.
        else:
             lista[-1:]=[] #in caso contrario rimuove la parola dalla lista di ritorno
             break

