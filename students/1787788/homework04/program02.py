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

import copy

class NodoTris:
	def __init__(self, griglia):
		self.nome = griglia
		self.lista_figli = [] #lista dei nodi figli
		self.vincente = ''
	
	def tipo(self):
		combinazione = [((0,0), (1,0), (2,0)), ((0,1), (1,1), (2,1)), ((0,2), (1,2), (2,2)), ((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), ((2,0), (2,1), (2,2)), ((0,0), (1,1), (2,2)),((2,0), (1,1), (0,2))]
		contatorePari = 0
		for coordinate in combinazione:
			lettere = [self.nome[y][x] for x,y in coordinate]
			if(len(set(lettere)) == 1 and set(lettere) != {''}):
				self.vincente = lettere[0]
				return(lettere[0])
		for x in range(0,3):
			for y in range(0,3):
				if(self.nome[y][x] == 'x' or self.nome[y][x] == 'o'):
					contatorePari += 1
		if(contatorePari == 9):
			self.vincente = '-'
			return '-'
		else:
			self.vincente = '?'
			return '?'
			
	def CalcolaNumeroVittorie(self, elemento, listavincente):
		if(elemento.vincente == 'x'):
			listavincente[2] += 1
		elif(elemento.vincente == 'o'):
			listavincente[1] += 1
		elif(elemento.vincente == '-'):
			listavincente[0] += 1
		for elemento in elemento.lista_figli:
			self.CalcolaNumeroVittorie(elemento, listavincente)
			
	def esiti(self):
		listavincenti=[0, 0, 0]
		self.CalcolaNumeroVittorie(self,listavincenti)
		return((listavincenti[0], listavincenti[1], listavincenti[2]))
	
	def vittorie_livello(self, giocatore, numeroFigli):
		listacontavero = [0]
		self.CalcolaNumeroVittoriePerGiocatore(giocatore,numeroFigli, listacontavero)
		return(listacontavero[0])
			
	def calcolaVincente(self, elemento, giocatore):
		return elemento.vincente==giocatore
		
	def CalcolaNumeroVittoriePerGiocatore(self,giocatore,numeroFigli, listacontavero, mosse = 0):  
		if numeroFigli==0:
			if self.calcolaVincente(self, giocatore):
				listacontavero[0] += 1
			return
		for elemento in self.lista_figli:
			mosse+=1
			if self.calcolaVincente(elemento, giocatore):
				if numeroFigli==mosse:
					listacontavero[0] += 1
			elemento.CalcolaNumeroVittoriePerGiocatore(giocatore, numeroFigli, listacontavero, mosse)
			mosse-=1
		return
		
	
	
	def strategia_vincente(self,giocatore):
		'''ciao'''
       
	   
def contaElementi(griglia, contatore1, contatore2):
	for elemento in griglia:
		for item in elemento:
			if item=='x':
				contatore1[0] += 1
			elif item=='o':
				contatore2[0] +=1
					 
def definisciPrimoMossa(griglia, contatore1, contatore2):
	if(contatore1[0] >= contatore2[0]):
		return 'o'
	else:
		return 'x'

from copy import deepcopy
def gen_tree(griglia):
	contatore1 = [0]
	contatore2 = [0]
	griglia1 = deepcopy(griglia)
	grid=NodoTris(griglia1)
	contaElementi(griglia, contatore1, contatore2)
	first = definisciPrimoMossa(griglia, contatore1, contatore2)
	if grid.tipo() =='?' or grid.tipo()=='-': 
		for x in range(0,3):
			for y in range(0,3):            
				if griglia1[y][x]=='':                
					griglia1[y][x]=first          
					grid.lista_figli.append(gen_tree(griglia1))
					griglia1[y][x]=''      
	return(grid)  


