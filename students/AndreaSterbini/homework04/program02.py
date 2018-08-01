'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3×3 caselle.
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

#esiti = {}

class NodoTris:
    def __init__(self, griglia):
        self.griglia = griglia
        self.figli   = [] #lista dei nodi figli
    
    def tipo(self):
        '''Tornare:
            'o' se vinta da 'o'
            'x' se vinta da 'x'
            '?' se partita in corso
            '-' se patta
        '''
        foundmo = True
        foundMo = True
        foundmx = True
        foundMx = True
        count   = 0
        g = self.griglia
        for c in ['o', 'x']:
            for i in range(3):
                # orizzontale
                if g[i][0] == g[i][1] == g[i][2] == c: return c
                # verticale
                if g[0][i] == g[1][i] == g[2][i] == c: return c
            # diagonale
            if g[0][0] == g[1][1] == g[2][2] == c: return c
            if g[0][2] == g[1][1] == g[2][0] == c: return c

        #print(count, self.griglia)
        count = 0
        for i in range(3):
            count += self.griglia[i].count('')
        if count:
            return '?'
        else:
            return '-'
        
    def esiti(self):
        '''inserire qui il vostro codice'''
        #tup = str(self.griglia)
        #if tup in esiti: return esiti[tup]
        pos = { 'o' : 1, '-': 0, 'x': 2 }
        esito = [0, 0, 0]
        if not self.figli:
            t = self.tipo()
            #print(t, self.griglia)
            esito[pos[t]] += 1
        for f in self.figli:
            for i, v in enumerate(f.esiti()):
                esito[i] += v
        res = tuple(esito)
        #esiti[tup] = res
        return res
    
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
        if h==0:
            return 1 if self.tipo() == giocatore else 0
        else:
            tot = 0
            for f in self.figli:
                tot += f.vittorie_livello(giocatore, h-1)
            return tot
    
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        t = self.tipo()
        if t == giocatore:
            return True
        if t == '-':
            return False
        if t != '?':
            return False
        if self.mossa() != giocatore:
            ok = True
            for f in self.figli:
                ok = ok and f.strategia_vincente(giocatore)
            return ok
        else:
            ok = False
            for f in self.figli:
                ok = ok or f.strategia_vincente(giocatore)
            return ok



    def mossa(self):
        count = 0
        for i in range(3):
            count += self.griglia[i].count('')
        return 'o' if count % 2 else 'x'

    def __str__(self, livello=0):
        s = ''
        s += '|  '*livello + str(self.griglia) + '\t' + self.tipo()
        for f in self.figli:
            s += '\n'+ f.__str__(livello+1)
        return s
        
def gen_tree(griglia):
    '''inserire qui il vostro codice'''
    root = NodoTris(griglia)
    if root.tipo() in ['o','x','-']:
        return root
    tocca = root.mossa()
    for x in range(3):
        for y in range(3):
            if griglia[x][y] == '':
                [[a,b,c],[d,e,f],[g,h,i]] = griglia
                griglia1 = [[a,b,c],[d,e,f],[g,h,i]]
                griglia1[x][y] = tocca
                root.figli.append(gen_tree(griglia1))
    return root


if __name__ == '__main__':
    griglia = [['x','o','o'],['x','x','o'],['','','']]
    griglia = [['x','o','o'],['x','x','o'],['','','o']]
    print(gen_tree(griglia))

