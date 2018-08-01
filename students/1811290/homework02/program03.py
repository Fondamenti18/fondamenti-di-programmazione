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

import string
def decod(pfile, codice):
    '''inserire qui il codice'''
    a=open(pfile,encoding='utf-8')
    elementi_trovati = []
    #Mi creo lista di numeri univoci del codice che mi serve dopo
    codice_univoco=""
    for k in range (0,len(codice)):
        if codice_univoco.find(codice[k])==-1:
            codice_univoco+=(codice[k])
    #Esamino linea per linea
    for linea in a:
        linea_pulita=""
        lettera_univoca=""
        linea_pulita=linea.rstrip(chr(10)) #levo il carattere di fine riga
        for k in range (0,len(linea_pulita)):
            # verifico se il carattere gia esiste,nel caso lo aggiungo
            if lettera_univoca.find(linea[k])==-1:
                lettera_univoca+=(linea[k])

        #Esamino solo le linee ove il numero di elementi diversi (univoci) della struttura e della linea sono uguali.
        if len (lettera_univoca)==len(codice_univoco):
            tabella_di_traduz = linea_pulita.maketrans(lettera_univoca,codice_univoco)
            parola_codificata = linea_pulita.translate (tabella_di_traduz)
            if parola_codificata==codice:
                elementi_trovati.append(linea_pulita)

    return set(elementi_trovati)            


