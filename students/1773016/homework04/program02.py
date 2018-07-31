import copy
import time
class NodoTris:
    #Funzioni Pubbliche--------------------------------------------------------------------------------------------------------
    def __init__(self, griglia):    #Costruttore
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.albero = {}
    def __str__(self):        #Funzione che viene chiamata quando si invoca il print sull'oggetto NodoTris
        self.__stampaPartita(self.nome)
        return ''
    def tipo(self):             #Fun che determina se una configurazione partita e una vittoria (per 'o' o 'x') o un pareggio
        type = ''               #Oppure è una configurazione non terminata
        griglia = self.nome
        terminato = self.__verificaTerminato(griglia)
        verifica = self.__verificaVittoria(griglia)               
        if terminato == '?' and verifica == '-':
            type = '?'
        else:
            type = verifica
        return type
    def esiti(self):         #Fun che presa una radice fa uno scan di tutti i nodi e riempie una tripla di risultati
        lista = [0,0,0]      #1°elem: pareggi, 2°elem: vittorie 'o', 3°elem: vittorie 'x'
        tipo = self.tipo()
        if tipo != '?':
            if tipo == '-':
                lista[0]+=1
            if tipo == 'o':    
                lista[1]+=1
            if tipo == 'x':
                lista[2]+=1
        self.__tuplaEsiti(lista,self.lista_figli)
        tupla = (lista[0],lista[1],lista[2])
        return tupla
    
    def vittorie_livello(self, giocatore, h):    #Fare uno scan dell'albero e contare per il livello (h) dell'albero le possibili  
        numVittorie = 0                          #vittorie per il giocatore passato come parametro
        if h == 0 and self.tipo() == giocatore:
            numVittorie = 1
        else:
            lista = []
            self.__scanVittorie(lista,self.lista_figli,giocatore,h,1)
            numVittorie = len(lista)
        return numVittorie  
    def strategia_vincente(self,giocatore): 
        vince = None
        controllo = [0,False]
        self.__checklivello(self.lista_figli,controllo)
        if giocatore == 'o' and controllo[1]:
            vince = True
        elif giocatore == 'x' and controllo:
            vince = False
        else:
            diz = {'x':'o','o':'x'}
            diz2 = {'x':-1,'o':1}
            giocatore = diz[giocatore]
            partita = self.__formatTab(self.nome)
            esito = self.__prosMossa(list(partita), giocatore.upper())
            if esito[0] == diz2[giocatore]:  
                vince = True
            else:
                vince = False
        return vince
    #Funzioni e Variabili Private----------------------------------------------------------------------------------------------
    def __checklivello(self,nodi,check,stop = False):
        if not stop:  
            for nodo in nodi:
                if nodo.tipo() == 'o':
                    check[1] = True
                    stop = True
                    self.__checklivello(nodo.lista_figli,check,stop)

    def __isVince(self,tab):
        for i in range(3):
            if len(set(tab[i * 3:i * 3 + 3])) is 1 and tab[i * 3] is not '-': return True
        for i in range(3):
            if (tab[i] is tab[i + 3]) and (tab[i] is tab[i + 6]) and tab[i] is not '-':
                return True
        if tab[0] is tab[4] and tab[4] is tab[8] and tab[4] is not '-':
            return True
        if tab[2] is tab[4] and tab[4] is tab[6] and tab[4] is not '-':
            return True
        return False

    def __prosMossa(self,tab, giocatore):
        if len(set(tab)) == 1: return 0, 4

        next = 'X' if giocatore == 'O' else 'O'
        if self.__isVince(tab):
            if giocatore is 'X':
                return -1, -1
            else:
                return 1, -1
        res_list = []
        c = tab.count('-')
        if c is 0:
            return 0, -1
        _list = []
        for i in range(len(tab)):
            if tab[i] == '-':
                _list.append(i)
        for i in _list:
            tab[i] = giocatore
            ret, move = self.__prosMossa(tab, next)
            res_list.append(ret)
            tab[i] = '-'
        if giocatore is 'X':
            maxele = max(res_list)
            return maxele, _list[res_list.index(maxele)]
        else:
            minele = min(res_list)
            return minele, _list[res_list.index(minele)]
    def __formatTab(self,griglia):
        stringa = ''
        for riga in griglia:
            for elem in riga:  
                if elem == '':
                    stringa += '-'
                else:
                    stringa += elem.upper()  
        return stringa          
    def __scanVittorie(self,vittorie,tempNodi,player,livello,tempLv):  #Funzione ricorsiva per vittorie_livello()  
        if tempLv == livello:
            for nodo in tempNodi:
                if nodo.tipo() == player: 
                    vittorie.append('c')     
        else:
            for nodo in tempNodi:
                self.__scanVittorie(vittorie,nodo.lista_figli,player,livello,tempLv+1) 
        
    def __tuplaEsiti(self,tupla,tempNodi):          #Funzione di supporto a Esiti()
        if tempNodi != []:
            for nodo in tempNodi:
                tipo = nodo.tipo()
                if tipo != '?':
                    if tipo == '-':
                        tupla[0]+=1
                    if tipo == 'o':    
                        tupla[1]+=1
                    if tipo == 'x':
                        tupla[2]+=1
                self.__tuplaEsiti(tupla,nodo.lista_figli)
    def __verificaOrizzontale(self,tab):             #Funzione di supporto a tipo()
        match = '-'
        for riga in tab:
            if riga[0]==riga[1] and riga[1]==riga[2] and riga[0]!='':
                match = riga[0]  
        return match
    def __verificaVerticale(self,tab):         #Funzione di supporto a tipo()
        match = '-'
        for colonna in range(3):
            if tab[0][colonna] == tab[1][colonna] and tab[1][colonna] == tab[2][colonna] and tab[0][colonna]!='':
                match = tab[0][colonna]
        return match
    def __verificaIncrociata(self,tab):         #Funzione di supporto a tipo()
        match = '-'
        if ((tab[0][0] == tab[1][1] and tab[1][1] == tab[2][2] and tab[0][0] != '') or 
            (tab[0][2] == tab[1][1] and tab[1][1] == tab[2][0] and tab[0][2] != '')):
            match = tab[1][1]
        return match
    def __verificaTerminato(self,tab):            #Funzione di supporto a tipo()
        match = '-'
        for elem in tab:
            if '' in elem:
                match = '?'
        return match
    def __verificaVittoria(self,tab):             #Funzione di supporto a tipo()
        test1 = self.__verificaOrizzontale(tab)
        test2 = self.__verificaVerticale(tab)
        test3 = self.__verificaIncrociata(tab)
        tests = [test1,test2,test3]   
        winner = '-'
        for elem in tests:
            if elem != '-':
                winner = elem
        return winner
    def __stampaPartita(self,par):              #Funzione di supporto a __str__()       
        print('#--------------------------------------#',end='')
        tempPar = copy.deepcopy(par)
        for riga in tempPar:
            if riga[0]=='':
                riga[0] = ' '
            if riga[1]=='':
                riga[1] = ' '
            if riga[2]=='':
                riga[2] = ' '
            print('\n%s %s %s'%(riga[0],riga[1],riga[2]),end='')
        
        
