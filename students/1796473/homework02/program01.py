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


def get_id(line):
    return int(line.replace(" ", "")[len(tag):])


def to_dict(posts):
    d = {}
    global tag
    tag = "<POST>"
    lines = posts.splitlines()
    id = get_id(lines[0])
    post = ""
    for i in range(1, len(lines)):
        if lines[i].replace(" ", "")[:len(tag)] == tag:
            d[id] = post
            id = get_id(lines[i])
            post = ""
        else:
            post += lines[i] + "\n"
    d[id] = post
    return d

def post(fposts, insieme):
    file = open(fposts, "r")
    fposts = file.read()
    file.close()
    posts = to_dict(fposts)
    risultato = set()
    for id, post in posts.items():
        post = post.lower()
        for parola in insieme:
            parola = parola.lower()
            i = 0
            for c in post:
                if i == len(parola):
                    if c.isalpha():
                        i = 0
                    else:
                        risultato.add(str(id))
                        break
                        
                if not c.isalpha():
                    i = 0
                    continue
                    
                if i == -1:
                    continue
                    
                if c == parola[i]:
                    i += 1
                else:
                    i = -1
            else:
                if i == len(parola):
                    risultato.add(str(id))
                continue
            break
    return risultato