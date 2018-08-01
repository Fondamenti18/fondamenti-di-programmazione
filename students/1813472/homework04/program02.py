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

import copy

class NodoTris:
		def __init__(self, griglia):
			self.nome = griglia
			self.lista_figli = [] #lista dei nodi figli
		
		
		def tipo(self):
			 
			
			for i in range(0,3):
				if self.nome[i][0]+self.nome[i][1]+self.nome[i][2]=="xxx":
					return "x"
				elif self.nome[i][0]+self.nome[i][1]+self.nome[i][2]=="ooo":
					return "o"
			for i in range(0,3):
				if self.nome[0][i]+self.nome[1][i]+self.nome[2][i]=="xxx":
					return "x"
				elif self.nome[0][i]+self.nome[1][i]+self.nome[2][i]=="ooo":
					return "o"
			if self.nome[0][0]+self.nome[1][1]+self.nome[2][2]=="xxx":
				return "x"
			elif self.nome[0][0]+self.nome[1][1]+self.nome[2][2]=="ooo":	
				return"o"
			if self.nome[2][0]+self.nome[1][1]+self.nome[0][2]=="xxx":
				return "x"
			elif self.nome[2][0]+self.nome[1][1]+self.nome[0][2]=="ooo":	
				return"o"	
			if "" in self.nome[0]+self.nome[1]+self.nome[2]:
				return "?"
			return "-"
			
		def esiti(self):
			patta=0
			o=0
			x=0
			return self.conta(patta,o,x)
			
		def vittorie_livello(self, giocatore, h):
			
			totale=0
			if self.tipo()==giocatore and h==0:
				return 1
			else:
				for figlio in self.lista_figli:
					totale=totale+figlio.conta_vittorie(giocatore,h,1)
			 	
			return totale	
		
		def strategia_vincente(self,giocatore):
			
			if self.tipo()==giocatore:
				return True
			else:
				for figlio in self.lista_figli:
					if figlio.strategia_vincente(giocatore)==True:
						return True
			return False			
		
		def conta_vittorie(self,giocatore,h,mossa):
			
			subtotale=0
			if h==mossa and self.tipo()==giocatore:
				return 1
			
			elif h>mossa:
				for figlio in self.lista_figli:
					subtotale=subtotale+ figlio.conta_vittorie(giocatore,h,mossa+1)
				
			return subtotale
		
		def conta(self,patta,o,x):
			
			
			if self.tipo()=="-":
				patta=patta+1
			elif self.tipo()=="o":
				o=o+1
			elif self.tipo()=="x":
				x=x+1
			
			else:
				for figlio in self.lista_figli:
					lista=figlio.conta(patta,o,x)
					patta=lista[0]
					o=lista[1]
					x=lista[2]
			return (patta,o,x)
		
		def giocatore_di_turno(self):
			totO=0
			totX=0
			for i in range(0,3):
				for y in range(0,3):
					if self.nome[i][y]=="o":
						totO=totO+1
					elif self.nome[i][y]=="x":
						totX=totX+1
			if totO>totX:
				return "x"
			else:
				return "o"

def presente(lista,nodo):
	for elemento in lista:
		if elemento.nome[0][0]==nodo.nome[0][0] and elemento.nome[0][1]==nodo.nome[0][1] and elemento.nome[0][2]==nodo.nome[0][2] and elemento.nome[1][0]==nodo.nome[1][0] and elemento.nome[1][1]==nodo.nome[1][1] and elemento.nome[1][2]==nodo.nome[1][2] and elemento.nome[2][0]==nodo.nome[2][0] and elemento.nome[2][1]==nodo.nome[2][1] and elemento.nome[2][2]==nodo.nome[2][2]:
			return 1	
	return 0		
						


def genera_mosse(nodo,g):
	for i in range(0,3):
			for y in range(0,3):
				
				if nodo.nome[i][y]=="" and nodo.tipo()=="?":
					nuovo=copy.deepcopy(nodo) 
					nuovo.nome[i][y]=g
					nuovo.lista_figli=[] 
					if presente(nodo.lista_figli,nuovo)==0:
						if g=="o":
							nuovo=genera_mosse(nuovo,"x")
						else:
							nuovo=genera_mosse(nuovo,"o")
						nodo.lista_figli.append(nuovo)  
	return nodo
	
	

	
def gen_tree(griglia):
		nodo=NodoTris(griglia)
		g=nodo.giocatore_di_turno()
		nodo=genera_mosse(nodo,g)
		
		return nodo
	
