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
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero
for j in k:
            if j<='A' or j<='Z':
                j=j.lower()
                print(j)
                stringa = stringa + j
            else:
                stringa=stringa+j



while i != len(stringa):                #vedo gli identificativi del post
                    if stringa[i].isnumeric()==True:
                    i=i+1
                    print(num)
.
'''


def post(fposts,insieme):
    #print(fposts)
    f = open(fposts)
    stringa=""
    num=""
    finale = []
    stringa1 = []
    temp = []
    k = ""#conversione tutto in minuscolo
    for h in insieme:
        k=k+h.lower()
        temp=temp+[k]
        k=""
        #print(temp)
    for line in f:
        stringa=""
        i=0
        stringa1=[]
        #print(line)
        if "<POST>" in line:
            stringa=line
            num=""
            #print(line)
            
            while i != len(stringa):
                    #print("lavoro")           #vedo gli identificativi del post
                    if stringa[i].isnumeric()==True:
                        num=num+ stringa[i]
                        
                        
                        print(num)
                    i=i+1
        else:
            stringa=line.lower()
            j=0
            i=0
            stringa1=stringa1+pulizia(stringa)
            if num=="10":
                print(stringa1)
            while j != len(temp):
                i=0
                while i != len(stringa1):
                    #print(temp)
                    if temp[j] == stringa1[i]:
                            #print(temp[j])
                            finale = finale + [num]
                    i=i+1
                    
                j=j+1
    f.close()
    #finale=sorted(set(finale))
    finale=set(finale)
    return(finale)
def pulizia(chiave):                 #funzione che elimina tutto ciò che non è alfabeto minuscolo
    new = ""
    new1 = []
    for carac in chiave:        #eliminaziuone caratteri strani
        if 'a'<= carac and   carac <= 'z':
            new=new + carac
        else:
            new1=new1 + [new]
            new=""
    #print(new1)
    return(new1)
                

