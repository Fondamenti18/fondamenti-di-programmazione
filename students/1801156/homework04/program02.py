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
Piu' precisamente: il primo elemento della tripla  è il numero di  patte possibili, 
il secondo è il numero di possibili vittorie  per il giocatore 'o' mentre  il terzo elemento 
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
    
    def tipo(self):
        '''inserire qui il vostro codice'''
        for y in range(0, 3):
            if self.nome[y][0] == self.nome[y][1] == self.nome[y][2] and self.nome[y][0] != '':
                return self.nome[y][0]
            if self.nome[0][y] == self.nome[1][y] == self.nome[2][y] and self.nome[0][y] != '':
                return self.nome[0][y]
        if self.nome[0][0] == self.nome[1][1] == self.nome[2][2] and self.nome[0][0] != '':
            return self.nome[0][0]
        if self.nome[0][2] == self.nome[1][1] == self.nome[2][0] and self.nome[2][0] != '':
            return self.nome[0][2]
        
        for y in range(0, 3):
            for x in range(0, 3):
                if self.nome[y][x] == '':
                    return '?'
        return '-'
    
    def esiti(self):
        '''inserire qui il vostro codice'''
        lista = find_result(self.nome)
#        print(lista)
#        i = 0
#        j = 0
#        while i < len(lista):
#            while j < len(lista):
#                if lista[i] == lista[j] and i != j:
#                    del lista[j]
#                    j -= 1
#                j += 1
#            i += 1
        
        diz = {
                '-' : 0,
                'o' : 0,
                'x' : 0,
               }
        check_result = False
        for w in range(0, len(lista)):
            for h in range(0, 3):
                if lista[w][h][0] == lista[w][h][1] == lista[w][h][2] and lista[w][h][0] != '':
                    diz[lista[w][h][0]] += 1
                    check_result = True
                if lista[w][0][h] == lista[w][1][h] == lista[w][2][h] and lista[w][0][h] != '':
                    diz[lista[w][0][h]] += 1
                    check_result = True
            if lista[w][0][0] == lista[w][1][1] == lista[w][2][2] and lista[w][0][0] != '':
                diz[lista[w][0][0]] += 1
                check_result = True
            if lista[w][0][2] == lista[w][1][1] == lista[w][2][0] and lista[w][0][2] != '':
                diz[lista[w][0][2]] += 1
                check_result = True
        
            if check_result == False:
                cont_segni = 0
                for y in range(0, 3):
                    for x in range(0, 3):
                        if lista[w][y][x] != '':
                            cont_segni += 1
                if cont_segni == 9:
                    diz['-'] += 1
        
        lista_result = []
        for key in diz:
            lista_result.append(diz[key])
        return tuple(lista_result)
    
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
        lista = calcolo_livello(self.nome, giocatore, h)
        #print(lista)
        i = 0
        while i < len(lista):
            if lista[i][1] != h:
                del lista[i]
                i -= 1
            i += 1
        #print(lista)
        
        esito = 0
        for x in range(0, len(lista)):
            for y in range(0, 3):
                if lista[x][0][y][0] == lista[x][0][y][1] == lista[x][0][y][2] and lista[x][0][y][0] == giocatore:
                    esito += 1
                if lista[x][0][0][y] == lista[x][0][1][y] == lista[x][0][2][y] and lista[x][0][0][y] == giocatore:
                    esito += 1
            if lista[x][0][0][0] == lista[x][0][1][1] == lista[x][0][2][2] and lista[x][0][0][0] == giocatore:
                esito += 1
            if lista[x][0][0][2] == lista[x][0][1][1] == lista[x][0][2][0] and lista[x][0][0][2] == giocatore:
                esito += 1
        
        return esito
    '''
    4)
    strategia_vincente(self,giocatore)
    che, dato un nodo radice di un albero di gioco ed uno dei due giocatori, restituisce True o False. 
    Restituisce True  se  giocatore ha una strategia vincente  nella partita 
    che ha come configurazione iniziale quella rappresentata dal nodo radice, False altrimenti.
    
    Nota che un giocatore ha una strategia vincente rispetto ad una certa configurazione se, 
    qualunque siano le mosse dell'avversario ha sempre la possibilita' di rispondere in modo 
    che la partita termini con la sua vittoria.
    '''
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        lista_nodi = strategia(self.nome)
#        for x in lista_nodi:
#            print(x)
#        print()
        check_nodo(self.nome, giocatore, lista_nodi)
#        print(lista_nodi)
        if len(lista_nodi):
            return True
        return False
        #print(lista_nodi)
        #print(lista)
        
