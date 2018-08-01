'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 33 caselle.
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
che la cella della griglia appartenente all'i-esima riga e alla j-esima colonna sia ancora libera, 
contenga il simbolo 'x' o contenga il simbolo 'o'. 

Data una configurazione C del gioco, l'albero di gioco per C e' l'albero che 
si ottiene ricorsivamente partendo dalla configurazione C e assegnando come figli le configurazioni 
che e' possibile ottenere da C con una mossa ulteriore del gioco. Ovviamente  risulteranno 
foglie dell'albero i possibili esiti della partita, vale a dire le diverse configurazioni a cui e' 
possibile arrivare partendo da C e che rappresentano patte, vittorie per 'o' o vittorie per 'x'.
Si veda ad esempio l'immagine albero_di_gioco.png che mostra l' albero di gioco che si ottiene a partire 
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

class NodoTris:
    
    numero_patte = 0
    numero_Vitt_x = 0
    numero_Vitt_o = 0
    livello_ricorsione = 0
    combinazioni_vincenti = [False, False, False, False, False, False, False, False]
    
    def __init__(self, griglia):
        self.nome = griglia
        self.nome1 = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.numero_patte = 0
        self.numero_Vitt_x = 0
        self.numero_Vitt_o = 0
        self.livello_ricorsione = 0
        self.combinazioni_vincenti = [False, False, False, False, False, False, False, False]

        
    def checkCasella(self, x, y, s):
        if self.nome[x][y] == s:
            return 1
        return 0
    
    def contaSimbolo(self, s):
        c = 0
        for i in range(len(self.nome)):
            for j in range(len(self.nome[0])):
                if self.nome[i][j] == s:
                    c += 1
        return c

    
    def checkVittoria(self, s): #prima x, poi y
        if self.checkCasella(0, 0, s) + self.checkCasella( 1, 0, s) + self.checkCasella( 2, 0, s) == 3:
            return 0
        if self.checkCasella( 0, 1, s) + self.checkCasella( 1, 1, s) + self.checkCasella( 2, 1, s) == 3:
            return 1
        if self.checkCasella( 0, 2, s) + self.checkCasella( 1, 2, s) + self.checkCasella( 2, 2, s) == 3:
            return 2
        if self.checkCasella( 0, 0, s) + self.checkCasella( 0, 1, s) + self.checkCasella( 0, 2, s) == 3:
            return 3
        if self.checkCasella( 1, 0, s) + self.checkCasella( 1, 1, s) + self.checkCasella( 1, 2, s) == 3:
            return 4
        if self.checkCasella( 2, 0, s) + self.checkCasella( 2, 1, s) + self.checkCasella( 2, 2, s) == 3:
            return 5
        if self.checkCasella( 0, 0, s) + self.checkCasella( 1, 1, s) + self.checkCasella( 2, 2, s) == 3:
            return 6
        if self.checkCasella( 2, 0, s) + self.checkCasella( 1, 1, s) + self.checkCasella( 0, 2, s) == 3:
            return 7
        return -1
    
    
    def tipo(self):
        comb_vinc_x = self.checkVittoria('x')
        comb_vinc_o = self.checkVittoria('o')
        if comb_vinc_x >= 0 and self.combinazioni_vincenti[comb_vinc_x] == False:
            self.combinazioni_vincenti[comb_vinc_x] == True
            return 'x'
        elif self.checkVittoria('o') >= 0 and self.combinazioni_vincenti[comb_vinc_o] == False:
            self.combinazioni_vincenti[comb_vinc_o] == True
            return 'o'
        else:
            numero_o = self.contaSimbolo('o')
            numero_x = self.contaSimbolo('x')
            caselle_vuote = 9 - (numero_o + numero_x)
            if caselle_vuote == 0:
                return '-'
            else:
                return '?'
            
    # tripla con numero_patte, numero_vitt_o, numero_vitt_x
    def esiti(self):
        #print('inizio esiti')
        esito_incompleto = self.tipo()
        if esito_incompleto == 'x':
            
            self.numero_Vitt_x += 1
         #   print('incremento vittoira x', self.numero_Vitt_x  )
        elif esito_incompleto == 'o':
            self.numero_Vitt_o +=1
          #  print('incremento vittoira o', self.numero_Vitt_o  )
        elif esito_incompleto == '-':
            self.numero_patte +=1
        else:
            numero_o = self.contaSimbolo('o')
            numero_x = self.contaSimbolo('x')
            if numero_o > numero_x:
                simbolo = 'x'
            else: simbolo = 'o'
            for i in range(3):
                for j in range(3):
                    if self.nome[i][j] == '':
                        self.nome[i][j] = simbolo
                        #print('aggiunta simbolo in', i, j, simbolo)
                        #self.livello_ricorsione += 1
                        self.esiti()
                        #self.livello_ricorsione -= 1
                        #print('rimozione simbolo da', i, j, self.nome[i][j])
                        self.nome[i][j] = ''
                    
                        #print('casella occupata', i, j, self.nome[i][j])
        #print('return esiti')
                        

        #if self.livello_ricorsione == 0:
        return (self.numero_patte, self.numero_Vitt_o, self.numero_Vitt_x)
    
    
    
    
    def vittorie_livello1(self, giocatore, h):
        #print('livello ricorsione: ', self.livello_ricorsione)
        esito_incompleto = self.tipo()
        #print('esito_tipo', esito_incompleto)
        if esito_incompleto == 'x':
            if giocatore == 'x':
                if self.livello_ricorsione != h: return 0
                elif self.livello_ricorsione == h:
                    self.numero_Vitt_x += 1
                    #print('incremento vittorie di', giocatore, 'livello', h, 'vittorie x', self.numero_Vitt_x, '-', self.nome[2][0], '-', self.nome[2][1], '-', self.nome[2][2])
            else:
                return 0
        elif esito_incompleto == 'o': 
            if giocatore == 'o':
                if self.livello_ricorsione != h: return 0
                elif self.livello_ricorsione == h:
                    self.numero_Vitt_o +=1
                    #print('incremento vittorie di', giocatore, 'livello', h, 'vittoire o', self.numero_Vitt_o, '-', self.nome[2][0], '-', self.nome[2][1], '-', self.nome[2][2] )
            else:
                return 0
        elif esito_incompleto == '-':
            self.numero_patte +=1
        else:
            numero_o = self.contaSimbolo('o')
            numero_x = self.contaSimbolo('x')
            if numero_o > numero_x:
                simbolo = 'x'
            else: 
                simbolo = 'o'
            for i in range(3):
                for j in range(3):
                    if self.nome[i][j] == '':
                        
                        #print('aggiunto', simbolo, 'in', i, j)
                        self.nome[i][j] = simbolo
                        self.livello_ricorsione += 1
                        self.vittorie_livello1(giocatore, h)
                        self.livello_ricorsione -= 1
                        #print('tolto', simbolo, 'da', i, j, 'livello ricorsione', self.livello_ricorsione)
                        self.nome[i][j] = ''
                    
        #if self.livello_ricorsione == 0:
        if giocatore == 'x': return self.numero_Vitt_x
        return self.numero_Vitt_o
        
    def vittorie_livello(self, giocatore, h):
        self.numero_patte = 0
        self.numero_Vitt_x = 0
        self.numero_Vitt_o = 0
        self.livello_ricorsione = 0
        self.combinazioni_vincenti = [False, False, False, False, False, False, False, False]
        #print('parametri', 'giocatore', giocatore, 'livello', h, 'vittorie x', self.numero_Vitt_x, 'vittorie o', self.numero_Vitt_o)
        return self.vittorie_livello1(giocatore, h)    
    
    def checkVuota(self):
        for i in range(3):
            for j in range(3):
                if self.nome[i][j] != '':
                    return False
        return True
   
    
def gen_tree(griglia):
    nt = NodoTris(griglia)
    #nt.fill_figli(nt)
    return nt


            
            
            
            
    
    

    
    
    
    
    
    
    
    