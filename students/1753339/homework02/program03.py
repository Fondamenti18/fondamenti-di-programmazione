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

def posizione(codice):
    '''questa funzione ritorna una lista di tupla,
    formate dalle coppie cifra-posizione (in codice)'''
    app = []
    c = len(codice)
    pos = []
    tupla = ()
    for i in range(c):
        app.append(i)
    for cifra,x in zip(codice,app):
        tupla = (cifra,x)
        pos.append(tupla)
    return(pos)

def occorrenza(codice):
    #questa funzione ritorna un dizionario che ha come chiave una cifra di codice e come valore associato l'occorrenza della cifra stessa
    diz = {}
    for cifra in codice:
        occ = codice.count(cifra)
        diz[cifra] = occ
    return(diz)

def ricerca(diz,pos):
    '''questa funzione restituisce una lista contenente liste di cifre uguali in codice'''
    matr = []
    for key in diz.keys():
        k = []
        if diz[key] >= 1:
            for tupla in pos:
                if tupla[0] == key:
                    k.append(tupla[1])
        matr.append(k)
    return(matr)

def decod(pfile, codice):
    '''inserire qui il codice'''

    # apro il file
    with open(pfile,'r') as f:
        parole = f.read()

    c = len(codice)
    # calcolo il numero di cifre nel codice

    l_parole = parole.splitlines()
	# creo una lista che ha per elementi le singole parole

    l_len = []
    # andrò a mettere in l_new le parole che hanno lunghezza esattamente uguale a c (lunghezza del codice)
    for parola in l_parole:
        if len(parola) == c:
            l_len.append(parola)

    # creo liste/dizionari, che mi serviranno per arrivare al risultato finale, tramite le funzioni definite fuori da decod
    pos = posizione(codice)
    diz_occ = occorrenza(codice)
    matr = ricerca(diz_occ, pos)

    rit = []
    # rit è la lista che devo ritornare (sarà poi portato in set)
    for word in l_len:
        rit.append(word)
        # aggiungo la parola alla lista che devo ritornare
        i_app = [] # i_app mi serve per tenere traccia delle lettere già incontrate nella word considerata
        for lista in matr:
            app = []
            for i in lista:
                c = word[i]
                app.append(c)
                app2 = app
            app2 = set(app)
            if len(app2) == 1 and app2 not in i_app:
                # se la lunghezza dell'insieme app2 è = 1 allora significa che tutte le lettere (delle posizioni considerate)
                # sono uguali e se non sono in i_app significa che non ci sono lettere uguali in posizioni diverse
                # A CIFRE DIVERSE CORRISPONDONO LETTERE DIVERSE!
                i_app.append(app2)
                continue
            else:
                # se una delle due condizioni nell'if non si verifica, significa che la parola NON deve essere ritornata, percui
                # la tolgo dall'insieme risultato ( per ora lista)
                rit.remove(word)
                break
            break

    rit = set(rit)
    return(rit)

