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
    
    # Importo i moduli string e codecs #
    
    import string
    import codecs
    
    # Utilizzando str.maketrans costruisco la tabella di decodifica in spazio dei caratteri speciali (string.punctuation) #
    
    tab_decod_car_spec = str.maketrans(string.punctuation, '                                ') # 32 spazi #
    
    # Creo un insieme (risultato) e lo inizializzo con un elemento superfluo che andrò ad eliminare #
    
    risultato = {'zac'}
    
    # Apro in sola lettura il file_input con la codifica utf-8 #
    
    try:
        file_input = codecs.open( fposts, "r", "utf-8" )
    
    except:
        print ('Il file', fposts, 'non è stato trovato')
        print(' ')

    '''
    Realizzo un ciclo di lettura di tutte le parole contenute nell'insieme (insieme) e dato che
    mi viene chiesto di considerare due parole uguali anche se il maiuscolo e il minuscolo non
    coincidono trasformo la parola_ins (cioè quella da cercare) in caratteri minuscoli.
    '''

    for parola_ins in insieme:
        parola_da_cercare  = str.lower(parola_ins)

        # Leggo riga per riga il file #
        
        for line in file_input:

            if line == '\n':
                pass
            
            # Se la riga non è vuota effettuo la trascodifica di ciascun carattere speciale in uno spazio #
            
            else:  
                linea_pulita = line.translate(tab_decod_car_spec)
                
                # con str.split divido la frase della riga (line) in stringhe di carattere minuscolo #
                
                linea_da_analizzare = str.split(str.lower(linea_pulita))
                
                for parola in linea_da_analizzare:
                    
                    # Se la parola è 'post' prendo la stringa con indice 1 cioè l'ID del post #
                    
                    if parola == 'post':
                        ID_del_post = linea_da_analizzare[1]
                        break
                
                # Cerco la parola nella linea e se la trovo aggiungo all'insieme risultato l'ID del post #
                    
                for parola in linea_da_analizzare:
                    
                    if parola == parola_da_cercare:
                        risultato.add(ID_del_post)
                        break
        
        # Punto alla prima riga del file #
        
        file_input.seek(0)
        
        risultato.discard('zac')
        
    return risultato