def strategia(grig, lista = [], liv = 1, call = False):
    from copy import deepcopy
    
    cont_spazi = False
    for h in range(0, 3):
        for w in range(0, 3):
            if grig[h][w] == 'o' or grig[h][w] == 'x':
                cont_spazi = True
    if cont_spazi == False:
        return 0
    
    if liv == 1:
        cont_x = 0
        cont_o = 0
        for h in range(0, 3):
            for w in range(0, 3):
                if grig[h][w] == 'o':
                    cont_o += 1
                elif grig[h][w] == 'x':
                    cont_x += 1
        if cont_x < cont_o and cont_o != 5:
            liv -= 1
    
    for y in range(0, 3):
        for x in range(0, 3):
            if grig[y][x] == '':
                check_result = False
                griglia_ap = deepcopy(grig)
                for h in range(0, 3):
                    if griglia_ap[h][0] == griglia_ap[h][1] == griglia_ap[h][2] and griglia_ap[h][0] != '':
                        check_result = True
                    if griglia_ap[0][h] == griglia_ap[1][h] == griglia_ap[2][h] and griglia_ap[0][h] != '':
                        check_result = True
                if griglia_ap[0][0] == griglia_ap[1][1] == griglia_ap[2][2] and griglia_ap[0][0] != '':
                    check_result = True
                if griglia_ap[0][2] == griglia_ap[1][1] == griglia_ap[2][0] and griglia_ap[0][2] != '':
                    check_result = True
                
                if check_result == False:
                    if liv % 2 == 1:
                        griglia_ap[y][x] = 'o'
                    else:
                        griglia_ap[y][x] = 'x'
                    lista += [[griglia_ap, liv]]
                    strategia(griglia_ap, lista, liv + 1)
    return lista



def check_nodo(griglia, giocatore, lista_nodi, liv = 1):
    from copy import deepcopy
    for y in range(0, 3):
        for x in range(0, 3):
            if griglia[y][x] == '':
                grig_ap = deepcopy(griglia)
                if liv % 2 == 1:
                    grig_ap[y][x] = 'o'
                else:
                    grig_ap[y][x] = 'x'
                check_result = False
                for h in range(0, 3):
                    if grig_ap[h][0] == grig_ap[h][1] == grig_ap[h][2] and grig_ap[h][0] != '':
                        if grig_ap[h][0] != giocatore:
                            check_result = True
                        else:
                            return lista_nodi
                    if grig_ap[0][h] == grig_ap[1][h] == grig_ap[2][h] and grig_ap[0][h] != '':
                        if grig_ap[0][h] != giocatore:
                            check_result = True
                        else:
                            return lista_nodi
                if grig_ap[0][0] == grig_ap[1][1] == grig_ap[2][2] and grig_ap[0][0] != '':
                    if grig_ap[0][0] != giocatore:
                        check_result = True
                    else:
                        return lista_nodi
                if grig_ap[0][2] == grig_ap[1][1] == grig_ap[2][0] and grig_ap[0][2] != '':
                    if grig_ap[0][2] != giocatore:
                        check_result = True
                    else:
                        return lista_nodi
                
                if check_result == False:
                    cont_segni = 0
                    for h in range(0, 3):
                        for w in range(0, 3):
                            if grig_ap[h][w] != '':
                                cont_segni += 1
                    if cont_segni == 9:
                        check_result = True
                if check_result == False:
                    check_nodo(grig_ap, giocatore, lista_nodi, liv + 1)
                else:
                    i = 0
                    while i < len(lista_nodi):
                        if grig_ap == lista_nodi[i][0]:
                            j = i + 1
                            k = i - 1
                            if j < len(lista_nodi) and k >= 0:
                                while lista_nodi[j][1] != 1:
                                    j += 1
                                while lista_nodi[k][1] != 1:
                                    k -= 1
                            v = k
                            while v < j:
                                del lista_nodi[k]
                                v += 1    
                        i += 1
                    #print(lista_nodi)
                    #print("1:", grig_ap)
                    #print("2:", griglia)
    
#nodo = NodoTris([['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']])
#nodo.strategia_vincente('x')



#lista = [[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', '', '']],
#         [['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', '']],
#         [['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', '']],
#         [['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', '']],
#         [['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'o']],
#         [['x', 'o', 'o'], ['x', 'x', 'o'], ['o', '', 'x']],
#         [['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', 'o']]]
#
#i = 0
#for x in lista:
#    print(x)
#print()
#while i < len(lista):
#    if [['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'x']] not in lista:
#        print("ok")
##    if lista[i] == [['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'o']]:
##        del lista[i]
##        i -= 1
#    i += 1
#for x in lista:
#    print(x)
#print()
#lista.remove([['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', '']])
#for x in lista:
#    print(x)


