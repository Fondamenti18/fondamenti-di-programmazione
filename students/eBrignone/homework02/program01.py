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
    stringa=fileToString(fposts)
    mappa=mapPost(stringa)
    insiemeId=set()
    for chiave,linea in mappa.items():
        for parola in insieme:
            parola=parola.lower()
            insid=testoContiene(linea,parola)

            if insid:
                insiemeId.add(str(chiave))
                
    return insiemeId
def testoContiene(testo,parola):
    indiceParola = -1
    buona = False
    try:
        while not buona:
            indiceParola = testo.index(parola,indiceParola+1)
            if(indiceParola>=1):
                if testo[indiceParola-1:indiceParola].isalnum():
                    buona = False
                elif testo[indiceParola+len(parola):indiceParola+len(parola)+1].isalnum():
                    buona = False
                else:
                    buona = True
            
    except:
        a=1
    return buona 


def fileToString(filename):
    #leggi file e metti tutto in una stringa
    try:
        file=open(filename,'r',encoding='utf8')
        testoFile=''
        for line in file.readlines():
            testoFile+=line.lower()
        return testoFile
    except:
        print("errore nell'apertura del file")
        
def mapPost(textString):
    lastPost = -1
    tag = "<post>"
    idPost = -1
    posts={}
    nextBreakLine=-1
    while(True):
        try:
            lastPost = textString.index(tag,lastPost+1)
            
            if idPost>-1:
                posts[idPost] = textString[nextBreakLine+1:lastPost]
            
            nextBreakLine = textString.index("\n",lastPost)
            idPost = int(textString[lastPost+len(tag):nextBreakLine])
        except:
           break
    posts[idPost] = textString[nextBreakLine+1:]
    return posts

