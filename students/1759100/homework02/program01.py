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
    la=[]
    risultato=set()
    with open(fposts,encoding='utf-8') as file:
        file=file.read() 
        post=file.splitlines() #elimina i caratteri di escape
        post=' '.join(post) #riunisce tutti gli elementi della lista con lo spazio
        post=post.split()
        post=elimina_spazi(post) #elimina eventuali spazi superflui
        post=post.split('<POST>')
        insieme=modifica(insieme)#trasforma l'insieme in una lista di stringhe minuscole
        for elemento in post: #per ogni elemento nel post cancella eventuali caratteri speciali
            l=elemento.split()
            la.append(''.join(l[:1])+' '+ delete(' '.join(l[1:])))
        post=la
        for elemento in post: #per ogni post cerca l'id 
            ID=itera(elemento,insieme)
            if ID!=None: #se l'ID non è nullo lo aggiunge all'insieme di ritorno
                risultato.add(ID)
    return risultato
    
def modifica(lis):
    '''ritorna l'insieme delle parole dove le parole sono tutte minuscole'''
    l=[]
    for elemento in lis:
        l.append(elemento.lower())
    return l

def itera(l1,l2):
    riga=l1.split() #splitta la riga tramite gli spazi
    for elemento in riga: #per ogni elemento della riga chiama la funzione verifica
        if verifica(elemento,l2)==1: #se verifica restituisce 1 ritorna riga[0] che corrisponde all'ID
            return riga[0]
            
        
def verifica(elemento,l2):
    i=0
    while i<len(l2): #per ogni parola nell'insieme verifica se la parola è uguale all'elemento in input
        #print(l2[i],elemento)
        if l2[i]==elemento:
            return 1 #se sono uguali restituisce 1
        else:
            i+=1 #altrimenti incrementa l'indice

    
        
def elimina_spazi(lst): #elimina eventuali spazi superflui
    la=[]
    for elemento in lst:
        if elemento!=' ':
            la.append(elemento)
    return ' '.join(la)
    
def delete(txt): #elimina caratteri speciali
    special=',.*+1234 567890-[]={}_:();!?|/"\''
    for char in special: #per ogni carattere speciale, se è presente nel testo lo splitta
        if char in txt:
            txt=txt.split(char)
            txt=elimina_spazi(txt)#elimina spazi superflui
    txt=txt.lower() #riduce tutte le lettere a minuscole
    return txt
    


    
