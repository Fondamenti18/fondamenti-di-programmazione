#

from copy import deepcopy

lunghezza = range(3)

class NodoTris:

    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = []
        self.stato = '?'
        self.livello = 0
    
    def tipo(self):   #ritorno dell'attributo stato
        return self.stato
        
    def esiti(self):   #conta degli stati
        tupla = [0,0,0]
        stringa = conta(self)
        for char in stringa:
            if char ==  '-': tupla[0] += 1
            elif char == 'o': tupla[1] += 1
            else: tupla[2] += 1
        return tuple(tupla)
        
    
    def vittorie_livello(self, giocatore, h): #conta delle vittorie
        numero_vittorie = 0
        return discendi(self, giocatore, h)
    

    def strategia_vincente(self,giocatore):  #strategia vincente tramite il metodo del "triangolo" o "l"

        count = 0
        if giocatore == 'x': avversario = 'o'
        else: avversario = 'x'
        diagonali = 0
        diagonali2 = 0
        diagonali = diagonale(self.nome, 0, 0, avversario)
        diagonali2 = diagonale2(self.nome, 0, 2, avversario)
        sommagiocatore = diagonali + diagonali2
        sommaavversario = diagonale(self.nome, 0, 0, giocatore) +  diagonale2(self.nome, 0, 2, giocatore)
        
        if giocatore == 'o' : 
        	sommagiocatore +=1
        	if self.nome[1][1] =='x' and self.nome[0][0] != 'o' and self.nome[0][2] != 'o' and self.nome[2][0] != 'o' and self.nome[2][2] != 'o':
        		sommagiocatore -=1
        if sommagiocatore > sommaavversario: return True
        return False

       
def diagonale(griglia, i, j, avversario, count = 0):

    if griglia[i][j] != avversario: 
        count += 1

    if i + 1 == 3: return count
    count = diagonale(griglia, i+2, j+2, avversario, count)

    return count

def diagonale2(griglia, i, j, avversario, count = 0):


    if griglia[i][j] != avversario: 
        count += 1

    if j -2 == -2: return count

    count = diagonale2(griglia, i+2, j-2, avversario, count)

    return count

def discendi(nodo, giocatore, h):

    if nodo.lista_figli == []:
        if nodo.livello == h and nodo.stato == giocatore: return 1

    tot = 0

    for figlio in nodo.lista_figli:

        tot += discendi(figlio,giocatore,h)
    return tot

def verifica_vittoria(griglia,nodo):


    for riga in lunghezza:
        if griglia[riga][0] == 'x' and griglia[riga][1] == 'x' and griglia[riga][2] == 'x':
            nodo.stato = 'x'
            return True
            
        elif griglia[riga][0] == 'o' and griglia[riga][1] == 'o' and griglia[riga][2] == 'o':
            nodo.stato = 'o'
            return True
            
        elif griglia[0][riga] == 'x' and griglia[1][riga] == 'x' and griglia[2][riga] == 'x':
            nodo.stato = 'x'
            return True
            
        elif griglia[0][riga] == 'o' and griglia[1][riga] == 'o' and griglia[2][riga] == 'o':
            nodo.stato = 'o'
            return True
            
    if griglia[0][0] == 'x' and griglia[1][1] == 'x' and griglia[2][2] == 'x':
        nodo.stato = 'x'
        return True

    elif griglia[0][0] == 'o' and griglia[1][1] == 'o' and griglia[2][2] == 'o':
        nodo.stato = 'o'
        return True

    elif griglia[0][2] == 'x' and griglia[1][1] == 'x' and griglia[2][0] == 'x':
        nodo.stato = 'x'
        return True

    elif griglia[0][2] == 'o' and griglia[1][1] == 'o' and griglia[2][0] == 'o':
        nodo.stato = 'o'
        return True

    elif '' not in griglia[0] and '' not in griglia[1] and '' not in griglia[2]:
        nodo.stato = '-'
        return True

    return False

def generatrice(griglia,precedente = '',livello = 0):

    nodo = NodoTris(griglia)
    griglia1= []
    turno = ''
    vittoria = False
    vittoria = verifica_vittoria(griglia,nodo)
    nodo.livello = livello
    livello +=1
    if vittoria == False: 
        for riga in lunghezza:
            for colonna in lunghezza:
        
                if griglia[riga][colonna] == '':

                    griglia1 = deepcopy(griglia)
                    if precedente == '' or precedente == 'x': turno = 'o'
                    else: turno = 'x' 
                    griglia1[riga][colonna] = turno

                    nodo.lista_figli += [generatrice(griglia1,turno,livello)]                    

    return nodo

def conta(nodo):
    
    if nodo.lista_figli == []:
        return nodo.stato

    stringa = ''
     
    for figlio in nodo.lista_figli:
        
        stringa += conta(figlio)

    return stringa

def gen_tree(griglia,lista=[]):
    
    nodo = generatrice(griglia)
    return nodo