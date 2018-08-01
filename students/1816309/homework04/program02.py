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
 'o' se la configurazione rappresentata dal nodo e' una configurazione di vittorie per il giocatore 'o'
 'x' se la configurazione rappresentata dal nodo e' una configurazione di vittorie per il giocatore 'x'
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
restituisce il numero di nodi che rappresentano una vittorie per il giocatore e si 
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
che la partita termini con la sua vittorie.

Potete ovviamente definire ulteriori  funzioni e altri metodi per la   Classe NodiTris 
se li  ritenete utili al fine della risoluzione del compito.

Potete assumere che le configurazioni di gioco rappresentate da griglia siano sempre configurazioni 
lecite (vale a dire ottenute dopo un certo numero di mosse a parire dalla griglia vuota).


AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate; non
importare moduli che non sono nella libreria standard.

ATTENZIONE: i test vengono eseguiti con un timeout globale di 2*N secondi (se il grader esegue N test).
'''

simboli = ['o','x']
simboli_esiti = ['-','o','x']
checks = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
analyze_child = '(map(lambda child: calcola_strategia(child,a_func ^ 1),ygg.lista_figli))'

class NodoTris:
	def __init__(self, griglia, chi_ha_mosso, ultima_mossa):
		self.nome = griglia #distesa
		self.lista_figli = []
		self.chi_ha_mosso = chi_ha_mosso
		self.risultato_board = calcola_risultato(self,ultima_mossa)

	def tipo(self):
		return self.risultato_board

	def esiti(self):
		lista_ris = calcola_esiti(self,[0,0,0])
		return (lista_ris[0],lista_ris[1],lista_ris[2])
		
	def vittorie_livello(self, giocatore, h):
		return calcola_vittorie(self,giocatore,h,0,0)

	def strategia_vincente(self,giocatore):
		mosso =  simboli[self.nome.count('o') == self.nome.count('x')]
		alterna = mosso == giocatore
		return calcola_strategia(self,alterna,giocatore)

def gen_tree(griglia):
	#trasforma la griglia in lista monodimensionale (per praticità)
	disteso = griglia[0]+griglia[1]+griglia[2]
	#conta il numero di 'o' presenti, per determinare chi sarà il prossimo a muovere
	num_o = disteso.count('o')
	#genera una collezione di spazi bianchi dove si andranno a inserire i simboli
	spazi = set()
	for i,e in enumerate(disteso):
		if e == '':
			spazi.add(i)
	#calcola per esclusione il numero di 'x'
	num_x = 9 - (num_o + len(spazi))
	#calcola il giocatore che ha appena mosso nella configurazione data
	giocatore_precedente = num_o == num_x
	#crea il nodo
	nodo_iniziale = NodoTris(disteso,'',0)
	#e da inizio alla creazione dell'albero se la configurazione fornita non corrisponde a una partita conclusa
	if nodo_iniziale.risultato_board == '?':
		for spazio in spazi:
			genera_nodo(nodo_iniziale,spazio,not giocatore_precedente,spazi ^ set([spazio]))
	return nodo_iniziale

def genera_nodo(padre,coordinate_mossa,giocatore,spazi):
	#crea una copia della vecchia griglia
	griglia = padre.nome[:]
	#inserisce il simbolo del giocatore che deve muovere nelle coordinate
	griglia[coordinate_mossa] = simboli[giocatore]
	#crea il nodo
	nodo = NodoTris(griglia,simboli[giocatore],coordinate_mossa)
	#e lo aggiunge alla lista dei figli del (nodo) padre
	padre.lista_figli.append(nodo)
	#ripete ricorsivamente tale funzione, riempendo gli spazi bianchi attualmente disponibili se la partita non è finita
	if nodo.risultato_board != '?':
		return
	for spazio in spazi:
		genera_nodo(nodo,spazio,not giocatore,spazi ^ set([spazio]))

def calcola_risultato(nodo,ultima_mossa):
	#popola la lista di controlli
	lista_controlli = []
	if nodo.chi_ha_mosso == '':
		lista_controlli = checks
	else:
		for e in checks:
			if ultima_mossa in e:
				lista_controlli.append(e)
	#controlla se c'è un vincitore
	risultato_board = ''
	for c1,c2,c3 in lista_controlli:
		if (nodo.nome[c1] == nodo.nome[c2] == nodo.nome[c3]) & ('' not in [nodo.nome[c1],nodo.nome[c2],nodo.nome[c3]]):
			risultato_board = nodo.nome[c1]
			break
	#in caso non ci fosse, determina se la partita è finita in parità, o può ancora continuare
	if not risultato_board:
		risultato_board = ['-','?']['' in nodo.nome]
	#conclude ritornando il risultato
	return risultato_board

def calcola_esiti(nodo,lista_esiti):
	#se il risultato del nodo esplorato è un risultato definito (x,o,-), incrementa di uno il relativo esito nella lista
	if nodo.risultato_board in simboli_esiti:
		lista_esiti[simboli_esiti.index(nodo.risultato_board)] += 1
	#e ripete ricorsivamente la funzione per i figli
	for figlio in nodo.lista_figli:
		lista_esiti = calcola_esiti(figlio,lista_esiti)
	return lista_esiti
	
def calcola_vittorie(nodo,giocatore,h,h_attuale,vittorie):
	#se sono arrivato al livello di profondità desiderato e il giocatore ricercato ha riportato una vittoria, la aggiungo
	if (h == h_attuale) & (giocatore == nodo.risultato_board):
		vittorie += 1
	#se sono ancora entro il livello di profondità richiesto, continuo ad avanzare
	if h_attuale < h:
		for figlio in nodo.lista_figli:
			vittorie = calcola_vittorie(figlio,giocatore,h,h_attuale+1,vittorie)
	#ritorno il valore contenuto in vittoria, così da passarlo di funzione in funzione, anche durante la risalita
	return vittorie

def calcola_strategia(nodo,alterna,giocatore):
	lista_controllo_livello = []
	for figlio in nodo.lista_figli:
		esito_ricercato =  (figlio.esiti()[simboli_esiti.index(giocatore)] > 0)
		lista_controllo_livello.append(esito_ricercato)
	esci = False
	if alterna:
		esci = not all(lista_controllo_livello)
	else:
		esci = not any(lista_controllo_livello)
	if esci:
		return False
	deeper_control = []
	for figlio in nodo.lista_figli:
		deeper_control.append(calcola_strategia(figlio,not alterna,giocatore))
	if alterna:
		return all(deeper_control)
	else:
		return any(deeper_control)