'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3 3 caselle.
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
#
class NodoTris:

	def __init__(self, griglia):
		self.nome = griglia
		self.lista_figli = [] #lista dei nodi figli
		self.expanded = False
		
	def isIncompleto(self,tris):
		for i in range(3):
			for j in range(3):
				if tris[i][j]== '':
					return True
		return False
	
	def isExpanded(self):
		return self.expanded
		
		
	def get_free_move(self):
		tris= self.nome
		if tris==None:
			return 9
		free_move=0
		for i in range(3):
			for j in range(3):
				if tris[i][j]== '':
					free_move+=1
		return free_move
	
	def isSoluzione(self,tris):
		incompleto= self.isIncompleto(tris)
		xwinning= self.isWinning('x', tris)
		owinning= self.isWinning('o', tris)
		if xwinning:
			return 'x'
		if owinning:
			return 'o'
		if incompleto:
			if not(xwinning or owinning):
				return '?'
		return '-'
		
	def getFigli(self):
		return self.lista_figli
	
	def isWinning(self,giocatore, tris):
		winningdiagonal_1=True
		winningdiagonal_2=True
		for i in range(3):
			winningrow=True
			winningcolumn=True
			
			if tris[i][i]!=giocatore:
				winningdiagonal_1=False
			if tris[i][2-i]!= giocatore:
				winningdiagonal_2=False
			for j in range(3):
				if tris[i][j]!=giocatore:
					winningrow=False
				if tris[j][i]!=giocatore:
					winningcolumn=False
			if winningrow or winningcolumn:
				return True
		if winningdiagonal_1 or winningdiagonal_2:
			return True
		return False			
				
		
	def trova_posizioni_vuote(self,tris):
		posizioni_vuote=[]
		for i in range(3):
			for j in range(3):
				if tris[i][j]=='':
					posizioni_vuote.append((i,j))
		return posizioni_vuote
		
	
	
	def mossa(self,n):
		if n%2==0:
			return 'o'
		else:
			return 'x'
	
	
	def invert_move(self,move):
		if move=='x':
			return 'o'
		else:
			return 'x'
	
	
	def __hash__(self):
		result=''
		if self.nome==None:
			return 'None'
		for i in range(3):
			for j in range(3):
				if self.nome[i][j]=='':
					result+='2'
				elif self.nome[i][j]=='o':
					result+='0'
				elif self.nome[i][j]=='x':
					result+='1'
					
		
		return int(result)		
			
		
    

    
	
	def stampaGriglia(self):
		print(self.nome)
	
	
	
	def expand_tree(self, next_move):
		tris = self.nome
		#print('TRIS = \n',tris)
		if not (self.isWinning('o', tris) or self.isWinning('x', tris)):
			if self.isIncompleto(tris):	#se e incompleto
		#		print('E iNcompletoooo')
				L=self.trova_posizioni_vuote(tris)
		#		print('L' , L)
				#if L != []:
				#	coppie = L[0]
				for coppie in L:
					i=coppie[0]
					j=coppie[1]
					tris_next= self.clone()
					
					tris_next[i][j]=next_move
					
					nodo_next= NodoTris(tris_next)
					self.lista_figli.append(nodo_next)
		#			print(' NODO   X    \n',nodo_next.nome)
					
					nodo_next.expand_tree(self.invert_move(next_move))
					
				
				
				
	
	def isFoglia(self):
		if(self.lista_figli == []):
			return True
		else:
			return False
	
	def trovaFoglieR(self, listaFoglie):
		if(self.isFoglia()):
			listaFoglie.append(self)
		else:
			for n in self.getFigli():
				n.trovaFoglieR(listaFoglie)
		
	
	def trovaFoglie(self):
		foglie = []
		self.trovaFoglieR(foglie)
		return foglie
		
	def stampaAlbero(self, str_level):
		print('nodo = ',str_level,self.nome)
		figli = self.lista_figli
		if figli == []:
			return
		for i in figli:		
			lev = str_level,'       '
			i.stampaAlbero(lev )	
		
	
	def equals(self,tris1, tris2):
		for i in range(3):
			for j in range(3):
				if tris1[i][j] != tris2[i][j]:
					return False
		return True
	
	def tipo(self):
		return self.isSoluzione(self.nome)
		
	def esiti(self):
		x = 0
		o = 0
		patte = 0
		if not self.isExpanded():
			
			
			#print('ESITI SELF = \n',self.nome)
			self.expand_tree(self.mossa(9-self.get_free_move()))
			#print('albero espanso')
			#self.stampaAlbero('')
		foglie = self.trovaFoglie()
		#print('FOGLIE !!! \n ')
		#for f in foglie:
		#	f.stampaGriglia()
		#input('Ciao')
		foglieDistinte = set(foglie)
		#print('foglieDistinte !!! \n ')
		for F in foglieDistinte:
		#	print('FOGLIA = ',F.nome)
			result = self.isSoluzione(F.nome)
			if result == 'x':
				x+=1
			if result == 'o':
				o+=1
			if result == '-':
				patte+=1
		self.expanded = True
		return (patte,o,x)
		
		
	def clone(self):
		Matrix = [[0 for g in range(3)] for r in range(3)]
		#print(Matrix)
		for i in range(3):
			for j in range(3):
				Matrix[i][j] = self.nome[i][j]
		return Matrix
		
	
	def estraiNodiPerLivello(self,h):
		nodiLivello = []
		self.estraiLivello(h,nodiLivello,0)
		return nodiLivello
		
	def estraiLivello(self,h,nodiLivello, currentLivello):
		if(h == currentLivello):
			nodiLivello.append(self)
		else:
			for n in self.getFigli():
				n.estraiLivello(h,nodiLivello,currentLivello+1)
        
	
	def vittorie_livello(self, giocatore, h):
		count = 0
		nodiLivelli = self.estraiNodiPerLivello(h)
		for n in nodiLivelli:
			if n.isSoluzione(n.nome) == giocatore:
				count+=1
		return count
		
        
    
	def getTuplaByNodi(self, nodi):
		
		if nodi == []:
			return None #quando non ci sono piu livelli disponibili
		x = 0
		o = 0
		patte = 0
		for n in nodi:
		#	print('FOGLIA = ',F.nome)
			result = self.isSoluzione(n.nome)
			if result == 'x':
				x+=1
			if result == 'o':
				o+=1
			if result == '-':
				patte+=1
		return (patte,o,x)
	'''
	def strategia_vincente(self,giocatore):
		self.esiti()
		h = 1
		result = False
		while(True):
			nodi = self.estraiNodiPerLivello(h)
			tupla = self.getTuplaByNodi(nodi)
			if tupla == None:
				return result
			#print(' WHILE livello: ',h,' tupla = ',tupla)
			#input('stampo la tupla!\n')
			#print('livello: ',h,' tupla = ',tupla)
			#print('giocatore vincente = ',giocatore)
			#print('tupla[1] = ',tupla[1])
			#print('tupla[2] = ',tupla[2])
			numNodiLevel = len(nodi)
			print('LIVELLO ',h,' ha ',numNodiLevel,' nodi')
			if giocatore == 'x':
				if h == 2:
					if int(tupla[1]) ==0 and int(tupla[2]) > 0:
						return True
				else:
					if h%2 == 0:
						if int(tupla[2]) == numNodiLevel:
							return True
				if h == 1:
					if int(tupla[2]) ==0 and int(tupla[1]) > 0:
						return False
				else:
					if h%2 != 0:
						if int(tupla[1]) == numNodiLevel:
							return False
			if giocatore == 'o':
				if h == 1:
					if int(tupla[2]) ==0 and int(tupla[1]) > 0:
						return True
				else:
					if h%2 != 0:
						if int(tupla[1]) == numNodiLevel:
							return True
				if h == 2:
					if int(tupla[1]) ==0 and int(tupla[2]) > 0:
						return False
				else:
					if h%2 == 0:
						if int(tupla[2]) == numNodiLevel:
							return False
			
			
			h+=1
'''
	

	def trovaPrimiFigliBuoni_OLD(self, h, giocatore, altezze):
		figli = self.getFigli()
		for n in figli:
			#print(n.stampaGriglia())
			tupla = self.getTuplaByNodi(figli)
			#print('LEN FIGLI = ',len(figli))
			#print('TUPLA = ',tupla)
			if giocatore == 'x':
				if len(figli) == tupla[2]:
			#		print('SIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIi  XXXXXX')
					if altezze == []:
			#			print('METTO DENTRO ALTEZZE');
						altezze.append(h+1)
						return
			if giocatore == 'o':
				if len(figli) == tupla[1]:
					if altezze == []:
						altezze.append(h+1)
			n.trovaPrimiFigliBuoni(h+1,giocatore,altezze)
		
	def trovaPrimiFigliBuoni(self, h, giocatore, altezze):
		figli = self.getFigli()
		for n in figli:
			#print(n.stampaGriglia())
			tupla = self.getTuplaByNodi(figli)
			#print('LEN FIGLI = ',len(figli))
			#print('TUPLA = ',tupla)
			if giocatore == 'x':
				if tupla[2] > 0 and tupla[1] == 0:
			#		print('SIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIi  XXXXXX')
					if altezze == []:
			#			print('METTO DENTRO ALTEZZE');
						altezze.append(h+1)
						return
			if giocatore == 'o':
				if tupla[1] > 0 and tupla[0] == 0:
					if altezze == []:
						altezze.append(h+1)
			n.trovaPrimiFigliBuoni(h+1,giocatore,altezze)

	def strategia_vincente(self,giocatore):
		self.esiti()
		altezze = []
		self.trovaPrimiFigliBuoni(0,'x',altezze)
		altezzaMinimaX = -1
		altezzaMinimaO = -1
		if altezze != []:
			altezzaMinimaX = altezze[0]
		
		altezze = []
		self.trovaPrimiFigliBuoni(0,'o',altezze)
		if altezze != []:
			altezzaMinimaO = altezze[0]
		
		nodiTurnoO = self.estraiNodiPerLivello(1)
		tuplaO = self.getTuplaByNodi(nodiTurnoO)
		if tuplaO[1] > 0 and tuplaO[2] == 0:
			altezzaMinimaO = 1
		nodiTurnoX = self.estraiNodiPerLivello(2)
		tuplaX = self.getTuplaByNodi(nodiTurnoX)
		if tuplaX[2] > 0 and tuplaX[1] == 0:
			altezzaMinimaX = 2
	
		winningH = self.min(altezzaMinimaO,altezzaMinimaX)
		
		#calcolo prima soluzione se l'altro e' scemo
		'''
		if altezzaMinimaX > 2: #perche se e 2 allora l'ho gia trovata perche non puo mai essere minore di 2
			h = 4
			while(True):
				if( h >=winningH):
					break;
				nodiTurnoX = self.estraiNodiPerLivello(h)
				if nodiTurnoX == []:
					break
				tuplaX = self.getTuplaByNodi(nodiTurnoX)
				if tuplaX[2] > 0 and tuplaX[1] == 0 :
					altezzaMinimaX = h
					break
				h+=1
				if h > winningH:
					break
					
		if altezzaMinimaO > 1: #perche se e 2 allora l'ho gia trovata perche non puo mai essere minore di 2
			h = 3
			while(True):
				if( h >=winningH):
					break;
				nodiTurnoO = self.estraiNodiPerLivello(h)
				if nodiTurnoO == []:
					break
				tuplaO = self.getTuplaByNodi(nodiTurnoO)
				if tuplaO[1] > 0 and tuplaO[2] == 0:
					altezzaMinimaO = h
					break
				h+=1
				if h > winningH:
					break
		'''
				
			
		#print('ALTEZZA MINIMA X',altezzaMinimaX)
		#print('ALTEZZA MINIMA O',altezzaMinimaO)
		if giocatore == 'x':
			if altezzaMinimaX < altezzaMinimaO:
				return True
		if giocatore == 'o':
			if altezzaMinimaX > altezzaMinimaO:
				return True
		return False
		
	def min(self, a,b):
		if a < b:
			return a
		return b
        
def gen_tree(griglia):
	nodo= NodoTris(griglia)
	return nodo
	
	


#nodo= NodoTris([['', 'o', 'x'], ['', '', ''], ['', '', '']])
#print(nodo.esiti())
#minH = nodo.strategia_vincente('x')
#print(nodo.strategia_vincente('o'))
#print(nodo.trova_posizioni_vuote([['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]))

#print(nodo.esiti())
#nodiLivelli = nodo.estraiNodiPerLivello(8)
#for n in nodiLivelli:
#	n.stampaGriglia()


#vinto =nodo.isSoluzione([['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']])
#print(vinto)
#print('',nodo.isSoluzione([['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'o']]))
#print(nodo.isSoluzione([['x', 'o', 'o'], ['x', 'x', 'o'], ['o', '', 'x']]))
#print(nodo.isSoluzione([['o', 'x', 'x'], ['o', 'o', 'x'], ['o', 'o', 'x']]))
#print(nodo.isSoluzione([['x', 'o', 'x'], ['x', 'o', 'o'], ['o', 'x', 'o']]))'''
