"""
I post di un forum sono raccolti in alcuni file che hanno il seguente formato. 
Un file contiene uno o piu' post, l'inizio di un post e' marcato da una linea che contiene
in sequenza le due sottostringhe "<POST>" ed "N" (senza virgolette) eventualmente 
inframmezzate, precedute e/o seguite da 0,1 o piu' spazi. 
"N" e' l'ID del post (un numero positivo).  
Il conte(si veda ad esempinuto del post e' nelle linee successive fino alla linea che marca il prossimo post
o la fine del file o il file "file01.txt").
E' assicurato che la stringa "<POST>" non e' contenuta in nessun post.

Nel seguito per parola intendiamo come al solito una qualsiasi sequenza di caratteri
alfabetici di lunghezza massimale. I caratteri alfabetici sono quelli per cui
ritorna True il metodo isalpha().

Scrivere una funzione post(fposts,insieme) che prende in input:
- il percorso di un file (fposts) 
- ed un insieme  di parole (insieme)
e che restituisce un insieme (risultato).

L'insieme restituito (risultato) dovra' contenere gli identificativi (ID) dei post 
che contengono almeno una parola dell'insieme in input.
Due parole sono considerate uguali anche se  alcuni caratteri alfabetici compaiono in una 
in maiuscolo e nell'altra in minuscolo.

Per gli esempi vedere il file grade.txt

AVVERTENZE:
    non usare caratteri non ASCII, come le lettere accentate;
    non usare moduli che non sono nella libreria standard.
NOTA: l'encoding del file e' 'utf-8'
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero.
"""

import re

POST_REX = re.compile(r"(?P<ID>\d+)\s*(?P<TEXT>[\s\S]+)")
ALPHA_CHAR = re.compile(r"[^a-z]+")


def post(fposts, insieme):
    all_text = open(fposts).read()
    raw_posts = all_text.split("<POST>")
    del raw_posts[0]

    insieme = {x.lower() for x in insieme}

    result = set()
    for post_text in raw_posts:
        post_match = POST_REX.search(post_text.lower())
        if post_match:
            post_id, text = post_match.group(1, 2)

            if set(ALPHA_CHAR.sub(" ", text).split()) & insieme:
                result.add(post_id)

    return result
