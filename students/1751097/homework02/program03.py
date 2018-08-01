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
    lista_candidati = generaCandidati(pfile, codice)
    
    # se il codice non ha ripetibili ritorno subito la lista dei candidati
    if len(codice) == len(set(codice)): return set(lista_candidati)
    
    #print(lista_candidati)
    posizioni_multipli = lettereMultiple(codice)

    #print(posizioni_multipli)
    parole_corrette = cercaParoleCorrette(lista_candidati, posizioni_multipli)
    #print(parole_corrette)
    return parole_corrette
    
    
"""
questa funzione si studia il codice per ricavare le posizione di eventuali ripetizioni di lettere.
"""
def lettereMultiple(codice):
    posizioni_multipli = {}      # Inizializzo dizionario per numero-posizioni
    for numero in codice:        # ciclo cifre
        if codice.count(numero) > 1 and numero not in posizioni_multipli.keys():   # verifico ci sia piu di un occorrenza del carattere e che non abbia già elaborato la cifra
            lista_pos = []
            start = 0                # inizializzo lo start che andra ad aggiornarsi
            while True:
                pos = codice.find(numero, start)   # cerco le ripetizioni
                if pos != -1:                 
                    start = pos + 1               # aumento l inizio dal quale fare la ricerca
                    lista_pos.append(pos)         # salvo la posizione.
                else:
                    break                         # non ho trovato ripetizioni.
            posizioni_multipli[numero] = lista_pos
        
    return posizioni_multipli

"""
questa funzione genera la parole candidate a essere corrispondenti al codice input.
"""
def generaCandidati(pfile, codice):          # Mi trovo i candidati confrontando il codice con le parole. 
    len_codice_set=len(set(codice))
    len_codice=len(codice)
    with open(pfile, "r") as dati:
        lista_candidati = []
        for parola in dati:
             parola = parola.strip()         # ripulisco la stringa.
             if len(parola) == len_codice and len(set(parola)) ==  len_codice_set:   # Verifico lunghezza parole e codice.
                 lista_candidati.append(parola)                                      # Candidato trovato, aggiungo.
    return lista_candidati

"""
questa funzione mi restituisce le parole corrette rispetto al codice fornito, analizzando la lunghezza e posizione delle ripetizioni.
"""
def cercaParoleCorrette(lista_candidati, posizioni_multipli):    
    parole_corrette = set()                                     # inizializzo l' insieme di output delle parole corrette.
    for parola in lista_candidati:                              # Ciclo le parole ideali dai candidati.
        for posizione in posizioni_multipli.values():           # Ciclo li liste contenenti le posizioni delle ripetizioni.
            carattere = set()
            for x in posizione:                                 # Ciclo le singole posizioni della lista delle stesse.
                carattere.add(parola[x])                          # mi memorizzo il carattere della parola a quella posizione.
            if len(carattere) != 1:                               # parola non è valida 
                break
        else:            
            parole_corrette.add(parola)                        # scrivo parola
            
    return parole_corrette            



if __name__ == '__main__':
    args        = ('file03.txt','121')
    expected    = {'afa', 'ada', 'gag', 'sos', 'ere', 'ivi', 'aia', 'ala', 'iti', 'odo', 'ara', 'ava', 'imi', 'oro', 'ama', 'non', 'idi', 'oso'}
    returned    = decod(*args)
    print(returned)
    args        = ('file03.txt','3533939339')
    expected    = {'ninnananna'}
    explanation = "il secondo e' l'insieme corretto"
    returned    = decod(*args)
    print(returned)
    args        = ('file03.txt','138831')
    expected    = set()
    explanation = "il secondo e' l'insieme corretto"
    returned    = decod(*args)
    print(returned)
    args       = ('file03.txt','609155')
    expected   = {'aderii', 'soiree', 'kaputt', 'scalee', 'servii', 'dormii', 'fornii', 
        'spedii', 'lintee', 'barcee', 'prozii', 'cornee', 'chinee', 'ipogee', 'stonii', 
        'vitree', 'lambii', 'acquee', 'sparii', 'tropee', 'arguii', 'limnee', 'gradii', 
        'trabee', 'giudee', 'livree', 'nutrii', 'orwell', 'colpii', 'carnee', 'pendii', 
        'sorbii', 'cupree', 'guarii', 'mirtee', 'platee', 'svenii', 'morfee', 'pentii', 
        'partii', 'lignee', 'tradii', 'patrii', 'brucii', 'idonee', 'tornii', 'yankee', 
        'reagii', 'bypass', 'abolii', 'condii', 'nausee', 'ruglii', 'svolii', 'mentii', 
        'stupii', 'mazdee', 'pigmee', 'epizoo', 'gremii', 'raspii', 'scolii', 'glacee', 
        'lauree', 'refill', 'restii', 'sancii', 'seguii', 'lincee', 'glorii', 'spazii', 
        'gneiss', 'brusii', 'sentii', 'svanii', 'tarpee', 'ronzii', 'spurii', 'uvacee', 
        'contee', 'ghinee', 'ascree', 'bandii', 'dionee'}
    explanation = "il secondo e' l'insieme corretto"
    returned    = decod(*args)    
    print(returned)

