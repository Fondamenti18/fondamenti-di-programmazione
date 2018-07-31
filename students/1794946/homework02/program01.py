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
def post(fpost,insieme):
    insieme2=set()
    h=alfabeto(fpost)
    b=numeri(fpost)
    w=' '
    for el in h:
        k=h.index(el)
        y=b[k]
        for g in insieme:
            if quarta(g) in el:
                insieme2.add(y)      
    return insieme2           
def quarta(g):
    m=len(g)+1
    u=g.ljust(m,' ')
    w=' '
    for x in u:
        w+=x.lower()
    return w

import re
def keep(fpost):
    lista=[]
    j = open(fpost,'r')
    d=j.read().replace('\n', '')
    for word in d:
        c=d.split('<POST>')
    j.close()
    for i in c:
        g=tu(i)
        if g!=None:
            lista.append(g)
    
    return lista
    
def tu(i):
    for x in i:
        q=re.sub('[^A-Za-z0-9]+',' ',i)
        if q and q.strip():
            return q
        else:
            None

def alfabeto(fpost):
    c=keep(fpost)
    lista=[]
    for i in c:
        lista.append(asd(i))
    return lista

def asd(i):
    q=''
    for x in i:
        if x.isalpha()==True or x==' ':
            q+=x.lower()
    return q

def numeri(fpost):
    c=keep(fpost)
    lista4=[]
    for el in c:
        
        s=re.search(r'\d+', el).group()
        lista4.append(s)
    return lista4


