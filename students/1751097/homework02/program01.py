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
Due parole sono considerate uguali anche se  alcuni caratteri alfabetici compaiono in una 
in maiuscolo e nell'altra in minuscolo.

Per gli esempi vedere il file grade.txt

AVVERTENZE:
	non usare caratteri non ASCII, come le lettere accentate;
	non usare moduli che non sono nella libreria standard.
NOTA: l'encoding del file e' 'utf-8'
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero.
'''
# -*- coding: utf-8 -*-

import re

def post(fposts,insieme):
    ''' implementare qui la funzione'''
    dizionario_post={} # inizializzo il dizionario e liste appoggio
    lista_post=[]
    lista_testi=[]
    post=""
    result = set()
    # gestisco apertura del file
    with open(fposts, "r", encoding="utf-8") as dati:
        contatore_post=1
        testo_post=""
        for riga in dati:
            #if not riga: continue
            riga=riga.strip() # pulisco riga
            if riga.find('<POST>') !=-1:
                if contatore_post > 1: # verifico che sto leggendo i post successivi al primo
                    lista_post.append(post)
                    lista_testi.append(testo_post)
                    testo_post=""
                # ricavo il numero del post
                post=riga[6:].strip() # il numnerello starà dentro post. partiamo da fine <post>, eliminiamo spazi e otteniamo numero. (SLICE)
                contatore_post+=1
            else:
                # sto leggendo righe di testo da associare a un post
                # rimpiazzo i caratteri non alfabetici con lo spazio
                testo_post+=re.sub('[^a-zA-Z]+', " ", riga).lower() + " "
        # all'uscita della lettura devo elaborare l'ultimo POST
        lista_post.append(post)
        lista_testi.append(testo_post)
        dizionario_post= getparole(lista_post, lista_testi) # funzione accoppia Post, testo.
        result = find_id(insieme, dizionario_post)         # Ritorna gli Id dei post che contengono almeno una delle parole trovate.   

    return result


    
"""
questa funzione restituisce un dizionario di insiemi di parole.
"""
def getparole(lista_post, lista_testi):
    dict_insiemi_parole = {}
    raccolta_parole = []                      # Inizializzo lista di insiemi parole.
    for testo in lista_testi:                 # Ciclo i testi dalla oppurtina lista.
       lista_new = testo.split(" ")           # trasformo le parole in elementi di una lista.
       raccolta_parole.append(set(lista_new)) # elimino parole duplicate e aggiungo l'insieme a una lista.
    dict_insiemi_parole = dict([(post, parole) for post, parole in zip(lista_post, raccolta_parole)]) # Dict comprehension perchè si.
    return dict_insiemi_parole

"""
questa funzione restituisce l'insieme degli Id dei post contenenti le parole da trovare.
"""
   
"""         
def find_id(insieme, dizionario_post):   
    postId = set()                                              # Inizializzo lista insieme per uso futuro.
    for id_post, insieme_parole in dizionario_post.items(): # Ciclo contemporaneamente il dizionario che stristuisce chaive, valore.
        for parola in insieme:                                      # Ciclo le parole dell' insieme fornito in input.
            if parola.lower() in insieme_parole:                # Se parola è contenuta in dizionario, allora aggiungo il post al mio insieme.
                postId.add(id_post)
    return postId 
"""
def find_id(insieme, dizionario_post):   
    postId = set()                                              # Inizializzo lista insieme per uso futuro.
    for id_post, post_insieme in dizionario_post.items(): # Ciclo contemporaneamente il dizionario che stristuisce chaive, valore.
        for parola in insieme:                              # Ciclo le parole dell' insieme fornito in input.
            if parola.lower() in post_insieme:                # Se parola è contenuta in dizionario, allora aggiungo il post al mio insieme.
                postId.add(id_post)
                break
    return postId 


if __name__ == '__main__':
    args        = ('file01.txt', {'return'})
    returned    = post(*args)    

