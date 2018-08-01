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

from random     import randint
from math import fabs

def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty, laps):
	
	giocatori = 'ABCDEFGHIJKLMNPQRSTUVWXYZ'
	
	if x == startx and y == starty:               #SE LA MACCHINA SI TROVA NELLA POSIZIONE INIZIALE, SI AVVIA 
		return(verso, 0)                          #NEL VERSO DI PERCORRENZA
		
	if laps != 0:                                 #SE HA COMPLETATO IL GIRO L'AUTO RALLENTA FINO A FERMARSI
		if vy == 0 and vx == 0:
			return(0, 0)
		if vy == 0:
			return(int(-vx//fabs(vx)), 0)
		else:
			return(int(-vx//fabs(vx)), int(-vy//fabs(vy)))
	
	############### PERCORRENZA ORIZZONTALE
	
	#CONTROLLO LA DIREZIONE IN CUI SI MUOVE LA MACCHINA
	
	if vx != 0 or vy == 0:
		if vx > 0:
			direzione = 2
			u = 1							#VERSO INCREMENTO X
		else:
			direzione = 4
			u = -1							#VERSO INCREMENTO X
			
		#CALCOLO DISTANZA DAL BORDO
		
		d = distanza(griglia_corrente, x, y, direzione)
		
		if griglia_corrente[y][x + vx] in giocatori:
			if vx != 0:
				return(-u, 0)
			else:
				return(0, -u)
		
		if d > 2:
			if griglia_corrente[y][x + vx + 2*u] == 'O':
				return(u, 0)
			elif griglia_corrente[y][x + vx] == 'O':
				return(u, 0)
			elif fabs(vx) > 1 and griglia_corrente[y][x + vx - u] != 'O':
				return(-u, -vy)
			else:
				return(0, -vy)
		else:
			d_up = distanza(griglia_corrente, x, y, 1)       #CALCOLO DISTANZA DALL'ALTO E DISTANZA
			d_down = distanza(griglia_corrente, x, y, 3)	 #DAL BASSO PER DECIDERE DOVE CURVARE
		
			if d_up > d_down:
				return(-u, -1)
			else:
				return(-u, 1)
		
	############### PERCORRENZA VERTICALE
	
	#CONTROLLO LA DIREZIONE IN CUI SI MUOVE LA MACCHINA
	
	if vy != 0 or vx == 0:
		if vy > 0:
			direzione = 3
			u = 1											  #VERSO INCREMENTO Y
		else:
			direzione = 1
			u = -1											  #VERSO INCREMENTO Y
		#CALCOLO DISTANZA DAL BORDO
	
		d = distanza(griglia_corrente, x, y, direzione)
		
		if d > 2:
			if griglia_corrente[y + vy + 2*u][x] == 'O':
				return(0, u)
			if griglia_corrente[y + vy][x] == 'O':
				return(0, u)
			elif fabs(vy) > 1 and griglia_corrente[y + vy - u][x] != 'O':
				return(-vx, -u)
			else:
				return(-vx, 0)
		else:
			d_right = distanza(griglia_corrente, x, y, 2)       #CALCOLO DISTANZA DA DESTRA E DISTANZA
			d_left = distanza(griglia_corrente, x, y, 4)	 #DA SINISTRA PER DECIDERE DOVE CURVARE
		
			if d_right > d_left:
				return(1, -u)
			else:
				return(-1, -u)
		
		
		
#FUNZIONE CHE CALOLA DISTANZA DA UN BORDO

def distanza(griglia_corrente, x, y, cardinale):
	'''cardinale indica il verso in cui calcolare la distanza (1 sopra, 2 destra, 3, sotto, 4 sinistra)'''
	distanza = 1
	if cardinale == 1:
		while griglia_corrente[y - distanza][x] != '#':
			distanza += 1
	elif cardinale == 2:
		while griglia_corrente[y][x + distanza] != '#':
			distanza += 1
	elif cardinale == 3:
		while griglia_corrente[y + distanza][x] != '#':
			distanza += 1
	elif cardinale == 4:
		while griglia_corrente[y][x - distanza] != '#':
			distanza += 1
	return distanza