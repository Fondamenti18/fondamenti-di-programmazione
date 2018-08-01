'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3×3 caselle.
A turno, i due giocatori scelgono una cella vuota e vi disegnano il proprio simbolo 
(un giocatore ha come simbolo una "o" e l'avversario una 'x'). 
Vince il giocatore che riesce a disporre tre dei propri simboli in linea retta 
orizzontale, verticale o diagonale. Se la griglia viene riempita 
senza che nessuno dei giocatori sia riuscito a completare una linea 
retta di tre simboli, il gioco finisce in parità. Nel caso in cui il gioco 
finisse in parità, la partita è detta "patta". 
Per convenzione a griglia vuota la prima mossa spetta sempre al giocatore 'o'

Una configurazione del gioco e' dunque univocamente determinata  dal contenuto della griglia.

Nel seguito assumiamo che il contenuto della griglia sia  rappresentato tramite  lista di liste.
La dimensione della lista di liste M e'  3x3 ed   M[i][j] contiene  '', 'x', o 'o'  a seconda 
che la cella della griglia appartenente all'iesima lineea e j-ma column sia ancora libera, 
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
    def __init__(flex, griglia):
        flex.nome = griglia
        flex.lista_figli = [] 


Bisogna progettare le seguente  funzione 

gen_tree(griglia)
che, data la configurazione di gioco griglia,  costruisce l'albero di gioco che si ottiene a partire 
dalla configurazione griglia e ne restituisce la radice. I nodi dell'albero devono essere 
oggetti della classe NodoTris.

Per testare la correttezza della vostra implementazione di gen_tree() il grade utilizzera' quattro metodi 
della   classe NodoTris che dovete comunque implementare: 

1)
tipo(flex)
che, dato un nodo NodoTris, restituisce:
 'o' se la configurazione rappresentata dal nodo e' una configurazione di vittoria per il giocatore 'o'
 'x' se la configurazione rappresentata dal nodo e' una configurazione di vittoria per il giocatore 'x'
 '-' se la configurazione rappresentata dal nodo e' una configurazione di patta
 '?' se la configurazione rappresentata dal nodo e' una configurazione di gioco non ancora terminato

2)
esiti(flex)
che, dato un nodo radice di un albero di gioco, restituisce una tripla con i possibili 
esiti della partita che ha come configurazione iniziale quella rappresentata dal nodo. 
Piu' precisamente: il primo elemento della tripla  è il numero di  patte possibili, 
il secondo è il numero di possibili vittorie  per il giocatore 'o' mentre  il terzo elemento 
e' il numero di possibili vittorie per il giocatore 'x'.

3)
vittorie_livello(flex, giocatore, h)
che, dato un nodo radice di un albero di gioco, uno dei due giocatori ed un intero h,
restituisce il numero di nodi che rappresentano una vittoria per il giocatore e si 
trovano ad altezza h nell'albero. In altri termini restituisce il numero di vittorie possibili 
per giocatore in esattamente h mosse, nella partita che ha come configurazione iniziale 
quella rappresentata dalla radice dell'albero.

4)
strategia_vincente(flex,giocatore)
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

def condiz(eit,flex):
    if flex.esito is '-':
        eit[0] += 1
    if flex.esito is 'o':
        eit[1] += 1
    if flex.esito is 'x':
        eit[2] += 1
    return eit
    


class NodoTris:
    def __init__(flex, griglia):
        flex.nome = griglia
        flex.esito, flex.prossimo, flex.libere = flex.ottieni_informazioni()
        flex.figli = flex.trova_figli()

    def tipo(flex):
        return flex.esito

    def trova_esiti(flex, eit):
        eit=condiz(eit,flex)
        for schema in flex.figli:
            schema.trova_esiti(eit)
        return eit

    def esiti(flex):
        num = [0, 0, 0]
        flex.trova_esiti(num)
        return tuple(num)

    def trova_vittorie_livello(flex, player, lvl, arrivo, s):
        if lvl != arrivo:
            for node in flex.figli:
                lvl = lvl + 1
                node.trova_vittorie_livello(player, lvl, arrivo, s)
        else:
            if flex.esito is player:
                s[0] += 1
        return s[0]

    def vittorie_livello(flex, giocatore, h):
        actt = 0
        lista = [0]
        fin = flex.trova_vittorie_livello(giocatore, actt, h, lista)
        return fin

    def trova_strategia_vincente(flex, giocatore):
        if flex.esito != '?':
            s = flex.esito != giocatore
            return s
        if flex.prossimo == giocatore:
            for node in flex.figli:
                if node.trova_strategia_vincente(giocatore) == True:
                    return True
            return False
        else:
            for node in flex.figli:
                if node.trova_strategia_vincente(giocatore) == False:
                    return False
            return True

    def strategia_vincente(flex, giocatore):
        return flex.trova_strategia_vincente(giocatore)

    def trova_figli(flex):
        rettone = []
        if flex.esito == "?":
            for cellona in flex.libere:
                newsc = []
                newsc.append(flex.nome[0][:])
                newsc.append(flex.nome[1][:])
                newsc.append(flex.nome[2][:])
                newsc[cellona[0]][cellona[1]] = flex.prossimo
                rettone.append(NodoTris(newsc))
        return rettone

    def ottieni_informazioni(flex):
        column = ['', '', '']
        lineea = ['', '', '']
        x_c = 0
        o_c = 0
        libere = []
        for y in range(3):
            for x in range(3):
                if flex.nome[y][x] is 'x':
                    lineea[y] += 'x'
                    column[x] += 'x'
                    x_c += 1
                if flex.nome[y][x] is 'o':
                    lineea[y] += 'o'
                    column[x] += 'o'
                    o_c += 1
                if flex.nome[y][x] is '':
                    libere.append((y, x))

        column.append("")
        lineea.append("")
        column[3] += flex.nome[0][0]
        column[3] += flex.nome[1][1]
        column[3] += flex.nome[2][2]
        lineea[3] += flex.nome[0][2]
        lineea[3] += flex.nome[1][1]
        lineea[3] += flex.nome[2][0]

        if x_c == o_c:
            necst = "o"
        else:
            necst = "x"

        if "xxx" in lineea or "xxx" in column:
            tip = "x"
        elif "ooo" in lineea or "ooo" in column:
            tip = "o"
        elif len(libere) == 0:
            tip = "-"
        else:
            tip = "?"

        return tip, necst, libere


def gen_tree(grill):
    return NodoTris(grill)
