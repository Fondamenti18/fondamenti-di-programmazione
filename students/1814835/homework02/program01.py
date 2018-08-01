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


#f = open(r'C:\Users\leonardo\Desktop\homework02\es1\file01.txt')
def post(f,insieme):
    f = open(f,'r')
    testo = f.read()
    utente=[]
    indice=[]
    a_utente=[]
    risultato=[]
    if risultato != []:
        risultato.clear()
    #for x in testo:
    #    if x == '?' or x == '.' or x == '"' or x == ':' or x == ',':
    #        testo = testo.replace(x,'')
    parole = testo.split()
    f.close()
    #for el in range(len(parole)):
    #    if parole[el] == '<POST>17':
    #        utente.append('17')
    #        a_utente.append(parole.index('<POST>17'))
        if parole[el] == '<POST>':
            utente.append(parole[el+1])
            a_utente.append(el+1)
    for i in insieme:
        for (x, parola) in enumerate(parole):
            if (parola.lower() == i.lower()):
                indice.append(x)
    for x in indice:
        for i in range(len(a_utente)):
            if i == (len(a_utente)-1):
                if x > a_utente[i]:
                    risultato.append(utente[i])
            else:
                if x > a_utente[i] and x < a_utente[(i+1)]:
                    risultato.append(utente[i])
    return set(risultato)
                
            
    
        


        
            

            
    
    
    

