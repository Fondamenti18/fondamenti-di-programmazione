'''
I post di un forum sono raccolti in alcuni file che hanno il seguente formato. 
Un file contiene uno o piu' post, l'inizio di un post e' marcato da una  che contiene
in sequenza le due sottostringhe "<POST>" ed "N" (senza virgolette) eventualmente 
inframmezzate, precedute e/o seguite da 0,1 o piu' spazi. 
"N" e' l'ID del post (un numero positivo).  
Il contenuto del post e' nelle lineae successive fino alla  che marca il prossimo post 
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
    
	with open(fposts, 'r', encoding = 'utf-8') as IN:

		d = {}

		for linea in IN:
			if(linea.find("<POST>") != -1):
				linea = linea.strip().split("<POST>")
				numero = ""
				for carattere in linea[1]:
					if(carattere.isdigit()):
						numero += carattere
				post_corrente = int(numero)
				d[post_corrente] = []
			else:
				linea = " ".join(linea.split())
				linea = linea.split(" ")
				for elemento in linea:
					parola = ""
					for carattere in elemento:
						if(carattere.isalpha()):
							parola += carattere
						else:
							break
					d[post_corrente].append(parola.lower())

	post_contenenti = set()

	for parola in insieme:
		parola = parola.lower()
		for chiave in d:
			if parola in d[chiave]:
				post_contenenti.add(str(chiave))

	return post_contenenti
