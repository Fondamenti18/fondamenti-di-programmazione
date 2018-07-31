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
controllo=[0]
def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty, laps):
    global controllo
    ax=0
    ay=0
    print(startx,starty,x,y,verso,vx,vy,y-1,x-1,y+1,x+1)
    if verso==-1:#si parte verso sx
        if laps==1:
            ax,ay=rallenta(ax,ay,vx,vy)
        elif y>= len(griglia_corrente)//2 and x<=(len(griglia_corrente[y]))//2: #basso-sx
            ax,ay=basso_sx_sx(ax,ay,vx,vy,x,y,car,griglia_corrente)
        elif y<= len(griglia_corrente)//2 and x<=len(griglia_corrente[y])//2:#alto-sx
            ax,ay=alto_sx_sx(ax,ay,vx,vy,x,y,car,griglia_corrente)
        elif y< (len(griglia_corrente)//2)-2 and x>=len(griglia_corrente[y])//2:#alto-dx
            ax,ay=alto_dx_sx(ax,ay,vx,vy,x,y,car,griglia_corrente)
        elif y>=(len(griglia_corrente)//2)-2 and x>=(len(griglia_corrente[y]))//2:#basso-dx
            ax,ay=basso_dx_sx(ax,ay,vx,vy,x,y,car,griglia_corrente)
            
    
    elif verso==+1 :#si parte verso dx
        if laps==1:
            ax,ay=rallenta(ax,ay,vx,vy)
        elif y>=(len(griglia_corrente)//2)-2 and x>=(len(griglia_corrente[y]))//2:#basso-dx
            ax,ay=basso_dx_dx(ax,ay,vx,vy,x,y,car,griglia_corrente)
        elif y< (len(griglia_corrente)//2)-2 and x>=len(griglia_corrente[y])//2:#alto-dx
            ax,ay=alto_dx_dx(ax,ay,vx,vy,x,y,car,griglia_corrente)
        elif y<= len(griglia_corrente)//2 and x<=len(griglia_corrente[y])//2:#alto-sx
            ax,ay=alto_sx_dx(ax,ay,vx,vy,x,y,car,griglia_corrente)
        elif y>= len(griglia_corrente)//2 and x<=(len(griglia_corrente[y]))//2: #basso-sx
            ax,ay=basso_sx_dx(ax,ay,vx,vy,x,y,car,griglia_corrente)
             
    return(ax,ay)

def basso_sx_sx(ax,ay,vx,vy,x,y,car,griglia_corrente):
    if (x-vx)>=0 and  griglia_corrente[y][x-vx-1]==' ' and -1<vx<1 and controllo[-1]!=2:
        ax,ay=sinistra(ax,ay,vy)
    elif y-vy>=0 and (griglia_corrente[y-vy-1][x-vx]==' '  or griglia_corrente[y-vy-1][x-vx]=='|' ) and -1<vx<1 and controllo[-1]!=3:
        ay=alto(ay,vy)
    elif x+vx<len(griglia_corrente[y]) and  griglia_corrente[y][x+vx+1]==' ' and -1<vx<1 and controllo[-1]!=0:
        ax,ay=destra(ax,ay,vy)
    elif y+vy<len(griglia_corrente) and griglia_corrente[y+vy+1][x-vx]==' '  and -1<vx<1 and controllo[-1]!=1:
        ay=basso(ay,vy)
    else:
        ax,ay=rallenta(ax,ay,vx,vy)
    return ax,ay
def alto_sx_sx(ax,ay,vx,vy,x,y,car,griglia_corrente):
    if x+vx<len(griglia_corrente[y]) and  griglia_corrente[y][x+vx+1]==' ' and -1<vx<1 and controllo[-1]!=0:
        ax,ay=destra(ax,ay,vy)
    elif y-vy>=0 and (griglia_corrente[y-vy-1][x-vx]==' '  or griglia_corrente[y-vy-1][x-vx]==car ) and -1<vx<1 and controllo[-1]!=3:
        ay=alto(ay,vy)
    elif y+vy<len(griglia_corrente) and (griglia_corrente[y+vy+1][x-vx]==' ')  and -1<vx<1 and controllo[-1]!=1:
        ay=basso(ay,vy)
    elif (x-vx)>=0 and  griglia_corrente[y][x-vx-1]==' ' and -1<vx<1 and controllo[-1]!=2:
        ax,ay=sinistra(ax,ay,vy)
    else:
        ax,ay=rallenta(ax,ay,vx,vy)
    return ax,ay
def alto_dx_sx(ax,ay,vx,vy,x,y,car,griglia_corrente):
    if x+vx<len(griglia_corrente[y]) and  griglia_corrente[y][x+vx+1]==' ' and -1<vx<1 and controllo[-1]!=0:
        ax,ay=destra(ax,ay,vy)
    elif y-vy>=0 and griglia_corrente[y-vy-1][x-vx]==' ' and -1<vx<1 and controllo[-1]!=3:
        ay=alto(ay,vy)
    elif y+vy<len(griglia_corrente) and griglia_corrente[y+vy+1][x-vx]==' '  and -1<vx<1 and controllo[-1]!=1:
        ay=basso(ay,vy)
    elif (x-vx)>=0 and  griglia_corrente[y][x-vx-1]==' ' and -1<vx<1 and controllo[-1]!=2:
        ax,ay=sinistra(ax,ay,vy)
    else:
        ax,ay=rallenta(ax,ay,vx,vy)
    return ax,ay
def basso_dx_sx(ax,ay,vx,vy,x,y,car,griglia_corrente):
    if y+vy+1<len(griglia_corrente) and griglia_corrente[y+vy+1][x-vx]==' ' and -1<vx<1:#basso
        ay=basso(ay,vy)
    elif x-vx-1>=0 and (griglia_corrente[y+vy][x-vx-1]==' ' or griglia_corrente[y+vy][x-vx-1]=='|') and -1<vx<1:
        ax,ay=sinistra(ax,ay,vy)
    elif x+vx+1<len(griglia_corrente[y]) and griglia_corrente[y+vy][x+vx+1]==' ' and -1<vx<1:
        ax,ay=destra(ax,ay,vy)
    elif y-vy-1>=0 and griglia_corrente[y-vy-1][x-vx]==' ' and -1<vx<1:
        ay=alto(ay,vy)
    else:
        ax,ay=rallenta(ax,ay,vx,vy)
    return ax,ay
def basso_dx_dx(ax,ay,vx,vy,x,y,car,griglia_corrente):
    if x+vx+1<len(griglia_corrente[y]) and (griglia_corrente[y+vy][x+vx+1]==' ' or griglia_corrente[y+vy][x+vx+1]=='|') and -1<vx<1:
        ax,ay=destra(ax,ay,vy)
    elif y-vy-1>=0 and griglia_corrente[y-vy-1][x-vx]==' ' and -1<vx<1:
        ay=alto(ay,vy)
    elif y+vy+1<len(griglia_corrente) and griglia_corrente[y+vy+1][x-vx]==' ' and -1<vx<1:
        ay=basso(ay,vy)
    elif x-vx-1>=0 and (griglia_corrente[y+vy][x-vx-1]==' ' or griglia_corrente[y+vy][x-vx-1]=='|') and -1<vx<1:
        ax,ay=sinistra(ax,ay,vy)
    else:
        ax,ay=rallenta(ax,ay,vx,vy)
    return ax,ay
def alto_dx_dx(ax,ay,vx,vy,x,y,car,griglia_corrente):
    if y-vy>=0 and griglia_corrente[y-vy-1][x-vx]==' '  and -1<vx<1 and controllo[-1]!=3:
        ay=alto(ay,vy)
    elif (x-vx)>=0 and  griglia_corrente[y][x-vx-1]==' ' and -1<vx<1 and controllo[-1]!=2:
        ax,ay=sinistra(ax,ay,vy)
    elif y+vy<len(griglia_corrente) and griglia_corrente[y+vy+1][x-vx]==' ' and -1<vx<1 and controllo[-1]!=1:
        ay=basso(ay,vy)
    elif x+vx<len(griglia_corrente[y]) and griglia_corrente[y][x+vx+1]==' ' and -1<vx<1 and controllo[-1]!=0:
        ax,ay=destra(ax,ay,vy)
    else:
        ax,ay=rallenta(ax,ay,vx,vy)
    return ax,ay
def alto_sx_dx(ax,ay,vx,vy,x,y,car,griglia_corrente):
    if (x-vx)>=0 and  griglia_corrente[y][x-vx-1]==' ' and -1<vx<1 and controllo[-1]!=2:
        ax,ay=sinistra(ax,ay,vy)
    elif y+vy<len(griglia_corrente) and griglia_corrente[y+vy+1][x-vx]==' ' and -1<vx<1 and controllo[-1]!=1:
        ay=basso(ay,vy)
    elif x+vx<len(griglia_corrente[y]) and griglia_corrente[y][x+vx+1]==' ' and -1<vx<1 and controllo[-1]!=0:
        ax,ay=destra(ax,ay,vy)
    elif y-vy>=0 and griglia_corrente[y-vy-1][x-vx]==' ' and -1<vx<1 and controllo[-1]!=3:
        ay=alto(ay,vy)
    else:
        ax,ay=rallenta(ax,ay,vx,vy)
    return ax,ay
def basso_sx_dx(ax,ay,vx,vy,x,y,car,griglia_corrente):
    if x+vx<len(griglia_corrente[y]) and  (griglia_corrente[y][x+vx+1]==' ' or griglia_corrente[y][x+vx+1]=='|') and -1<vx<1 and controllo[-1]!=0:
        ax,ay=destra(ax,ay,vy)
    elif y+vy+1<len(griglia_corrente) and griglia_corrente[y+vy+1][x-vx]==' '  and -1<vx<1 and controllo[-1]!=1:
        ay=basso(ay,vy)
    elif y-vy>=0 and griglia_corrente[y-vy-1][x-vx]==' ' and -1<vx<1 and controllo[-1]!=3:
        ay=alto(ay,vy)
    elif (x-vx)>=0 and  griglia_corrente[y][x-vx-1]==' ' and -1<vx<1 and controllo[-1]!=2:
        ax,ay=sinistra(ax,ay,vy)
    else:
        ax,ay=rallenta(ax,ay,vx,vy)
    return ax,ay
               
def rallenta(ax,ay,vx,vy):
    if vx<=-1:
        ax+=1
    elif vx>=1:
        ax-=1
    if vy==-1:
        ay+=1
    elif vy==1:
        ay-=1
    return ax,ay
def alto(ay,vy):
    if vy<=-1:
        ay+=1
    else:
        ay-=1
    controllo.append(1)
    return ay
def basso(ay,vy):
    if vy<=-1:
        ay+=1
    elif vy>=1:
        ay-=1
    else:
        ay+=1
    #print(controllo)
    controllo.append(3)
    return ay
def sinistra(ax,ay,vy):
    if vy<=-1:
        ay+=1
    elif vy>=1:
        ay-=1
    else:
        ax-=1
    controllo.append(0)
    return ax,ay
def destra(ax,ay,vy):
    if vy<=-1:
        ay+=1
    elif vy>=1:
        ay-=1
    else:
        ax+=1
    controllo.append(2)
    return ax,ay