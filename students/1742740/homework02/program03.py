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
def analizza(parola,codice):
        dizionario={}
        if len(parola)!=len(codice): #torna false se la lunghezza della parola non e' uguale a quella del codice di analizzare
            return False
        else:
            for c in range(len(parola)): #ciclo che pone come chiave nel dizionario il numero in codice e gli assegna la lettera corrispondente in parola
                if codice[c] not in dizionario.keys() and parola[c] not in dizionario.values():
                    dizionario[codice[c]]=parola[c]
                elif codice[c] in dizionario.keys() and dizionario[codice[c]]==parola[c]:
                    continue
                else:    #se prova a sostituire la lettera assegnata al numero con una diversa ritorna false
                    return False
                    break
        return True #se la parola ha stessa struttura di codice ritorna true


def decod(pfile, codice):
    with open(pfile,encoding='utf-8') as doc: #apre il file
        testo=doc.read()
        parole=testo.split() #crea una lista con le parole in testo
        risultato=[]
        for parola in parole:
            if analizza(parola,codice): #usa analizza su tutte le parole
                risultato.append(parola) #aggiunge la parola per cui analizza ritorna true in risultato
            else:
                continue
        return set(risultato)



