'''
Obiettivo dell'esercizio e' sviluppare la strategia di gioco di una macchinetta che gira su una pista di formula 1.

Il gioco consiste in un percorso di gara, rappresentato da una griglia di caratteri
(' '=vuoto, '#' = ostacolo, 'A....Z' = auto, '|' = traguardo 'O' = buca tutti gli altri caratteri sono ostacoli)
nella quale si trova la macchina del giocatore (un carattere 'A..Z'), che deve:
	correre attorno alla pista per un intero giro senza sbattere contro ostacoli o altre macchine
	raggiungere il traguardo
	fermarsi senza sbattere (vx=vy=0)

Il punteggio di gioco e' il numero di step che sono stati necessari a percorrere la gara e fermarsi senza sbattere.

Ad ogni istante il simulatore della macchinetta conosce:
	x, y:   la posizione della macchina sulla griglia di gioco
	vx, vy: la velocita' corrente della macchina
Ad ogni step della simulazione il giocatore puo' solo:
	incrementare di 1, decrementare di 1 o lasciare come sono i valodi vx, vy della velocita' (-1,0,+1)
corrispondentemente il simulatore:
	somma gli incrementi/decrementi alle due variabili vx,vy
	somma le velocita' vx,vy alla posizione x,y ottenendo la prossima posizione della macchina
	controlla se la nuova posizione e' vuota
		se la nuova posizione e' occupata (da un ostacolo o da un'altra macchina) il gioco termina senza completare la corsa
		se la posizione contiene una buca si slitta di un carattere a caso fino a restare sulla strada o su un ostacolo
		altrimenti si sposta la macchina sulla nuova posizione
	se il traguardo e' stato raggiunto nella direzione giusta e la macchina e' ferma (vx=vy=0) la gara termina
	altrimenti si riesegue un nuovo step (chiedendo alla funzione 'ai' del giocatore cosa fare)

Il programma che dovete realizzare e' l'AI che guida la macchina, che riceve come input:
	la griglia di gioco del passo precedente (comprese le altre macchine)
	la griglia di gioco del passo corrente (comprese le altre macchine)
	la posizione x,y della propria macchina
	la velocita' vx,vy della propria macchina
	il carattere che individua la vostra macchina
	il verso di rotazione (-1= si parte verso sinistra rispetto al traguardo, +1= si parte verso destra rispetto al traguardo)
	la posizione startx,starty di partenza della macchina
	(NUOVO) il numero di attraversamenti del traguardo fatti dalla macchina (contromano se negativo)
e deve produrre in output la coppia:
	ax, ay  variazione della velocita (coppia di valori -1,0,+1)
La simulazione di tutti i 3 percorsi di gara per la qualificazione (senza visualizzazione) deve impiegare al piu' 1 minuto.

In questo esercizio la valutazione avverra' in tre fasi:
	giro di qualificazione: 
		la macchina gira sulla pista di gara da sola, senza altri concorrenti su 3 piste in cui non sono presenti barriere di buche
		superare questa prova da' il punteggio minimo di qualificazione (18)
	giro di premio:
		la macchina gira su una pista di gara simile (ma diversa) da quella "Roma" che contiene barriere di buche
		superare questa prova da' il punteggio di qualificazione 24

	La classifica ottenuta nella qualificazione viene usata per determinare i gironi e poi il torneo di gara della fase successiva
	chi non completa il giro di qualificazione non partecipa al successivo torneo e non e' sufficiente

	Gironi e torneo ad eliminazione:
		(per ogni scontro vengono eseguite due gare, con A a sinistra e B a destra e viceversa)
		viene organizzato un torneo in cui prima si eseguono dei gironi di 4-5 auto
			Le due auto che ottengono il miglior punteggio sul girone partecipano alle eliminatorie successive
			Per ogni gara del girone vengono assegnati:
				3 punti a chi vince la gara
				1 punto per pareggio o scontro
				0 punti a chi perde
				a parita' di punteggio vince la macchina che ha fatto meno incidenti
				a parita' di incidenti viene simulata un'altra gara con una pista con barriere di buche (tipo "roma" per intenderci)

		Le due auto qualificate di ciascun girone partecipano ad una fase eliminatoria a scontro diretto
			l'auto vincente passa il turno (in caso di patta su esegue una gara aggiuntiva con barriere di buche casuali)

	La classifica finale della fase a scontro diretto determina i voti:
		I livelli del torneo ad eliminazione individuano i voti ottenuti, a seconda del numero di partecipanti (per esempio 6 livelli -> 2.1 voti per livello circa)
		Per avere la sufficienza bisogna aver completato almeno il giro di qualificazione sulle diverse piste
		Se una macchina ha ottenuto il voto 24 nella fase di qualificazione, il voto finale dell'esercizio e' almeno 24

COMPORTAMENTO: le auto che usano comportamenti scorrette non superano la qualificazione. Es.
	- precalcolare offline la strategia e inserirla nel programma
	- andare apposta contro l'auto dell'avversario
	- ...

ATTENZIONE: NON usate lettere accentate ne' nel codice ne' nei commenti

'''

from random import randint

buffer_step = []
buffer_path = []
final_sprint = False

