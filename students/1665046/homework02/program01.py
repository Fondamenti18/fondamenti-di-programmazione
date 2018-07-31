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

import re 

def noalpha(s):
	noa = ''
	for c in s:
		if not (c in noa or c.isalpha()):
			noa += c
	return noa 



def words(s):
	noa = noalpha(s)
	for c in noa:
		s = s.replace(c, ' ')
	return s.split()




def post(fpost,insieme):
	dizionario = {}
	chiavediz = set()
	f = open(fpost,'r')
	text = f.read()
	f.close()
	match = re.findall(r'(<POST>)(\s*)(\d+)(\n*)((\w*[\s,.:?!\'()=\;\_\]\[\*\-\+]*)+)(\n*)',text, re.UNICODE)
	for tupla in match:
		dizionario[tupla[2]]=tupla[4].lower()
	for k, v in dizionario.items():
		ww = words(v)
		contains = el_in_list(insieme, ww)
		if contains:
			chiavediz.add(k)
	return chiavediz 


def el_in_list(l1,l2):
	# l1 è l'insieme del pofessore
	# l2 è il valore associato a una chiave
	for w in l1:
		if w.lower() in l2:
			return True
	return False 



#def post(fposts,insieme):

