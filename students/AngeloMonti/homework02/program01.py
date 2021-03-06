'''
I post di un forum sono raccolti in alcuni file che hanno il seguente formato. 
Un file contiene uno o piu' post, l'inizio di un post e' marcato da una linea che contiene
in sequenza le due sottostringhe "<POST>" ed "N" (senza virgolette) eventualmente 
inframmezzate, precedute e/o seguite da  spazi. "N" e' l'ID del post (un numero positivo).  
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
NOTA: l'encoding del file è 'utf8'
===================================
ATTENZIONE: Se il grader non termina entro 5 minuti il punteggio dell'esercizio e' zero.
                                           ========
'''
        


def post(fposts,insieme):
    ''' implementare qui la funzione'''
    with  open(fposts) as f:
        testo= f.read().split('<POST>')
    insRIS=set()
    parole=[x.lower() for x in insieme]
    for post in testo:
        for j in parole:
            post=post.lower()
            t=trovato=0
            while not trovato:
                i = post.find(j,t)
                if i==-1:break
                if post[i-1].isalpha()==False and post[i+len(j)].isalpha()==False:
                    insRIS.add(post[:post.find('\n')].strip())
                    trovato=1
                else: t=i+len(j)
    return insRIS









