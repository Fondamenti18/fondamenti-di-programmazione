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
---> Due parole sono considerate uguali anche se  alcuni caratteri alfabetici compaiono in una 
---> in maiuscolo e nell'altra in minuscolo.

Per gli esempi vedere il file grade.txt

AVVERTENZE:
	non usare caratteri non ASCII, come le lettere accentate;
	non usare moduli che non sono nella libreria standard.
NOTA: l'encoding del file e' 'utf-8'
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero.
'''

def post(fposts,insieme):
    txt=open(fposts)
    verifica='<POST>'
    post=''
    idPost=''
    risultato=set()
    for riga in txt:
        if verifica in riga:
            #appena trova una verifica, la funzione controllaParole controlla
            #se le righe accumulate FINO A QUEL MOMENTO in "post" contengono
            #le parole dell'insieme.
            controllaParole(post, insieme, idPost, risultato)
            #^^^^la esegue troppe volte?^^^^^
            
            #rimuove il contenuto di post per ricominciare con un nuovo post
            post=''
            #quando trova la verifica nella riga, la divide dal numero che la
            #segue e memorizza il numero seguente come ID
            try:
                idPost=riga.split()[1]
            except:
                idPost=riga.strip().split('>')[1]
        #per ogni riga del ciclo, se non c'è verifica, l'aggiunge alla variabile
        #post da passare alla funzione controllaParole non appena compare un 
        #nuovo <POST>
        if riga.strip()!='':
            post+=riga
    #si riesegue la funzione affinché anche ultimo post (id=7) venga analizzato
    controllaParole(post, insieme, idPost, risultato)
 
    txt.close()
    return risultato

def controllaParole(post, insieme, idPost, risultato):
    '''effettua i controlli di corrispondenza tra le parole di insieme e il testo.'''
    for parola in insieme:
        #rende tutta la parola minuscola
        parola=parola.lower()
        #cerca se le parole dell'insieme sono in qualche post
        if parola in post.lower():
            for el in post.split():        
                if el[0].isalpha()==True and el[-1].isalpha()==False:
                #se l'ultimo carattere non è alfabetico, si esegue la funzione seguente per rendere el solo alpha
                    el=pulisciel(el)
                #se la corrispondenza tra le parole è perfetta, si adda l'id all'insieme risultato
                if el.lower()==parola:
                    risultato.add(idPost)
    return risultato

def pulisciel(el):
    '''elimina i caratteri non alfabetici della parola el data in input'''
    while el[-1].isalpha()==False:
        el=el[:-1]
    return el
                    

if __name__=='__main__':
    post('file01.txt', {'non','Si'})