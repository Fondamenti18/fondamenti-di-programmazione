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

def post(fposts,insieme):
'''


def post(fposts,insieme):
    insieme=valori(insieme)
    #print(insieme)
    li=len(insieme)
    #print(li)
    #fposts='C:/Users/sergi_000/.anaconda/homework02/es1/file01.txt'
    file=open(fposts,'r',encoding='utf8')
    file=file.read()                  #legge il file
    #file=''.join(str(e) for e in file)  #da lista a str
    #strfile=strfile.split('\n')
    file=file.strip()
    file=file.split('<POST>')        #split str ->lista  
    #print(file)
    ll=len(file)
    #print(ll)
    lista=[]
    for l in range(ll):
        for i in range(li):
            #print(insieme[i])
            #print(file[l])
            
            b=insieme[i].lower() in file[l].lower()
            if (b)==True:
                lista+=[l]
            #print(i,l)
    lista_npost=npost(file)  
    #print(lista_npost)
    #print(lista)
    ris=risultato(lista,lista_npost)
    return set(ris)
            
    #file.split('\n')
    #print(file)
    
    

def valori(insieme):
    ris=[]
    insieme=list(insieme)
    l=len(insieme)
    for i in range(l):
        ris+=[insieme[i]]
    return ris

def npost(file):
    ris=[]
    l=len(file)
    for i in range(l):
        ris+=[primon(file[i])]
    return ris
    

            
def primon(f):
    start=None
    end=None
    flaginsert=None
    for i in range(len(f)):
        if f[i]>= chr(48) and f[i]<= chr(57):
            if flaginsert==None:
                start=i
                end=i
                flaginsert=1
                
            else:
                end=i
        else:
            if flaginsert==1:
                return f[start:end+1]
        #print(i)
    return '0'
            
    
def risultato(lista,lista_npost):
    l=len(lista)
    #print(l)
    ris=[]
    for i in range(l):
        
        p=lista[i]
        ris+=[lista_npost[p]]
        #print(p)
        
    
    return ris
    
    
    