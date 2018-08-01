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
    with open(pfile, 'r') as file:
        parole = file.readlines()


    paroleLungheN = []
    for parola in parole:
        if len(parola) == len(codice) + 1:
            paroleLungheN.append(parola[:-1])

    risultati = set()


    for parola in paroleLungheN:
        # azzero le associazioni per QUESTA parola nel ciclo
        associazioni = {}
        # per ogni tupla (i, lettera) nella parola
        for i, lettera in enumerate(parola):
            # mi assicuro che codice[i] ('1', '2', '1') non sia
            # gia presente nelle chiavi e che
            # la lettera non sia gia presente nei valori
            if not codice[i] in associazioni.keys() and lettera not in associazioni.values():
                # allora posso creare un record nella tabella delle associazioni
                associazioni[codice[i]] = lettera

        s = ''
        # "s" mi serve per ricostruire la parola
        # se ricostruendola vedo che ha subito modifiche, vuol dire che
        # non ha rispettato la codifica.

        for c in codice:
            # se la parola possiede lettere che in fase di codifica
            # non hanno ricevuto un indice associato,
            # allora salto il ciclo, perche se questa lettera non ha un
            # numero associato non posso ricostruire la parola
            if not c in associazioni.keys():
                continue
            else:
                # appendo a s il valore associato all'indice numerico
                s += associazioni[c]
        # se riottengo la parola stessa anche dopo la decodifica
        # ho ricostruito bene la parola e posso aggiungerla al set finale
        if parola == s:
            risultati.add(s)

    return risultati




