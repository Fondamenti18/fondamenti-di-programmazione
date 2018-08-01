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

	with open(fposts, encoding = 'utf-8') as f:
		page = f.read().lower()

	caso = list(insieme)
	for i in range(len(caso)):
		caso[i] = caso[i].lower()
	insieme = set(caso)

	returnSet = set()
	returnSetFinal = set()
	page = page.replace('\n', ' ')
	newPage = ''
	stringa = ''
	letteraPrev = ''
	for valore in page:
		for lettera in valore:
			if lettera == ' ':
				if lettera == letteraPrev:
					stringa += ''
				else:
					stringa += ' '
			elif lettera == '>':
				stringa += '> '
			elif lettera == '\n':
				stringa += '\n '
			elif lettera == '<':
				stringa += '<'
			elif (ord(lettera) >= 97 and ord(lettera) <= 122) or (ord(lettera) >= 65 and ord(lettera) <= 90) or (ord(lettera) >= 48 and ord(lettera) <= 57):
				stringa += lettera
			elif (ord(lettera) == 91 or ord(lettera) == 93):
				stringa += ' '
			letteraPrev = lettera
	newPage += stringa
	stringa = ''
	newPage = newPage.split('<post>')
	for val in newPage:
		if(len(val) > 1):
			subList = val.split()
			a = [subList[0]]
			setTemp = set(subList[1:])
			if (len(insieme & setTemp) > 0):
				returnSetFinal = returnSetFinal | set(a)
	return returnSetFinal

#post('file01.txt', {'non','Si'})
