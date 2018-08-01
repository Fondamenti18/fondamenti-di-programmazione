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
from pprint import pprint
class NodoTris:
	def __init__(self, griglia):
		self.nome = griglia
		self.lista_figli = [] #lista dei nodi figli    
		self.check_vit = self.tipo()

	def tipo(self):
		patta = True
		for var1 in range(3):
			counter = 0
			if self.nome[var1][0]== '': 
				patta = False
				continue
			else: 
				v=self.nome[var1][0]
				for var2 in range(3):
					#controllo orizzontale
					if self.nome[var1][var2] == v:
						counter += 1
					elif self.nome[var1][var2] == '':
						patta = False
						break
				if counter == 3:
					#print(counter)
					return v

		for var1 in range(3):
			counter = 0
			if self.nome[0][var1]== '': 
				patta = False
				continue
			else: 
				v=self.nome[0][var1]
				for var2 in range(3):
					#controllo orizzontale
					if self.nome[var2][var1] == v:
						counter += 1
					elif self.nome[var2][var1] == '':
						patta = False
						break
				if counter == 3:
					return v

		counter =  0
		if self.nome[0][0]== '': 
			patta = False
		else: 
			v=self.nome[0][0]
			for var1 in range(3):
				if self.nome[var1][var1] == v:
					counter += 1
				elif self.nome[var1][var1] == '':
					patta = False
					break
			if counter == 3:
				return v

		counter =  0
		if self.nome[2][0]== '': 
			
			patta = False
		else: 
			v=self.nome[2][0]
			for var1 in range(3):
				if self.nome[2-var1][var1] == v:
					counter += 1
				elif self.nome[2-var1][var1] == '':
					patta = False
					break
			if counter == 3:
				return v
			#caso patta
		if patta:
			return'-'
		return '?'

	def esiti(self,patte=0,ix=0,o=0,var=(0,0,0)):
		v=self.check_vit
		if  v == 'x':
			ix+= 1
		elif v == 'o':
			o+= 1
		elif v == '-':
			patte+= 1
		for child in self.lista_figli: var=child.esiti(patte,ix,o,var)
		var=(var[0]+patte,var[1]+o,var[2]+ix)
		return var
	
	def vittorie_livello(self, giocatore, h,livello=0,counter=0 ):
		if livello > h:return counter
		if livello == h and giocatore == self.check_vit:
		   # print(counter)
			return counter+1
		for child in self.lista_figli:
		   counter = child.vittorie_livello(giocatore,h,livello+1,counter) 
		return counter
	
	def strategia_vincente(self,giocatore,ris=False):
		if self.check_vit == giocatore:
			ris=True
			return ris
		if self.check_vit != '?':
			ris=False
			return ris
		for child in self.lista_figli: ris=child.strategia_vincente(giocatore,ris)
		return ris

	#def __repr__(self): return 'Nodo(' + str(self.nome) + ",\n Figli: " + str(self.lista_figli) + ')'
		
def check_mossa(griglia):
	counter = 0
	for y in griglia:
		for x in y:
			if x == '':
				pass
			else:
				counter += 1
	if counter % 2 == 0:
		return 0 #configurazione che inizia con 'o'
	else: 
		return 1 #configurazione che inizia con 'x'

def genera_albero(gr,mossa):
	if type(gr) != NodoTris:
		gr = NodoTris(gr)
	#print('gr.nome =     ',gr.nome)
	newnodo=[riga[:] for riga in gr.nome]
	#print(gr.nome,'  ',gr.check_vit,'s')
	if gr.check_vit != '?': return gr
	for y in range(3):
		for x in range(3):
			if gr.nome[y][x] == '':
				if mossa % 2 == 0:
					newnodo[y][x] = 'o'
				else:
					newnodo[y][x] = 'x' 
				newFiglio=NodoTris(newnodo)
				genera_albero(newFiglio,mossa+1)
				gr.lista_figli.append(newFiglio)
				newnodo[y][x]=''
				#print(gr.nome,gr.check_vit,'  ')
	return  gr

def gen_tree(griglia):
	mossa = check_mossa(griglia)
	rad = genera_albero(griglia,mossa)
	return rad

#gen_tree([['', 'o', 'x'], ['', '', ''], ['', '', '']])