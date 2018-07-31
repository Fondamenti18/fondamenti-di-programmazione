'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3Ã—3 caselle.
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
from copy import deepcopy
from copy import copy
import timeit
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
    
    def tipo(self):
        '''inserire qui il vostro codice'''
        griglia=self.nome
        #print(griglia)
        
        for x in range(0,3):
            if griglia[x][0] == 'o' or griglia[x][0]=='x':
                if griglia[x][0] == griglia[x][1] and griglia[x][0] == griglia[x][2]:
                    #print('ciao')
                    return griglia[x][0]
            if griglia[0][x] == 'o' or griglia[0][x]=='x':
                if griglia[0][x] == griglia[1][x] and griglia[0][x] == griglia[2][x]:
                    return griglia[0][x]
        #for y,val in enumerate(griglia):
            
        if griglia[0][0] == 'o' or griglia[0][0] =='x':
            if griglia[0][0] == griglia[1][1] and griglia[0][0] == griglia[2][2]:
                return griglia[0][0]
        if griglia[0][2] == 'o' or griglia[0][2] =='x':
            if griglia[0][2] == griglia[1][1] and griglia[0][2] == griglia[2][0]:
                return griglia[0][2]
            
        for x in griglia:
            for y in x:
                if y == '':
                    return '?'
        
        return '-'

        
    def esiti(self):
        '''inserire qui il vostro codice'''
        p=0
        o=0
        x=0
        #griglia=self.nome
        ls=[]
        #radice=gen_tree(griglia)
        f=(foglia(self,ls))
        o=(f.count('o'))
        p=(f.count('-'))
        x=(f.count('x'))
        return (p,o,x)
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
        griglia=self.nome
        #print(griglia)
        #print('\n')
        lv=0
        vit=[]
        
        caca=lvl(self,lv,h,giocatore,vit)
        #print(caca.count(1))
        return caca.count(1)
        #for x in radice.lista_figli:
            #print(x.nome)
            #print('lv 1')
            #for y in x.lista_figli:
                #print(y.nome)
                #print('lv 2')
                #for z in y.lista_figli:
                    #print(z.nome)
                    #print('lv 3')
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        p=0
        o=0
        x=0
        #print(self)
        ris=''
        ls=[]
        #v=onekill(self,ris)
        #mr=[]
        #mr=bobo(self,mr,0)
        #print(mr)
        #d={}
        #for x,val in enumerate(mr):
          #  if isinstance(mr[x], int):
                #print(mr[x])
         #       d[mr[x]]=x
        #print(d)
        #por=(min(list(d.keys())))
        v=True
        dd=deepcopy(self)
        #poro=(d[por])-1
        v=AI(dd,giocatore,dd.nome)
        return v
#def zero(griglia,x,y,s):
def cosHelp(griglia,x,y,s):
    if griglia[x][y] == '':
        griglia[x][y] = s
        return 1
def cos(griglia,x,y,s):
    a=cosHelp(griglia,x+1,y-1,s)
    if a == 1:
        return 1
    b=cosHelp(griglia,x+1,y+1,s)
    if b == 1:
        return 1
    c=cosHelp(griglia,x-1,y-1,s)
    if c == 1:
        return 1
    d=cosHelp(griglia,x-1,y+1,s)    
    if d == 1:
        return 1
    return 0


def cos1Help(griglia,x,y,x2,y2,s):
    
    if griglia[x][y] == '' and griglia[x2][y2] == '':   
        griglia[x2][y2]=s
                        #print('cane1')
        return 1
def cos1(griglia,x,y,s):
    a=cos1Help(griglia,x+1,y,x+2,y,s)
    if a == 1:
        return 1                    
    if y == 0:
        #continuare
        b=cos1Help(griglia,x,y+1,x,y+2,s)
        if b== 1:
            return 1
    elif y == 2:
        c=cos1Help(griglia,x,y-1,x,y-2,s)
        if c == 1:
            return 1
    else:
        d=cosHelp(griglia,x,y+1,s)
        if d == 1:
            return 1
        e=cosHelp(griglia,x,y-1,s)
        if e == 1:
            return 1
        
    return 0


