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

class NodoTris:
	def __init__(self, griglia):
		self.nome = griglia
		self.lista_figli = [] #lista dei nodi figli
    
	def tipo(self):
		lo=0
		lx=0
		vx=0
		vo=0
		rt='?'
		for r in range(3):
			for c in range(3):
				if self.nome[r][c]=='o': lo+=1
				elif self.nome[r][c]=='x': lx+=1
		if (self.nome[0][0]=='o' and self.nome[0][1]=='o' and self.nome[0][2]=='o') or (self.nome[1][0]=='o' and self.nome[1][1]=='o' and self.nome[1][2]=='o') or \
			(self.nome[2][0]=='o' and self.nome[2][1]=='o' and self.nome[2][2]=='o') or (self.nome[0][0]=='o' and self.nome[1][0]=='o' and self.nome[2][0]=='o') or \
			(self.nome[0][1]=='o' and self.nome[1][1]=='o' and self.nome[2][1]=='o') or (self.nome[0][2]=='o' and self.nome[1][2]=='o' and self.nome[2][2]=='o') or \
			(self.nome[0][0]=='o' and self.nome[1][1]=='o' and self.nome[2][2]=='o') or (self.nome[0][2]=='o' and self.nome[1][1]=='o' and self.nome[2][0]=='o'):
				vo=1
				rt='o'
		elif (self.nome[0][0]=='x' and self.nome[0][1]=='x' and self.nome[0][2]=='x') or (self.nome[1][0]=='x' and self.nome[1][1]=='x' and self.nome[1][2]=='x') or \
			(self.nome[2][0]=='x' and self.nome[2][1]=='x' and self.nome[2][2]=='x') or (self.nome[0][0]=='x' and self.nome[1][0]=='x' and self.nome[2][0]=='x') or \
			(self.nome[0][1]=='x' and self.nome[1][1]=='x' and self.nome[2][1]=='x') or (self.nome[0][2]=='x' and self.nome[1][2]=='x' and self.nome[2][2]=='x') or \
			(self.nome[0][0]=='x' and self.nome[1][1]=='x' and self.nome[2][2]=='x') or (self.nome[0][2]=='x' and self.nome[1][1]=='x' and self.nome[2][0]=='x'):
				vx=1
				rt='x'
		if vx==0 and vo==0 and (lx+lo)==9: rt='-'
		return rt


	def esiti(self):
		re=[0,0,0]
		if self.tipo()=='-': re[0]+=1
		elif self.tipo()=='o': re[1]+=1
		elif self.tipo()=='x': re[2]+=1
		reappo=list()
		for appo in self.lista_figli:
			reappo=appo.esiti()
			re[0]+=reappo[0]
			re[1]+=reappo[1]
			re[2]+=reappo[2]
		return (re[0],re[1],re[2])


	def vittorie_livello(self, giocatore, h):
		rv=0
		if self.tipo()==giocatore and h==0:
			rv+=1
			return rv
		prec=h-1
		if prec>=0:
			for f in self.lista_figli:
				rv+=f.vittorie_livello(giocatore,prec)
		return rv


	def strategia_vincente(self,giocatore):
		lo=0
		lx=0
		plv=''
		primo='x'
		res=list()
		for r in range(3):
			for c in range(3):
				if self.nome[r][c]=='o': lo+=1
				elif self.nome[r][c]=='x': lx+=1
		if (lo+lx)%2==0: primo='o'
		rvp=self.vittorie_livello(primo,1)
		if rvp>0: plv=primo
		else:
			res=self.esiti()
			if res[1]>res[0]+res[2]: plv='o'
			else: plv='x'
		return plv==giocatore


import copy

def gen_tree(griglia):
	radice=NodoTris(griglia)
	if radice.tipo()=='?':
		lo=0
		lx=0
		mo='x'
		freec=list()
		for r in range(3):
			for c in range(3):
				if radice.nome[r][c]=='o': lo+=1
				elif radice.nome[r][c]=='x': lx+=1
				else: freec.append([r,c])
		if (lo+lx)%2==0: mo='o'
		for l in freec:
			appo=copy.deepcopy(griglia)
			appo[l[0]][l[1]]=mo
			radice.lista_figli.append(gen_tree(appo))
	return radice

