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


def ripulisci(content):
    ris = ''
    for c in content:
        if c.isalpha():
            ris += c
        else:
            ris += ' '
    return ris

def post(fposts,insieme):
    ''' implementare qui la funzione'''
    ris = set()
    lines = []
    with open(fposts, encoding='utf-8') as f:
        testo = f.read()
        lines = testo.split('\n')

    nr = 0
    while nr < len(lines):
        l = lines[nr].strip(' ')
        l = l.replace(' ', '')
        if l.startswith('<POST>'):
            numPost = l[6:]
            content = ''
            nr += 1
            while nr < len(lines):
                if not(lines[nr].strip(' ').replace(' ', '').startswith('<POST>')):
                    content += lines[nr] + ' '
                    nr += 1
                else:
                    nr -= 1
                    break

            content = content.lower()
            content = ripulisci(content)
            content = content.split(' ')
            for p in insieme:
                if p.lower() in content:
                    ris.add(numPost)
        nr += 1
    return ris




