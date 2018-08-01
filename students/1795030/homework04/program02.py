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

CHECK = False

def Controllo_O(griglia):
    s = ''
    for i in range(3):
        if  griglia[i][0] == griglia[i][1] == griglia[i][2] == 'o' or griglia[i][0] == griglia[i][1] == griglia[i][2] == 'x':
            s = 'o' if griglia[i][0] == 'o' else 'x'
            CHECK = True
            break
        else:
            CHECK = False
    return s, CHECK

def Controllo_V(griglia):
    s = ''
    for i in range(3):
        if griglia[0][i] == griglia[1][i] == griglia[2][i] == 'o' or griglia[0][i] == griglia[1][i] == griglia[2][i] == 'x' :
            s = 'o' if griglia[0][i] == 'o' else 'x'
            CHECK  = True
            break
        else:
            CHECK = False
    return s, CHECK

def Controllo_Obl_Sx_Dx(griglia):
    s = ''
    if griglia[0][0] == griglia[1][1] == griglia[2][2] == 'o' or griglia[0][0] == griglia[1][1] == griglia[2][2] == 'x':
        s = 'o' if griglia[0][0] == 'o' else 'x'
        CHECK = True
    else:
        CHECK = False
    return s, CHECK

def Controllo_Obl_Dx_Sx(griglia):
    s = ''
    if griglia[0][2] == griglia[1][1] == griglia[2][0] == 'o' or griglia[0][2] == griglia[1][1] == griglia[2][0] == 'x':
        s = 'o' if griglia[0][2] == 'o' else 'x'
        CHECK = True
    else:
        CHECK = False
    return s, CHECK

def Controllo_Patta(griglia):
    i = 0
    s, CHECK = Controllo_O(griglia)
    s1, CHECK1 = Controllo_V(griglia)
    s2, CHECK2 = Controllo_Obl_Sx_Dx(griglia)
    s3, CHECK3 = Controllo_Obl_Dx_Sx(griglia)
    if not CHECK and not CHECK1 and not CHECK2 and not CHECK3:
        for y in griglia:
            if not '' in y:
                i += 1
            else:
                i = 0
    if i == 0:
        return False
    else:
        return True

def Tipo(griglia):
    if type(griglia) == str:
        griglia = ReconvertToList(griglia)
    s, CHECK = Controllo_O(griglia)
    s1, CHECK1 = Controllo_V(griglia)
    s2, CHECK2 = Controllo_Obl_Sx_Dx(griglia)
    s3, CHECK3 = Controllo_Obl_Dx_Sx(griglia)
    if CHECK:
        return s
    elif CHECK1:
        return s1
    elif CHECK2:
        return s2
    elif CHECK3:
        return s3
    elif Controllo_Patta(griglia):
        return '-'
    else:
        return '?'
        
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli

    def tipo(self):
        griglia = self.nome
        s, CHECK = Controllo_O(griglia)
        s1, CHECK1 = Controllo_V(griglia)
        s2, CHECK2 = Controllo_Obl_Sx_Dx(griglia)
        s3, CHECK3 = Controllo_Obl_Dx_Sx(griglia)
        if CHECK:
            return s
        elif CHECK1:
            return s1
        elif CHECK2:
            return s2
        elif CHECK3:
            return s3
        elif Controllo_Patta(griglia):
            return '-'
        else:
            return '?'
        
        
    def esiti(self):
        griglia = self.nome
        dizionario_albero = gen_tree2(griglia)
        patta = 0
        vittoria_o = 0
        vittoria_x = 0
        if type(dizionario_albero) == list:
            s = Tipo(dizionario_albero)
            if s == 'o':
                vittoria_o += 1
            elif s == 'x':
                vittoria_x += 1
            elif s == '-':
                patta += 1
            return (patta, vittoria_o, vittoria_x)
        elif type(dizionario_albero) == dict:
            for key in dizionario_albero:
                value = dizionario_albero[key]
                if len(value) != 0:
                    for x in value:
                        s = Tipo(x)
                        if s == 'o':
                            vittoria_o += 1
                        elif s == 'x':
                            vittoria_x += 1
                        elif s == '-':
                            patta += 1
            return (patta, vittoria_o, vittoria_x)
            
    
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
    
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''

MOSSA_O = False
MOSSA_X = False

def gen_tree(griglia):
    albero_nodo0 = []
    dizionario_albero = {}
    lista_stringhe = []
    for liste in griglia: CHECK = True if not '' in liste else False
    lista_stringhe = Lista_S_Lista(griglia, lista_stringhe)
    if CHECK:
        albero_nodo0 += griglia
        return NodoTris(albero_nodo0)
    else:
        dizionario_albero = Ricorsione_GA(lista_stringhe, dizionario_albero)
        return NodoTris(griglia)

