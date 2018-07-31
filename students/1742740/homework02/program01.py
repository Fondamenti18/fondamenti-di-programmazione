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

def noalpha(testo): #funzione che torna una stringa di caratteri non alfabetici nel testo
    noalfa=""
    for y in testo:
        for i in y:
            if not i.isalpha() and i not in noalfa:
                noalfa+=i
    return noalfa

def sostituire(arg): #funzione che sostituisce i caratteri noalpha con spazi
    noalfa=noalpha(arg)
    for y in noalfa:
        arg=arg.replace(y," ")
    return arg.lstrip()

def indici(stringa): #funzione che torna una lista con gli indici dei vari posts
    lista=stringa.lstrip().split("<POST>")
    l_indici=[]
    for i in range(len(lista)):
        v=lista[i]
        v=v.lstrip()
        if v=='':
            continue
        indice=''
        j=0
        while v[j].isnumeric(): #gli indici dei posts sono i primi numeri nella stringa
            indice+=v[j]
            j += 1
        l_indici.append(indice)
    return l_indici

def trova(parola,testo): #funzione che torna true se parola e' in testo
    testo=testo.split()
    for i in testo:
        if parola.lower()==i:
            return True
            break
    return False



def post(fpost,insieme):
    with open(fpost,encoding='utf-8') as doc: #apre il documento
        doc=doc.read()
        risultato=[]
        lista_post=doc.lstrip().split("<POST>") #crea la lista con i vari posts
        lista_indici=indici(doc) #crea la lista con gli indici dei vari posts
        i=0
        max=len(lista_post)
        while i<max:
            if lista_post[i]=='': #se il post e' vuoto lo cancella
                del(lista_post[i])
                max-=1
                continue
            lista_post[i] = sostituire(lista_post[i].lower()).lstrip() #chiama la funzione che pulisce il testo sul post
            for parola in insieme:
                if trova(parola,lista_post[i]): #se una delle parole in insieme e' nel post[i] aggiunge l'indice i del post al risultato
                    risultato.append(lista_indici[i])
                    break
            i+=1
        return set(risultato)




