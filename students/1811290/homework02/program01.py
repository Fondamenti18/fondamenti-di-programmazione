'''
I post di un forum sono raccolti in alcuni file che hanno il seguente formato. 
Un file contiene uno o piu' post, l'inizio di un post e' marcato da una linea
che contiene in sequenza le due sottostringhe "<POST>" ed "N" (senza virgolette)
eventualmente inframmezzate, precedute e/o seguite da 0,1 o piu' spazi. 
"N" e' l'ID del post (un numero positivo).  
Il contenuto del post e' nelle linee successive fino alla linea che marca il
prossimo post  o la fine del file (si veda ad esempio il file "file01.txt"). 
E' assicurato che la stringa "<POST>" non e' contenuta in nessun post.

Nel seguito per parola intendiamo come al solito una qualsiasi sequenza di
caratteri
alfabetici di lunghezza massimale. I caratteri alfabetici sono quelli per cui
ritorna True il metodo isalpha().

Scrivere una funzione post(fposts,insieme) che prende in input:
- il percorso di un file (fposts) 
- ed un insieme  di parole (insieme)
e che restituisce un insieme (risultato).


L'insieme restituito (risultato) dovra' contenere gli identificativi (ID)
dei post che contengono almeno una parola dell'inseme in input.
Due parole sono considerate uguali anche se  alcuni caratteri alfabetici
compaiono in una in maiuscolo e nell'altra in minuscolo.

Per gli esempi vedere il file grade.txt

AVVERTENZE:
	non usare caratteri non ASCII, come le lettere accentate;
	non usare moduli che non sono nella libreria standard.
NOTA: l'encoding del file e' 'utf-8'
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di
quel test e' zero.
'''

import string
def post(fposts,insieme):
    a=open(fposts,encoding='utf-8') #apre il testo con variabile a
    elenco_post=[]
    trovato_elemento_nel_post = 'F'

    #Converto l'insieme dato in minuscole
    stringa_minuscola_insieme=""
    parola_minuscola_insieme=[]
    for x in insieme:
        stringa_minuscola_insieme = x.lower()
        parola_minuscola_insieme.append(stringa_minuscola_insieme)
    insieme_minuscolo = set(parola_minuscola_insieme)    

    for linea in a:
     
        #controllo se c'e' POST. Se c'e', trovo l'ID del post e lo salvo in una variabile
        if linea.find('<POST>')!=-1:
            pos_ini_post = linea.find('<POST>')
            numero_post=''
            trovato_elemento_nel_post = 'F'
            for k in range(pos_ini_post+6,len(linea)):
                if ord(linea[k:k+1])>= 48 and ord(linea[k:k+1]) <= 57 :
                    numero_post=numero_post+linea[k:k+1]
 
        #Per velocizzare il programma, faccio la ricerca degli elementi dell'insieme sulle nuove linee solo
        #se il POST non e' gia' nel mio elenco.
        if trovato_elemento_nel_post == 'F':
           #converto la linea in minuscole
            linea_minuscola = linea.lower()
   
            #Pulisco la linea dai caratteri non alfabetici sostituendoli con spazi,
            #(che verranno eliminati con il successivo split)
            linea_alfabetica = ""
            for k in range (0,len(linea_minuscola)):
                if linea_minuscola[k:k+1].isalpha():
                    lettera_da_inserire = linea_minuscola[k]
                else:
                    lettera_da_inserire = ' '
                linea_alfabetica = linea_alfabetica+lettera_da_inserire

            #Inserisco le parole della linea (minuscole e solo alfabetica) in una lista
            lista_parole=linea_alfabetica.split()
           
            #elementi_insieme = len (insieme)
            elementi_lista = len (lista_parole)
            # controllo se le parole della linea sono nell'insieme 
            for k in range (0, elementi_lista):
                if lista_parole[k] in insieme_minuscolo:
                    elenco_post.append(numero_post)
                    trovato_elemento_nel_post ='T'
                    break
                
      
    insieme_da_ritornare = set(elenco_post)
    return insieme_da_ritornare


post('file01.txt',{'non','Si'})
