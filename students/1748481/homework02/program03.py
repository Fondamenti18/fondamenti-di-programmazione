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
def lunghezza(l, c): #funzione per escludere le parole con lunghezza diversa dallo schema del codice
    l1=[]
    for word1 in l: #ciclo per
        if len(c)==len(word1):
            l1.append(word1)
    return(l1)

def clear(r):
    l=[]
    for word in r: #ciclo for per pulire le parole dai caratteri non alfabetici
        if "\n" in word:
            word=word.replace("\n", "")
            l.append(word)
    return(l)

def conf(l, c):
    #ora devo ricostruire le parole tramite dizionario e confrontarle con le parole nella lista
    #se sono uguali allora ggiongo word1 alla lista di appoggio, altrimenti ignoro la parola e vado avanti
    stringa=''
    ris=[]
    for word in l:
        diz={}
        for let in word:
            for n in c:
                if n not in diz.keys() and let not in diz.values():
                    diz[n]=let
        for n1 in c:
            if n1 in diz.keys():
                stringa+=diz[n1]
        if stringa==word:
            ris.append(word)
            stringa=''
        else:
            stringa=''
    return(ris)

def decod(pfile, codice):
    '''inserire qui il codice'''
    riga=[]
    with open(pfile, 'r', encoding='utf-8') as fp:
        for word in fp:
            riga.append(word)
    l=[]
    l1=[]
    r=[]
    l=clear(riga)
    l1=lunghezza(l, codice)
    r=conf(l1, codice)
    return(set(r))
