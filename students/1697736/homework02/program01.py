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

def noalpha(qu):
    noa = ''
    for c in qu:
        if not (c in noa or c.isalpha() or isNumber(c)):
            noa += c
    return noa

def words(qu):
    noa = noalpha(qu)
    for c in noa:
        qu = qu.replace(c, ' ')
    return qu.lower().split()



def isNumber(n):
    numeri = ['1','2','3','4','5','6','7','8','9','0']
    if n in numeri:
        return True


def post(fposts,insieme):
    ''' implementare qui la funzione'''
    ris = set()
    newinsieme = set()
    for el in insieme:
        newinsieme.add(el.lower())
    with open(fposts, encoding='utf-8-sig') as f:
        fr = f.read()
        fr = fr.lower()
        frep = fr.replace('\n', ' ')
        frep = frep.replace('  ', ' ')
        f_split = frep.split('<post>')
        for j,_ in enumerate(f_split):
            parole = words(f_split[j])
            for p in parole:
                if p in newinsieme:
                    ris.add(parole[0])
        return ris