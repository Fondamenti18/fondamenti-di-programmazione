import copy

#classe del nodo
class NodoTris:
    
    #costruttore
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] 

    #ritorna le posizioni delle caselle vuote (pari->x, dispari->o)
    def liberi(self):
        ins=set()
        for iriga in range(3):
            for iel in range(3):
                if self.nome[iriga][iel] == '':
                    ins.add((iriga,iel))
        return ins

    #ritorna l avversario del giocatore di turno
    def nemico(self):
        cnt=self.turno()
        if cnt%2==0: return 'x'
        return 'o'
    
    #ritorna il giocatore di turno
    def gioc(self):
        cnt=self.turno()
        if cnt%2==0: return 'o'
        return 'x'

    #ritorna il numero di caselle riempite (pari->o, dispari->x)
    def turno(self):
        cnt=0
        for riga in self.nome:
            for el in riga:
                if el != '':
                    cnt+=1
        return cnt

    #controllo delle orizzontali
    def controllo_h(self):
        for iriga in range(3):
            ch=self.nome[iriga][0]; cnt=0
            if ch!='':
                for icol in range(3):
                    if ch!=self.nome[iriga][icol]: icol+=1
                    else: cnt+=1
                    if cnt==3: return ch
        return '/'

    #controllo delle verticali 
    def controllo_v(self):
        for icol in range(3):
            ch=self.nome[0][icol]; cnt=0
            if ch!='':
                for iriga in range(3):
                    if ch!=self.nome[iriga][icol]: iriga+=1
                    else: cnt+=1
                    if cnt==3: return ch
        return '/'

    #controllo delle diagonali
    def controllo_d(self):
        if self.nome[0][0] ==self.nome[1][1] and self.nome[1][1] ==self.nome[2][2]  and self.nome[0][0]!='':
            return self.nome[0][0]
        if self.nome[0][2] ==self.nome[1][1] and self.nome[1][1] ==self.nome[2][0]  and self.nome[0][2]!='':
            return self.nome[0][2]
        return '/'


    #ritorna un char che descrive la situzione della scacchiera
    def tipo(self):
        a=self.controllo_d()
        if a!='/':return a
        a=self.controllo_h()
        if a!='/':return a
        a=self.controllo_v()
        if a!='/':return a
        if self.turno()==9:return '-'
        return '?'        

    #funzione ricorsiva per esiti
    def esito(self,patte,vitto,vittx):
        if len(self.lista_figli)==0:
            a=self.tipo()
            if a=='-': patte+=1
            elif a=='o': vitto+=1
            elif a=='x': vittx+=1
        
        else:
            for el in self.lista_figli:
                patte,vitto,vittx=el.esito(patte,vitto,vittx)
                
        return patte, vitto, vittx

    #ritorna una tripla del conteggio delle possibili vittorie/pareggi
    def esiti(self):
        t1,t2,t3=self.esito(0,0,0)
        return (t1,t2,t3)

    #funzione ricorsiva per vittoria livello
    def vittoria(self,giocatore,h,vittorie,passaggi):
        if passaggi==h and len(self.lista_figli)==0 and self.tipo()==giocatore :vittorie+=1
        elif passaggi<h:
            for el in self.lista_figli:
                vittorie=el.vittoria(giocatore,h,vittorie,passaggi+1)
        return vittorie

    #ritorna il numero di vittorie possibili con h mosse per un dato giocatore
    def vittorie_livello(self,giocatore, h):
        return self.vittoria(giocatore,h,0,0)

    #funzione ricorsiva di strategia_vincente, ritorna un contatore che indica se esista o meno una strategia vincente
    def vincente(self, livello, giocatore) :
        
        base = -10
        if giocatore == 'x':   base = +10
        
        #partita finita
        ris=self.tipo(); rest=0
        if ris!='?' :
            if 'x' == ris : rest= livello-10 
            elif 'o' == ris : rest= 10-livello 
            return rest

        #partita ancora senza esito
        avversario=self.nemico()
        for figlio in self.lista_figli :
            nuova_base= figlio.vincente(livello+1,avversario)  
            if giocatore == 'x' and nuova_base < base: base=nuova_base  
            elif giocatore == 'o' and nuova_base > base: base=nuova_base
    
        return base

    #ritorna true se un giocatore ha almeno una strategia 'vincente', falso altrimenti.
    def strategia_vincente(self,giocatore):
        if self.vincente(0,giocatore)>0: return True
        return False


#----------------- Funzioni di generazione ----------------#
 
def copia_griglia(griglia):
    nuova_griglia=[]
    for iriga in range(3):
        riga=[]
        for iel in range(3):
            riga+=[griglia[iriga][iel]]
        nuova_griglia+=[riga]
    return nuova_griglia

#funzione ricorsiva per generare l albero
def genera_albero(nodo):

    ins=nodo.liberi()
    cnt=len(ins)
    
    if cnt!=0:
        
        if cnt%2 ==0:player='x'
        else:player='o'
        
        while len(ins)>0:
            griglia=copia_griglia(nodo.nome)
            iriga,iel=ins.pop()
            griglia[iriga][iel]=player
            nodo.lista_figli+=[NodoTris(griglia)]

        if cnt!=1:
            for el in nodo.lista_figli:
                if el.tipo()=='?':
                    genera_albero(el)
        
    return nodo

#genera l albero dalla radice
def gen_tree(griglia):
    nodo=NodoTris(griglia)
    return genera_albero(nodo)