def cos2(griglia,x,y,s):
    a=cos1Help(griglia,x-1,y,x-2,y,s)
    if a == 1:
        return 1
    
    if y == 0:
        b=cos1Help(griglia,x,y+1,x,y+2,s)
        if b == 1:
            return 1
        
    elif y == 2:
        c=cos1Help(griglia,x,y-1,x,y-2,s)
        if c == 1:
            return 1
    else:
        d=cosHelp(griglia,x,y+1,s)
        if d == 1:
            return 1
        e=cosHelp(griglia,x,y-1,s)
        if e == 1:
            return 1
    return 0
    
def vittoria(griglia,s):
    #metodo basato sulla mia esperienza sul tris, campione imbattuto alle superiori ! tenica a delta o del lato, infallibili al massimo patta
    #ciao prof! spero non le esplodano gli occhi alla vista di questa spazzatura T T
       
    for x in range(0,3):
        for y in range(0,3):
            if griglia[x][y] == s:
                #print(griglia[x][y],x,y)
                if x == 1 and y == 1:
                    #print('ciaosss')
                    po=cos(griglia,x,y,s)
                    if po == 1:
                        return po
                    
                if x == 0:
                    #print(s,y)
                    po2=cos1(griglia,x,y,s)
                    if po2 == 1:
                        return 1
                if x == 2:
                    #
                    po3=cos2(griglia,x,y,s)
                    if po3 == 1:
                        return 1
    pat=0                    
    for x in range(0,3):
        pat+=(griglia[x].count(''))
    if pat == 1:
        for x in range(0,3):
            for y in range(0,3):
                if griglia[x][y] == '':
                    griglia[x][y] = s
                    return 1
    #print(pat)                    
    return 0
                    
                        
                        #controllare meglio le combinazioni della strategia e 
                        #vedere se il doppio for non crea problemi
                    
def counter(griglia,s,m):
    for x in range(0,3):
        if griglia[x][0] == m or griglia[x][2]==m:
            #print('x')
            
            if griglia[x][0] == griglia[x][2]:
                #print('1.1')
                if griglia[x][1]== '':
                    griglia[x][1]=s
                    return 1
            if griglia[x][0] == griglia[x][1]:
                
                if griglia[x][2]=='':
                    griglia[x][2]=s
                    #print('1.2')
                    return 1
            if griglia[x][1] == m and griglia[x][1] == griglia[x][2]:
                if griglia[x][0]=='':
                    griglia[x][0]=s
                    #print('1.3')
                    return 1
            #print(griglia)
        if griglia[0][x] == m :
            #print(s)
            if  griglia[0][x] == griglia[2][x]:
                #print('2.1')
                if griglia[1][x] == '':
                    griglia[1][x] = s
                    return 1
            if griglia[1][x] == griglia[0][x]:
                if griglia[2][x]=='':
                    griglia[2][x]=s
                    #print('2.2')
                    return 1
            if griglia[1][x] == m and griglia[1][x] == griglia[2][x]:
                if griglia[0][x]=='':
                    griglia[0][x]=s
                    #print(griglia[1][x])
                    #print('2.3')
                    return 1
    if griglia[0][0] == m or griglia[0][2] == m :
        #print('ci')
        if griglia[0][0] == m and griglia[0][0] == griglia[1][1]:
            #print('1')
            if griglia[2][2]== '':
                griglia[2][2]=s
                return 1
        if griglia[0][0] == m and griglia[0][0] == griglia[2][2]:
            #print('vi')
            if griglia[1][1] == '':
                griglia[1][1] = s
                return 1
        if griglia[1][1] == m and griglia[1][1] == griglia[2][2]:
            #print('ddi')
            if griglia[0][0] == '':
                griglia[0][0] = s
                return s
    if griglia[0][2] == m or griglia[1][1] == m:
        #print('di')
        if griglia[0][2] == griglia[1][1] :
            if griglia[2][0] =='':
                griglia[2][0] = s
                return 1
        if griglia[0][2] == griglia[2][0]:
            if griglia[1][1] =='':
                griglia[1][1] = s
                return 1
        if griglia[1][1] == m and griglia[1][1] == griglia[2][0]:
          if  griglia[2][0] == '':
                griglia[2][0] = s
                return 1
        
    return 0
