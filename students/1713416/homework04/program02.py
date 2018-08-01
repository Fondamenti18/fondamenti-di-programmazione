'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3×3 caselle.
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

from copy import deepcopy
class NodoTris:
	def __init__(self, griglia):
		self.nome = griglia
		self.lista_figli = [] #lista dei nodi figli
	
	def colonna(self, i):
		if (self.nome[0][i] == self.nome[1][i] == self.nome[2][i]) and self.nome[1][i]:
			return self.nome[0][i]
		return ''
	
	def riga(self, i):
		if self.nome[i].count(self.nome[i][0]) == 3:
			return self.nome[i][0]
		return ''
	
	def diagonaledx(self):
		if (self.nome[1][1] == self.nome[2][2] == self.nome[0][0]) and self.nome[1][1]:
			return self.nome[1][1]
		return ''
	
	def diagonalesx(self):
		if (self.nome[0][2] == self.nome[1][1] == self.nome[2][0]) and self.nome[1][1]:
			return self.nome[1][1]
		return ''
	
	def tipo(self):
		for i in range(3):
			if self.riga(i):
				return self.nome[i][0]
			if self.colonna(i):
				return self.nome[0][i]
			if self.diagonaledx() or self.diagonalesx():
				return self.nome[1][1]
		if '' in self.nome[0] or '' in self.nome[1] or '' in self.nome[2]:
			return '?'
		return '-'
	
	def esiti(self):
		a = {'x':0, 'o':0, '-':0}
		if not self.lista_figli:
			a[self.tipo()] += 1
			return (a['-'], a['o'], a['x'])
		a = (0, 0, 0)
		for i in self.lista_figli:
			a = somma(a, i.esiti())
		return a 
	
	def vittorie_livello(self, giocatore, h):
		if h == 0:
			if self.tipo() == giocatore:
				return 1
			return 0
		h -= 1
		a = 0
		for j in self.lista_figli:
			a += j.vittorie_livello(giocatore, h)
		return a

	def strategia_vincente(self, giocatore):
		gioca = ['x', 'o']
		avv = gioca[(gioca.index(giocatore) + 1)%2]
		if not self.lista_figli:
			if self.tipo() == giocatore:
				return True
			if self.tipo() == avv:
				return False
		if self.vittorie_livello(avv, 1) == 0 and self.vittorie_livello(giocatore, 1) != 0:
			return True 
		if self.vittorie_livello(avv, 1) != 0 and self.vittorie_livello(giocatore, 1) == 0:
			return False
		a = True 
		for i in self.lista_figli:
			a = a and i.strategia_vincente(giocatore)
		return a 
		
	def strategia_vincente1(self, giocatore):
		if not self.lista_figli:
			if self.tipo() == giocatore:
				return True
			return False
		g = turno(self.nome)
		if giocatore == g:
			return mio(self, giocatore)
		return tuo(self, giocatore)
	
def mio(radice, giocatore):
	if not radice.lista_figli:
		return True
	if radice.vittorie_livello(giocatore, 1) != 0:
		return True
	a = False
	for i in radice.lista_figli:
		a = a or tuo(radice, giocatore)
	return a 
	
def tuo(radice, giocatore):
	if not radice.lista_figli:
		return False
	if radice.vittorie_livello != 0:
		return False
	a = True
	for i in radice.lista_figli:
		a = a and mio(radice, giocatore)
	return a 

def turno(griglia):
	x = griglia[0].count('x') + griglia[1].count('x') + griglia[2].count('x')
	o = griglia[0].count('o') + griglia[1].count('o') + griglia[2].count('o')
	if x == o:
		return 'o'
	return 'x'

def gen_tree(griglia):
	giocatore = turno(griglia)
	return genera(griglia, giocatore)
	
def genera (griglia, giocatore):
	radice = NodoTris(griglia)
	if radice.tipo() != '?':
		return radice
	sp = spazi(griglia)
	gioca = ['o', 'x']
	g = gioca[(gioca.index(giocatore)+1)%2]
	for x, y in sp:
		i = deepcopy(griglia)
		i[x][y] = giocatore
		radice.lista_figli += [genera(i, g)]
	return radice

def spazi(griglia):
	spazi = set()
	for i in range(3):
		nsp = griglia[i].count('')
		if nsp == 3:
			spazi.update([(i,1), (i,0), (i,2)])
		if nsp == 1:
			spazi.add((i, griglia[i].index('')))
		if nsp == 2:
			spazi.add((i, griglia[i].index('')))
			griglia[i].reverse()
			spazi.add((i, 2 - griglia[i].index('')))
			griglia[i].reverse()
	return spazi
	
def somma(a, b):
  c = (a[0] + b[0], a[1] + b[1], a[2] + b[2])
  return c
	
  