def gen_tree2(griglia):
    albero_nodo0 = []
    dizionario_albero = {}
    lista_stringhe = []
    for liste in griglia: CHECK = True if not '' in liste else False
    lista_stringhe = Lista_S_Lista(griglia, lista_stringhe)
    if CHECK:
        albero_nodo0 += griglia
        return albero_nodo0
    else:
        s = Tipo(griglia)
        if s == 'o' or s == 'x':
            return griglia
        else:
            dizionario_albero = Ricorsione_GA(lista_stringhe, dizionario_albero)
        return dizionario_albero
    
def Ricorsione_GA(lista_stringhe, dizionario_albero):
    MOSSA_O = True
    i = 0
    for element in lista_stringhe:
        if not ' ' in element:
            i += 1
    if i == len(lista_stringhe)*9:
        return dizionario_albero
    else:
        if MOSSA_O:
            lista2 = []
            for stringhe in lista_stringhe:
                lista = []
                indice = 0
                lista_stringhe, lista2 = Mossa_O(lista, lista2, indice, stringhe)
                for element in lista_stringhe:
                    s = Tipo(element)
                    if not s == 'o' or not s == 'x':        #inizio cambio della funzione
                        dizionario_albero[element] = []
                        lista_stringhe.remove(element)      #Fine cambio della funzione    
                dizionario_albero[stringhe] = lista_stringhe
            MOSSA_O = False
            MOSSA_X = True
        if MOSSA_X:
            lista3 = []
            for stringhe in lista2:
                lista = []
                indice = 0
                lista_stringhe, lista3 = Mossa_X(lista, lista3, indice, stringhe)
                for element in lista_stringhe:
                    s = Tipo(element)
                    if not s == 'o' or not s == 'x':        #Inizio cambio della funzione
                        dizionario_albero[element] = []
                        lista_stringhe.remove(element)      #Fine Cambio della funzione
                dizionario_albero[stringhe] = lista_stringhe
            MOSSA_X = False
            dizionario_albero = Ricorsione_GA(lista3, dizionario_albero)
        return dizionario_albero
        

def Mossa_O(lista, lista2, indice, s):
    lista1= []
    s1 = ''
    if indice == len(s): return lista, lista2
    if not s[indice] == ' ':
        indice += 1
        return Mossa_O(lista, lista2, indice, s)
    else:
        for x in s: lista1.append(x)
        lista1[indice] = 'o'
        for x in lista1: s1+=x
        lista.append(s1); lista2.append(s1); indice += 1
        return Mossa_O(lista, lista2, indice, s)

def Mossa_X(lista, lista2, indice, s):
    lista1 = []
    s1 = ''
    if indice == len(s): return lista, lista2
    if not s[indice] == ' ':
        indice += 1
        return Mossa_X(lista, lista2, indice, s)
    else:
        for x in s: lista1.append(x)
        lista1[indice] = 'x'
        for x in lista1: s1+=x
        lista.append(s1); lista2.append(s1); indice+= 1
        return Mossa_X(lista, lista2, indice, s)

def Lista_S_Lista(griglia, lista):
    stringa = ''
    for y in griglia:
        for x in y: stringa += ' ' if x == '' else x
    lista.append(stringa)
    return lista

def ReconvertToList(stringa):
    matrice_risultato = [['' for x in range(3)] for y in range(3)]
    i_y = 0
    i_x = 0
    for lettera in stringa:
        if i_x == 3:
            i_x = 0
            i_y += 1
        matrice_risultato[i_y][i_x] = lettera
        i_x += 1
    return matrice_risultato


if __name__ == '__main__':
    g0=[['', '', ''], ['', '', ''], ['', '', '']]
    g1=[['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
    g2=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'o']]
    g3=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', '', 'x']]
    g4=[['o', 'x', 'x'], ['x', 'o', 'o'], ['o', 'o', 'x']]
    g5=[['', 'x', ''], ['', 'o', ''], ['', '', '']]
    g6=[['', 'o', ''], ['', 'x', ''], ['', '', '']]
    g7=[['', 'x', 'o'], ['', '', ''], ['', '', '']]
    g8=[['', 'o', 'x'], ['', '', ''], ['', '', '']]
    #listac = [NodoTris(g1), NodoTris(g2), NodoTris(g3), NodoTris(g4)]
    listaa = [g1, g2, g3, g4]
    #print(gen_tree(g1))
    #listac = [gen_tree(x) for x in listaa]
    #lista = [y.tipo() for y in listac]
    #print(lista)
    #lista2 = [y.esiti() for y in listac]
    #print(lista2)
    print(gen_tree2(g1))
    #print(Ricorsione_GA(['xxoxoox  '], {}))
    #print(Tipo([['x', 'o', 'o'], ['x', 'x', 'o'], [' ', 'o', ' ']]))
    #print(Tipo(g4))
