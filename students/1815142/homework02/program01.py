
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
    t=open(fposts)
    t=t.readlines()
    off=0
    indici_post=[]
    f=[]
    for g in range(len(t)):
        t[g]=' '+t[g]
    for g in range(len(t)):
        stringa=''
        if t[g-off].find('POST')!=-1:
            t[g-off]=t[g-off].replace(' ','')
            for i in t[g-off]:
                if i.isalpha()==False:
                    stringa+=i
            t[g-off]=stringa[2:]
            indici_post.append(g-off)
        t[g-off]=t[g-off].lower()
        if t[g-off].find('POST')==-1:
            if t[g-off].find("\n")!=-1:
                t[g-off]=t[g-off].replace("\n",'')
            if t[g-off]=='':
                t.remove(t[g-off])
                off+=1
            for i in t[g-off]:
                if i.isalnum()==False and i!=' ':
                    t[g-off]=t[g-off].replace(i,' ')
            a=t[g-off].lower()
            for i in insieme:
                i=i.lower()
                i=' '+i+' '
                if a.find(i)!=-1:
                    indici_post.append(t[g-off])
    indici_post.append(int('1234567890'))
    for i in range((len(indici_post)-1)):
        if type(indici_post[i])==int and type(indici_post[i+1])==str:
            f.append((t[indici_post[i]]))
    return(set(f))


