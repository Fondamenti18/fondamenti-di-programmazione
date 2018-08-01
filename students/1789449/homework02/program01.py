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


def trovaID(s):
    cane=''
    lista=[]
    for x in range(len(s)):
        for y in s[x]:
            if(y >='0')and(y<='9'):
                cane+=y
                
            else:
                break
        #print(cane)
        
        lista.append(cane)
        cane=''
    #del lista[0]
    return lista
    

def cerca(ids,testo,insieme):
    y = 0
    od = []
    o = -1
    i = []
    s=[]
    se=set()
    insieme=list(insieme)
    #insieme=str(insieme).strip("{'}")
    #print(insieme)
    #s=str(insieme).split()
    #print(insieme)
    
    cavallo=[]
    #print(ids)
    #print(testo[0])
    for x in range(len(testo)):
        cavallo=testo[x].split()
        for y in cavallo:
            for z in range(len(insieme)):
                if(y.find((insieme[z]).lower())!= -1 and len(y.strip("?!.,-%&$/()[]{}@òàùù#")) == len(insieme[z])):
                #print(y)
                    #print(cavallo)
                    se.add(ids[x])
                
        #o = x.find(insieme)
        #if(x in s):
         #   print(x)
        #print(o)
        #if (o != -1):
         #   i.append(x)
        
          #  print(x[o])
    
    #print(ids)
    return se


def post(fposts,insieme):
    ''' implementare qui la funzione'''
    f = open(fposts)
    
    testo = f.read()
    
    #print(testo)
    
    testo = testo.lower()
    
    testo1 = testo.split('<post>')
    testo = testo.replace(' ','')
    testo=testo.split('<post>')
    del testo[0]
    del testo1[0]
    #print(testo)
    
    ids = trovaID(testo)
    
    return cerca(ids,testo1,insieme)
    
    #print(idd)
    
    #for x in range(len(testo)):
        
        
            
#print(post("file01.txt",{'no'}))