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

#nodo
class Nodo:
	def __init__ (self,nome,vicini):
		self.nome=nome
		self.vicini=set(vicini)
		
#grafo classe principale
class Grafo:
	def __init__(self):
		self.nodi={}

	def addN(self,nome):
		if nome in self.nodi:
			return
		self.nodi[nome]=Nodo(nome,set())

	def addA(self,nodo1,nodo2):
		if nodo1 not in self.nodi:
			
			return
		if nodo2 not in self.nodi:
			
			return
		self.nodi[nodo1].vicini.add(nodo2)
		self.nodi[nodo2].vicini.add(nodo1)

	def getVicini(self,nome):
		if nome not in self.nodi:
			return
		return self.nodi[nome].vicini
	
	def getNodi(self):		
		return self.nodi.keys()
	
	def getArchi(self):
		archi=set()
		for nome,nodo in self.nodi.items():
			for vicini in nodo.vicini:
				if (vicini,nome) in archi:
					continue
				archi.add((nome,vicini))
		return archi



	    

#genera un'albero dal grafo
def gen_tree(grafo,nome):
	visti=set([nome])
	prossimi=set([nome])
	tree={nome:None}
	while prossimi:
		nuovi=set()
		while prossimi:
			u=prossimi.pop()			
			for v in grafo.getVicini(u):
				if v not in visti:
					visti.add(v)
					nuovi.add(v)
					tree[v]=u
		prossimi=nuovi
	return tree


#dall'albero ricava il percorso
def percorso(tree, nome):
	radice=None
	for u,nxt in tree.items():
		if nxt==None:
			radice=u
			break
	if nome in tree:
		p=[nome]
		while nome!=radice:			
			nome=tree[nome]
			p.insert(0,nome)
	return p

#genera il grafo dalla mappa di gioco		
def gen_graph(mappa,car):
	global circuito
	circuito=Grafo()
	vicini=[(-1,0),(1,0),(0,-1),(0,1)]	
	for y in range(len(mappa)):
		for x in range(len(mappa[0])):
			if mappa[y][x]==" " or mappa[y][x]=="O" or mappa[y][x]==car :
				circuito.addN((x,y))
	for y in range(len(mappa)):
		for x in range(len(mappa[0])):
			if mappa[y][x]==" " or mappa[y][x]=="O" or mappa[y][x]==car :
				for i,j in vicini:
					ii=i+x
					jj=j+y
					if mappa[jj][ii]==" " or mappa[jj][ii]=="O" or mappa[jj][ii]==car  :
						circuito.addA((x,y),(ii,jj))





def decisione(pross,vx,vy,x,y, mappa):
	ris=[]
	if mappa[pross[1]][pross[0]]=="O":
		
		if vx!=0:
			if mappa[pross[1]+1][pross[0]]==" ":
				pross=(pross[0],pross[1]+1)
			elif mappa[pross[1]-1][pross[0]]==" ":
				pross=(pross[0],pross[1]-1)
		elif vy!=0:
			if mappa[pross[1]][pross[0]+1]==" ":
				pross=(pross[0]+1,pross[1])
			elif mappa[pross[1]][pross[0]-1]==" ":
				pross=(pross[0]-1,pross[1])
	if pross[0]>x:
		if vx==1:
			ris.append(0)
		else:
			ris.append(1)
	elif pross[0]==x:
		if vx==0:
			ris.append(0)
		elif vx==1:
			ris.append(-1)
		else:
			ris.append(1)
	elif pross[0]<x:
		if vx==-1:
			ris.append(0)
		else:
			ris.append(-1)
	if pross[1]>y:
		if vy==1:
			ris.append(0)
		else:
			ris.append(1)
	elif pross[1]==y:
		if vy==0:
			ris.append(0)
		elif vy==1:
			ris.append(-1)
		else:
			ris.append(1)
	elif pross[1]<y:
		if vy==-1:
			ris.append(0)
		else:
			ris.append(-1)
	return ris



circuito=Grafo()
cdiz={}
path=[]

def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty, laps):
        global circuito,cdiz,path
        if laps==0 and vx==0 and vy==0:
                gen_graph(griglia_corrente,car)
                cdiz={}
                path=[]
                if verso ==1:                       
                        return 1,0                                             
                else:
                        return -1,0                        
        
        if len(cdiz)==0:
                if verso==1:
                        cdiz=gen_tree(circuito,(x+1,y))
                        path=percorso(cdiz,(startx-2,starty))
                        path=path[:-3]
                     
                else:
                        cdiz=gen_tree(circuito,(x-1,y))
                        path=percorso(cdiz,(startx+2,starty))
                        path=path[:-3]
                  
                        
        if len(path)>0:
                pross=path.pop(0)                
                if pross==(x,y):
                        pross=path.pop(0)               
                v=decisione(pross,vx,vy,x,y,griglia_corrente)
               
                return(v[0],v[1])
        
        if laps ==1:
                if verso==1 and vx!=0:
                        return -1,0
                elif verso==-1 and vx!=0:
                        return 1,0
        return 0,0
                        
                        
                        
                

        
                

        
    
    
    
  
