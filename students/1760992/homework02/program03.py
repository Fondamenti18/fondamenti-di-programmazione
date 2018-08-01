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


import re
import string
def decod(pfile, codice):   
    in_file = open(pfile,"r")
    testo = in_file.read()
    in_file.close()

    testo=testo.split()
    lun_cod=len(codice)
    y=[]
    for parola in testo:
        if len(parola)==lun_cod:
            risultato=confronto(parola,codice)
            if risultato == True:
                y.append(parola)
    insieme_parole=set(y)            
    return insieme_parole
                





def confronto(parola,codice):
    cp=[]
    cs=[]
    r=''
    r.join(parola)
    i=0
    while i < len(parola):
        cp=pos(parola,parola[i])
        cs=pos(codice,codice[i])
        if cp != cs:
            return False
        i=i+1

    return True
        
        




def pos(parola,c):
    position=[]
    i=0
    while i < len(parola):
        if parola[i] == c:
            position.append(i)
        i=i+1

    return position
