'''
I post di un forum sono raccolti in alcuni file che hanno il seguente formato. 
Un file contiene uno o piu' post, l'inizio di un post e' marcato da una linea che contiene
in sequenza le due sottostringhe "<POST>" ed "N" (senza virgolette) eventualmente 
inframmezzate, precedute e/o seguite da 0,1 o piu' spazi. 
"N" e' l'ID del post (un numero positivo).  
Il contenuto del post e' nelle linee successive fino alla linea che marca il prossimo post 
o la fine del file (si veda ad esempio il file "file01.txt"). 
E' assicurato che la stringa "<POST>" non e' contenuta in nessun post.

Nel seguito per  parola intendiamo come al solito una qualsiasi sequenza di caratteri
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
    with open(fposts, "r", -1, "utf-8") as file:
        risultato=readLine(file, insieme)
    return risultato
    
def readLine(file, words):
    Id=""
    risultato=set()
    #Scorre le righe
    for line in file:
        #POST
        if line.find("<POST>") != -1:
            #Get ID
            Id = str(int(line.replace(" ", "").split("<POST>")[1]))
        elif Id!="" and line.strip()!="":
                #Search find
                if findWords(line.lower(), Id, words):
                    risultato.add(Id)
    return risultato

def findWords(line, Id, words):
    flag=False
    #Scorre le parole della riga
    for wl in line.replace("'", " ").split():
        if not wl.isalpha():
            wl=clearWord(wl)
        for wSet in words:
            if wl==wSet.lower():
                flag=True
                break
    return flag

#Pulisce parole con caratteri non alfanumerici agli estremi
def clearWord(word):
    for c in word:
        word=word.strip(c) if not c.isalnum() else word
    return word



