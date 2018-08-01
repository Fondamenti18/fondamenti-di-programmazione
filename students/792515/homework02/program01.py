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
    lsFilePost=[] #lista che conterrà tutti i record del post...
    strIDFilePost='' #stringa che contiene l'ID del post
    lsIDFilePostOccorrenze=[] #lista che conterrà le ID dei post con le occorrenze delle parole...
    lsParole=[] #lista che conterrà le parole (codici alfanumerici) trovate in ciascun record del file
    lsParoleInsiemeMaiusc=[] #lista che conterrà le parole dell'insieme formattate in maiuscolo
    Failetto=open(fposts,'r', encoding='utf-8') #apro il file in sola lettura
    lsFilePost=Failetto.readlines() #metto i record del file in una lista
    Failetto.close() #chiudo il file
    LenMin=999 #questa variabile conterrà la lunghezza della più piccola parola nell'insieme in input
    lsParoleInsiemeMaiusc, LenMin = FormatInsieme(insieme) #ricavo la lista con le parole dell'insieme in input in maiuscolo, ed anche il valore della lunghezza della più piccola parola dell'insieme
    for i in range(len(lsFilePost)): #ciclo su tutti i record del file (precedentemente inseriti nella lista lsFilePost)
#Se trovo la parola <POST>, scrivo l'ID del post nella stringa strIDFilePost...
        if fnStrPost(lsFilePost[i]):
            strIDFilePost=fnIDPost(lsFilePost[i])
            Trovato=False
#... se non trovo l'ID, vuol dire che sono in una riga con del testo. Ricercherò le parole dell'insieme a due condizioni:
#1) non devo aver già trovato prima, nello stesso post, un'occorrenza di una parola presente nell'insieme in input
#2) la lunghezza della riga deve essere maggiore o uguale alla lunghezza della più piccola parola nell'insieme in input
        elif Trovato==False and len(lsFilePost[i].strip())>=LenMin:
            lsParole=fnAlfabetico(lsFilePost[i].strip())
#...se ho trovato un'occorrenza, aggiungo la stringa con l'ID del post alla lista delle occorrenze...
#...avendo trovato un'occorrenza, non ho più bisogno di cercare occorrenze nello stesso post (Trovato==True)...
            if len (set(lsParoleInsiemeMaiusc) & set(lsParole))>0:
                lsIDFilePostOccorrenze=lsIDFilePostOccorrenze+[strIDFilePost]
                Trovato=True
    return set(lsIDFilePostOccorrenze)

#La funzione restituisce True se la sottostringa "<POST>" si trova all'interno della stringa in input, FALSE altrimenti
def fnStrPost(strPost):
    return '<POST>' in strPost

#la funzione restituisce l'ID del post...
def fnIDPost(strPost):
    lsNumeri=['0','1','2','3','4','5','6','7','8','9']
    strIDPost=''
    for i in range(len(strPost)):
        if strPost[i] in lsNumeri:
            strIDPost=strIDPost+strPost[i]
    return strIDPost

#Questa funzione analizza il testo del post distinguendo i caratteri alfabetici dai caratteri non alfabetici. Le parole (isalpha()='True') vengono riportate in maiuscolo nella stringa "strAlfabetico" e separate da un underscore
def fnAlfabetico(strPost):
    lsAlfabetico=[]
    strAlfabetico=''
    for i in range(len(strPost)):
        if strPost[i].isalpha():
            strAlfabetico=strAlfabetico+strPost[i].upper()
        else:
            lsAlfabetico=lsAlfabetico+[strAlfabetico]
            strAlfabetico=''
    lsAlfabetico=lsAlfabetico+[strAlfabetico]
    return lsAlfabetico

#Questa funziona formatta l'insieme mettendo le parole in maiuscolo e ricavando la lunghezza minima delle parole...
def FormatInsieme(insi):
    lsFormatInsieme=[]
    LunghezzaMinima=999
    for parola in insi:
        lsFormatInsieme=lsFormatInsieme+[parola.upper()]
        if len(parola)<LunghezzaMinima:
            LunghezzaMinima=len(parola)
    return lsFormatInsieme, LunghezzaMinima