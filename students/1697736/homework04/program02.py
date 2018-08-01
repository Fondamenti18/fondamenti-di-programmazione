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

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        cross = 0
        circ = 0
        muoveCr = False
            
        if self.tipo()=="?":
            for righe in griglia:
                for casella in righe:
                    if casella == "o":
                        circ += 1
                    if casella == "x":
                        cross += 1
            if cross < circ:
                muoveCr = True
            for j,riga in enumerate(griglia):
                for i,_ in enumerate(riga):
                    if griglia[j][i] == "":
                        g2=self.duplica(griglia)
                        if muoveCr == True:
                            g2[j][i] = "x"
                        else:
                            g2[j][i] = "o"
                        self.lista_figli.append(gen_tree(g2))
    
    def duplica(self,griglia):
        ret=[]
        for j,colonna in enumerate(griglia):
            ret.append([])
            for i,riga in enumerate(colonna):
                ret[j].append(griglia[j][i])
        return ret
    
    
    def tipo(self):
        '''inserire qui il vostro codice'''
        
        for i in range(3):
            #righe
            if "x" in self.nome[i][0]and "x" in self.nome[i][1]and "x" in self.nome[i][2]:
                return "x"
            if "o" in self.nome[i][0]and "o" in self.nome[i][1]and "o" in self.nome[i][2]:
                return "o"  
            #colonne
            if "x" in self.nome[0][i]and "x" in self.nome[1][i]and "x" in self.nome[2][i]:
                return "x"
            if "o" in self.nome[0][i]and "o" in self.nome[1][i]and "o" in self.nome[2][i]:
                return "o"  
            
        if self.nome[0][0] == "x" and self.nome[1][1] == "x" and self.nome[2][2] == "x":
                return "x"
        if self.nome[0][0] == "o" and self.nome[1][1] == "o" and self.nome[2][2] == "o":
                return "o"
        
        if self.nome[0][2] == "x" and self.nome[1][1] == "x" and self.nome[2][0] == "x":
            return "x"
        if self.nome[0][2] == "o" and self.nome[1][1] == "o" and self.nome[2][0] == "o":
            return "o"
        
        for j in self.nome:
            if '' in j:
                return "?"
            
        return "-"
    
    def vincite(self,array):
        for n in self.lista_figli:
            ti=n.tipo()
            if ti == "-":
                array[0] += 1
            if ti == "o":
                array[1] += 1
            if ti == "x":
                array[2] += 1
            if ti == "?":
                n.vincite(array)
        
            
        
    def esiti(self):
        '''inserire qui il vostro codice'''
        arr = [0,0,0]
        
        ti=self.tipo()
        if ti == "-":
            arr[0] += 1
        if ti == "o":
            arr[1] += 1
        if ti == "x":
            arr[2] += 1
            
        self.vincite(arr)
        
        return (arr[0],arr[1],arr[2])
    
    def livello(self,h, hnow, player):
        
        win=0
        for el in self.lista_figli:
            if hnow == h and el.tipo() == player:
                win+=1
            if hnow < h and el.tipo() == "?":
                win+=el.livello(h,hnow+1,player)
        return win
            
    
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
        win = 0
        hnow = 1
        if h==0 and self.tipo()==giocatore:
            win+=1
        win+=self.livello(h,hnow,giocatore)
        
        return win
    '''   
    def vincenti(self,player):
        
        indet=True
        vittoria=True
        if self.tipo()=="?":
            for figlio in self.lista_figli:
                if figlio.tipo() != "?":
                    indet=False
                    break
            if indet:
                for figlio in self.lista_figli:
                    for figlio2 in figlio.lista_figli:
                        if figlio2.tipo()!=player:
                            vittoria=False
                            break
                    if not vittoria:
                        break
                if not vittoria:
                    for figlio in self.lista_figli:
                        ret = figlio.vincenti(player)
                        if ret == True:
                            return True
                    return False
            else:
                return False
        else:
            return False
            
                            
                
        '''
    def vincenti(self,h, hnow,vittorie):
        
        for el in self.lista_figli:
            if hnow == h:
                vittorie.append(el.tipo())
            if hnow < h and el.tipo() == "?":
                el.vincenti(h,hnow+1,vittorie)
        
    
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        vittorie=[]
        prossimo=True
        if self.tipo()=='?':
            #controllo se tutte le mosse successive sono indeterminate
           for figli in self.lista_figli:
                if figli.tipo() != '?':
                    prossimo=False
                    break
           if prossimo == True:
                for figli in self.lista_figli:
                    vittorie=[]
                    vittoria=True
                    figli.vincenti(1,1,vittorie)
                    #controllo le vittorie dei miei nipoti
                    for vi in vittorie:
                        if vi != giocatore:
                            vittoria=False
                            break
                    if vittoria == True:
                        return True
                ## i nipoti non sono vittorie sicure
                for figli in self.lista_figli:
                    rit = figli.strategia_vincente(giocatore)
                    if rit == True:
                        return True
            ##else return false
                    
        return False
     
        
        
        
        
def gen_tree(griglia):
    '''inserire qui il vostro codice'''
    triss = NodoTris(griglia)
    return triss
                        


if __name__ == '__main__':
    
    g0 = g1 = g2 = g3 = g4 = g5 = g6 = g7 = g8 = listaa = listab = listac = rad = None

    #def setup():
    #    global g0, g1, g2, g3, g4, g5, g6, g7, g8, listaa, listab, listac, rad
    g0=[['', '', ''], ['', '', ''], ['', '', '']]
    g1=[['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
    g2=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'o']]
    g3=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', '', 'x']]
    g4=[['o', 'x', 'x'], ['x', 'o', 'o'], ['o', 'o', 'x']]
    
    g5=[['', 'x', ''], ['', 'o', ''], ['', '', '']]
    g6=[['', 'o', ''], ['', 'x', ''], ['', '', '']]
    g7=[['', 'x', 'o'], ['', '', ''], ['', '', '']]
    g8=[['', 'o', 'x'], ['', '', ''], ['', '', '']]
    
    listaa=[g1, g2, g3, g4]
    listab=[g5, g6, g7, g8]
    lista1= [gen_tree(x) for x in listab]
    listac=[gen_tree(x) for x in listaa]
    
    g=gen_tree(g8)
    print(g.strategia_vincente('o'))
    #expected    = [0, 1, 0, 1]

