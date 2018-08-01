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

def createAssociation(word, codice):
    #Prende in input una parola ed una codifica associando in un dizionario 
    #ogni lettera ad un numero del codice in base al numero delle loro occorrenze
    Relations={}
    index=0
    LenWord=len(word)
    while index<LenWord:
        if word[index] not in Relations:
            CharCount=word.count(word[index])
            CodeCount=codice.count(codice[index])
            if CharCount==CodeCount:
                Relations[word[index]]=codice[index]
        index=index+1
    return Relations


def compare(word, codice, MyCoding):
    #Prende in input una parola, una codifica in numeri e un dizionario di 
    #codifica. Compara la parola ed il codice e ritorna True o False in base 
    #alla loro compatibilità
    index=0
    LenCode=len(codice)
    while index<LenCode:
        if MyCoding.get(word[index])!=codice[index]:
            return False
        index=index+1
    return True


def decod(pfile, codice):
    with open(pfile, 'r') as f:
        Words=f.read()
    
    #Variabili utili
    MyWords=Words.split("\n")
    Compatible=set()
    LenCode=len(codice)
    #Iterazione
    for word in MyWords:
        if len(word)==LenCode:
            MyCoding=createAssociation(word,codice)
            if compare(word, codice, MyCoding)==True:
                Compatible.add(word)
    return Compatible


