
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] 
        self.player= ''
        self.type= self.tipo()
        self.foglie= {'-':0, 'x':0, 'o':0}
        

    def findEmptySlots(self, emptySlots=set() ):
            for y in range(3):
                for x in range(3):
                    if self.nome[y][x]== '':
                        emptySlots.add((x,y))
            return emptySlots
    
    def tipo(self):       
        schema=(((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),((0,0),(1,0),(2,0)),((0,1),(1,1),(2,1)),((0,2),(1,2),(2,2)),((0,0),(1,1),(2,2)),((0,2),(1,1),(2,0)))
        for a, b, c in schema:
            if (len(set((self.nome[a[0]][a[1]],self.nome[b[0]][b[1]],self.nome[c[0]][c[1]]))))== 1:
                return (self.nome[a[0]][a[1]] if self.nome[a[0]][a[1]]!= '' else '?' )
        else :
            for i in self.nome:
                if '' in i:
                    return '?'
            return '-'
        
    def esiti_radice(self, count=0):
        dizionnario={0:'-', 1:'o', 2:'x'}
        if count>2: return (self.foglie['-'], self.foglie['o'], self.foglie['x'])
        else :  return self.esiti_radice(count+1)
        
    def esiti_nodo(self):
        if self.type!= '?':
            return {'-': (1, 0, 0), 'o': (0, 1, 0), 'x': (0, 0, 1)}[self.type]

        risultato=[0, 0, 0]

        for nuovoNodo in self.lista_figli:
            esitiFiglio=nuovoNodo.esiti()
            risultato=[risultato[i]+ esitiFiglio[i] for i in range(3)]

        return tuple(risultato)
    
    def esiti (self):
    
        if self.foglie['-'] or self.foglie['o'] or self.foglie['x']:
            return self.esiti_radice()
        else:
            return self.esiti_nodo()
        
    def vittorie_livello(self, giocatore, h):

        if not h:
            if self.type == giocatore: return 1
            else: return 0

        if self.type!= '?': return 0
        
        risultato=0

        for nuovoNodo in self.lista_figli:
            risultato+= nuovoNodo.vittorie_livello(giocatore, h-1)
        
        return risultato
        
    
    def strategia_vincente(self,giocatore):

        
        if self.vittorie_livello(self.player, 1):
            return (True if self.player== giocatore else False)

        risultato= (False if self.player== giocatore else True)

        for nuovoNodo in self.lista_figli:
            if giocatore == self.player:
                risultato= risultato or nuovoNodo.strategia_vincente(giocatore)
            else:
                risultato= risultato and nuovoNodo.strategia_vincente(giocatore)
        return risultato

        
from copy import deepcopy

        
def gen_tree(griglia, radice=0, first=1, emptySlots=set() ):

    albero= NodoTris(griglia)
    
    if first:
        radice= albero
        emptySlots= albero.findEmptySlots()

    if albero.type != '?':
        radice.foglie[albero.type]+= 1
        
        return albero
    
          
    albero.player =('x' if(len(emptySlots)%2==0) else 'o')
    
    for slot in emptySlots:
        nuovoNodo= deepcopy(griglia)
        nuovoNodo[slot[1]][slot[0]]= albero.player
        albero.lista_figli.append(gen_tree(nuovoNodo, radice, 0, emptySlots.difference({slot})))
    return albero
