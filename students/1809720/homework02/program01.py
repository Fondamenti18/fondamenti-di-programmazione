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
    import re                                                                      #importo la libreria re (regular expressions)     
                                                                                   #per poter usare i comandi di ricerca re.findall         
    def check_numero_post(k):
        n_post = []                                                                # k è una lista contenente tutti i post
        stringa_post = str(k)                                                      # la posizione x-esima di k viene trasformata in stringa                                                                                # quindi un singolo post viene messo in stringa_post
        n_post = re.findall(r'^\D*(\d+)', stringa_post)                            # avviene la ricerca del primo numero tramite re.findall ecc..
        return n_post                                                              # trovabile all'interno nel post, ovvero n_post
            
    def check_parole(insieme, k):   
        lista = list(insieme)                                                      # l'insieme viene trasformato n lista
        lista_numeri = []                                                          # dichiaro la lista dove andrà a finire il numero del post
        i=0                                                                        # in cui vengono trovati gli elementi che cerchiamo
        x=1
        while x<len(k):                                                            # scorro la lista contenente tutti i post del file
            while i<len(lista):                                                    # scorro la lista contentente le parole da cercare 
                solv = re.findall('[A-Za-z0-9_]+', k[x])                           # uso la re per cercare la parola in k[x] e la metto in solv 
                if (lista[i].lower() in solv) or (lista[i].title() in solv):       # metto un if che funzioni sia per maiuscole che per minuscole 
                    appoggio = check_numero_post(k[x])                             # richiamo la funzione che trova il numero del post e lo metto 
                    lista_numeri = lista_numeri + appoggio                         # in una variabile di appoggio, che poi metto nella lista_numeri     
                i+=1
            i=0                                                                    # qua metto i=0 per ricominciare dal primo elemento di insieme 
            x+=1
        return(lista_numeri)

    datafile = open(fposts, encoding="utf-8")                                      # apro il file, fpost è il nome, encoding è nel testo dell'es. 
    string = ''                                                                    # preparo una stringa vuota 
    for x in datafile:                                                             # scorro il file 
        string = string + x                                                        # metto in string ogni linea del file
    k = string.split("<POST>")                                                     # splitto la stringa in una lista, con <POST> come separatore 
    result = check_parole(insieme, k)                                              # richiamo la funzione definita sopra 
    r=set(result)                                                                  # ritrasformo il risultato in un insieme
    return r                                                                       # restituisco l'insieme 