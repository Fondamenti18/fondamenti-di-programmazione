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
def is_new_post(line):
    try:
        if line.strip().split('>')[0] == '<POST':
            return True
        else:
            return False
    except:
        return False
   
def findID(stringa):
    ID=''
    for el in stringa: #(che sarà equivalente al post in qualche modo):
        if el in set('1234567890'):
            ID+=el
        else:
            break
    return ID

def findCycle(stringa,parola):
    n=0
    posizioni=[]
    stringa=stringa.lower()
    while n<len(stringa):
        if stringa.find(parola, n)!=-1:
            posizioni.append(stringa.find(parola,n))
            n=stringa.find(parola,n)+len(parola)
        else:
            break
    return posizioni
            
            
        
        
def has_word(stringa, parola):
    if findCycle(stringa, parola)!=[]:
        n=0 #indice degli elementi nella stringa 'posizioni'
        while n<len(findCycle(stringa,parola)):
                      
            if not stringa[findCycle(stringa,parola)[n]-1].isalpha() and not stringa[findCycle(stringa,parola)[n]+len(parola)].isalpha():
                n+=1
                return 1
            else: 
                n+=1
    #stringa[stringa.find(parola)-1].isalpha() and not stringa[stringa.find(parola)+len(parola)].isalpha()
    else:
        return -1
        

def crea_insiemeOUT(lista, insieme):
        insiemeOUT=set()
        for stringa in lista:
            for parola in insieme:
                word=parola.lower()
                if has_word(stringa, word)==1:
                    insiemeOUT.add(findID(stringa))
                    break
        return insiemeOUT
        

def post(fposts,insieme):
    with open (fposts, 'r', encoding='utf-8') as f:
        lines=f.readlines()
        lista=[]
        n=-1
        #riempio la lista con tante stringhe, ognuna equivalente ad un post
        for line in lines:
            if not is_new_post(line):
                lista[n]+=line   
            else:
                lista.append(line)
                n+=1
            
        #cancello spazi e POST all'inizio di ogni stringa
        for stringa in lista:
            lista[lista.index(stringa)]=stringa.replace('<POST>','').strip()

        #metto tutto insieme
        return crea_insiemeOUT(lista,insieme)
        
          

     

#with open('C:/Users/Admin_2/Documenti/Blubdoc/UNI/programmazione/file01.txt', 'r', encoding='utf-8') as f:
