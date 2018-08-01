'''   
I post di un forum sono raccolti in alcuni file che hanno il seguente formato. 
Un file contiene uno o piu' post, l'inizio di un post e' marcato da una linea che contiene
in sequenza le due sottostringe "<POST>" ed "N" (senza virgolette) eventualmente 
inframmezzate, precedute e/o seguite da 0,1 o piu' spazi. q
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
     
     inspost=rimpiazza(fposts)
     info=clista(fposts)
     dizionario= dict(zip(info, inspost))
     insieme=list(insieme)    
     for y in range(len(insieme)):
         insieme[y]=insieme[y].lower() 
     y=0
     n=[]
     controllo = True
     a=0
     while y<len(insieme):
         x=0
         while x<len(dizionario):
             if insieme[y] in inspost[x] and controllo == True:
                 a = inspost[x].find(insieme[y])
                 if not inspost[x][a-1].isalpha() and not inspost[x][a+len(insieme[y])].isalpha():
                     n.append(info[x])
                 else:
                     x-=1
                     controllo = False
             
             elif insieme[y] in inspost[x][a+len(insieme[y]):]:
                 a = inspost[x].find(insieme[y][a+len(insieme[y]):])
                 if not inspost[x][a-1].isalpha() and not inspost[x][a+len(insieme[y])].isalpha():
                     n.append(info[x])
                 controllo = True
             x=x+1
         y=y+1
     n=set(n)    
     return n
 
def clista(fposts):
    l=rimpiazza(fposts)
    a=0
    clista= []
    while a < len(l):
        l[a] = eliminas(l[a])
        N=[]
        u=0
        while u < len(l[a]):
            if l[a][u].isdigit():
                N.append(l[a][u])
            else:
                break
            u+=1
        clista.append(''.join(N))
        a+=1
    return clista
def eliminas(stringa):
    listav = list(stringa)
    while listav[0]==' ':
        del listav[0]
    return ''.join(listav)



def rimpiazza(fposts):
    file=open(fposts, "r",encoding="utf-8")    
    lettura=file.read()
    k=lettura.replace('\n',' ')
    k=k.lower()
    h=k.split('<post>')
    del h[0] 
    return h