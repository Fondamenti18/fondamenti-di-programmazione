import copy
import cProfile
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
    
    def tipo(self):
        '''inserire qui il vostro codice'''
        for lista in self.nome:
            if '' not in lista:                
                if lista[0]==lista[1]==lista[2]:                                   
                    return lista[0]
                
        for i in range(0,3):                           
            if self.nome[0][i]==self.nome[1][i]==self.nome[2][i]:
                if self.nome[0][i] != '':
                    return self.nome[0][i]

        if self.nome[0][0]==self.nome[1][1]==self.nome[2][2]:
            if self.nome[0][0] != '':
                return self.nome[0][0]

        if self.nome[0][2]==self.nome[1][1]==self.nome[2][0]:
            if self.nome[0][2] != '':
                return self.nome[0][2]
        if '' not in self.nome[0] and '' not in self.nome[1] and '' not in self.nome[2]:
            return '-'
        
        return '?' 
        
    def esiti(self):
        '''inserire qui il vostro codice'''
        vittorie_x=0
        vittorie_o=0
        patta=0
        chi_vince=self.tipo()
        if chi_vince=='-':
            patta+=1
        if chi_vince=='x':
            vittorie_x+=1
        if chi_vince=='o':
            vittorie_o+=1
        for x in self.lista_figli:
            esito_figli= x.esiti()
            vittorie_x+=esito_figli[2]
            vittorie_o+=esito_figli[1]
            patta+=esito_figli[0]
            
        return patta,vittorie_o,vittorie_x
    
    def vittorie_livello(self, giocatore, h, livello=0):
        '''inserire qui il vostro codice'''
        conta=0
        if livello == h and giocatore == self.tipo():
            conta+=1
        for x in self.lista_figli:
           conta += x.vittorie_livello(giocatore,h,livello+1)
           
        return conta

    
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        pass
                    
    
    def stampa_albero(self):
        print(self.nome)
        for figlio in self.figli:
            figlio.stampa_albero()
        
def gen_tree(griglia):
    '''inserire qui il vostro codice'''
    radice = NodoTris(griglia)
    if radice.tipo()=='?':
        turnoo=turno(griglia)
        for lista in range(0,3):
            for x in range(0,3):
                if griglia[lista][x]=='':
                    copia=copy.deepcopy(griglia)
                    copia[lista][x]=turnoo
                    radice.lista_figli+=[gen_tree(copia)]
    return radice

def turno(griglia):
    conta_x=0
    conta_o=0
    for lista in griglia:
        for y in lista:
            if y=='o':
                conta_o+=1
            if y=='x':
                conta_x+=1
    if conta_x < conta_o:
        return 'x'
    if conta_x >= conta_o:
        return 'o'

