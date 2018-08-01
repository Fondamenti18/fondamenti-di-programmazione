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

import re, string

def post(fposts,insieme):
    ''' implementare qui la funzione'''
    return get_text(fposts, insieme)


def n(w):
    for p in string.punctuation:
        w = w.replace(p, ' ')
    return w.lower().strip()

def get_post(filename):
    text_formatted = ""
    l = []
    with open(filename, mode='r', encoding='utf-8') as file:
        for linea in file:
            text_formatted += re.sub('\s+', ' ', linea) if linea.rstrip() else ""
    for testo in text_formatted.split('<POST>'):
        #testo = testo.lstrip().lower()
        #testo = re.sub(r'(?<=\d)[,\.]','', testo)
        #print(testo)
        testo = n(testo)
        testo = l.append(testo.split(' ', 1))
    return l

def get_text(filename, testo):
    p = get_post(filename)
    r = []
    for parola in testo:
        is_alpha(parola)
        for k, v in enumerate(p):
                try: 
                    if parola.lower() in v[1].split():
                        r.append(v[0])
                except IndexError:
                    pass
    return set(r)
def test(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def is_in_text(word, txt):
    rx = r'\b{0}\b'.format(re.escape(word))
    return True if re.search(rx, txt) else False

def is_alpha(w):
    if w.isalpha() is False:
            return
            