'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3x3 caselle.
A turno, i due giocatori scelgono una cella vuota e vi disegnano il proprio simbolo 
(un giocatore ha come simbolo una "o" e l'avversario una 'x'). 
Vince il giocatore che riesce a disporre tre dei propri simboli in linea retta 
orizzontale, verticale o diagonale. Se la griglia viene riempita 
senza che nessuno dei giocatori sia riuscito a completare una linea 
retta di tre simboli, il gioco finisce in parita'. Nel caso in cui il gioco 
finisse in parita', la partita e' detta "patta". 
Per convenzione a griglia vuota la prima mossa spetta sempre al giocatore 'o'

Una configurazione del gioco e' dunque univocamente determinata  dal contenuto della griglia.

Nel seguito assumiamo che il contenuto della griglia sia  rappresentato tramite  lista di liste.
La dimensione della lista di liste M e'  3x3 ed   M[i][j] contiene  '', 'x', o 'o'  a seconda 
che la cella della griglia appartenente all'iesima riga e j-ma colonna sia ancora libera, 
contenga il simbolo 'x' o contenga il simbolo 'o'. 

Data una configurazione C del gioco, l'albero di gioco per C e' l'albero che 
si ottiene ricorsivamente partendo dalla configurazione C e assegnando come figli le configurazioni 
che e' possibile ottenere da C con una mossa ulteriore del gioco. Ovviamente  risulteranno 
foglie dell'albero i possibili esiti della partita vale a dire le diverse configurazioni cui e' 
possibile arrivare partendo da C e che rappresentano patte, vittorie per 'o' o vittorie per 'x'.
Se veda ad esempio l'immagine albero_di_gioco.png che mostra l' albero di gioco che si ottiene a partire 
dalla configurazione rappresentata da [['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
 

Si consideri la seguente Classe di oggetti:


class NodoTris:
	def __init__(self, griglia):
		self.nome = griglia
		self.lista_figli = [] 


Bisogna progettare le seguente  funzione 

gen_tree(griglia)
che, data la configurazione di gioco griglia,  costruisce l'albero di gioco che si ottiene a partire 
dalla configurazione griglia e ne restituisce la radice. I nodi dell'albero devono essere 
oggetti della classe NodoTris.

Per testare la correttezza della vostra implementazione di gen_tree() il grade utilizzera' quattro metodi 
della   classe NodoTris che dovete comunque implementare: 

1)
tipo(self)
che, dato un nodo NodoTris, restituisce:
 'o' se la configurazione rappresentata dal nodo e' una configurazione di vittoria per il giocatore 'o'
 'x' se la configurazione rappresentata dal nodo e' una configurazione di vittoria per il giocatore 'x'
 '-' se la configurazione rappresentata dal nodo e' una configurazione di patta
 '?' se la configurazione rappresentata dal nodo e' una configurazione di gioco non ancora terminato

2)
esiti(self)
che, dato un nodo radice di un albero di gioco, restituisce una tripla con i possibili 
esiti della partita che ha come configurazione iniziale quella rappresentata dal nodo. 
Piu' precisamente: il primo elemento della tripla  e' il numero di  patte possibili, 
il secondo e' il numero di possibili vittorie  per il giocatore 'o' mentre  il terzo elemento 
e' il numero di possibili vittorie per il giocatore 'x'.

3)
vittorie_livello(self, giocatore, h)
che, dato un nodo radice di un albero di gioco, uno dei due giocatori ed un intero h,
restituisce il numero di nodi che rappresentano una vittoria per il giocatore e si 
trovano ad altezza h nell'albero. In altri termini restituisce il numero di vittorie possibili 
per giocatore in esattamente h mosse, nella partita che ha come configurazione iniziale 
quella rappresentata dalla radice dell'albero.

4)
strategia_vincente(self,giocatore)
che, dato un nodo radice di un albero di gioco ed uno dei due giocatori, restituisce True o False. 
Restituisce True  se  giocatore ha una strategia vincente  nella partita 
che ha come configurazione iniziale quella rappresentata dal nodo radice, False altrimenti.

