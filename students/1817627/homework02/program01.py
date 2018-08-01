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
Due parole sono considerate uguali anche se alcuni caratteri alfabetici compaiono in una 
in maiuscolo e nell'altra in minuscolo.

Per gli esempi vedere il file grade.txt

AVVERTENZE:
	non usare caratteri non ASCII, come le lettere accentate;
	non usare moduli che non sono nella libreria standard.
NOTA: l'encoding del file e' 'utf-8'
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero.
'''


def post(fposts,insieme):
    dizpost=dizionario(fposts)
    newins=set()
    for i in dizpost:
       for c in dizpost[i]:
            if not c.isalpha():
                dizpost[i]=dizpost[i].replace(c,' ')
       for p in insieme:
           if p.lower() in dizpost[i].split():
               newins.add(i)
               break
    return newins
    
        
        
def lavorapost(file):
    '''restituisce una lista che ha come elementi tutti gli id dei post'''
    listaid=[]
    file=open(file)
    for riga in file:
        if riga.find('<POST>')!= -1:
            a=riga.strip()
            b=list(a)
            b.insert(6,' ')
            c=''.join(b)
            listaid+=[int(i) for i in c.split() if i.isdigit()]
    return listaid 
        

def workonpost(file):
    '''restituisce una lista che ha come elementi i testi completi
    di ciascun post'''
    file=open(file)
    testo=file.read()
    lista=[]
    testo1=testo.split('<POST>')
    n=0
    while n<len(testo1):
        lista+=[testo1[n].lower().strip()]
        n+=1
    return lista[1:]
        
        
def dizionario(file):
    '''restituisce un dizionario che ha come chiavi gli elementi 
    della lista restituita dalla funzione workonpost ovvero i testi
    completi di ogni post e come elementi gli id dei post'''
    n=0
    dicto={}
    listaid=workonpost(file)
    postid=lavorapost(file)
    while n<len(listaid):
        dicto.update({str(postid[n]):str(listaid[n])})
        n+=1
    return dicto
        
        
        