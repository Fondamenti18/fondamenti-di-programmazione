# Un  file di compiti contiene informazioni su un insieme di compiti da
# eseguire. Esistono  due tipologie di compiti:
#   - compiti che possono essere eseguiti indipendentemente dagli altri.
#   - compiti da svolgere solo al termine di un compito preliminare.
#
# I compiti del primo tipo sono codificati nel file mediante una linea che
# contiene in sequenza le due sottostringhe "comp" ed "N" (senza virgolette)
# eventualmente inframmezzate, precedute e/o seguite da spazi. "N" è l'ID del
# compito (un numero positivo).
# Compiti del secondo tipo sono codificati nel file mediante due linee di
# codice.
#   -- la prima  linea, contiene in sequenza le due sottostringhe "comp" ed "N"
#      (senza virgolette) eventualmente inframmezzate, precedute e/o seguite da
#      spazi. "N" è l'ID del compito (un numero positivo).
#   -- la seconda linea (immediatamente successiva nel file) contiene in
#      sequenza le due sottostringhe "sub" ed "M" (senza virgolette)
#      eventualmente inframmezzate, precedute e/o seguite da spazi. "M" è l'ID
#      del compito preliminare.
#
# Il seguente file di compiti contiene informazioni su 4 compiti (con
# identificativi 1, 3, 7 e 9). I compiti con identificativi 1 e 9 possono essere
# svolti indipendentemente dagli altri mentre i compiti con identificativo 3 e 7
# hanno entrambi un compito preliminare.
#
# comp 3
#  sub 9
#        comp1
# comp              9
#    comp 7
# sub3
#
# Scrivere la funzione pianifica(fcompiti, insi, fout) che prende in input:
#   - il percorso di un file (fcompiti)
#   - un insieme  di ID di compiti da cercare (insi)
#   - ed il percorso di un file (fout)
# e che salva in formato JSON nel file fout un dizionario (risultato).
#
# Il dizionario (risultato) dovrà contenere come chiavi gli identificativi (ID)
# dei compiti presenti in fcompiti e richiesti nell'insieme insi. Associata ad
# ogni ID x del dizionario deve esserci una lista contenente gli identificativi
# (ID) dei compiti che bisogna eseguire prima di poter eseguire il compito x
# richiesto (ovviamente la lista di un ID di un compito che non richide un
# compito preliminare risulterà vuota ). Gli (ID) devono comparire nella lista
# nell'ordine di esecuzione corretto, dal primo fino a quello precedente a
# quello richiesto (ovviamente il primo ID di una lista non vuota corriponderà
# sempre ad un compito che non richiede un compito preliminare).
#
# Si può assumere che:
#    - se l' ID di un compito che richieda un compito preliminare è presente
#      in fcompiti allora anche l'ID di quest'ultimo è presente in fcompiti
#    - la sequenza da associare al compito ID del dizionario esiste sempre
#    - non esistono cicli (compiti che richiedono se stessi anche
#      indirettamente)
#
# Ad esempio per il file di compiti fcompiti contenente:
#
# comp 3
#  sub 9
#        comp1
# comp              9
#    comp 7
# sub3
#
# al termine dell'esecuzione di  pianifica(fcompiti,{'7','1','5'}, 'a.json')
# il file 'a.json' deve contenere il seguente dizionario {'7':['9','3'],'1':[]}
#
# Per altri esempi vedere il file grade02.txt
#
# AVVERTENZE:
#   - non usare caratteri non ASCII, come le lettere accentate;
#   - non usare moduli che non sono nella libreria standard.
# NOTA: l'encoding del file e' 'utf-8'
# ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio
# di quel test e' zero.
#
# Svolto da Emanuele Petriglia

from re import compile
from json import dump
from collections import deque

def get_dict(text):
    '''Ritorna un dizionario composto dai compiti come chiave e dalle
    dipendenze (non risolte) come attributo. Nel caso un compito non ha
    nessuna dipendenza l'attributo ha valore None.
    '''
    # Spiegazione regex:
    # (?= <- Positive Lookahead, ossia asserisce che ESISTA questo gruppo;
    #    comp <- Cerca la parola comp
    #    \s* <- Dopo la parola "comp" ci sono spazi (zero o più);
    #    (?P<comp> <- Gruppo catturante di nome "comp";
    #             \d+ <- Cattura una o più cifre (l'id);
    #    ))
    # (?: <- Gruppo non catturante;
    #    .+? <- Uno o più posizioni (qualsiasi carattere);
    #    \n  <- Esattamente il carattere newline;
    #    ){1} <- Trova UNA sola corrispondenza;
    # (?:
    #    \s*
    #    sub <- Esattamente la parola "sub"
    #    \s*
    #    (?P<sub>
    #            \d+
    #    ))? <- Questo gruppo può esistere zero od una volta.
    #
    # Effetto regex: con il metodo findall restituisce tuple composte dal primo
    # elemento che è l'id del compito, mentre il secondo elemento è l'id della
    # dipendenza.
    superpowers = compile(
        r"(?=comp\s*(?P<comp>\d+))(?:.+?\n){1}(?:\s*sub\s*(?P<sub>\d+))?")

    return dict(superpowers.findall(text))

def pianifica(fcompiti,insi,fout):
    jobs = get_dict(open(fcompiti).read())

    # Rimuove gli ID che non esistono.
    insi = set(filter(lambda job: job in jobs, insi))

    def gen_deps(job):
        '''Sviluppa le dipendenze di un compito passato come argomento,
        ritornando una tupla composta dalla chiave (il compito) ed una lista
        di dipendenze.
        '''
        sub = jobs[job]
        deps = deque() # Deque permette l'accesso rapido in testa ed in coda.

        while sub:
            deps.appendleft(sub)
            sub = jobs[sub]

        return job, list(deps)

    final_jobs = dict(map(lambda job: gen_deps(job), insi))

    dump(final_jobs, open(fout, "w"))

# Nota: l'uso delle regex rallenta leggermente il tempo di esecuzione, perchè
# il modulo 're' è poco ottimizzato.