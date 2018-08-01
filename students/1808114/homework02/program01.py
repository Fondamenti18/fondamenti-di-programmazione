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
import sys

def find_id(string):
    i = 0
    strid = ""
    while True:
        if string[i].isdigit():
            strid += string[i]
            i += 1
        else: break
    return strid

def space_rmv(lst, t = 0):
    lst = lst.split(' ')
    while True:
        if lst[0] == '' and len(lst) > 1:
            del lst[0]
        else: break
    return " ".join(lst)

def confronto(post, ins):
    i = 0
    while i < len(ins) and len(post) >= len(ins[i]):
        n = post.find(ins[i])
        if n > -1:
            if (not post[n-1].isalpha()) and (not post[n+len(ins[i])].isalpha()):
                return False
            elif not confronto(post[n+1:], ins):
                return False
        i += 1
    return True

def post(fposts,insieme):
    ''' implementare qui la funzione'''
    sys.setrecursionlimit(3500)
    f = open(fposts,"r",encoding="utf-8")
    content = f.read().replace("\n", " ").split("<POST>")
    lst = list(insieme)
    for c in range(len(lst)):
        lst[c] = lst[c].lower()
    listout = []
    c = 0
    while c < len(content):
        content[c] = space_rmv(content[c])
        content[c] = content[c].lower()
        if confronto(content[c], lst):
            del content[c]
        else:
            listout.append(find_id(content[c]))
            c += 1
    ins=set(listout)
    f.close()
    return ins