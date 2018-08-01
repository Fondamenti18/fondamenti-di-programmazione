

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.lscelle_vuote=self.esplora_griglia_vuote()
        self.lsriempite=self.esplora_griglia_riempite()
        self.turno=self.definisci_turno()
        
        self.d1=[self.nome[0][0],self.nome[1][1],self.nome[2][2]]
        self.d2=[self.nome[0][2],self.nome[1][1],self.nome[2][0]]
        
        self.r1=[self.nome[0][0],self.nome[0][1],self.nome[0][2]]
        self.r2=[self.nome[1][0],self.nome[1][1],self.nome[1][2]]
        self.r3=[self.nome[2][0],self.nome[2][1],self.nome[2][2]]
        
        self.c1=[self.nome[0][0],self.nome[1][0],self.nome[2][0]]
        self.c2=[self.nome[0][1],self.nome[1][1],self.nome[2][1]]
        self.c3=[self.nome[0][2],self.nome[1][2],self.nome[2][2]]
        
        self.lsvittoria_o=['o','o','o']
        self.lsvittoria_x=['x','x','x']
                
        self.livello=len(self.lsriempite) #9-len(self.lscelle_vuote)
        self.g0=[[['o', '', ''], ['', '', ''], ['', '', '']],[['', 'o', ''], ['', '', ''], ['', '', '']],[['', '', ''], ['', 'o', ''], ['', '', '']]]
        self.coeff=(4,4,1)
        
    def genera_figli(self):
        if self.tipo()=='?' and len(self.lista_figli)==0:
            for c in range(len(self.lscelle_vuote)):
                lsnodo=[]
                for j in range(3):
                    ls=[]
                    for i in range(3):
                        ls+=[self.nome[j][i]]
                    lsnodo+=[ls]
                self.lista_figli+=[lsnodo]
            for c in range(len(self.lscelle_vuote)):
                i,j=self.lscelle_vuote[c]
                self.lista_figli[c][j][i]=self.turno    
        return self.lista_figli

    def genera_stirpe(self):
        self.genera_figli()
        self.lsmosse+=self.lista_figli
        for figlio in self.lsmosse:
            nodo=NodoTris(figlio)
            nodo.genera_figli()
            if nodo.livello+1>9:
                break
            self.dzmosse[nodo.livello+1]+=nodo.lista_figli
            self.lsmosse+=nodo.lista_figli
            #self.lsmosse.remove(figlio)
        self.dzmosse[self.livello]=[self.nome]
        if len(self.lista_figli)>0:
            self.dzmosse[self.livello+1]=self.lista_figli
        return self.dzmosse
            
    def esplora_griglia_vuote(self):
        lsvuote=[]
        for j in range(3):
            for i in range(3):
                if self.nome[j][i]=='':
                    lsvuote+=[(i,j)]
        return lsvuote

    def esplora_griglia_riempite(self):
        lsriempite=[]
        for j in range(3):
            for i in range(3):
                if self.nome[j][i]!='':
                    lsriempite+=[(i,j)]
        return lsriempite
    
    def definisci_turno(self):
        if len(self.lscelle_vuote)==0:
            return ''
        elif len(self.lscelle_vuote)%2==0:
            return 'x'
        else:
            return 'o'
        
    def tipo(self):
        '''inserire qui il vostro codice'''        
        if self.vittoria_o():
            return 'o'
        elif self.vittoria_x():
            return 'x'
        elif self.griglia_riempita():
            return '-'
        else:
            return '?'

    def vittoria_o(self):
        return self.d1==self.lsvittoria_o or self.d2==self.lsvittoria_o or \
    self.r1==self.lsvittoria_o or self.r2==self.lsvittoria_o or self.r3==self.lsvittoria_o or \
    self.c1==self.lsvittoria_o or self.c2==self.lsvittoria_o or self.c3==self.lsvittoria_o
    
    def vittoria_x(self):
        return self.d1==self.lsvittoria_x or self.d2==self.lsvittoria_x or \
    self.r1==self.lsvittoria_x or self.r2==self.lsvittoria_x or self.r3==self.lsvittoria_x or \
    self.c1==self.lsvittoria_x or self.c2==self.lsvittoria_x or self.c3==self.lsvittoria_x
    
    def vittoria_in_tasca(self, giocatore):
        ls=[self.d1,self.d2,self.r1,self.r2,self.r3,self.c1,self.c2,self.c3]
        v=0
        if giocatore=='o':
            avversario='x'
        else:
            avversario='o'
        for l in ls:
            if l.count(giocatore)==2 and l.count('')==1:
                v+=1
            elif l.count(avversario)==2 and l.count('')==1 and self.turno==avversario:
                return False
        if v>=2:
            return True
        return False
        
    def griglia_riempita(self):
        return len(self.lscelle_vuote)==0

    def conta_esiti(self):
        patta=0
        vince_o=0
        vince_x=0
        if self.tipo()=='-':
            patta=1
        elif self.tipo()=='o':
            vince_o=1
        elif self.tipo()=='x':
            vince_x=1
        return (patta,vince_o,vince_x)
        
    def esiti(self):
        '''inserire qui il vostro codice'''
        if self.nome==[['', '', ''], ['', '', ''], ['', '', '']]:
            return self.esiti_g0()
        
        p,o,x=self.conta_esiti()
        self.genera_figli()
        for f in self.lista_figli:
            p_n,o_n,x_n=NodoTris(f).esiti()
            p+=p_n
            o+=o_n
            x+=x_n
        return(p,o,x)
    
    def esiti_g0(self):
        p=o=x=0
        for i in range(len(self.g0)):
            p_i,o_i,x_i=NodoTris(self.g0[i]).esiti()
            p+=(p_i*self.coeff[i])
            o+=(o_i*self.coeff[i])
            x+=(x_i*self.coeff[i])
        return (p,o,x)
            
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
        if self.nome==[['', '', ''], ['', '', ''], ['', '', '']]:
            return self.vittorie_livello_g0(giocatore, h)
        
        vittorie=0
        
        if h==0 and self.tipo()==giocatore:
            return 1
        elif self.livello+h<5:
            return 0
                
        if self.livello<=9:
            #print(giocatore, 'vittorie',vittorie)
            #l=h-1
            if h<0:
                return vittorie
            
            self.genera_figli()
            for f in self.lista_figli:
                vittorie+=NodoTris(f).vittorie_livello(giocatore,h-1)
        return vittorie
    
    def vittorie_livello_g0(self, giocatore, h):
        vittorie=0
        if (giocatore=='o' and h in (0,1,2,3,4,6,8)) or \
        (giocatore=='x' and h in (0,1,2,3,4,5,7,9)):
            return 0
        for i in range(len(self.g0)):
            v_i=NodoTris(self.g0[i]).vittorie_livello(giocatore,h-1)
            vittorie+=(v_i*self.coeff[i])
        return vittorie
    
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        if self.vittoria_in_tasca(giocatore) or self.tipo()==giocatore:
            return True
        else:
            self.genera_figli()
            for f in self.lista_figli:
                return NodoTris(f).strategia_vincente(giocatore)
        return False
            
def gen_tree(griglia):
    '''inserire qui il vostro codice'''    
    config=NodoTris(griglia)

    return config