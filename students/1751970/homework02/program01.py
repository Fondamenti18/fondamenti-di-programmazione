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
    with open(fposts, 'r') as f:variabile=f.read()   
    d={}
    lista2=[]
    if "<POST>" in variabile: #se c'è <POST> in variabile
        lista = variabile.split('<POST>') #divido il testo quando c'è <POST>
        for valore in lista: 
            for chiave in valore.split(): 
                if chiave.isdigit(): #prendo il numero identificativo del post
                    d[chiave]=valore # e lo metto come chiave del dizionario
    
                    for x in valore:
                        lista = [c if c.isalpha() else "*" for c in x] #se non è alfabetico metto *
                        lista2 += ''.join(lista) #lo aggiungo alla lista2
                        lista2=''.join(lista2) #trasformo la lista2 in stringa
                    d[chiave]=lista2 #metto lista2 come valore del dizionario
                    parole=lista2.split("*") #elimino *
                    appoggio=parole[:] #faccio una copia di parole in appoggio
                    
                    for x in appoggio:
                        if x =="":
                            parole.remove(x) #rimuovo tutti gli spazi vuoti
                        d[chiave]=parole #aggiorno il contenuto di valore nel dizionario
                    lista2=[]
    w=[]
    for chiave, valore in d.items():  #itero sulla chiave e il valore del dizionario     
        for x in valore:
            x=x.lower() #trasformo la stringa tutta minuscola
            for y in insieme:
                y=y.lower() #trasformo la stringa tutta minuscola
                if x==y: #se x è uguale a y
                    w.append(chiave) #aggiungi la chiave del dizionario a w
    if '0' in w:
        w.remove('0')
    
    c=set(w)
    return c