def calcolo_livello(grig, giocatore, h, liv = 1, lista = [], call = False):
    if call == False:
        lista.clear()
    from copy import deepcopy
    grig_ap = deepcopy(grig)
    
    cont_spazi = False
    for h in range(0, 3):
        for w in range(0, 3):
            if grig[h][w] == 'o' or grig[h][w] == 'x':
                cont_spazi = True
    if cont_spazi == False:
        return 0
    
    if liv == 1:
        cont_x = 0
        cont_o = 0
        for h in range(0, 3):
            for w in range(0, 3):
                if grig[h][w] == 'o':
                    cont_o += 1
                elif grig[h][w] == 'x':
                    cont_x += 1
        if cont_x < cont_o and cont_o != 5:
            liv -= 1
    
    cont = 0
    for el in grig_ap:
        if '' not in el:
            cont += 1
    if cont == 3:
        return [grig_ap]
    
    for y in range(0, 3):
        for x in range(0, 3):
            if grig[y][x] == '':
                grig_ap = deepcopy(grig)
                if liv % 2 == 1:
                    grig_ap[y][x] = 'o'
                else:
                    grig_ap[y][x] = 'x'
                check_result = False
                for h in range(0, 3):
                    if grig_ap[h][0] == grig_ap[h][1] == grig_ap[h][2] and grig_ap[h][0] != '':
                        check_result = True
                    if grig_ap[0][h] == grig_ap[1][h] == grig_ap[2][h] and grig_ap[0][h] != '':
                        check_result = True
                if grig_ap[0][0] == grig_ap[1][1] == grig_ap[2][2] and grig_ap[0][0] != '':
                    check_result = True
                if grig_ap[0][2] == grig_ap[1][1] == grig_ap[2][0] and grig_ap[0][2] != '':
                    check_result = True
                
                if check_result == False:
                    cont_segni = 0
                    for h in range(0, 3):
                        for w in range(0, 3):
                            if grig_ap[h][w] != '':
                                cont_segni += 1
                    if cont_segni == 9:
                        check_result = True
                if check_result == False:
                    calcolo_livello(grig_ap, giocatore, h, liv + 1, lista, True)
                lista += [[grig_ap, liv]]
                    #print(lista)
                #print(grig_ap, liv) #grig_ap va messo in una lista per controllare gli esiti
                    #print(liv)
    return lista
def gen_tree(griglia, liv = 1):
    from copy import deepcopy
    nodo = NodoTris(griglia)
    for y in range(0, 3):
        for x in range(0, 3):
            if griglia[y][x] == '':
                check_result = False
                griglia_ap = deepcopy(griglia)
                for h in range(0, 3):
                    if griglia_ap[h][0] == griglia_ap[h][1] == griglia_ap[h][2] and griglia_ap[h][0] != '':
                        check_result = True
                    if griglia_ap[0][h] == griglia_ap[1][h] == griglia_ap[2][h] and griglia_ap[0][h] != '':
                        check_result = True
                if griglia_ap[0][0] == griglia_ap[1][1] == griglia_ap[2][2] and griglia_ap[0][0] != '':
                    check_result = True
                if griglia_ap[0][2] == griglia_ap[1][1] == griglia_ap[2][0] and griglia_ap[0][2] != '':
                    check_result = True
                
                if check_result == False:
                    if liv % 2 == 1:
                        griglia_ap[y][x] = 'o'
                    else:
                        griglia_ap[y][x] = 'x'
                    nodo.lista_figli += [gen_tree(griglia_ap, liv + 1)]
                #print(griglia_ap, liv) #va messo in una lista per controllare gli esiti
                #print(liv)
    return nodo
def find_result(grig, liv = 1, lista = [], call = False):
    if call == False:
        lista.clear()
    
    cont_spazi = False
    for h in range(0, 3):
        for w in range(0, 3):
            if grig[h][w] == 'o' or grig[h][w] == 'x':
                cont_spazi = True
    if cont_spazi == False:
        return 0
    
    if liv == 1:
        cont_x = 0
        cont_o = 0
        for h in range(0, 3):
            for w in range(0, 3):
                if grig[h][w] == 'o':
                    cont_o += 1
                elif grig[h][w] == 'x':
                    cont_x += 1
        if cont_x < cont_o and cont_o != 5:
            liv -= 1
    
    from copy import deepcopy
    grig_ap = deepcopy(grig)
    
    cont = 0
    for el in grig_ap:
        if '' not in el:
            cont += 1
    if cont == 3:
        return [grig_ap]
    
    for y in range(0, 3):
        for x in range(0, 3):
            if grig[y][x] == '':
                grig_ap = deepcopy(grig)
                if liv % 2 == 1:
                    grig_ap[y][x] = 'o'
                else:
                    grig_ap[y][x] = 'x'
                check_result = False
                for h in range(0, 3):
                    if grig_ap[h][0] == grig_ap[h][1] == grig_ap[h][2] and grig_ap[h][0] != '':
                        check_result = True
                    if grig_ap[0][h] == grig_ap[1][h] == grig_ap[2][h] and grig_ap[0][h] != '':
                        check_result = True
                if grig_ap[0][0] == grig_ap[1][1] == grig_ap[2][2] and grig_ap[0][0] != '':
                    check_result = True
                if grig_ap[0][2] == grig_ap[1][1] == grig_ap[2][0] and grig_ap[0][2] != '':
                    check_result = True
                
                if check_result == False:
                    cont_segni = 0
                    for h in range(0, 3):
                        for w in range(0, 3):
                            if grig_ap[h][w] != '':
                                cont_segni += 1
                    if cont_segni == 9:
                        check_result = True
                if check_result == False:
                    find_result(grig_ap, liv + 1, lista, True)
                else:
                    lista += [grig_ap]
                    #print(lista)
                    #print(grig_ap) #grig_ap va messo in una lista per controllare gli esiti
                    #print(liv)
    return lista