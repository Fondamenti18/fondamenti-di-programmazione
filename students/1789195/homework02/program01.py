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
	lst=[]	#lista lst
	lstPost=[]	#lista post
	lstDef=[]	#lista definitiva
	with open(fposts, encoding='utf-8') as f:	#apre file 
		testo = f.read()	#legge tutto il file e lo mette nella variabile testo
		
		lst=testo.lower().strip().split('<post>')	#inserisce in una lista il testo, convertito in lettere minuscole, eliminati spazi iniziali e finali, e splittato rispetto alla parola post
		for carattere in lst: #scorre lista lst
		  t=''.join(carattere)    #nella variabile 't' inserisce la lista convertita in stringa
		  for i in t: #scorre la variabile t
		      if not i.isalnum(): #se il carattere non è alfanumerico
		          t=t.replace(i,' ')  #elimina il carattere dalla stringa t
		  t=t.split() #splitta la stringa 
		  for val in insieme: #scorre l'insieme
		      if(val.lower() in t):   #se il valore convertito in minuscolo è presente nella lista t
		          lstDef.append(t[0]) #aggiunge alla lista lstDef il valore nell'indice 0 della lista t
		      		      
	return(set(lstDef))	#ritorna un insieme, converto con set la lista lstDef
	
if __name__ == '__main__':  
	print(post('file01.txt', {'return'}))
	