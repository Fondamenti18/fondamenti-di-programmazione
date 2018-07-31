'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3×3 caselle.
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


# Inizio Definizione della Classe NodoTris(griglia)
class NodoTris:

	def __init__(self, griglia):
		self.nome = griglia
		self.lista_figli = [] #lista dei nodi figli

	def tipo(self):
		# Per testare la correttezza della vostra implementazione di gen_tree() il grade utilizzera' quattro metodi 
		# della   classe NodoTris che dovete comunque implementare:
		# 1) tipo(self)
		# che, dato un nodo NodoTris, restituisce:
		#  'o' se la configurazione rappresentata dal nodo e' una configurazione di vittoria per il giocatore 'o'
		#  'x' se la configurazione rappresentata dal nodo e' una configurazione di vittoria per il giocatore 'x'
		#  '-' se la configurazione rappresentata dal nodo e' una configurazione di patta
		#  '?' se la configurazione rappresentata dal nodo e' una configurazione di gioco non ancora terminato
		griglia = self.nome
		l = griglia[0] + griglia[1] + griglia[2]
		if (griglia[0][0] == griglia[1][1] and griglia[1][1] == griglia[2][2])   and (griglia [0][0] != ''):
			return griglia [0][0]
		if (griglia [0][2] == griglia [1][1] and griglia [1][1] == griglia[2][0]) and (griglia [2][0] != ''):
			return griglia [2][0] 
		for j in griglia : 
			r = all([i == 'x' for i in j])
			s =  all([i == 'o' for i in j]) 
			if r :
				return 'x'
			if s :
				return 'o'
		for k in range(3) : 
			if griglia[0][k] == griglia[1][k] and griglia[0][k] == griglia[2][k] and griglia[0][k] != '' : 
				return griglia[0][k]
		if '' not in l:
			return '-'
		return '?'

	def esiti(self) :
		# Per testare la correttezza della vostra implementazione di gen_tree() il grade utilizzera' quattro metodi 
		# della   classe NodoTris che dovete comunque implementare:
		# 2) esiti(self)
		# che, dato un nodo radice di un albero di gioco, restituisce una tripla con i possibili 
		# esiti della partita che ha come configurazione iniziale quella rappresentata dal nodo. 
		# Piu' precisamente: il primo elemento della tripla  e' il numero di  patte possibili, 
		# il secondo e' il numero di possibili vittorie  per il giocatore 'o' mentre  il terzo elemento 
		# e' il numero di possibili vittorie per il giocatore 'x'.
		tripla_esiti = [0,0,0]	# lista = tripla (num. -,num. vittorie o,num. vittorie x) (:-; vedi su google "in python function parameters are passed by value or by reference")
		visita_per_esiti(self,tripla_esiti)
		return (tripla_esiti[0],tripla_esiti[1],tripla_esiti[2]) # ritorna la tripla richiesta.

	def vittorie_livello(self, giocatore, h) :
		# Per testare la correttezza della vostra implementazione di gen_tree() il grade utilizzera' quattro metodi 
		# della   classe NodoTris che dovete comunque implementare:
		# 3) vittorie_livello(self, giocatore, h)
		# che, dato un nodo radice di un albero di gioco, uno dei due giocatori ed un intero h,
		# restituisce il numero di nodi che rappresentano una vittoria per il giocatore e si 
		# trovano ad altezza h nell'albero. In altri termini restituisce il numero di vittorie possibili 
		# per giocatore in esattamente h mosse, nella partita che ha come configurazione iniziale 
		# quella rappresentata dalla radice dell'albero.
		num_vittorie_giocatore = [0]	# lista = [il numero di vittorie del giocatore al livello h] (:-; vedi anche "https://docs.python.org/3/faq/programming.html#why-did-changing-list-y-also-change-list-x")
		visita_per_vittorie_livello(self,giocatore,h,num_vittorie_giocatore)
		return num_vittorie_giocatore[0] # ritorna il valore richiesto.

	def strategia_vincente(self,giocatore) :
		# Per testare la correttezza della vostra implementazione di gen_tree() il grade utilizzera' quattro metodi 
		# della   classe NodoTris che dovete comunque implementare:
		# 4) strategia_vincente(self,giocatore)
		# che, dato un nodo radice di un albero di gioco ed uno dei due giocatori, restituisce True o False. 
		# Restituisce True  se  giocatore ha una strategia vincente  nella partita 
		# che ha come configurazione iniziale quella rappresentata dal nodo radice, False altrimenti.
		# 
		# Nota che un giocatore ha una strategia vincente rispetto ad una certa configurazione se, 
		# qualunque siano le mosse dell'avversario ha sempre la possibilita' di rispondere in modo 
		# che la partita termini con la sua vittoria.
		inv_sym = 0 if giocatore == 'o' else 1 # Il 'inv_sym' di Irene calcolato con il ternary operator del Python (si veda https://docs.python.org/3/faq/programming.html#is-there-an-equivalent-of-c-s-ternary-operator)
		# self.esiti(self) # ritorna la tripla (num. -,num. vittorie o,num. vittorie x), quindi:
		num_patte = self.esiti()[0] # = num. di patte
		num_vitt_giocatore = self.esiti()[inv_sym+1] # = num. vittorie di giocatore
		num_vitt_avversario = self.esiti()[(inv_sym+1)%2+1] # = num. vittorie dell'avversario del giocatore
		if num_vitt_giocatore < num_vitt_avversario  and num_patte == 0 :
			return True
		else :
			return False
