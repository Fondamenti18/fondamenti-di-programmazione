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
'''

from random     import randint


""" 1  2  3
     \ | /
   0 -[x]- 4
     / | \
    7  6  5 """

bloccato=False
motivo=""
def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty, laps):
    global bloccato,motivo
    if laps==1:
        return -(vx),-(vy)
    ax=0
    ay=0
    pixel_0=griglia_corrente[y][x-1]
    pixel_1=griglia_corrente[y-1][x-1]
    pixel_2=griglia_corrente[y-1][x]
    pixel_3=griglia_corrente[y-1][x+1]
    pixel_4=griglia_corrente[y][x+1]
    pixel_5=griglia_corrente[y+1][x+1]
    pixel_6=griglia_corrente[y+1][x]
    pixel_7=griglia_corrente[y+1][x-1]
    if bloccato==True:
        if motivo in ["alto-sinistra","alto-destra"]:
            bloccato=False
            return 0,1
        elif motivo in ["basso-sinistra","basso-destra"]:
            bloccato=False
            return 0,-1
    if vx==0 and vy==0 and laps==0 and bloccato==False:
        return verso,0
    if vx==-1 and vy==0:#sinistra
        if pixel_0==" " or pixel_0=="|":
            return 0,0
        elif pixel_1==" ":
            return 0,-1
        elif pixel_7==" ":
            return 0,1
        elif pixel_2==" ":
            return 1,-1
        elif pixel_6==" ":
            return 1,1
    elif vx==-1 and vy==-1:#alto-sinistra
        if pixel_1==" ":
            return 0,0
        elif pixel_2==" ":
            return 1,0
        elif pixel_0==" ":
            return 0,1
        else:
            bloccato=True
            motivo="alto-sinistra"
            return -(vx),-(vy)
    elif vx==0 and vy==-1:#alto
        if pixel_2==" ":
            return 0,0
        elif pixel_3==" ":
            return 1,0
        elif pixel_1==" ":
            return -1,0
        elif pixel_4==" ":
            return 1,1
        elif pixel_0==" ":
            return -1,1
    elif vx==1 and vy==-1:#alto-destra
        if pixel_3==" ":
            return 0,0
        elif pixel_2==" ":
            return -1,0
        elif pixel_4==" ":
            return 0,1
        else:
            bloccato=True
            motivo="alto-destra"
            return -(vx),-(vy)
    elif vx==1 and vy==0:#destra
        if pixel_4==" " or pixel_4=="|":
            return 0,0
        if pixel_3==" ":
            return 0,-1
        if pixel_5==" ":
            return 0,+1
        if pixel_2==" ":
            return -1,-1
        if pixel_6==" ":
            return -1,1
    elif vx==1 and vy==1:#basso a destra
        if pixel_5==" ":
            return 0,0
        if pixel_4==" ":
            return 0,-1
        if pixel_6==" ":
            return -1,0
        else:
            bloccato=True
            motivo="basso-destra"
            return -(vx),-(vy)
    elif vx==0 and vy==1:#basso
        if pixel_6==" ":
            return 0,0
        elif pixel_5==" ":
            return 1,0
        elif pixel_7==" ":
            return -1,0
        elif pixel_4==" ":
            return 1,-1
        elif pixel_0:
            return -1,-1
    elif vx==-1 and vy==1:#basso a sinistra
        if pixel_7==" ":
            return 0,0
        if pixel_0==" ":
            return 0,-1
        if pixel_6==" ":
            return 1,0
        else:
            bloccato=True
            motivo="basso-sinistra"
            return -(vx),-(vy)
    
        
        
            
            
        
    
