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
    file=open(pfile,"r")
    righefile=file.readlines()
    for i in range(0,len(righefile)):
        righefile[i]=righefile[i].replace("\n","")
    insiemeout=set()
    for i in righefile:
        parolagiusta=True
        numeri={}
        dizionario={}
        if len(i)!=len(codice):
            continue
        for j in range(0,len(codice)):
            if i[j] not in dizionario and codice[j] not in numeri:
                dizionario[i[j]]=codice[j]
                numeri[codice[j]]=i[j]
            elif i[j] in dizionario and codice[j] in numeri:
                if i[j]==numeri[codice[j]] and codice[j]==dizionario[i[j]]:
                    continue
                else:
                    parolagiusta=False
            else:
                    parolagiusta=False
        if parolagiusta:
            insiemeout.add(i)
    return insiemeout
    
    
    
    
    




