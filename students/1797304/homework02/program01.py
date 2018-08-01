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
def stringa_alnum(fposts):
    with open(fposts,encoding='utf-8')as t:
        leggi=t.read()
        minuscole=leggi.lower()
        stringa=minuscole.replace('\n',' ')
        caratteri=set(minuscole)
        elimina={'<','>'}
        caratteri=caratteri.difference(elimina)
        for c in caratteri:
            if not c.isalnum():
                stringa=stringa.replace(c,' ')
        return stringa


    
def post(fposts,insieme):
    insieme_minuscole=[x.lower() for x in insieme]
    ID=[]
    testo_post=[]
    risultato=set()
    stringa=stringa_alnum(fposts)
    post_divisi=stringa.split('<post>')
    parole=[stringa.split()for stringa in post_divisi]  
    for lista in parole:
        if lista==[]:
            next
        else:
            testo_post.append(lista)
            ID.append(lista[0])
    dizionario_coppie=dict(zip(ID,testo_post))
    for k,v in dizionario_coppie.items():
        for parola in v:
            if parola in insieme_minuscole:
                risultato.add(k)
    return risultato
        
            
        
                       
            
        
        

    
      
       
    
        
      
        
       
        
                
                    
    
    
            
                
                
                
            
        
            
    


