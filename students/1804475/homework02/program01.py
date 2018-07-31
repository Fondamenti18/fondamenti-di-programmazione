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
def post(fposts, insieme):
    risultato = set()
    f=open(fposts,'r')
    insieme = insiemeMinuscolo(insieme)
    for linea in f:
        if '<POST>'  in linea:
            idpost=trovaid(linea)    
        else: 
            aggiungere(risultato,linea,insieme,idpost)
    return risultato

def toglipunt (stringa):
    snopunt = stringa
    for c in stringa:
        if not c.isalpha() and c != "<" and c != ">" and not c.isnumeric():
            snopunt = snopunt.replace(c," ")
    return snopunt

def insiemeMinuscolo(insieme):
    minuscolo = set()
    for x in insieme:
        if not x.islower():
            minuscolo.add(x.lower())
        else:
            minuscolo.add(x)
    return minuscolo
    
def trovaid(linea):
    parole = linea.split()
    if len(parole) == 1:
        idpost=parole[0][6:]
    else:
        idpost = parole [1]
    return idpost

def aggiungere(risultato,linea,insieme,idpost):
    lnopunt = toglipunt(linea).split()
    for x in lnopunt:
        if x.lower() in insieme:
            risultato.add(idpost)
    