Nota che un giocatore ha una strategia vincente rispetto ad una certa configurazione se, 
qualunque siano le mosse dell'avversario ha sempre la possibilita' di rispondere in modo 
che la partita termini con la sua vittoria.

Potete ovviamente definire ulteriori  funzioni e altri metodi per la   Classe NodiTris 
se li  ritenete utili al fine della risoluzione del compito.

Potete assumere che le configurazioni di gioco rappresentate da griglia siano sempre configurazioni 
lecite (vale a dire ottenute dopo un certo numero di mosse a parire dalla griglia vuota).


AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate; non
importare moduli che non sono nella libreria standard.

ATTENZIONE: i test vengono eseguiti con un timeout globale di 2*N secondi (se il grader esegue N test).
'''

from copy import deepcopy

class NodoTris:
	def __init__(self, griglia, turn=None, livello=0):
		self.nome = griglia
		self.lista_figli = [] #lista dei nodi figli
		self.turno = turn
		self.lvl = livello
	
	def who_play(self):
		griglia_inline = []
		griglia_inline.extend(self.nome[0])
		griglia_inline.extend(self.nome[1])
		griglia_inline.extend(self.nome[2])
		if set(griglia_inline) == {''}:
			self.turno = 'o'
		if griglia_inline.count('x')<griglia_inline.count('o'):
			self.turno = 'x'
		if griglia_inline.count('o')==griglia_inline.count('x'):
			self.turno = 'o'
		#print ((griglia_copy[0].extend(griglia_copy[1])).extend(griglia_copy[2]))
		#print (griglia_copy)
		#if self.griglia

	def tipo(self):
		if self.nome[0].count('o')==3 or self.nome[1].count('o')==3 or self.nome[2].count('o')==3:
			return 'o'
		elif [self.nome[i][0] for i in range(0,3)].count('o')==3 or [self.nome[i][1] for i in range(0,3)].count('o')==3 or [self.nome[i][2] for i in range(0,3)].count('o')==3:
			return 'o'
		elif [self.nome[0][0],self.nome[1][1],self.nome[2][2]].count('o')==3 or [self.nome[0][2],self.nome[1][1],self.nome[2][0]].count('o')==3:
			return 'o'
		elif self.nome[0].count('x')==3 or self.nome[1].count('x')==3 or self.nome[2].count('x')==3:
			return 'x'
		elif [self.nome[i][0] for i in range(0,3)].count('x')==3 or [self.nome[i][1] for i in range(0,3)].count('x')==3 or [self.nome[i][2] for i in range(0,3)].count('x')==3:
			return 'x'
		elif [self.nome[0][0],self.nome[1][1],self.nome[2][2]].count('x')==3 or [self.nome[0][2],self.nome[1][1],self.nome[2][0]].count('x')==3:
			return 'x'
		else:
			for i in range(0,3):
				if '' in self.nome[0] or '' in self.nome[1] or '' in self.nome[2]:
					return '?'
			else:
				return '-'


	def esiti(self,result = None):
		if result is None:
			result = [0,0,0]
		if self.tipo() == '-':
			result[0] += 1
		if self.tipo() == 'o':
			result[1] += 1
		if self.tipo() == 'x': 
			result[2] += 1
		for figlio in self.lista_figli:
			figlio.esiti(result)
		return tuple(result)
	
	def vittorie_livello(self, giocatore, h, result=None):
		if result is None:
			result = 0
		if self.tipo() == giocatore and self.lvl==h:
			result +=1
		for figlio in self.lista_figli:
			result = figlio.vittorie_livello(giocatore,h,result)
		return result
	
	def strategia_vincente(self,giocatore):
		if self.turno==giocatore:
			lista=[] 
			for figlio in self.lista_figli:
				if figlio.esiti()[1]>0:
					lista.append(True)
			if lista.count(True)==len(lista):
				return True
		else:
			for figlio in self.lista_figli:
				figlio.strategia_vincente(giocatore)
		return False



def sviluppa_albero(curr_config):
	possible_moves = []
	for i in range(len(curr_config.nome)):
		for j in range(len(curr_config.nome[0])):
			if curr_config.nome[i][j]=='' and curr_config.tipo()=='?':
				possible_moves.append([i,j])
	if len(possible_moves)>0:
		curr_config.who_play()
		#print (curr_config.turno)
		if curr_config.turno == "o":
			for pair in possible_moves:
				#print (curr_config.nome)
				lista_clone = deepcopy(curr_config.nome)
				lista_clone[pair[0]][pair[1]]='o'
				#print (lista_clone)
				figlio = NodoTris(lista_clone)
				curr_config.lista_figli.append(figlio) #appendo la griglia come oggetto nodo
				figlio.lvl = curr_config.lvl+1
			#print(curr_config.lista_figli)
		if curr_config.turno == "x":
			for pair in possible_moves:
				lista_clone = deepcopy(curr_config.nome)
				lista_clone[pair[0]][pair[1]]='x'
				figlio = NodoTris(lista_clone)
				curr_config.lista_figli.append(figlio) #appendo la griglia come oggetto nodo
				figlio.lvl = curr_config.lvl+1
			#print(curr_config.lista_figli)
		for config in curr_config.lista_figli:
			#controllo se il gioco e' finito
			if config.tipo()=='?' or config.tipo()=='-':
				sviluppa_albero(config)
	return curr_config
	#print (curr_config.lista_figli)
		

def print_recursively(curr_config):
	#print (curr_config.lvl)
	#print (curr_config.tipo())
	#print (curr_config.esiti())
	print (curr_config.nome)
	print("\n")
	for figlio in curr_config.lista_figli:
		print_recursively(figlio)

def gen_tree(griglia):
	'''inserire qui il vostro codice'''
	curr_config = NodoTris(griglia)
	curr_config.lvl = 0
	tree=sviluppa_albero(curr_config)
	#implementato in sviluppa_albero
	#possible_moves = []
	#for i in range(len(curr_config.nome)):
	#	for j in range(len(curr_config.nome[0])):
	#		if curr_config.nome[i][j]=='':
	#			possible_moves.append([i,j])
	#curr_config.who_play()
	##print (curr_config.turno)
	#if curr_config.turno == "o":
	#	for pair in possible_moves:
	#		#print (curr_config.nome)
	#		lista_clone = deepcopy(curr_config.nome)
	#		lista_clone[pair[0]][pair[1]]='o'
	#		#print (lista_clone)
	#		curr_config.lista_figli.append(NodoTris(lista_clone)) #appendo la griglia come oggetto nodo
	#	#print(curr_config.lista_figli)
	#if curr_config.turno == "x":
	#	for pair in possible_moves:
	#		lista_clone = deepcopy(curr_config.nome)
	#		lista_clone[pair[0]][pair[1]]='x'
	#		curr_config.lista_figli.append(NodoTris(lista_clone)) #appendo la griglia come oggetto nodo
	#	#print(curr_config.lista_figli)
	
	#print_recursively(curr_config)
	#print (curr_config.esiti())
	return curr_config

#g1=[['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
#g2=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'o']]
#g3=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', '', 'x']]
#g4=[['o', 'x', 'x'], ['x', 'o', 'o'], ['o', 'o', 'x']]
#


#gen_tree(g1)
#gen_tree(g2)
#gen_tree(g3)
#gen_tree(g4)
#
#lista=[g1, g2, g3, g4]
#lista1=[gen_tree(x) for x in lista]

#print ([lista1[0].vittorie_livello('o',h) for h in range(4)])
#print ([lista1[0].vittorie_livello('x',h) for h in range(4)])
#print ([lista1[0].strategia_vincente('x')])