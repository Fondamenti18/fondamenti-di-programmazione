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
    ''' implementare qui la funzione'''
    from pprint import pprint
    risultato={}
    post={}
    ris=[]
    file=''
    punt='''.,?!:'''
    
    
    f = open(fposts, "r")
    f = f.read()
    f= f.lower()

    for x in f:
        if x not in punt:
            file += x

    l=file.split('\n')
    l[:]=[x.replace(x," ") if x in punt else x  for x in l ]   
    l[:]=[x.replace('<post>'," ") for x in l]
    l[:]=[x.strip() for x in l if x!=""]

    n=[x for x in l if x.isdigit()]
    l[:]=[x.replace(x,'<>') if x in n else x for x in l]         

    p=" ".join(l).split("<>")
    p[:]=[x for x in p if x!=""]
    for i in range(0,len(n)):
        post[n[i]]=p[i]

    for x in insieme:
        ris+=[k for k in n if x.lower() in post[k].split()]

    
    return set(ris)


















    


