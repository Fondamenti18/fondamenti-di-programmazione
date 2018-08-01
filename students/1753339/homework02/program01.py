'''
I post di un forum sono raccolti in alcuni file che hanno il seguente formato. 
Un file contiene uno o piu' post, l'inizio di un post e' marcato da una linea che contiene
in sequenza le due sottostringhe "<POST>" ed "N" (senza virgolette) eventualmente 
inframmezzate, precedute e/o seguite da 0,1 o piu' spazi. 
"N" e' l'ID del post (un numero positivo).  
Il contenuto del post e' nelle linee successive fino alla linea che marca il prossimo post 
o la fine del file (si veda ad esempio il file "file01.txt"). 
E' assicurato che la stringa "<POST>" non e' contenuta in nessun post.

Nel seguito per parola intendiamo come al solito una qualsiasi sequenza di caratteri
alfabetici di lunghezza massimale. I caratteri alfabetici sono quelli per cui
ritorna True il metodo isalpha().

Scrivere una funzione post(fposts,insieme) che prende in input:
- il percorso di un file (fposts) 
- ed un insieme  di parole (insieme)
e che restituisce un insieme (risultato).

L'insieme restituito (risultato) dovra' contenere gli identificativi (ID) dei post 
che contengono almeno una parola dell'inseme in input.
Due parole sono considerate uguali anche se  alcuni caratteri alfabetici compaiono in una 
in maiuscolo e nell'altra in minuscolo.

Per gli esempi vedere il file grade.txt

AVVERTENZE:
	non usare caratteri non ASCII, come le lettere accentate;
	non usare moduli che non sono nella libreria standard.
NOTA: l'encoding del file e' 'utf-8'
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero.
'''


def controllo(elem):
    # controllo: funzione che contolla che l'elemento sia composto da caratteri alfabetici
    l_corr = []
    # utilizzo una lista di appoggio
    for lettera in elem:
        if lettera.isalpha() == True:
            l_corr.append(lettera)
        else:
            break
    elem = ''.join(l_corr)
    elem = elem.lower()
    return (elem)

def associa(l_posts):
    ''' questa funzione associa ad ogni ID le parole del post corrispondente'''
    diz = {}
    for stringa in l_posts:
        lst = stringa.split()
        words = ''
        if lst == []:
            continue
        else:
            ident = lst[0]
            words += stringa
            diz[ident] = words
    return diz

def matrice(diz):
    '''questa funzione crea una matrice che contiene i post, ed ogni post contiene le parole splittate (qui ho ancora i tutti i tipi di carattere)'''
    matr = []
    for val in diz.values():
        matr.append(val.split())
    return matr


def post(fposts, insieme):
    ''' implementare qui la funzione'''
    # apro il file di input, assegnandogli il nome txt
    with open(fposts, 'r') as f:
        txt = f.read()

    # porto a minuscole tutte le lettere dell'insieme di confronto dato in input dato che non bisogna fare distinzioni tra maiuscole e minuscole
    insieme_a = []
    for parola in insieme:
        parola1 = parola.lower()
        insieme_a.append(parola1)
    insieme = insieme_a

    l_posts = txt.split('<POST>')

    # diz è un dizionario che ha come chiavi gli ID dei post e come valori associati i post corrispondeti
    diz = associa(l_posts)
    matr = matrice(diz)
    # controllo mediante la funzione definita esternamente quali elementi posso accettare e quali no mediante la lista rit, che verrà
    # poi modificata in un insieme
    rit = []
    for post in matr:
        for el in post:
            el = controllo(el)
            for parola in insieme:
                ris = post[0]
                if el == parola:
                    rit.append(ris)
    rit = set(rit)
    return rit

