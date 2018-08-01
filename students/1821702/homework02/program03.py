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
def codifica(struttura,parola,risultato):
    lettere = []
    numeri = []
    diz = {}
    c = ''
    for x in parola:
        if x not in lettere:
            lettere.append(x)
    for y in struttura:
        if y not in numeri:
            numeri.append(y)
    if len(lettere) == len(numeri):
        for i in range(len(lettere)):
            diz[lettere[i]] = numeri[i]
        for l in parola:
            c = c + diz[l]
        if c == struttura:
            risultato.add(parola)
    return risultato
    
def controllo(stringa):
    for i in stringa:
        if i.isnumeric() == False:
            return i.isnumeric()
    return i.isnumeric()

def pulizia(parola):
    c = ''
    for i in parola:
        if i.isalpha():
            c += i
        else:
            return c
    return c
    
def decod(pfile, codice):
    cont = controllo(codice)
    if cont == True:
        risultato = set()
        f = open(pfile)
        while 1:
            parola = f.readline()
            parola = pulizia(parola)
            if parola == "":
                break
            elif len(parola) == len(codice):
                codifica(codice,parola,risultato)
                continue
            else:
                continue
    else:
        return 'la struttura deve essere solo numerica'
    return risultato
    

