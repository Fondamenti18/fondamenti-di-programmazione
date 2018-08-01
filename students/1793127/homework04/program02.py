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
from copy import deepcopy
class NodoTris:
	def __init__(self, griglia):
		self.nome = griglia
		self.lista_figli = [] #lista dei nodi figli
		self.tipologia='?'
		
	def tipo(self):
		cont=0
		if triso(self.nome)==True:
			self.tipologia='o'
		elif trisx(self.nome)==True:
			self.tipologia='x'
		else:
			for x in self.nome:
				for y in x:
					if y=='':
						cont+=1
						break
			if cont==0:
				self.tipologia='-'
		return self.tipologia
		
	def esiti(self):
		contx=0
		conty=0
		contpari=0
		lst=[]
		e=(0,0,0)
		e=esiti_ric(self,contx,conty,contpari,lst)
		return e
    
	def vittorie_livello(self, giocatore, h):
		cont=0
		n=0
		cont=vittorie_livello_ric(self,cont,n,giocatore,h)
		return cont
    
	def strategia_vincente(self,giocatore):
		d={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
		d=gen_dict(self,d)
		for x in d:
			for x in d[x]:
				if (x.tipo()=='x' and giocatore=='o') or (x.tipo()=='o' and giocatore=='x'):
					return False
				if x.tipo()==giocatore:
					return True
		return False


def gen_tree(griglia):
	nodo=NodoTris(griglia)
	n=0
	mos=''
	ric_gen_tree(nodo,n,mos)
	return nodo
	
def ric_gen_tree(nodo,n,mos):
	lst=[]
	l=[]
	lista_figli=[]
	if n==0:
		contx=0
		conto=0
		for riga in nodo.nome:
			for casella in riga:
				if casella=='o':
					conto+=1
				if casella=='x':
					contx+=1
		if contx<conto:
			mos='x'
		if contx==conto:
			mos='o'
	righe=len(nodo.nome)
	colonne=len(nodo.nome[0])
	for riga in range(righe):
		for colonna in range(colonne):
			if nodo.nome[riga][colonna]=='':
				lst.append((riga,colonna))
	for x in lst:
		i,j=x[0],x[1]
		nChild=deepcopy(nodo.nome)
		nChild[i][j]=mos
		l.append(nChild)
		nodo.lista_figli.append(nChild)
	for i in range(len(l)):
		nodo.lista_figli[i]=NodoTris(l[i])
	for x in nodo.lista_figli:
		if mos=='x' and trisx(x.nome)==False:
			ric_gen_tree(x,n+1,mos='o')
		if mos=='o' and triso(x.nome)==False:
			ric_gen_tree(x,n+1,mos='x')

def triso(griglia):
		bol=False
		if (griglia[0][0]=='o' and griglia[1][1]=='o' and griglia[2][2]=='o') or (griglia[0][0]=='o' and griglia[0][1]=='o' and griglia[0][2]=='o') or (griglia[0][0]=='o' and griglia[1][0]=='o' and griglia[2][0]=='o') or (griglia[0][2]=='o' and griglia[1][2]=='o' and griglia[2][2]=='o') or (griglia[0][1]=='o' and griglia[1][1]=='o' and griglia[2][1]=='o') or (griglia[1][0]=='o' and griglia[1][1]=='o' and griglia[1][2]=='o') or (griglia[0][2]=='o' and griglia[1][1]=='o' and griglia[2][0]=='o') or (griglia[2][2]=='o' and griglia[2][1]=='o' and griglia[2][0]=='o'):
			bol=True
		return bol
	
def trisx(griglia):
		bol=False
		if (griglia[0][0]=='x' and griglia[1][1]=='x' and griglia[2][2]=='x') or (griglia[0][0]=='x' and griglia[0][1]=='x' and griglia[0][2]=='x') or (griglia[0][0]=='x' and griglia[1][0]=='x' and griglia[2][0]=='x') or (griglia[0][2]=='x' and griglia[1][2]=='x' and griglia[2][2]=='x') or (griglia[0][1]=='x' and griglia[1][1]=='x' and griglia[2][1]=='x') or (griglia[1][0]=='x' and griglia[1][1]=='x' and griglia[1][2]=='x') or (griglia[0][2]=='x' and griglia[1][1]=='x' and griglia[2][0]=='x') or (griglia[2][2]=='x' and griglia[2][1]=='x' and griglia[2][0]=='x'):
			bol=True
		return bol
	
def esiti_ric(self,contx,conty,contpari,lst):
		if self.tipo()=='?':
			for x in self.lista_figli:
				if x.tipo()=='x':
					contx+=1
				elif x.tipo()=='o':
					conty+=1
				elif x.tipo()=='-':
					contpari+=1
				elif x.tipo()=='?':
					(contpari,conty,contx)=esiti_ric(x,contx,conty,contpari,lst)
		elif self.tipo()=='x':
			contx+=1
		elif self.tipo()=='o':
			conty+=1
		elif self.tipo()=='-':
			contpari+=1
		return(contpari,conty,contx)
	
def vittorie_livello_ric(self,cont,n,gioc,h):
	n+=1
	if n<=h:
		for x in self.lista_figli:
			if x.tipo()=='?':
				cont=vittorie_livello_ric(x,cont,n,gioc,h)
			elif x.tipo()==gioc and n==h:
				cont+=1
	return cont
	
def gen_dict(self,d):
	x=self.nome
	cont=0
	for riga in x:
		for colonna in x[0]:
			if colonna=='x' or colonna=='o':
				cont+=1
	if cont>=5:
		d[cont].append(self)
	for child in self.lista_figli:
		d=gen_dict(child,d)
	return d
		