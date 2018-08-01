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
    
    insieme_ris = set()                    # L'insieme_ris sarebbe l'elenco degli ID da ritornare
    apri_testo = open (fposts)
    leggi_il_testo=apri_testo.read()                 
    splitta_il_testo=leggi_il_testo.split('<POST>')
    
    for el in splitta_il_testo:
        skywalker = el.split()
        for luke in skywalker:
            vader = list(luke)
            for darth in vader:
                if darth=='[':              # L'[i] dà molto fastidio
                    darth='q'
                if darth==']':              # IDem
                    darth='q'
                if darth.isalpha()==False:
                    vader.remove(darth)
                else:
                    pass
                darthvader=''.join(vader)
            quasi_finito = darthvader.lower()
            
            for han in insieme:
                solo = han.lower()
                if solo == quasi_finito:
                    insieme_ris.add(skywalker[0])
                else:
                    pass
    insieme_ris==insieme
    
    return insieme_ris