#def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty): # vecchia versione
def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty, laps):
	global final_sprint
	#reset vars if new game started
	new_game = (vx == vy == 0) & (griglia_corrente[y][x-verso] == '|') & (griglia_corrente == griglia_precedente) #CHECK GRIGLIA_PRECEDENTE
	if new_game:
		reset_vars()
		calcaulte_path(car,griglia_corrente,x,y,verso)
	#eat steps in buffer
	if buffer_step:
		return buffer_step.pop()
	#eat nodes in buffer
	if buffer_path:
		calculate_steps(x,y,buffer_path.pop())
		return buffer_step.pop()
	if not laps and not final_sprint:
		final_sprint = True
		return (verso,0)
	elif not laps and final_sprint:
		return (0,0)
	elif laps:
		return (verso*(-1),0)

def calcaulte_path(car,griglia_corrente,x,y,verso):
	grid = [r[:] for r in griglia_corrente]
	mapGridToNum(grid,car)
	writeDistances(grid,x,y)
	tmp_path = findPath(grid, findGoal(griglia_corrente,x,y,verso))
	global buffer_path
	buffer_path = findTurns(tmp_path)

def writeDistances(grid,starting_x,starting_y):
	unseen = [(starting_x,starting_y)]
	while unseen:
		x,y = unseen.pop()
		for dy in range(-1,2):
			for dx in range(-1,2):
				try:
					if (dx == dy == 0) | (grid[y+dy][x+dx] < 0):
						continue
					if grid[y+dy][x+dx] == float('inf'):
						unseen.append((x+dx,y+dy))
					grid[y+dy][x+dx] = min(grid[y+dy][x+dx],grid[y][x]+1)
				except Exception as e:
					pass

def findGoal(griglia_corrente,x,y,verso):
	goal = None
	if griglia_corrente[y][x - (2*verso)] == ' ':
		return (x - (2*verso),y)
	for y_g in range(len(griglia_corrente)):
		for x_g in range(len(griglia_corrente[0])):
			if griglia_corrente[y_g][x_g] == '|':
				goal = [goal,(x_g - (2*verso),y_g)][griglia_corrente[y_g][x_g - (2*verso)] == ' ']
	return goal

def findPath(grid, goal):
	if (goal == None) or (grid[goal[1]][goal[0]] == float('inf')):
		return [(0,1)]*10
	tmp_path = []
	curPos = goal
	tmp_path.append(goal)
	while(grid[curPos[1]][curPos[0]] != 0):
		nextPos = findSmallestNeighbour(curPos[0], curPos[1], grid)
		tmp_path.append(nextPos)
		curPos = nextPos
	return tmp_path

def findTurns(path):
	turns = []
	direction = (0, 0)
	for i in range(1, len(path)):
		nextDirection = (path[i][0] - path[i - 1][0], path[i][1] - path[i - 1][1])
		if nextDirection != direction:
			turns.append(path[i - 1])
			direction = nextDirection
	return turns

def findSmallestNeighbour(x,y,grid):
	smallest = float('inf')
	coords = (0,0)
	for dy in range(-1,2):
		for dx in range(-1,2):
			if (dx == dy == 0):
				continue
			try:
				a_x = x + dx
				a_y = y + dy
				if 0 <= grid[a_y][a_x] <= smallest:
					smallest = grid[a_y][a_x]
					coords = (a_x,a_y)
			except Exception as e:
				pass
	return coords

def calculate_steps(x,y,target):
	tmp_buff = []
	d,g = dir_and_gap(x,y,target[0],target[1])
	oppo_d = (d[0]*(-1),d[1]*(-1))
	while g > 0:
		mult = int(g**0.5)
		tmp_buff += [d]*mult + [oppo_d]*mult
		g -= mult**2
	#removes redundance
	new_b = []
	skipped = False
	for i in range(len(tmp_buff)-1):
		if skipped:
			skipped = False
			continue
		if (tmp_buff[i] == oppo_d) & (tmp_buff[i+1] == d):
			skipped = True
			new_b.append((0,0))
		else:
			new_b.append(tmp_buff[i])
	new_b.append(tmp_buff[-1])
	#reverses steps
	global buffer_step
	buffer_step = new_b[::-1]

def dir_and_gap(x,y,tx,ty):
	deltax = (tx-x)
	deltay = (ty-y)
	direcx = 0
	direcy = 0
	if deltax != 0:
		direcx = deltax//abs(deltax)
	if deltay != 0:
		direcy = deltay//abs(deltay)
	return ((direcx,direcy)),(max(abs(deltax),abs(deltay)))

def mapGridToNum(grid,car):
	#maybe fix x & y
	for x in range(0, len(grid)):
		for y in range(0, len(grid[0])):
			grid[x][y] = mapCharToNum(grid[x][y],car)

def mapCharToNum(char_,car):
	if char_ == ' ':
		return float("inf")
	if char_ == '#':
		return -2
	if char_ == 'O':
		return -3
	if char_ == '|':
		return -4
	if char_ == car:
		return 0
	return -ord(char_)

def reset_vars():
	global buffer_step
	global buffer_path
	global final_sprint
	buffer_step = []
	buffer_path = []
	final_sprint = False