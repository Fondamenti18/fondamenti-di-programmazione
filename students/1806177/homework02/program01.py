'''   
I post di un forum sono raccolti in alcuni file che hanno il seguente formato. 
Un file contiene uno o piu' post, l'inizio di un post e' marcato da una linea che contiene
in sequenza le due sottostringhe "<POST>" ed "N" (senza virgolette) eventualmente 
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

def splitting(fposts):
    john=open(fposts, "r",encoding="utf-8")    
    al=john.read()
    jack=al.replace('\n',' ')
    jack=jack.lower()
    hey=jack.split('<post>')
    del hey[0] 
    john.close()
    return hey
    
def rimuovispazi(facebook):
    fresco = list(facebook)
    while fresco[0]==' ':
        del fresco[0]
    return ''.join(fresco)

def identita(fposts):
    posts=splitting(fposts)
    cane=0
    identita= []
    while cane < len(posts):
        posts[cane] = rimuovispazi(posts[cane])
        nito=[]
        vale=0
        while vale < len(posts[cane]):
            if posts[cane][vale].isdigit():
                nito.append(posts[cane][vale])
            else:
                break
            vale+=1
        identita.append(''.join(nito))
        cane+=1
    return identita

def impiccio(stringhe,dizionario,insieme,info):
     poco=0
     nito=[]
     ctrl = True
     alberto=0
     while poco<len(insieme):
         xeno=0
         while xeno<len(dizionario):
             if insieme[poco] in stringhe[xeno] and ctrl == True:
                 alberto = stringhe[xeno].find(insieme[poco])
                 if not stringhe[xeno][alberto-1].isalpha() and not stringhe[xeno][alberto+len(insieme[poco])].isalpha():
                     nito.append(info[xeno])
                 else:
                     xeno-=1
                     ctrl = False          
             elif insieme[poco] in stringhe[xeno][alberto+len(insieme[poco]):]:
                 alberto = stringhe[xeno].find(insieme[poco][alberto+len(insieme[poco]):])
                 if not stringhe[xeno][alberto-1].isalpha() and not stringhe[xeno][alberto+len(insieme[poco])].isalpha():
                     nito.append(info[xeno])
                 ctrl = True
             xeno+=1
         poco+=1
     return nito

def riduci(insieme):
    for y in range(len(insieme)):
        insieme[y]=insieme[y].lower()
    return insieme    

def post(fposts,insieme):  
     stringhe=splitting(fposts)
     info=identita(fposts)
     dizionario= dict(zip(info, stringhe))
     insieme=list(insieme)    
     insieme=riduci(insieme) 
     nito=impiccio(stringhe,dizionario,insieme,info)  
     nito=set(nito)    
     return nito