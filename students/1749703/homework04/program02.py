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
in esattamente h mosse per il giocatore specificato, nella partita che ha come configurazione iniziale 
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

g0=[['', '', ''], ['', '', ''], ['', '', '']]
g1=[['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
g2=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'o']]
g3=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', '', 'x']]
g4=[['o', 'x', 'x'], ['x', 'o', 'o'], ['o', 'o', 'x']]

def fp(row):
	row = deepcopy(row)
	for x in range(0, 3):
		if row[x] == '':
			row[x] = ' '
	return row
	
def other(giocatore):
	return ['o', 'x'][int(giocatore == 'o')]
		
class NodoTris:
	def __countsymbols__(self, symbol):
		return sum([row.count(symbol) for row in self.grid])
		
	def __getCurrentPlayer__(self):
		ocount, xcount = self.__countsymbols__('o'), self.__countsymbols__('x')
		return ['x', 'o'][int(xcount >= ocount)]
	
	def __assertGridDetails__(self):
		self.current_player = self.__getCurrentPlayer__() 
		self.isIncomplete = False
		for row in self.grid:
			if '' in row:
				self.isIncomplete = True
				break
				
	def __test_horizontal_win__(self):
		for row in self.grid:
			# print("analyzing row: {} | win: {} | set: {}".format(row, len(set(row)) == 1 and not '' in row, set(row)))
			if len(set(row)) == 1 and not '' in row:
				return row[0]
	
	def __test_vertical_win__(self):
		for col in range(0, 3):
			line = [self.grid[0][col], self.grid[1][col], self.grid[2][col]]
			# print("analyzing column: {} | win: {} | set: {}".format(line, len(set(line)) == 1 and not '' in line, set(line)))
			if len(set(line)) == 1 and not '' in line:
				return line[0]
				
	def __test_diagonal_win__(self):
		line1 = [self.grid[0][0], self.grid[1][1], self.grid[2][2]]
		line2 = [self.grid[0][2], self.grid[1][1], self.grid[2][0]]
		if len(set(line1)) == 1 and not '' in line1:
			return self.grid[0][0]
		elif len(set(line2)) == 1 and not '' in line2:
			return self.grid[0][2]

	def __getTests__(self):
		return [self.__test_horizontal_win__(), self.__test_vertical_win__(), self.__test_diagonal_win__()]
			
	def __print__(self):
		print("[{}\n {}\n {}] = {}, {}, {}\n".format(fp(self.grid[0]), fp(self.grid[1]), fp(self.grid[2]), self.tipo(), self.__getTests__(), self.depth))
	
	def __init__(self, griglia, depth = 0):
		self.grid = griglia
		self.projections = [] # lista di NodoTris
		self.__assertGridDetails__()
		self.depth = depth
			
		# self.__print__()
		if self.tipo() == '?':
			for ri, row in enumerate(self.grid):
				for ci, cell in enumerate(row):
					if cell == '':
						newgrid = deepcopy(griglia)
						newgrid[ri][ci] = self.current_player
						self.projections += [NodoTris(newgrid, depth + 1)]
		
	#nonR 
	def tipo(self):
		# o, x, ?, - : winO, winX, ???, tie
		tests = self.__getTests__()
		if set(tests) == {None}:
			return ['-', '?'][int(self.isIncomplete)]
		else:
			return ['o', 'x'][int('x' in tests)]
		
	#R
	def esiti(self):
		owins, xwins, ties = 0, 0, 0
		type = self.tipo()
		owins += int(type == 'o')
		xwins += int(type == 'x')
		ties += int(type == '-')
		
		for p in self.projections:
			proj_r = p.esiti()
			ties += proj_r[0]
			owins += proj_r[1]
			xwins += proj_r[2]
		
		return ties, owins, xwins
	
	
	def __getAll__(self):
		proj = [] 
		proj += self.projections
		for p in self.projections:
			proj += p.__getAll__()
		return proj
	
	#R
	def vittorie_livello(self, giocatore, h):
		# quante vittorie per <giocatore>(['o','x']) al livello <h>(int) ?
		projections = self.__getAll__()
		return len([p for p in self.__getAll__() if p.depth == h and p.tipo() == giocatore])
	
	def __find_best_move__(self, plr):
		paths = [path for path in self.__getAll__() if path.tipo() == plr]
		if paths:
			best = paths[0]
			for path in paths:
				if path.depth < best.depth:
					best = path
			return best
	
	#R
	def strategia_vincente(self, giocatore):
		print(giocatore, self.current_player, self.current_player is giocatore)
		if self.projections:
			if self.current_player is not giocatore:
				# loss_paths = [proj for proj in self.projections if proj.tipo() in ['?', other(giocatore)]]
				certain_loss_paths = [proj for proj in self.projections if proj.tipo() == other(giocatore)]
				
				if certain_loss_paths:
					print("---")
					return False
				else:
					best = self.__find_best_move__(self.current_player)
					worst = self.__find_best_move__(other(self.current_player))
					return best.strategia_vincente(other(giocatore))
					# print("shortest loss is: ")
					# best.__print__()
					# print("shortest win is: ")
					# worst.__print__()
				#elif loss_paths:
				#	for path in loss_paths:
				#		path.__print__()
				#		return path.strategia_vincente(giocatore)
			else:
				# victory_paths = [proj for proj in self.projections if proj.tipo() in ['?', giocatore]]
				certain_victory_paths = [proj for proj in self.projections if proj.tipo() == giocatore]
				if certain_victory_paths:
					print("---")
					return True
				else:
					best = self.__find_best_move__(self.current_player)
					worst = self.__find_best_move__(other(self.current_player))
					return worst.strategia_vincente(giocatore)
					# print("shortest win is: ")
					# best.__print__()
					# print("shortest loss is: ")
					# worst.__print__()
				# elif victory_paths:
				#	for path in victory_paths:
				#		path.__print__()
				#		return path.strategia_vincente(giocatore)
		else:
			return self.tipo() == giocatore
#R		
def gen_tree(griglia):
	# griglia è una configurazione di gioco
	return NodoTris(griglia)
	
#x = gen_tree(g0)
#print("generated: ", len(x.__getAll__()))
#for n in range(10):
#	print(x.vittorie_livello('o', n)) # print("l{}: {}".format(n, x.vittorie_livello('o', n)))