'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3Ã—3 caselle.
A turno, i due giocatori scelgono una cella vuota e vi disegnano il proprio simbolo 
(un giocatore ha come simbolo una "o" e l'avversario una 'x'). 
Vince il giocatore che riesce a disporre tre dei propri simboli in linea retta 
orizzontale, verticale o diagonale. Se la griglia viene riempita 
senza che nessuno dei giocatori sia riuscito a completare una linea 
retta di tre simboli, il gioco finisce in paritÃ . Nel caso in cui il gioco 
finisse in paritÃ , la partita Ã¨ detta "patta". 
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
Piu' precisamente: il primo elemento della tripla  Ã¨ il numero di  patte possibili, 
il secondo Ã¨ il numero di possibili vittorie  per il giocatore 'o' mentre  il terzo elemento 
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

import copy

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
    
    def __str__(self):
        return str(self.nome)
       
    def check_caselle_piene(self):
        cas_piene = 0
        for i in range(3):
            for x in range(3):
                if self.nome[i][x] == 'x' or self.nome[i][x] == 'o':
                    cas_piene += 1
        return cas_piene
                        
    def check_vitt_diag_sxtodx(self):
        x1 = self.nome[0][0]
        x2 = self.nome[1][1]
        x3 = self.nome[2][2]
        vincitore = ''
        if x1 == x2 and x2 == x3:
            if x1 != '':
                vincitore = x1
                return x1
        return vincitore
    
    def check_vitt_diag_dxtosx(self):
        x1 = self.nome[0][2]
        x2 = self.nome[1][1]
        x3 = self.nome[2][0]
        vincitore = ''
        if x1 == x2 and x2 == x3:
            if x1 != '':
                vincitore = x1
                return x1
        return vincitore
    
    def check_vittoria_orizz(self):
        vincitore = ''
        for riga in range(3):
            x1 = self.nome[riga][0]
            x2 = self.nome[riga][1]
            x3 = self.nome[riga][2]
            if x1 == x2 and x2 == x3:
                if x1 != '':
                    return x1
        return vincitore
    
    def check_vittoria_vert(self,colonna):
        vincitore = ''
        for colonna in range(3):
            x1 = self.nome[0][colonna]
            x2 = self.nome[1][colonna]
            x3 = self.nome[2][colonna]
            if x1 == x2 and x2 == x3:
                if x1 != '':
                    return x1
        return vincitore
            
    def part_in_corso(self):
        config = '-'
        for riga in range(3):
            for cas in range(3):
                if self.nome[riga][cas] == '':
                    config = '?'
                    return config
        return config
    
    def tipo(self):
        vincitore = self.check_vitt_diag_dxtosx()
        if vincitore != '':
            return vincitore
        vincitore = self.check_vitt_diag_sxtodx()
        if vincitore != '':
            return vincitore
        vincitore = self.check_vittoria_orizz()
        if vincitore != '':
            return vincitore
        vincitore = self.check_vittoria_vert(0)
        if vincitore != '':
            return vincitore
        if vincitore == '':
            return self.part_in_corso()
                
    def esiti(self):
        patta = 0
        o = 0
        x = 0
        esito = self.tipo()
        if esito == 'x':
                x +=1
        if esito == 'o':
                o +=1
        if esito == '-':
                patta +=1
        if len(self.lista_figli) != 0:
            for child in self.lista_figli:
                esito_figlio = child.tipo()
                if esito_figlio == '?':
                    ris = child.esiti()
                    patta += ris[0]
                    o += ris[1]
                    x += ris[2]
                else:
                    if esito_figlio == 'x':
                        x += 1
                    if esito_figlio == 'o':
                        o += 1
                    if esito_figlio == '-':
                        patta += 1
        return (patta,o,x)                       
    
    def trova_livello(self,livello,giocatore,h):
        esito = self.tipo()
        livellofiglio = []
        if esito == giocatore and livello == h:
            return [livello]
        if livello < h:
            if esito != '-':
                for child in self.lista_figli:
                    livellofiglio += child.trova_livello(livello+1,giocatore,h)
        return livellofiglio
            
    
    def vittorie_livello(self, giocatore, h):
        livello = self.trova_livello(0,giocatore,h)
        return len(livello)
    
    def doppio_gioco(self,giocatore,strategia):
        terminata = self.stato_partita(self.lista_figli)
        if terminata == False :
            n = 0
            i = len(self.lista_figli)
            n += self.vittorie_livello(giocatore,2)
            if i == n:
                strategia = True
            else:
                for child in self.lista_figli:
                    strategia = child.doppio_gioco(giocatore,strategia)
                    if strategia == True:
                        break
        return strategia
    
    def stato_partita(self,figli):
        for x in figli:
            if x.tipo() == '?':
                terminata = False
            else:
                terminata = True
                break
        return terminata
        
          
    def strategia_vincente(self,giocatore):
        strategia = False
        n = self.vittorie_livello(giocatore,1)
        if n == 1:
            strategia = True
        else:
            strategia = self.doppio_gioco(giocatore,strategia)
        return strategia
                    
def gen_tree(griglia, pross_giocatore = '?'):
    g = NodoTris(griglia)
    mosse = g.check_caselle_piene()
    if pross_giocatore == '?':
        if mosse % 2 == 0:
            pross_giocatore = 'o'
        else:
            pross_giocatore = 'x'
    elif pross_giocatore != '?':
        if pross_giocatore == 'x':
            pross_giocatore = 'o'
        else:
            pross_giocatore = 'x'
    if mosse > 4:
        if g.tipo() == '?':
            for x in range(3):
                for y in range(3):
                    if griglia[x][y] == '':
                        figlio = griglia_figlio(griglia,x,y,pross_giocatore)
                        g.lista_figli.append(gen_tree(figlio,pross_giocatore))
    else:
        for x in range(3):
            for y in range(3):
                if griglia[x][y] == '':
                    figlio = griglia_figlio(griglia,x,y,pross_giocatore)
                    g.lista_figli.append(gen_tree(figlio,pross_giocatore))
    return g


def print_tree(nodo,livello):
    print(' '*livello + str(nodo.nome) + nodo.tipo())
    for child in nodo.lista_figli:
        print_tree(child,livello+1)

def griglia_figlio(griglia,posx,posy,giocatore):
    figlio = []
    for x in range(3):
        figlio.append(griglia[x][:])
    figlio[posx][posy] = giocatore
    return figlio

# =============================================================================
# g0=[['', '', ''], ['', '', ''], ['', '', '']]
# g = gen_tree(g0)
# =============================================================================

