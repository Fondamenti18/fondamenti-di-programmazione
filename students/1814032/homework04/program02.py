'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3x3 caselle.
A turno, i due giocatori scelgono una cella vuota e vi disegnano il proprio simbolo 
(un giocatore ha come simbolo una "o" e l'avversario una 'x'). 
Vince il giocatore che riesce a disporre tre dei propri simboli in linea retta 
orizzontale, verticale o diagonale. Se la griglia viene riempita 
senza che nessuno dei giocatori sia riuscito a completare una linea 
retta di tre simboli, il gioco finisce in parità. Nel caso in cui il gioco 
finisse in parità, la partita è detta "patta". 
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
Piu' precisamente: il primo elemento della tripla  è il numero di  patte possibili, 
il secondo è il numero di possibili vittorie  per il giocatore 'o' mentre  il terzo elemento 
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

o_s = ['-','o','x','?']
symbol = ['o','x']
checks = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
precomp_checks = list(map(lambda c: list(filter(lambda uc: c in uc,checks)),range(9)))
analyze_logic = ['any','all']
analyze_whole = '(map(lambda child: child.outcomes[p] > 0,ygg.lista_figli))'
p = 'null'

class NodoTris:
	def __init__(self, griglia, player_symb, unrolled_coord, starting=0):
		self.nome = griglia #unrolled
		self.lista_figli = []
		self.whatmoved = unrolled_coord
		self.whomoved = player_symb
		self.result = check_result(self,starting)
		self.outcomes = {'x':0,'o':0,'-':0,'?':0}
		self.outcomes[self.result] += 1

	def tipo(self):
		return self.result

	def esiti(self):
		#gli esiti vengono generai in maniera ricorsiva durante la risalita della funzione gen_tree (linea 150) per essere usati in strategia vincente. Anche se è insensato ricalcolarli qui, ho visto che influisce di pochi millisecondi, quindi alla fine ho deciso di ricalcolarli anche qui, così da non avere problemi con la ricorsione. 
		o_l = [0,0,0,0]
		e = get_outcomes(self,o_l)
		return (o_l[0],o_l[1],o_l[2])
		#return (self.outcomes['-'],self.outcomes['o'],self.outcomes['x'])

	def vittorie_livello(self, giocatore, h):
		wins = [0]
		calculate_wins(self,giocatore,h,0,wins)
		return wins[0]

	def strategia_vincente(self,giocatore):
		a_func = self.whomoved == giocatore
		global p
		p = giocatore
		return strategy_analyze(self,a_func)

def gen_tree(g):
	'''generates game's tree'''
	unrolled = g[0]+g[1]+g[2]
	num_o = unrolled.count('o')
	blanks = set(map(lambda i: i[0],(filter(lambda t: t[1] == '',enumerate(unrolled)))))
	god = NodoTris(unrolled,symbol[1],0,1)
	yggdrasil_spawner(god,god.nome,0,(num_o != (9 - (num_o + len(blanks)))) ^ 1,blanks,1)
	return god.lista_figli[0]

def yggdrasil_spawner(daddy,old_g,u_c,player,blanks,starting=0):
	'''creates tree's structure by adding generated nodes to father'''
	g = old_g[:]
	g[u_c] = [symbol[player],g[u_c]][starting]
	little_yggdrasil = NodoTris(g,symbol[player],u_c,starting)
	daddy.lista_figli.append(little_yggdrasil)
	next(filter(lambda b: yggdrasil_spawner(little_yggdrasil,little_yggdrasil.nome,b,player ^ 1,blanks.difference([b])), [set(),blanks][little_yggdrasil.result=='?']),True)
	#calculate outcomes adding children's outcomes
	next(filter(lambda child: add_outcomes(little_yggdrasil,child),little_yggdrasil.lista_figli),True)

def check_result(ygg_node,starting):
	'''returns result of game's board. When possible, it checks only last move's affected tris combinations'''
	winner = list(filter(lambda c: (ygg_node.nome[c[0]] == ygg_node.nome[c[1]] == ygg_node.nome[c[2]]) & ('' not in [ygg_node.nome[c[0]],ygg_node.nome[c[1]],ygg_node.nome[c[2]]]), [precomp_checks[ygg_node.whatmoved],checks][starting]))+[(0,0)]
	return [ygg_node.nome[winner[0][0]],['-','?']['' in ygg_node.nome]][len(winner)<=1]

def add_outcomes(ygg,child):
	'''add every entry of child outcome dict to father outcome dict'''
	next(filter(lambda s: add_o(ygg,child,s),iter(ygg.outcomes)),True)

def add_o(ygg,child,s):
	ygg.outcomes[s] += child.outcomes[s]
	
def calculate_wins(ygg_node,player,h,explored_h,wins):
	wins[0] += [0,1][(h == explored_h) & (player == ygg_node.result)]
	next(filter(lambda y: calculate_wins(y,player,h,explored_h+1,wins),[[],ygg_node.lista_figli][(explored_h+1)<=h]),True)

def strategy_analyze(ygg,a_func):
	'''alternates all and any checks on children, based on wheter who moved is the same as the searched player'''	
	first_l = list(map(lambda child: child.outcomes[p] > 0,ygg.lista_figli))
	first_block = [any(first_l),all(first_l)][a_func]
	second_l = eval(['[False]','children_check_list(ygg,a_func)'][first_block])
	second_block = [any(second_l),all(second_l)][a_func]
	return [False,second_block][first_block]

def children_check_list(ygg,a_func):
	'''had to add this one because of scope problem with eval'''
	return list(map(lambda child: strategy_analyze(child,a_func ^ 1),ygg.lista_figli))
	
def get_outcomes(ygg,outcomes_list):
	outcomes_list[o_s.index(ygg.result)] += 1
	next(filter(lambda c: get_outcomes(c,outcomes_list),ygg.lista_figli),True)