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



def getDictPost(filename):
    dictPost = {}
    id_post = None
    lista = []
    variabileControllo = '<POST>'
    for line in filename:
        line = line.lower()
        if variabileControllo.lower() in line:
            if id_post is not None and len(lista) > 0:
                dictPost[id_post] = lista
            id_post = line.split(variabileControllo.lower())[1].strip()
            lista = []
        else:
            if len(line.strip()) > 0:
                lista.append(line.strip())
    if len(lista) > 0:
        dictPost[id_post] = lista
    for key, value in dictPost.items():
        dictPost[key] = " ".join(value)
    return dictPost

def removeSpecialChar(parola):
    import re
    parola = re.sub(r"[^A-Za-z0-9]", " ", parola)
    return parola

def post(fposts,insieme):
    lista = []
    with open(fposts) as f:
        dictPost = getDictPost(f)
        for parola in insieme:
            parola = parola.lower()
            for key, value in dictPost.items():
                value = removeSpecialChar(value)
                value = value.split(" ")
                if parola in value:
                    lista.append(key)
        return set(lista)
    
 


