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
    ''' implementare qui la funzione'''
    
    ins=set()
    ins2=set()
    for parola in insieme:  #formatto ogni parola dell'insieme in minuscolo
        parola=parola.lower()
        ins2.add(parola)   
        
    with open(fposts,'r') as file:
        lista,enumerazione=trova(file)   #cerco linea di inizio post
        
        lista1=analisipost(ins2,lista,file,enumerazione) #errore   #cerco quali post hanno almeno una parola
        for x in lista1:  #aggiungo ID di ogni post all'insieme
            ins.add(x)
    return ins
         
def analisipost(insieme,lista,file,enumerazione):
    
    ultimovalore=len(lista)
    
    
    lista1=[]   #lista dove inserisco gli ID
    n=0  #n è il contatore che conta gli elementi della lista degli id che ho esaminato
    i=0   # i serve per calcolare l'indice, numera le righe
    while i<=enumerazione[-1][0]:
        indice=enumerazione[i][0]
        #indice serve per contare le righe    
        
        
        
       
        if n==ultimovalore-1: # per correggere errore a 206(valore finale) 
            
               
            controllo=check2(enumerazione[i][1],insieme)
            
            if controllo: 
                segnofinale=trova_id(enumerazione,lista[n]) #trova ID che corrisponde all'inizio dell'intervallo esaminato
                
                lista1.append(segnofinale)   
                
        elif n<ultimovalore-1: #esaminare valori al di sotto dell'ultimo valore della lista degli ID
            
            if indice<lista[n+1]:   # analisi per cambiare i due estremi dell'intervallo
                
                
                
                valoreiniziale=lista[n]

                
                valorefinale=lista[n+1]
                if indice==lista[-1]-1:
                    n=ultimovalore-1
                    continue
            elif indice>lista[n+1] and indice<lista[-1]:   
                
                n+=1
                valoreiniziale=lista[n]
                valorefinale=lista[n+1]
             
                
            if indice in range(valoreiniziale+1,valorefinale):  # controllo se cè almeno una parola
                controllo=check2(enumerazione[i][1],insieme)
            
                if controllo:
                
                    segnoperpost=trova_id(enumerazione,lista[n])
                
                    n+=1  #per saltare al prossimo post quando hai trovato almeno una parola
                    lista1.append(segnoperpost)
        i+=1      
      
    return lista1        
          
                   
                     
        
         
         
         

        
def trova(file):   #cerca le righe dove cè l'ID
    lista=[]
    insieme=set()
    insieme.add('POST')
    enumerazione=list(enumerate(file)) #creo una coppia formata dal numero riga e dalla stringa corrispondente
    

    for indice,x in enumerazione:  #controllo
        
        
        controllo=check(x,insieme)
       


        if controllo:
            
            lista.append(indice)
            
     
    return lista,enumerazione
            
def trova_id(enumerazione,elemento):  #trova l'Id corrispondente al post
    
    riga=enumerazione[elemento][1]  #prende la stringa
    
    riganuova=riga.replace(" ","")  #rimuove gli spazi
   
    riganuova=riganuova.replace("<POST>","")  #rimuove la stringa <POST>
    riganuova=riganuova.strip() #rimuove gli accapi
    return riganuova
    
def check(riga,insieme):   # controlla se cè l'Id nella riga
    
    
    stringa=''
    risultato=False     
    parole=riga.split()
    
    
    for parola in parole:           
        if not  parola.isalpha():   
            for carattere in parola:
                if  carattere.isalpha():
                    stringa=stringa+carattere
            parola=stringa
        
            stringa=''        
                
        if parola in insieme:
            risultato=True
               
    return risultato
       
                
def check2(riga,insieme):  # controlla se nella riga cè almeno una parola dell'insieme
       
    riganuova=riga.lower()
    parole=riganuova.split()                                  
    risultato=False   
    
    for parola in parole:
       
        if not parola.isalpha():
            
            if not parola[-1].isalpha():
                parola=parola.replace(parola[-1],'')   
                    
                 
        if parola in insieme:
            risultato=True           
    return risultato 


