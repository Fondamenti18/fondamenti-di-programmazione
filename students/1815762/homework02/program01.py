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
    f = open(fposts)
    a=f.read()
    a=a.lower()
    l=a.split()
    f.close()
    lst=[]
    x=0
    n=len(l)
    g=[]
    while x<n:
        g.append(l[x].split("<post>"))
        x+=1
    
    
    
    x=0 
    while x<len(g):
        y=0
        while y<len(g[x]):
            if g[x][y].isdigit()==True:
                lst.append(g[x][y])
            y+=1
        x+=1
    
    x=0
    while x<len(lst):
        if lst[x]=='0':
            lst.pop(x)
        x+=1
    

    x=0
    z=-1
    cont=0
    cont2=0
    k=set([])
    codice=list(insieme)
    for x in range(len(codice)):
        codice[x]=codice[x].lower()
    x=0
    longe=len(insieme)
    while x<len(g):
        y=0
        while y<len(g[x]):
            j=0
            if g[x][y].isdigit()==True and g[x][y]!='0':
                z+=1
                cont=0
                cont2=0
            if g[x][y]==codice[j] or g[x][y]==codice[j]+'?' or g[x][y]==codice[j]+'.':
                cont+=1
            if cont>0:
                k.add(lst[z])
            if longe>1:
                i=0
                j+=1
                while i<j:
                    if g[x][y]==codice[j] or g[x][y]==codice[j]+'?' or g[x][y]==codice[j]+'.':
                        cont2+=1
                    if cont2>0:
                        k.add(lst[z])
                        
                    i+=1
    
                
            y+=1
        x+=1
          
    return(k)
    
    





