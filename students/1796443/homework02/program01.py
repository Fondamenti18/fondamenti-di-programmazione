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
def crea_lista(fposts):
    f=open(fposts, 'r', encoding='utf-8')
    t=f.read()
    f.close()
    ls=t.split('<POST>')
    i=0
    while i<len(ls):
        ls[i]=ls[i].split()
        i+=1
    i=len(ls)-1
    while i>=0:
        if len(ls[i])==0:
            del ls[i]
        i-=1
    return ls

def mod_lista(ls):
    c=0
    for l in ls:
        j=0
        for s1 in l:
            controllo=True
            s=''
            i=1
            for a in s1:
                if j==0:
                    s=s+a
                elif a.isalpha() and controllo and i!=len(s1):
                    if ord(a)<97:
                        a=chr(ord(a)+32)
                    s=s+a
                elif i==len(s1):
                    if a.isalpha():
                        if ord(a)<97:
                            a=chr(ord(a)+32)
                        s=s+a
                else:
                    s=''
                    controllo=False
                i+=1
            ls[c][j]=s
            j+=1
        c+=1
    return ls

def crea_ins(insieme,ls):
    ins=set()
    for l in ls:
        controllo=False
        j=1
        while j<len(l) and  not controllo:
            if l[j] in insieme:
                ins.add(l[0])
                controllo=True
            else:
                j+=1
    return ins

def mod_insieme(insieme):
    lsd=[]
    for x in insieme:
        s=''
        for y in x:
            if ord(y)<97:
               y=chr(ord(y)+32)
            s=s+y
        lsd+=[s]
    for x in lsd:
        insieme.add(x)
    return insieme

def post(fposts,insieme):
    ''' implementare qui la funzione'''
    ls=crea_lista(fposts)
    ls=mod_lista(ls)
    insieme=mod_insieme(insieme)
    return crea_ins(insieme,ls)