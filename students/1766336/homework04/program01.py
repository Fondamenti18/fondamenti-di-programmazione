import json
import collections
class Nodo:
    def __init__ (self, nome):
        self.nome = nome
        self.figli = []
    def addfiglio (self, figlio):
        self.figli.append(figlio)
        """self.figli.sort()"""
    def getnomifigli (self):
        nomifigli=[]
        for figlio in self.figli:
            nomifigli.append(figlio.nome)
        return nomifigli


def genera_sottoalbero(fnome, x, fout):
    with open(fnome) as f:     
        dizionariojson = json.load(f)
    nodoalpha = True
    nodoradice = Nodo('')
    radicealbero = Nodo('')
    for key in dizionariojson:
        newnodo = Nodo(key)
        if key == x:
            nodoradice = newnodo
        if nodoalpha:
            radicealbero = newnodo
            nodoalpha = False
        addNodo(radicealbero, newnodo, dizionariojson)

    sottodizionario = {}
    newdizionario = {}
    sottodizionario = creasottoalbero (nodoradice, newdizionario)
    newdizionarioo = collections.OrderedDict(sorted(newdizionario.items(), key=lambda t: t[0]))
    with open(fout, 'w') as outfile:  
        json.dump(newdizionarioo, outfile)


def addNodo (radicealbero, newnodo, dizionariojson):
    if newnodo.nome in dizionariojson[radicealbero.nome]:
        radicealbero.addfiglio(newnodo)
        return
    indice = 0
    nfigli = len(radicealbero.figli)
    while indice < nfigli:
        addNodo(radicealbero.figli[indice], newnodo, dizionariojson)
        indice += 1


def creasottoalbero (nodoradice, newdizionario):
    numfigli = len(nodoradice.figli)
    nomifigli=[]
    for figlio in nodoradice.figli:
        nomifigli.append(figlio.nome)
    nomifigli.sort()
    newdizionario[nodoradice.nome] = nomifigli
    indice = 0
    if numfigli != 0:
        while indice < numfigli:
            newdizionario = creasottoalbero(nodoradice.figli[indice], newdizionario)
            indice += 1
    return newdizionario

    

def cancella_sottoalbero(fnome, x, fout):
    with open(fnome) as f:     
        dizionariojson = json.load(f)
    nodoalpha = True
    nodoradice = Nodo('')
    radicealbero = Nodo('')
    for key in dizionariojson:
        newnodo = Nodo(key)
        if key == x:
            nodoradice = newnodo
        if nodoalpha:
            radicealbero = newnodo
            nodoalpha = False
        addNodo(radicealbero, newnodo, dizionariojson)

    newdizionario = {}
    creasottoalbero (nodoradice, newdizionario)
    ciao = dizionariojson
    for key in list(dizionariojson):
        if key in newdizionario:
            ciao.pop(key, None)
    for key in dizionariojson:
        for value in dizionariojson[key]:
            if value in newdizionario:
                ciao[key].remove(value)
    with open(fout, 'w') as outfile:
        json.dump(ciao, outfile)


def dizionario_livelli(fnome, fout):
    with open(fnome) as f:     
        dizionariojson = json.load(f)
    nodoalpha = True
    radicealbero = Nodo('')
    for key in dizionariojson:
        newnodo = Nodo(key)
        if nodoalpha:
            radicealbero = newnodo
            nodoalpha = False
        addNodo(radicealbero, newnodo, dizionariojson)

    jdizionario = {}
    for key in dizionariojson:
        livello = calcolalivello(radicealbero, key)
        lista = []
        if livello in jdizionario:
            lista = jdizionario[livello]
        lista.append(key)
        lista.sort()
        jdizionario[livello] = lista
    with open(fout, 'w') as outfile:
        json.dump(jdizionario, outfile)


def calcolalivello(radicealbero, key):
    return calcola_livello(radicealbero, key, 0)
    
def calcola_livello(radicealbero, key, livellocorrente):
    livellorisultato = -1
    if radicealbero.nome == key:
        livellorisultato = livellocorrente
    else:
        for figlio in radicealbero.figli:
            livellorisultato = calcola_livello(figlio, key, livellocorrente +1)
            if livellorisultato != -1:
                break
    return livellorisultato

def dizionario_gradi_antenati(fnome,y,fout):
    with open(fnome) as f:     
        dizionariojson = json.load(f)
    nodoalpha = True
    radicealbero = Nodo('')
    for key in dizionariojson:
        newnodo = Nodo(key)
        if nodoalpha:
            radicealbero = newnodo
            nodoalpha = False
        addNodo(radicealbero, newnodo, dizionariojson)

    listaantenati = {}
    for key in dizionariojson:
        nodiantenati=[]
        ris = contaantenati(radicealbero, key, nodiantenati)
        conta = 0
        if ris == True:
            for nodo in nodiantenati:
                if len(dizionariojson[nodo]) == y:
                    conta += 1
        listaantenati[key] = conta
    with open(fout, 'w') as outfile:  
        json.dump(listaantenati, outfile)


def contaantenati(radicealbero, key, nodiantenati):
        if radicealbero.nome == key:
            return True
        indice = 0
        risultato = False
        size = len(radicealbero.figli)
        while indice < size:
            risultato |= contaantenati(radicealbero.figli[indice], key, nodiantenati)
            indice += 1
        if risultato == True:
            nodiantenati.append(radicealbero.nome)
            return True
        return False

"""genera_sottoalbero('Alb100.json', 'ultras', 'ciao.json')"""



                    
     

