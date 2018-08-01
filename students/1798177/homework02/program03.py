# Abbiamo una stringa i cui elementi sono cifre tra '0' e '9' (comprese) che
# rappresenta la struttura di una parola. La parola contiene al piu' 10 lettere
# diverse (ma puo' essere piu' lunga di 10 lettere se alcune sono ripetute), e
# la struttura si ottiene dalla parola sostituendo ciascuna lettera con una
# cifra, secondo le regole:
#   - a lettera uguale corrisponde cifra uguale
#   - a lettere diverse corrispondono cifre diverse
#
# Esempio: 'cappello' -> '93447228'
# Esempio: 'cappello' -> '12334556'
#
# Sia data una "struttura" ed un insieme di parole.
# Vogliamo ottenere il sottoinsieme delle parole date compatibili con la
# struttura data.
#
# Esempio: se la struttura e' '1234' e le parole sono { 'cane', 'gatto', 'nasa',
# 'oca', 'pino'} le parole dell'insieme che sono compatibili con la struttura
# sono {'pino', 'cane'}
#
# Scrivere una funzione decod( pfile, struttura) che prende in input:
#   - il percorso di un file (pfile), contenente testo organizzato in righe
#     ciascuna composta da una sola parola
#   - una stringa di almeno 1 carattere, composta solo da cifre (la struttura
#     delle parole da cercare)
# La funzione deve restituire l'insieme delle parole di pfile che sono
# compatibili con la struttura data.
#
# Per gli esempi vedere il file grade03.txt
#
# AVVERTENZE:
#   - non usare caratteri non ASCII, come le lettere accentate;
#   - non usare moduli che non sono nella libreria standard.
# NOTA: l'encoding del file e' 'utf-8'
# ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di
# quel test e' zero.
#
# Svolto da Emanuele Petriglia.

def get_struct(word):
    '''Data una parola ritorna la sua forma normalizzata.

    Esempi:
    >>> get_struct('cappello')
    01223445
    >>> get_struct('93447228')
    01223445
    '''
    word = word.replace('\n', '')

    return ''.join(map(lambda char: str(word.index(char)), word))

def get_set(lines, code):
    '''Ritorna un insieme composto dalle parole corrispondenti alla struttura
    'code' data presenti in 'lines'.
    '''
    len_code = len(code)
    code = get_struct(code)

    # Queste funzioni anonime servono per il filtraggio successivo.
    check_len = lambda word: len(word[:-1]) == len_code
    check_struct = lambda word: get_struct(word[:-1]) == code

    # 1. Si filtrano le parole di stessa lunghezza con la struttura.
    words = set(filter(check_len, lines))

    # 2. Si filtrano le parole con la stessa struttura.
    words = set(filter(check_struct, words))

    # 3. Si rimuove il carattere newline dalle parole restanti.
    return set(map(lambda word: word[:-1], words))

def decod(pfile, codice):
    # Non si controlla se il file è stato aperto perchè il grader inserisce
    # file esistenti e con il percorso giusto.
    pfile = open(pfile)

    result = get_set(pfile, codice)

    pfile.close()

    return result
