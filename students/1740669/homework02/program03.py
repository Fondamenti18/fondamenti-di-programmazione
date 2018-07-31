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


def conta_cifre(codice):
    occorrenze_cifra = {}
    lista_occorrenze_cifre = []
    for cifra in (codice):
        occorrenze_cifra[cifra] = codice.count(cifra)           #contatore occorrenze cifra
    lista_occorrenze_cifre = list(occorrenze_cifra.values())    #conversione dict in lista
    return lista_occorrenze_cifre


def conta_lettere(parola):
    occorrenze_lettera = {}
    lista_occorrenze_lettere = []
    for lettera in (parola):
        occorrenze_lettera[lettera] = parola.count(lettera)     #contatore occorrenze cifra
    lista_occorrenze_lettere = list(occorrenze_lettera.values())#conversione dict in lista
    return lista_occorrenze_lettere


def decod (pfile,codice):
    parole_compatibili = []
    occorrenze_codice = []
    occorrenze_parola = []
    Input_file = open (pfile,'r')                       #apertura file
    while 1:
        parola_completa = Input_file.readline()         #legge il contenuto della linea
        parola = parola_completa.rstrip()               #elimina il carattere \n che manda a capo
        if parola == "":				#parola vuota = fine file
            break					# esco dal while
        occorrenze_codice = conta_cifre(codice)	        # conta occorrenze cifre nel codice
        occorrenze_parola = conta_lettere(parola)       # conta occorrenze lettera in parola
        if occorrenze_codice == occorrenze_parola:
            parole_compatibili.append(parola)		#inserimento parola nella lista
    Input_file.close()
    elenco_parole = set(parole_compatibili)
    return elenco_parole

    





