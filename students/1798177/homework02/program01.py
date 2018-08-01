# I post di un forum sono raccolti in alcuni file che hanno il seguente formato.
# Un file contiene uno o più post, l'inizio di un post è marcato da una linea
# che contiene in sequenza le due sottostringhe "<POST>" ed "N" (senza
# virgolette) eventualmente inframmezzate, precedute e/o seguite da 0,1 o più
# spazi. "N" è l'ID del post (un numero positivo).
#
# Il contenuto del post è nelle linee successive fino alla linea che marca il
# prossimo post o la fine del file (si veda ad esempio il file "file01.txt").
#
# E' assicurato che la stringa "<POST>" non e' contenuta in nessun post.
#
# Nel seguito per parola intendiamo come al solito una qualsiasi sequenza di
# caratteri alfabetici di lunghezza massimale. I caratteri alfabetici sono
# quelli per cui ritorna True il metodo isalpha().
#
# Scrivere una funzione post(fposts,insieme) che prende in input:
#   - il percorso di un file (fposts)
#   - ed un insieme  di parole (insieme)
# e che restituisce un insieme (risultato).
#
# L'insieme restituito (risultato) dovrà contenere gli identificativi (ID) dei
# post che contengono almeno una parola dell'inseme in input.
#
# Due parole sono considerate uguali anche se alcuni caratteri alfabetici
# compaiono in una in maiuscolo e nell'altra in minuscolo.
#
# Per gli esempi vedere il file grade.txt
#
# AVVERTENZE:
#   - non usare caratteri non ASCII, come le lettere accentate;
#   - non usare moduli che non sono nella libreria standard.
# NOTA: l'encoding del file e' 'utf-8'
# ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio
# di quel test e' zero.
#
# Svolto da Emanuele Petriglia.

from re import compile, IGNORECASE, DOTALL

def get_posts(posts, word):
    '''Ritorna un insieme composto dagli ID dei post dove compare la parola
    contenuta in word, in modod case insensitive.
    '''
    # Spiegazione Regex
    #
    # Note preliminari: "r" serve per indicare che la stringa è in formato raw,
    # ossia non gestisce i "\", inoltre word[::-1] restituisce la parola
    # specchiata.
    #
    # Regex:
    # (?: <- Gruppo non bloccante, ossia non viene mostrato.
    #    \b <- Asserzione che garantisce che non ci siano caratteri alfanumerici
    #      parola <- Parola da cercare specchiata (es "Si"->"iS")
    #    \b)
    # (?:
    #    .+? <- Qualsiasi carattere, almeno uno o più
    #    (\d+) <- Due cifre numeriche, salvate in un gruppo (ossia l'ID)
    #    \s* <- Qualsiasi spazio bianco, almeno zero o più
    #    >TSOP<) <- Si ferma quando incontra questa parola, ossia "<STOP>".
    #
    # Parametri: IGNORECASE (case insensitive) e DOTALL (ossia conta gli "\n").
    #
    # Effetto: ritorna un insieme con gli ID dei post in cui c'è la parola da
    # trovare (attenzione, l'ID è specchiato!).
    superpowers = compile(r"(?:\b" + word[::-1] + r"\b)(?:.+?(\d+)\s*>TSOP<)",
                          IGNORECASE | DOTALL)

    return set(superpowers.findall(posts))

def post(fposts, insieme):
    # Ritorna il testo di un file specchiato. Non si controlla se il file esiste
    # perchè il grader ce lo garantisce.
    posts = open(fposts).read()[::-1]

    result = set()

    # La lista di ritorno viene scartata.
    list(map(lambda word: result.update(get_posts(posts, word)), insieme))

    # Ogni ID rovesciato viene rimesso a posto (vedere "get_posts(...)").
    return set(map(lambda reversed_id: reversed_id[::-1], result))

# L'uso delle regex comporta un rallentamento dell'esecuzione perchè il modulo
# 're' è poco ottimizzato.
