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
    testo = ""
    insieme = insieme
    s_testo = []
    post_ris = []
    with open(fposts, mode='r', encoding="utf-8") as file:
        testo+=file.read()
    
    s_testo=testo.split("<POST>")[1:]
    for post in s_testo:
        crea_diz_post(post,insieme,post_ris)
    return set(post_ris)


def crea_diz_post(post,insieme,post_ris):
    linee = []
    
    testo_post = ""
    punteggiatura = ''',.;:\"'!?^()/°*[]'''
    linee = post.splitlines()
    testo_post=" ".join(linee[1:]).replace("\n"," ").lower()
    
    id_post = get_id(linee)
    
    ##print("\n\n",testo_post,"\n")
    for c in testo_post:
        if c in punteggiatura:
            ##print("rimuovo: ",c)
            testo_post=testo_post.replace(c," ")
    
    ##print(testo_post,"\n\n")
    parole_testo = testo_post.split(" ")
    cerca_insi(insieme,parole_testo,id_post,post_ris)

def cerca_insi(insieme,parole_testo,id_post,post_ris):
    for parola in insieme:
        if parola.lower() in parole_testo:
            post_ris.append(id_post)

def get_id(linee):
    id_post = ""
    for l in linee[0]:
        if l.isnumeric(): id_post+=l
    return id_post
    
    
    
    
    
    
    
    
    
