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
    insieme=modifica_insieme_iniziale(insieme)
    lista= crea_lista(fposts)
    insieme_id=set()
    for parola in insieme:
        for linea in lista:
            s=linea[2]
            if(parola in s):
                insieme_id.add(linea[1])
    return insieme_id

def rimuovi_punteggiatura(string):
    nuovastringa=""
    for char in string:
        if char in "?:.;,!-_":
            continue
        else:
            nuovastringa=nuovastringa+char
    return nuovastringa
            
def modifica_insieme_iniziale (insieme):
    for a in insieme:
        maiusc=a.upper()
        insieme.remove(a)
        insieme.add(maiusc)
    return insieme
        
def crea_lista (fposts):
    elenco=[]
    f=open(fposts, 'r', encoding='utf-8')
    for linee in enumerate(f):
        pos=linee[1].find('<POST>')
        if (pos!=-1):
            new=linee[1].split('>',-1)
            post_id=new[1].split()
        maiusc=linee[1].upper()
        maiusc=rimuovi_punteggiatura(maiusc)
        lista=maiusc.split()
        dizio=set()
        for elemento in lista:
            dizio.add(elemento)
            elenco.append((linee[0], post_id[0],dizio))
    f.close()
    return  elenco