def near(radice,griglia):
    s='o'
    m='x'
    #print(griglia)
    #griglia=radice.nome
    xx=0
    oo=0
    if radice.tipo() == '?':
        for yy,val in enumerate(radice.nome):
            xx+=(radice.nome[yy].count('x'))
            oo+=(radice.nome[yy].count('o'))
        if xx == oo:
            #print(griglia)
            uno=counter(griglia,s,s)
            if uno == 0:
                c=counter(griglia,s,m)
                if c == 0:            
                    vittoria(griglia,s)
        else:
            #print(griglia)
            uno=counter(griglia,m,m)
            #print(griglia)
            if uno == 0:
                c=counter(griglia,m,s)
                #print(griglia)
                if  c == 0:
                    vittoria(griglia,m)
        near(NodoTris(griglia),griglia)

        return griglia
    else:
        
        return griglia
            
                        
                   
            
  
def AI(radice,giocatore,griglia):
    #ris=''
    #print(radice.nome)
    #print(giocatore)


    gr=(near(radice,griglia))
    nd=NodoTris(gr)
    #print(nd.tipo(),giocatore)
    if nd.tipo() == giocatore:
        #print('cane')
        return True
    else:
        #print('gatto')
        return False
    #print(nd.tipo())

        #else:
            #counter(radice.nome,'o')
        #else:
            #counter(radice.nome,'x')
    #print(xx,oo)
def lvl(radice,lv,h,giocatore,vit):
    #pass
    #print('livello',lv)
    #print(radice.nome)
    if(lv == h):
        if radice.tipo() == giocatore:
            #print(radice.tipo())
            return 1
    for x in radice.lista_figli:
        
        c=(lvl(x,lv+1,h,giocatore,vit))
        if c == 1:
            vit+=[c]
    #print(vit)
    return vit
def foglia(radice,ls):
    
    if radice.lista_figli == []:
        #print(radice.tipo())
        return radice.tipo()
    for x in radice.lista_figli:
        ls.append(foglia(x,ls))
    
    return ls
def gen_rad(griglia,radice):
    if radice == None or radice == []:
        return NodoTris(griglia)
    
    return radice
def ins(griglia,radice,rado):
    #print(radice)
    if radice == None or radice == []:
        #print('d')
        return NodoTris(griglia)   
    if rado.lista_figli == []:
        #print('ciao')
        rado.lista_figli.append(ins(griglia,radice.lista_figli,rado))
    else:
        fake=None
        rado.lista_figli.append(ins(griglia,fake,rado))
    #radice.lista_figli.append(ins(griglia,radice.lista_figli[0]))
    return rado
def gen_gr(radice,x,y):
    xx=0
    oo=0

    gr=[]

    for xu in radice.nome:
        gr+=[copy(xu)]
    for yy,val in enumerate(radice.nome):
            xx+=(radice.nome[yy].count('x'))
            oo+=(radice.nome[yy].count('o'))
    if xx == oo:
        gr[x][y]='o'
    else:
        gr[x][y]='x'

    return gr
def acc(radice):
    for x,val in enumerate(radice.nome):
        for y,val in enumerate(radice.nome[x]):
            if radice.nome[x][y] == '':
                #radicecop=deepcopy(radice)
                #print(radice.nome)
                grigliaP=gen_gr(radice,x,y)
                #print()
                radice=ins(grigliaP,radice,radice)
    return radice
                
