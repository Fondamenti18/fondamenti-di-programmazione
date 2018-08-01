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



# questa funzione controlla ogni parola dei post del dizionario e la "pulisce", ovvero rimpiazza con uno spazio i caratteri non alfabetici
def pulisciParola(parola):
    lista = list(parola)
    s = ''
    for count,char in enumerate(lista):
        if char.isalpha() == False:
            lista[count] = ' '
    return s.join(lista)    

# prende in input il percorso di un file e un insieme di parole
def post(fposts, insieme):  
    fposts = open(fposts)
    stringaTesto = fposts.read() # con stringaTesto leggo il contenuto del file e lo trasformo in stringa
    listaPost = stringaTesto.split('<POST>') # con listaPost divido la stringaTesto in vari post  
    dizMinuscolo = {}   
    result = set()

    for post in listaPost:# per ogni post nella lista dei post
        copiaElem = post.lower()# creo una variabile copia in cui aggiungo il post in caratteri minuscoli
        listaID = copiaElem.split() # listaID mi serve per controllare parola per parola
        if len(listaID) != 0: # se la lunghezza di listaID non è 0 
            chiave = listaID[0] # aggiungo nella chiave del dizionario, l'id del post
            dizMinuscolo[chiave] = copiaElem # associo ad ogni chiave, ovvero all'id, il corrispondente post
        
    for chiave in dizMinuscolo.keys():# per ogni post nella lista dei post a caratteri minuscoli
        lista2 = []
        valore = dizMinuscolo[chiave]
        for parola in valore.split(): # per ogni parola nel post 'splittato', ovvero diviso in parole
            parolaNuova = pulisciParola(parola) # richiamo la funzione che pulisce la parola
            x = parolaNuova.split()
            for elemento in x:
                lista2.append(x) # nella lista aggiungo ogni elemento della lista pulita creata dalla funzione pulisciParola
        dizMinuscolo[chiave] = lista2 # questa lista la associo ora alla chiave del dizionario
     
    # a questo punto ho i valori del dizionario in minuscolo e con solo caratteri alphabetici e verifico ,per ogni parola di ogni post, se è presente nell'insieme
    for chiave in dizMinuscolo.keys():
        for parola in dizMinuscolo[chiave]:
            for elemento in parola:
                for char in insieme:
                    if elemento == char.lower():
                        result.add(chiave)
    return result
                


            
        



