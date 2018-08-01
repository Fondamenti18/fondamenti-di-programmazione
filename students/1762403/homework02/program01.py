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
    dicPosts = posts(fposts)
    result = set()
    for key in dicPosts.keys():
        for word in insieme:
            if(countW(dicPosts[key], word)):
                result.add(key)
    return result
            

def posts(filename):
    #Funzione che si occupa di suddividere il file in tutti post ritornando una dizionario con chiave l'ID del post e valore il testo
    dizPosts = dict() #dizionario che conterrà i post
    with open(filename, 'r', encoding='utf-8') as file:
        #recupero tutte le linee
        lines = file.readlines()
    key = ''
    for line in lines:
        lineNotSpace = line.replace(' ', '')
        if(lineNotSpace != '\n'):
            if(lineNotSpace[:6] == '<POST>'):
                #Creo la chiave con l'ID del post
                key = lineNotSpace[6:].replace('\n', '')
                dizPosts[lineNotSpace[6:].replace('\n', '')] = ''
            else:
                dizPosts[key] = dizPosts[key] + line
    return dizPosts


def countW(text, word):
    #Inizializzo le varibili
    lenWord = len(word)
    check = False
    #Tutti i testi in minuscolo
    text = text.lower()
    word = word.lower()
    
    num = text.count(word)
    
    if(num != 0):
        index = 0
        for i in range(num):
            if(i == 0):
                text = text[index:]
            else:
                text = text[index + lenWord:]
            
            index = text.find(word)
            
            if(not text[index + lenWord].isalpha()):
                if(not text[index - 1].isalpha()):
                    check = True
    
    return check