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






def rielaboratesto(f1):
    d={}
    d1={}
    with open(f1, encoding='utf-8') as f:
        for l in f:
           b=l.replace('\n',' ').strip()
           if b.find('<POST>')!=-1:
               n1=b[b.find('<POST>')+6:].strip()
               d[n1]=[]
           else:
               d[n1]+=b.split()
    for c in d.keys():
        d1[c]=[]
        for a in d[c]:
            nw=''
            for m in a:
                p=m.lower()
                if not p.isalpha():
                    nw+=' '
                else:
                   nw+=p
            d1[c]+=[nw]
    d2={}
    for e in d1.keys():
        d2[e]=[]
        for c in d1[e]:
            d2[e]+=c.split()
    return d2
    
    
def post(fposts,insieme):
    ''' implementare qui la funzione''' 
    d4={}
    d4=rielaboratesto(fposts)
    insieme3=set()
    for u in insieme:
        insieme3.add(u.lower())
    d3={}

    for e in d4.keys():
        d3[e]=set(d4[e])
    insieme1=set()      
    for e in d4.keys():
            if((d3[e] & insieme3)):
               insieme1.add(e)
    return insieme1       