# Fine definizione della Classe NodoTris(griglia).

# Inizio codice per la generazione dell'albero:
def gen_tree(griglia) :
	nodo_griglia = NodoTris(griglia)
	ricorsione_gen_tree(nodo_griglia)
	return nodo_griglia

def ricorsione_gen_tree(nodo_griglia):
	# calcolo di chi è il turno
	turno_giocatore = turno(nodo_griglia.nome)
	tipo = nodo_griglia.tipo()
	if tipo == '?':
		for i in range(3) :
			for j in range(3) :
				if nodo_griglia.nome[i][j] == '' :
					temp_griglia = copy1(nodo_griglia.nome) # copia la griglia !!!
					temp_griglia[i][j] = turno_giocatore # modifica la copia della griglia !!!
					nodo_griglia_new = NodoTris(temp_griglia)
					nodo_griglia.lista_figli.append(nodo_griglia_new)
					ricorsione_gen_tree(nodo_griglia_new)
	

def turno(griglia) : 
	l = griglia[0] + griglia[1] + griglia[2]
	if (9 - l.count('')) % 2 == 0 :
		return 'o'
	else : 
		return 'x'
# Fine codice per la generazione dell'albero.

def visita_per_vittorie_livello(nodo_griglia,giocatore,h,num_vittorie_giocatore) :
	risultato = nodo_griglia.tipo()
	if h == 0 :
		if risultato == giocatore :
			num_vittorie_giocatore[0] = num_vittorie_giocatore[0] + 1
	else :
		for x in nodo_griglia.lista_figli :
			visita_per_vittorie_livello(x,giocatore,h-1,num_vittorie_giocatore)

def visita_per_esiti(nodo_griglia,tripla_esiti) :
	tipo = nodo_griglia.tipo()
	if tipo != '?' :
		if tipo == '-' :
			tripla_esiti[0] += 1
		if tipo == 'o' :
			tripla_esiti[1] += 1
		if tipo == 'x' :
			tripla_esiti[2] += 1
	else :
		for x in nodo_griglia.lista_figli :
			visita_per_esiti(x,tripla_esiti)
def copy1(nodo_griglia):
	griglia1= []
	for i in range(3):
		appo = []
		for j in range(3):
			appo.append(nodo_griglia[i][j])
		griglia1.append(appo)
	return griglia1