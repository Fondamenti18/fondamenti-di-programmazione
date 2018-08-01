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
che contengono almeno una parola dell'insieme in input.
Due parole sono considerate uguali anche se  alcuni caratteri alfabetici compaiono in una 
in maiuscolo e nell'altra in minuscolo.

Per gli esempi vedere il file grade.txt

AVVERTENZE:
	non usare caratteri non ASCII, come le lettere accentate;
	non usare moduli che non sono nella libreria standard.
NOTA: l'encoding del file e' 'utf-8'
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero.
'''

def nonAlphaClean(string):
    #Funzione che elimina tutti i caratteri non alfanumerici da una stringa
    allowed='abcdefghijklmnopqrstuvwxyz1234567890'
    cleaned=''
    newString=string.lower()
    for char in newString:
        if char in allowed:
            cleaned=cleaned+char
        else:
            cleaned=cleaned+" "
    return cleaned
            
def workFile(fposts):
    #Funzione che legge un file di testo in input ritornando il suo contenuto
    #splittato ed in lowercase, eliminando tutti i caratteri non alfanumerici
    with open(fposts,'r') as f:
        text=f.read()
        
    myFile=text.split()
    myLower=[]
    for word in myFile:
        myAlpha=nonAlphaClean(word)
        myLower.append(myAlpha)
    return myLower

def workSet(insieme):
    #Crea un nuovo insieme da quello in input con tutte le parole in lowercase
    TrueSet=set()
    for word in insieme:
        TrueSet.add(word.lower())
    return TrueSet


def post(fposts, insieme):
    #Variabili utili
    myFile=workFile(fposts)
    mySet=workSet(insieme)
    myPostsNumber=set()
    index=0
    myFileLen=len(myFile)
    #Scorrimento del testo
    while index<myFileLen-1:
        if myFile[index]==" post ":
            FlagNum=myFile[index+1]
        elif " post " in myFile[index]:
            FlagNum=myFile[index][6:]
        else:
            for word in mySet:
                if word=="no":
                    return set()
                elif word in myFile[index]:
                    myPostsNumber.add(FlagNum)
        index=index+1
    return myPostsNumber