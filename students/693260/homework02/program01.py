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
    
    ListaPostTrovati = []
    
    #Apro il file
          
    FilePost = open(fposts)
        
    NumeroPost = 0
        
    ParolaTrovata = False
    
    linea = FilePost.readline()
    
    while linea != '':
        
        if linea.find("<POST>") > -1:
                
            #E la linea dove c e scritto <POST> e quindi sta per iniziare un nuovo post
            NumeroPost = linea[linea.index("<POST>") + 6:].replace("\n", "").replace(" ", "")
                      
            ParolaTrovata = False   
            
        else:
            
            lineaminuscole = linea.lower()
                
            #Se sono in questo else significa che sto leggendo una riga di un post
            
            if not ParolaTrovata:
                
                for parola in insieme:
                    
                    parola = parola.lower()
                    
                    #Controllo preliminare per capire se conviene ricercare con maggior precisione la parola data
                    if lineaminuscole.find(parola) == -1:
                        
                        continue
                    
                     #Primo controllo (meno veloce): la linea letta ha meno caratteri della parola cercata
                    
                    if len(lineaminuscole) < len(parola):
                        
                        continue                    
                    
                    #Secondo controllo (piu veloce): la linea letta contiene solo la parola cercata
                    if lineaminuscole == parola:
                            
                        ParolaTrovata = True
                            
                        ListaPostTrovati.append(NumeroPost)
                            
                        break

                    #Dichiarazione ed assegnazione dei valori alle variabili che serviranno
                    #nei prossimi due controlli
                    
                    lunghezzalinea = len(lineaminuscole)
                        
                    lunghezzaparola = len(parola)
                        
                    #Terzo controllo: vedo se la linea finisce con la parola che cerco
                    if linea.endswith(parola):
                        

                        
                        if not linea[lunghezzalinea - 1 - lunghezzaparola].isalpha:
                            
                            ParolaTrovata = True
                            
                            ListaPostTrovati.append(NumeroPost)
                            
                            break                                  
                    
                    '''
                    Quinto controllo (il piu lento): per ogni volta che controllo se la linea inizia
                    con la parola, mi creo in caso negativo una sottostringa e vedo se questa inzia per la parola
                    o se non è abbastanza capiente per contenere la parola che cerco
                    '''
                    
                    sottolinea = lineaminuscole[0:]
                    
                    while len(sottolinea) > lunghezzaparola:
                        
                        if sottolinea.startswith(parola) and not sottolinea[lunghezzaparola].isalpha():
                                                
                            ParolaTrovata = True
                        
                            ListaPostTrovati.append(NumeroPost)
                        
                            break
                        
                        #Trovo il primo carattere di spazio, se presente
                        
                        indicecarattere = 0
                        
                        while sottolinea[indicecarattere].isalpha():
                            
                            indicecarattere += 1
                            
                        sottolinea = sottolinea[indicecarattere + 1:]
            
        linea = FilePost.readline()
            
    FilePost.close
    
    return set(ListaPostTrovati)
