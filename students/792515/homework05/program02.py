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

def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty,laps):
    '''inserite qui il vostro codice'''
    F1=percorso(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty,laps)
    F1.trova_riferimenti(griglia_corrente, griglia_precedente)
    F1.attenzione_macchine()
    #print(F1.lsattenzione_macchine)
    F1.acquisici_dzpunti(x,y,griglia_corrente)
    return F1.chi_va_piano(x,y,vx,vy,laps)

class percorso:
    def __init__(self, griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty,laps):
        self.griglia_x=len(griglia_corrente[0])
        self.griglia_y=len(griglia_corrente)
        self.pista=' '
        self.buca='O'
        self.traguardo='|'
        self.io=car
        self.lsmacchine=['A','B','C','D','E','X']
        self.lsaltre_macchine=list(set(self.lsmacchine)-set([car]))
        self.lsattenzione_macchine=[]
        self.dz_altre_macchine={}
        self.lstraguardo=[]
        self.lsstep_intorno=[(0,-1),(0,1),(-1,-1),(-1,1),(-1,0),(1,-1),(1,1),(1,0)]
        self.lsstep_traguardo=[(0,-1),(0,1),(-verso,-1),(-verso,1),(-verso,0)]
        #self.lsstep_percorso=[(1,0),(-1,0),(0,1),(0,-1)]#step dritti
        #self.lsstep_cambio_dir=[(1,1),(1,-1),(-1,1),(-1,-1)]#step cambio_dir
        self.lsacc=[0,-1, 1]
        self.dzpunti={}
        
    def in_pista(self,i,j):
        return 0<= i <self.griglia_x and 0<= j <self.griglia_y

#1
    def trova_riferimenti(self,griglia_corrente,griglia_precedente):
        #self.dzpunti[0]=[]
        ls=[]
        for j in range(self.griglia_y):
            for m in self.lsaltre_macchine: #trovo le altre macchine
                if m in griglia_corrente[j]:
                    i=griglia_corrente[j].index(m)
                    self.dz_altre_macchine[m]=[(),()]
                    self.dz_altre_macchine[m][0]=(i,j)
                    ls.append(m)
            for m in ls:
                if m in griglia_precedente[j]: #trovo le altre macchine
                    i=griglia_precedente[j].index(m)
                    self.dz_altre_macchine[m][1]=(i,j)
            if self.traguardo in griglia_corrente[j]: # trovo il traguardo
                i=griglia_corrente[j].index(self.traguardo)
                #self.lspunti.append((i,j))
                self.dzpunti[(i,j)]=(0,True)
        return
#2    
    def attenzione_macchine(self):
        ls_x=[]
        ls_y=[]
        for d in self.dz_altre_macchine.keys():
            p0=self.dz_altre_macchine[d][0]
            p1=self.dz_altre_macchine[d][1]
            i0,j0=p0
            i1,j1=p1
            vx_m=i0-i1
            vy_m=j0-j1
            for l in self.lsacc:
                ls_x.append(vx_m+l)
                ls_y.append(vy_m+l)
            for lx in ls_x:
                for ly in ls_y:
                    self.lsattenzione_macchine.append((lx+i0,ly+j0))
        return

#3
    def acquisici_dzpunti(self,x,y,griglia_corrente):
        ls=self.acquisici_intorno_traguardo(griglia_corrente)
        while not (x,y) in self.dzpunti.keys():
            i,j=ls[0]
            ls.pop(0)
            for s in self.lsstep_intorno:
                sx,sy=s
                #print((i+sx,j+sy))
                if self.in_pista(i+sx,j+sy) and \
                (griglia_corrente[j+sy][i+sx]==self.pista or griglia_corrente[j+sy][i+sx]==self.buca or griglia_corrente[j+sy][i+sx]==self.io) and \
                not ((i+sx,j+sy) in self.dzpunti.keys()):
                    ls.append((i+sx,j+sy))
                    p=self.dzpunti[(i,j)][0]
                    if griglia_corrente[j+sy][i+sx]==self.pista or griglia_corrente[j+sy][i+sx]==self.io:
                        self.dzpunti[(i+sx,j+sy)]=(p+1,True)
                    else:
                        self.dzpunti[(i+sx,j+sy)]=(p+1,False)
        return
    
    def acquisici_intorno_traguardo(self,griglia_corrente):
        ls=[i for i in self.dzpunti.keys()]
        lsnew=[]
        while len(ls)>0:
            i,j=ls[0]
            ls.pop(0)
            for s in self.lsstep_traguardo:
                sx,sy=s
                if self.in_pista(i+sx,j+sy) and \
                (griglia_corrente[j+sy][i+sx]==self.pista or griglia_corrente[j+sy][i+sx]==self.buca or griglia_corrente[j+sy][i+sx]==self.io) and \
                not ((i+sx,j+sy) in self.dzpunti.keys()):
                    lsnew.append((i+sx,j+sy))
                    if griglia_corrente[j+sy][i+sx]==self.pista:
                        self.dzpunti[(i+sx,j+sy)]=(1,True)
                    else:
                        self.dzpunti[(i+sx,j+sy)]=(1,False)
        return lsnew
                
    def cambia_direzione(self,x,y,vx,vy):
        lsx=[]
        lsy=[]
        for s in self.lsacc:
            if abs(vx+s)<=1:
                lsx.append(vx+s)
        for s in self.lsacc:
            if abs(vy+s)<=1:
                lsy.append(vy+s)
        for i in range(len(lsx)):
            for j in range(len(lsy)):
                newvx=lsx[i]
                newvy=lsy[j]
                if self.posso_muovere(x+newvx,y+newvy,x,y):
                    return (newvx-vx,newvy-vy)
        return (self.frena(vx),self.frena(vy))
        
    def dove_sono(self,x,y):
        return self.dzpunti[(x,y)][0]
    
    def mi_avvicino(self,i,j,x,y):
        return (i,j) in self.dzpunti.keys() and self.dzpunti[(i,j)][0]<self.dove_sono(x,y) and self.dzpunti[(i,j)][1]==True and not (i,j) in self.lsattenzione_macchine

    def posso_muovere(self,i,j,x,y):
        return (i,j) in self.dzpunti.keys() and self.dzpunti[(i,j)][0]-self.dove_sono(x,y)==-1 and self.dzpunti[(i,j)][1]==True and not (i,j) in self.lsattenzione_macchine
                      
    def chi_va_piano(self,x,y,vx,vy, laps):
        if laps>0:
            return (self.rallenta(vx),self.rallenta(vy))
        if self.posso_muovere(x+vx,y,x,y):
            return (0,self.frena(vy))
        elif self.posso_muovere(x,y+vy,x,y):
            return (self.frena(vx),0)
        elif self.posso_muovere(x+vx,y+vy,x,y):
            return (0,0)
        else:
            return self.cambia_direzione(x,y,vx,vy)                
    
    def rallenta(self,v):
        vf=0
        if v>=1:
            vf-=1
        elif v<=-1:
            vf+=1
        return vf
        
    def frena(self,v):
        return -v