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
POST = "<POST>"

'''main function, returna gli ID dei post contenenti le stringhe date in input'''
def post(fposts,insieme):
	data = load_file(fposts)
	indexes = set(list())
	for i,l in enumerate(data):
		line = l
		text = ""
		index = 0
		if(is_post(line)):
			line = clean_post(line)
			index = i+1
		while(index < len(data) and not is_post(data[index])):
			text += (data[index])
			index += 1
			i = index
		text = text.lower().split()
		for e in insieme:
			for c in text:
				if(not e.lower() in c): continue
				if(e.lower() == clean_string(c)):
					indexes.add(line)
	return indexes

'''verifica se la stringa data in input e' un post'''
def is_post(line):
	return POST in str(line)

'''funzione eseguita su una riga contenente la costante POST e la pulisce mantenendo solo l'id'''
def clean_post(s):
	temp = ""
	for c in s:
		if(c.isdigit()):
			temp += c
	return temp

'''pulisce la stringa restituendone una nuova con solo caratteri che rispettano isalpha()'''
def clean_string(s):
	new_string = ""
	for c in s:
		if(c.isalpha()):
			new_string += c
	return new_string

'''carica in memoria il file txt dato in input'''
def load_file(f):
	data = []
	with open(f) as my_file:
		for line in my_file:
			data.append(line)
	return data
