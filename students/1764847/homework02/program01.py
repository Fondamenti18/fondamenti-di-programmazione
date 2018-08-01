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



def post(fposts,insieme):
    '''Prende in input il percorso di un file ed un insieme di parole,
    restituisce un insieme contenente gli identificativi dei post
    che contengono almeno una parola dell'insieme in input'''
    ins = set()
    d = readText(fposts)
    splitSpace = []
    lstValori = list(d.values())
    lstChiavi = list(d.keys())
    insiemeLower = insieme.copy()
    for i in insieme:
        insiemeLower.add(i.lower())
    for i in range(len(lstValori)):
        splitSpace += [lstValori[i].split()]
    j = 0
    for lista in splitSpace:
        for i in lista:
            if not i.isalpha():
                i = removeChr(i)
            if i.lower().strip() in insiemeLower:
                ins.add(lstChiavi[j].strip())
                break
        j += 1  
    return ins
                                
 

def removeChr(s):
    '''Presa in input una stringa, ne restituisce un'altra con solo caratteri
    alfabetici'''
    stringa = ''
    for i in s:
        if i.isalpha():
            stringa += i
        else:
            stringa += ' '
    return stringa
            


def readText(pFile):
    '''Preso in input un file contenente dei post, restituisce la lista di
    tutti i post'''
    lstPost = []
    d = {}
    forum = ''
    f = open(pFile, 'r', encoding='utf-8')
    for riga in f.readlines():
        forum += riga.lstrip()
    f.close()
    lstPost = forum.split('<POST>')
    for i in lstPost:
        i = i.strip()
        d[i[0:i.find('\n')]] = i[i.find('\n')+1 :]
    return d