#End Classe
#Funzioni di supporto a gen_tree(griglia)---------------------------------------------------------------------------------------    
def cordVuote(partita):
    cordinate = []
    for riga in range(len(partita)):
        for colonna in range(len(partita[0])):
            if partita[riga][colonna] == '':
                cordinate.append((colonna,riga))   
    return cordinate
def prossimaMossa(partita):
    stringa = ''
    mossa = '-'
    indMossa = -1
    for riga in partita:
        for elem in riga:
            stringa+=elem
    numX = stringa.count('x')
    numO = stringa.count('o')     
    if numX == numO:
        mossa = 'o'
        indMossa = 0
    elif numX != numO and numX+numO!=9:
        mossa = 'x'
        indMossa = 1
    return mossa, indMossa
def generaAlb(par,diz,tempMossa):          #Fun corretta ma troppo lenta con la configurazione partita vuota (la g5 in basso)
    mosse = ['o','x']
    if par.tipo()=='?':
        cordinate = cordVuote(par.nome) 
        for cord in cordinate:
            tempPar = copy.deepcopy(par.nome)
            tempPar[cord[1]][cord[0]] = mosse[tempMossa] 
            partita = NodoTris(tempPar)  
            par.lista_figli.append(partita)
        diz[par] = par.lista_figli
        for elem in par.lista_figli:
            if tempMossa+1!=2:
                generaAlb(elem,diz,tempMossa+1)
            else:
                generaAlb(elem,diz,0)
def generaAlb2(par,diz,listaMatrici,tempMossa):            #Da testare
    mosse = ['o','x']
    if par.tipo()=='?':
        cordinate = cordVuote(par.nome) 
        for cord in cordinate:
            tempPar = copy.deepcopy(par.nome)
            tempPar[cord[1]][cord[0]] = mosse[tempMossa]
            if tempPar not in listaMatrici:
                listaMatrici.append(tempPar)
                partita = NodoTris(tempPar)  
                diz[str(tempPar)] = partita
                par.lista_figli.append(partita)
                if tempMossa+1!=2:
                    generaAlb2(partita,diz,listaMatrici,tempMossa+1)
                else:
                    generaAlb2(partita,diz,listaMatrici,0)
            else:
                par.lista_figli.append(diz[str(tempPar)])
        
#------------------------------------------------------------------------------------------------------------------------------- 
def gen_tree(griglia):      #Funzionante ma troppo lenta 
    tab = NodoTris(griglia)   
    listaNodi = []  
    lPartite = [griglia]
    dizOcc = {}
    mossa,indice = prossimaMossa(griglia)
    generaAlb2(tab,dizOcc,lPartite,indice)       
    return tab






