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


def getID(stringa):
    numeri = '0123456789'
    id = ''
    indice = 0
    while indice <= len(stringa):
        if stringa[indice] in numeri:
            id += stringa[indice]
            indice += 1
        else:
            break
    return id

def post(fposts,insieme):
    ''' implementare qui la funzione'''
    lista = []
    listaID = []
    lettere = 'abcdefghijklmnopqrstuvwxyz'
    with open(fposts, encoding='utf-8') as file:
        testo = file.read()
    testo = testo.lower()
    testo = testo.strip()
    lista_post = testo.split('<post>')
    insieme_nuovo = set()
    for p in insieme:
        insieme_nuovo.add(p.lower())
    for elem in lista_post:
        if elem != '':
            lista.append(elem.strip())
    for parola in insieme_nuovo:
        for post in lista:
            if parola in post:
                l = find(post,parola)
                lungh = len(parola)
                s = ' !,.:;-?'
                for e in l:
                    if post[e+lungh] in s and (post[e-1] in s or post[e-1] == '\n'):
                        listaID.append(getID(post))
                        break
    return set(listaID)


def find(s, ch):
    l = []
    while s.find(ch) != -1:
        l.append(s.find(ch))
        s = s[:s.find(ch)]+len(ch)*'.' +s[s.find(ch)+len(ch):]
    return l

