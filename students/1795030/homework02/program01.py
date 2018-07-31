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

from re import match

def post(fposts,insieme):
    s = no_spazi(fposts)
    s = lista(s)
    s = lista_in_l(s)
    m = []
    for el in insieme:
        for x in range(len(el)):
            if el[x].isupper():
                insieme.remove(el)
                insieme.add(el.replace(el[x], el[x].lower()))
    q = insieme
    for el in s:
        for x in el[1]:
            for i in q:
                if i in x:
                    if len(x) == len(i):
                        m.append(el[0])
                    else:
                        if not x[len(i)].isalpha():
                            m.append(el[0])
    for el in m:
        if m.count(el) > 1:
            m.remove(el)
    j = []
    for el in m:
        if el in range(0, 100):
            j.append(el.strip())
        else:
            j.append(el.replace('\n', '').strip())
    m = j
    ins = set(m)
    return ins
    


def lista(s):
    l = []
    for el in s:
        m = match('\d+', el)
        m1 = m.group(0)
        l.append([m1, el[len(m1):]])
    return l

def no_spazi(fposts):
    s = open(fposts).read().lower().split('<post>')
    n = []
    for x in range(len(s)):
        n.append(s[x].strip())
    s = n
    s.remove('')
    return s

def lista_in_l(s):
    for el in s:
        el[1] = el[1].split()
    return s


