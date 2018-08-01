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
    import collections
    parole = []
    numeri = []
    post = dividiPost(fposts)
    
    for lista in post:
        
        parole += [[parole for parole in creaListaParole(lista)]]
        numeri += [' '.join([numeri for numeri in creaListaNumeri(lista)])]
    
   
    dizionario = [(k,v) for (k, v) in zip(numeri, parole)]   
    dizionario = collections.OrderedDict(dizionario)
   

    risultato = trova(dizionario, insieme)
    return risultato




def dividiPost(fposts):
    '''lista del file in singoli post'''
    
    f = open(fposts, encoding = 'UTF-8')
    s = f.read()
    a1 = s.lower()
    a = a1.split('<post>')  #abbiamo il file diviso per post
    return a
        

def creaListaParole(fposts):
    '''di ogni singolo post crea la lista delle parole'''
    parole = []
    parola = ''
    for carattere in fposts:
        if carattere.isalpha(): parola += carattere
        else: 
            if parola: 
                parole.append(parola)
                parola = ''
    if parola: parole.append(parola)
    return parole


def creaListaNumeri(fposts):
    '''di ogni singolo post crea la lista dei numeri'''
    numeri = []
    numero = ''
    for carattere in fposts:
        if carattere.isnumeric(): numero += carattere
        else: 
            if numero: 
                numeri.append(numero)
                numero = ''
                break
    if numero: numeri.append(numero)
    return numeri

def trova(dizionario, insieme):
    lista = []
    for parola in insieme:
        parola = parola.lower()
        lista += ((k) for k,v in dizionario.items() if parola in v) 
        
    risultato = set(lista)
    return risultato









if __name__ == '__main__':
    post('file01.txt', {'no'})