def pos_1(radice):
    #print(radice.nome)
    radice=acc(radice)
    for z,val in enumerate (radice.lista_figli):
        if radice.lista_figli[z].tipo() == '?':
            radice.lista_figli[z]=(pos_1(radice.lista_figli[z]))
    return radice

    
        
def gen_tree(griglia):
    '''inserire qui il vostro codice'''
    radice=None
    l=[]
    #radicecop=deepcopy(radice)
    
    radice=ins(griglia,radice,radice)
    #radicecop=deepcopy(radice)
    #print(radicecop)
    radice=pos_1(radice)
    #for x in radice.lista_figli:
        #print(x.nome)
        #for y in x.lista_figli:
            #print(y.nome)
            #for z in y.lista_figli:
                #print(z.nome)
        #print('\n')

    
    return radice



        


g0=[['', '', ''], ['', '', ''], ['', '', '']]
g1=[['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
g2=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'o']]
g3=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', '', 'x']]
g4=[['o', 'x', 'x'], ['x', 'o', 'o'], ['o', 'o', 'x']]

g5=[['', 'x', ''], ['', 'o', ''], ['', '', '']]
g6=[['', 'o', ''], ['', 'x', ''], ['', '', '']]
g7=[['', 'x', 'o'], ['', '', ''], ['', '', '']]
g8=[['', 'o', 'x'], ['', '', ''], ['', '', '']]

#listaa=[g1, g2, g3, g4]
#listab=[g5, g6, g7, g8]
#☺poo=[['', 'o', 'x'], ['', '', ''], ['', '', '']]
#poo=[['', 'x', 'o'], ['', '', ''], ['', '', '']]
#mr=[]
#d={}
#poo=[['', 'o', 'x'], ['', '', ''], ['', '', '']]
#ada=gen_tree(poo)
#rint(poo)
#pp=[['', 'o', 'x'], ['', '', ''], ['x', 'o', 'o']]
#print(poo)
#print(ada.strategia_vincente('o'))
#counter(pp,'o','o')
#print(pp)
#(counter(poo,'o','x')) 
    #print('cazzo')
    #vittoria(poo,'o')
#print(poo)

#c = counter(poo,'x','o')
#if c == 0:
    #print('ciao')
    #vittoria(poo,'x')



    
#print(poo) #implementare patta finale#print(ada.strategia_vincente('o'))
#counter(poo,'x','o')

#for x in poo:
    #print(x.count(''))
#if (counter(poo,'o','x')) == 0:
    
#    vittoria(poo,'o') #proseguimento della funzione vittoria, counter funza
    #print(poo)
#c = counter(poo,'x','o')
#print(poo)    
#if c == 0:
    
#    vittoria(poo,'x')

#counter(poo,'o','o')
#print(poo)
#vittoria(poo,'o') #proseguimento della funzione vittoria, counter funza
#print(poo)
#print(poo)
    

        #print(mr[x],x)
#bobo1(ada)
#ada.strategia_vincente

#listac=[program02.gen_tree(x) for x in listaa]
#rad=None

#aba=gen_tree(g1)
#aba.vittorie_livello('o',1)
#ll=[aba]
#print(ll[0].strategia_vincente('o'))
#print(aba.strategia_vincente('o'))

#print(listac[0].strategia_vincente('o'))
#print(aba)
#print(aba.tipo())
#listaa=[g1, g2, g3, g4]
#listac=[gen_tree(x) for x in listaa]
#print(aba.esiti())
#aba.vittorie_livello('x',2)
#import time

#tempo_iniziale = time.time()

# INSERISCI QUI LE TUE OPERAZIONI

#tempo_finale = time.time()
#print ("Impiegati", str(tempo_finale - tempo_iniziale), "secondi.")