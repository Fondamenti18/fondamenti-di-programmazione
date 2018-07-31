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
def controllo(parola,codice):
    ''' questa funzione verifica la validità della parola '''
    insieme=set() # contiene i numeri già esaminati
    for i,c in enumerate(codice):
        if parola[i].isalpha(): # se il carattere è alfabetico vuol dire che non è stato ancora mai incontrato nella parola
            if not c in insieme:
                g=parola[i] # per prima cosa mi salvo il valore del carattere
                parola=parola.replace(g,c) # sostituisco tutte le occorrenze di quel carattere
            insieme.add(c) # aggiungo il carattere all'insieme dei caratteri già letti
    if parola==codice: return True # a questo punto mi ritrovo con la parola scritta uguale al cdice se è esatta
    return False

def decod(pfile, codice):
    '''inserire qui il codice'''
    ret=set()
    with open(pfile,'r') as f:
        p=len(codice)
        contenuto=[x for x in f.read().split('\n') if len(x)==p] # leggo dal file solo le parole con lunghezza uguale alla lunghezza del codice
        for parola in contenuto:
            if controllo(parola,codice):
                    ret.add(parola)
        return ret














