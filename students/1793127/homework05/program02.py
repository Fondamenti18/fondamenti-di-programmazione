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
import math
from copy import deepcopy
flag=0
retroVERT=False
cont=0
from random     import randint
#def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty): # vecchia versione
def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty, laps):
	global flag
	global retroVERT
	global cont
	if x==startx and y==starty:
		flag=0
		retroVERT=False
		cont=0
	incr=0
	nDX=1
	nSX=1
	nUP=1
	nDOWN=1
	while griglia_corrente[y][x+nDX]==' ' or griglia_corrente[y][x+nDX]=='|' or (griglia_corrente[y][x+nDX]=='O' and griglia_corrente[y][x+nDX+1]!='#' and griglia_corrente[y][x+nDX+2]!='#'):
		nDX+=1
	while griglia_corrente[y][x-nSX]==' '  or griglia_corrente[y][x-nSX]=='|' or (griglia_corrente[y][x-nSX]=='O'and griglia_corrente[y][x-nSX-1]!='#'and griglia_corrente[y][x-nSX-2]!='#' ):
		nSX+=1
	while griglia_corrente[y+nDOWN][x]==' ' or (griglia_corrente[y+nDOWN][x]=='O'and griglia_corrente[y+nDOWN+1][x]!='#'and griglia_corrente[y+nDOWN+2][x]!='#'):
		nDOWN+=1
	while griglia_corrente[y-nUP][x]==' ' or (griglia_corrente[y-nUP][x]=='O'and griglia_corrente[y-nUP-1][x]!='#'and griglia_corrente[y-nUP-2][x]!='#'):
		nUP+=1
	if verso==1:
		while flag!=5:
			if laps==1:
				if vx!=0:
					incr=-1
					incr,retroORIZ=noBUCAoriz(griglia_corrente,y,x,vx,incr)
					return(incr,0)
				else:
					flag=5
			elif retroVERT==True:
				if griglia_corrente[y+vy][x-1]==' ' and cont<2:
					if cont==0:
						cont+=1
						return(-1,0)
					else:
						return(0,0)
				flag=0
				retroVERT=False
				return(+1,opp(vy))
			elif (nDX>sommatoria(vx)+vx+1) and flag==0:
				incr=+1
				incr,retroVERT=noBUCAoriz(griglia_corrente,y,x,vx,incr)
				return(incr,0)
			elif vx>0 and flag==0:
				incr=-1
				incr,retroVERT=noBUCAoriz(griglia_corrente,y,x,vx,incr)
				return(incr,0)
			elif flag==0:
				if nUP>=nDOWN:
					flag=1
				else:
					flag=3
			elif (nUP>sommatoria(vy)+math.fabs(vy)+1) and flag==1:
				incr=-1
				incr,retroVERT=noBUCAvert(griglia_corrente,y,x,vy,incr)
				return(0,incr)
			elif vy<0 and flag==1:
				incr=+1
				incr,retroVERT=noBUCAvert(griglia_corrente,y,x,vy,incr)
				return(0,incr)
			elif flag==1:
				if nSX>=nDX:
					flag=2
				else:
					flag=0
			elif (nSX>sommatoria(vx)+math.fabs(vx)+1) and flag==2 and vx>-6:
				incr=-1
				incr,retroVERT=noBUCAoriz(griglia_corrente,y,x,vx,incr)
				return(incr,0)
			elif (nSX>sommatoria(vx)+math.fabs(vx)+1) and flag==2:
				incr=0
				incr,retroVERT=noBUCAoriz(griglia_corrente,y,x,vx,incr)
				return(incr,0)
			elif vx<0 and flag==2:
				incr=+1
				incr,retroVERT=noBUCAoriz(griglia_corrente,y,x,vx,incr)
				return(incr,0)
			elif flag==2:
				if nDOWN>=nUP:
					flag=3
				else:
					flag=1
			elif (nDOWN>sommatoria(vy)+vy+1) and flag==3:
				incr=+1
				incr,retroVERT=noBUCAvert(griglia_corrente,y,x,vy,incr)
				return(0,incr)
			elif vy>0 and flag==3:
				incr=-1
				incr,retroVERT=noBUCAvert(griglia_corrente,y,x,vy,incr)
				return(0,incr)
			elif flag==3:
				if nDX>=nSX:
					flag=0
				else:
					flag=2
		return(0,0)
	if verso==-1:
		while flag!=5:
			if laps==1:
				if vx!=0:
					incr=+1
					incr,retroVERT=noBUCAoriz(griglia_corrente,y,x,vx,incr)
					return(incr,0)
				else:
					flag=5
			elif retroVERT==True:
				if griglia_corrente[y+vy][x+1]==' ' and cont<2:
					if cont==0:
						cont+=1
						return(+1,0)
					else:
						return(0,0)
				flag=2
				retroVERT=False
				return(-1,opp(vy))
			elif (nSX>sommatoria(vx)+math.fabs(vx)+1) and flag==0:
				incr=-1
				incr,retroVERT=noBUCAoriz(griglia_corrente,y,x,vx,incr)
				return(incr,0)
			elif vx<0 and flag==0:
				incr=+1
				incr,retroVERT=noBUCAoriz(griglia_corrente,y,x,vx,incr)
				return(incr,0)
			elif flag==0:
				if nUP>=nDOWN:
					flag=1
				else:
					flag=3
			elif (nUP>sommatoria(vy)+math.fabs(vy)+1) and flag==1:
				incr=-1
				incr,retroVERT=noBUCAvert(griglia_corrente,y,x,vy,incr)
				return(0,incr)
			elif vy<0 and flag==1:
				incr=+1
				incr,retroVERT=noBUCAvert(griglia_corrente,y,x,vy,incr)
				return(0,incr)
			elif flag==1:
				if nDX>=nSX:
					flag=2
				else:
					flag=0
			elif (nDX>sommatoria(vx)+vx+1) and flag==2:
				incr=+1
				incr,retroVERT=noBUCAoriz(griglia_corrente,y,x,vx,incr)
				return(incr,0)
			elif vx>0 and flag==2:
				incr=-1
				incr,retroVERT=noBUCAoriz(griglia_corrente,y,x,vx,incr)
				return(incr,0)
			elif flag==2:
				if nDOWN>=nUP:
					flag=3
				else:
					flag=1
			elif (nDOWN>sommatoria(vy)+vy+1) and flag==3:
				incr=+1
				incr,retroVERT=noBUCAvert(griglia_corrente,y,x,vy,incr)
				return(0,incr)
			elif vy>0 and flag==3:
				incr=-1
				incr,retroVERT=noBUCAvert(griglia_corrente,y,x,vy,incr)
				return(0,incr)
			elif flag==3:
				if nSX>=nDX:
					flag=0
				else:
					flag=2
		return(0,0)
		
def noBUCAoriz(g,y,x,vx,inc):
	retro=False
	incr=deepcopy(inc)
	if g[y][x+vx+inc]=='O':
		incr=0
		if g[y][x+vx+incr]=='O':
			incr=opp(inc)
	if incr==0 and g[y][x+vx-1]=='O' and g[y][x+vx-2]=='O':
		retro=True
		incr=+1
	return incr,retro
	
def noBUCAvert(g,y,x,vy,inc):
	retro=False
	incr=deepcopy(inc)
	if g[y+vy+inc][x]=='O':
		incr=0
		if g[y+vy+incr][x]=='O':
			incr=opp(inc)
	if incr==0 and g[y+vy-1][x]=='O' and g[y+vy-2][x]=='O':
		retro=True
		incr=+1
	return incr,retro
		
def sommatoria(x):
	x=math.fabs(x)
	som=0
	cont=0
	while x!=0:
		if cont==0:
			som=x
			cont+=1
		else:
			som=som+x
		x=x-1
	return som

def opp(x):
	return (x*-1)
		