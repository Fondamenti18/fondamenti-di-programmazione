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

def conversione(fposts , insieme):

    #conversione di un file in una stringa s
    s = ''
    for l in open(fposts).readlines():
        s += l
    s = s.lower()
    s = s.replace('<post>',' <post> ')
    
    
    tmp = ''
    for conta , val in enumerate(s):
        if s[conta].isalnum() == True or s[conta].isspace() == True or s[conta] == '<' or s[conta] == '>':
            tmp += s[conta]
        else:
            tmp += ' '
    s = tmp
    s = s.split()    #spezza una stringa in una lista di elementi, tranne gli spazi
    
    #conversione dell'insieme in una stringa s2, e poi in una lista
    s2 = ''
    for i in insieme:
        s2 += i + ' '
    s2 = s2.lower()
    s2 = s2.split()
    
    return s , s2
    
def post(fposts,insieme):
    stringa , lista = conversione(fposts,insieme)
    
    risultato = set()
    tmp = set()
    indice = ''
    for l in lista:
        for conta , val in enumerate(stringa):
            if val == '<post>':
                indice = stringa[conta + 1]
            elif val == l:
                tmp = {indice}
                risultato = risultato | tmp
    
    return risultato
    
if __name__ == '__main__':
    print(post("file01.txt" , {'no'}))
