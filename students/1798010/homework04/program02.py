pattern = []

class NodoTris:
    def __init__(self, griglia):
        
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.type = self.tipo()
        self.result = (-1,-1,-1)
        self.next = "stop"
        
    def tipo(self):
    
        last = ""
        empty = False
        
        for pat in pattern:
            
            last = self.nome[pat[0][0]][pat[0][1]]
            
            if last == '':
                empty = True
                continue
            
            skip = False
        
            for i in range(1,3):
                       
                cur = self.nome[pat[i][0]][pat[i][1]]
                       
                if cur != last:
                    skip = True          
                    
                    if not empty and cur == '':
                        empty = True
                    
                    break
                    
            if skip:
                continue
            else:
                return last
                break
            
        if empty:
            return '?'
            
        return '-'
     
    def esiti(self,count = -1):
        
        n,o,x = 0,0,0
        
        if count > 0:
            count -= 1
        
        if self.type == '-':
            return 1,0,0
        elif self.type == 'o':
            return 0,1,0
        elif self.type == 'x':
            return 0,0,1
        else:
        
            if count == 0:
                return 1,0,0
        
            for node in self.lista_figli:                
                                                                   
                N,O,X = node.esiti(count)
                
                n += N
                o += O
                x += X
            
            self.result = (n,o,x)
            return n,o,x
    
    def vittorie_livello(self, giocatore, h):
        
        
        h -= 1
        
        if h == 0:
            c = 0
            for child in self.lista_figli:      
                if child.type == giocatore:
                    c += 1
            return c
        else:
            c = 0
        
            for child in self.lista_figli:
                c += child.vittorie_livello(giocatore,h)
                
            return c
        
        return 0
        
    
    def strategia_vincente(self,giocatore):
        
        player = 2
        if giocatore == 'o':
            player = 1
        
        if self.type == '?':
            if self.next != giocatore:
                
                for child in self.lista_figli:
                    if not child.strategia_vincente(giocatore):
                        return False
                
                return True
            else:
                for child in self.lista_figli:
                    if child.strategia_vincente(giocatore):
                        return True
                        
                return False
        else:
            return self.type == giocatore
        
def gen_tree(griglia):
    
    global pattern
    
    pattern = [ [(x,y) for y in range(3)] for x in range(3)]
    pattern += [ [(y,x) for y in range(3)] for x in range(3)]
    pattern += [[ (x,x) for x in range(3) ]]
    pattern += [[ (x,2-x) for x in range(3) ]]
    
    x,o = 0,0
    
    #print(griglia)
    
    for xx in range(3):
        for y in range(3):
            #print(xx,y)
            if griglia[xx][y] == 'x':
                x += 1
            elif griglia[xx][y] == 'o':
                o += 1
    
    startNode = NodoTris(griglia)
    
    if x == o:
        makeMove(startNode,'o')
    elif x > o:
        makeMove(startNode,'o')
    else:
        makeMove(startNode,'x')
    
    #startNode.esiti()
    return(startNode)
    
def makeMove(node,player):
        
    next = 'x'
    if player == "x":
        next = 'o'
    
    node.next = player
    
    for x in range(3):
        for y in range(3):
            if node.nome[x][y] == '':
                newGrid = [[node.nome[x][y] for y in range(3)] for x in range(3)]
                newGrid[x][y] = player 
                
                newNode = NodoTris(newGrid)
                node.lista_figli.append(newNode)
                
                if newNode.type == "?":
                    makeMove(newNode,next)
            

def printTree(node):

    frontier = [node]
    
    while len(frontier) > 0:
        current = frontier.pop()
        print('Winner:',current.type,"\n'-' 'o' 'x' :",current.esiti(),"\nNext:",current.next)
        for y in range(3):
            print(current.nome[y])
            
        print("\n" * 3)
        
        for n in current.lista_figli:
            frontier.append(n)

                

#startGrid = [['o','x','o'],
#['x','o','x'],
#['','','']]
#startGrid = [['','',''],['','',''],['','','']]

#node = gen_tree(startGrid) 
#printTree(node)
#print(node.esiti())
