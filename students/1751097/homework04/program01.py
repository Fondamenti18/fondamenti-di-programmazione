'''
Diciamo che un dizionario d rappresenta un albero (e lo indichiamo come dizionario-albero)
se ciascuna chiave di d e' un identificativo di un nodo dell'albero  e l'attributo della chiave e' la lista 
(eventualmente vuota) degli identificativi dei  figli del nodo. Gli identificativi dei nodi 
all'interno delle liste sono in ordine lessicografico crescente.



Ecco un esempio di dizionario d che rappresenta un dizionario-albero

d={
'a':['b'],
'b':['c','d'],
'c':['i'],
'd':['e','l'],
'e':['f','g','h'],
'f':[],
'g':[],
'h':[],
'i':[],
'l':[]
}

L'albero rappresentato da d e'

                             'a'
                              |
                _____________'b'____________             
               |                            |            
              'c'                  ________'d'_______   
               |                  |                  |  
              'i'         _______'e'_______         'l'
                         |        |        |               
                        'f'      'g'      'h'


Implementare le seguenti funzioni:

1) 
la funzione genera_sottoalbero(fnome,x,fout) che, presi:

- il nome di un file json contenente un dizionario-albero  d (fonome)
- un identificativo x
- il nome di un file json (fout)

produce   il  dizionario-albero che rappresenta   il sottoalbero  radicato 
nell'identificativo x che si ottiene dal dizionario-albero d. 
Il dizionario-albero ottenuto va registrato nel file fout.
Se l'identificativo x non e' tra i nodi di d allora  il dizionario-albero prodotto 
deve essere vuoto.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di 
genera_sottoalbero(fname,'d',fout)
il file fout conterra' il dizionario
{'f': [], 'g': [], 'h': [], 'e': ['f', 'g', 'h'], 'l': [], 'd': ['e', 'l']}



2)
la funzione cancella_sottoalbero(fnome,x,fout) che, presi:

- il nome di un file json contenente un dizionario-albero  d (fonome)
- un identificativo x
- il nome di un file json (fout)

ricava  da d il sottoalbero radicato in x e lo salva nel file fout.
Se x non e' presente tra le chiavi di  d allora  il dizionario-albero d non viene modificato.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di 
cancella_sottoalbero(fname,'d',fout)
il file fout conterra' il dizionario
{'a': ['b'], 'b': ['c'], 'c': ['i'], 'i':[]}


3)
la funzione dizionario_livelli(fnome, fout) che, presi:
- il nome di un file json contenente un dizionario-albero  d (fonome)
- il nome di un file json (fout)

costruisce il  dizionario che ha come  chiavi i livelli del dizionario-albero d. L'attributo di una 
chiave di valore x e' la lista degli identificativi  dei nodi che si trovano a livello x  nell'albero rappresentato da d. 
La lista e' ordinata lessicograficamente ed in modo crescente. 
Il dizionario cosi' costruito va registrato nel file fout.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di  
dizionario_livelli(fname,fout)
il file fout conterra' il dizionario
{0: ['a'], 1: ['b'], 2: ['c', 'd'], 3: ['e','i','l'], 4: ['f', 'g', 'h']}

4)
la funzione dizionario_gradi_antenati(fnome,y,fout) che, presi:
- il nome di un file json contenente un dizionario-albero  d (fonome)
- un intero y
- il nome di un file json (fout)

costuisce  il dizionario che ha come chiavi gli identificativi dei nodi dell'albero 
rappresentato dal dizionario-albero d, Attributo di una chiave di valore x e' il numero 
di antenati di grado y che ha il nodo con identificativo x nell'albero.
Registra il dizionario costruito nel file fout.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di  
dizionario_gradi_antenati(fnome,2,fout)
il file fout conterra' il dizionario 
{'a': 0, 'b': 0, 'c': 1, 'd': 1, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 1, 'l': 2}

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate; non
importare moduli che non sono nella libreria standard.
'''



import json
from functools import reduce


class Node_Tree(object):
    def __init__(self, key, depth=0, father=None):
        self.key = key
        self.content = []
        self.depth = depth
        self.father = father
        

''' funzione 1'''
def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    dizionario, radice = leggi_albero(fnome)
    
    albero = generate_tree(dizionario, radice, 0, None)
    
    nodo_x = tree_filter(albero, x)
    
    out = serializza(nodo_x)
    
    scrivi_albero(out, fout)
    
    #print_Tree(albero, 0)

    
''' funzione 2'''
def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    dizionario, radice = leggi_albero(fnome)
    
    albero = generate_tree(dizionario, radice, 0, None)
    
    if albero.key == x: # voglio cancellare tutto l'albero!
        out = {}    
    else:
        nuovo_albero = elimina_rami(albero, x)
        out = serializza(nuovo_albero)
    
    scrivi_albero(out, fout)
    

''' funzione 3'''
def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    dizionario, radice = leggi_albero(fnome)
    
    albero = generate_tree(dizionario, radice, 0, None)  # chiamo la ricorsiva di lettura che mi crea i nodi gerarchici
    diz_result = estrai_livelli(albero, 0, {})    # ritorna dizionario già riempito con i nodi ai livelli.
    scrivi_albero(diz_result, fout)


''' funzione 4'''
def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    dizionario, radice = leggi_albero(fnome)
    
    albero = generate_tree(dizionario, radice, 0, None)   # chiamo la ricorsiva di lettura che mi crea i nodi gerarchici
    diz_result = antenati(albero, y, [], {})
    scrivi_albero(diz_result, fout)   
    
'''
Funzione ricorsiva di generazione struttura dei nodi (albero)
Riceve un dizionario e la voce e genra un nod
ricva i figli e ricorsivamente per ognuno di questi richiama se stessa aggiornando il nodo
alla fine della funziona torna chiaramente il nodo radice!
Parametri:
@ dizionario = tutto il dizionario passato    
@ key =  chiave del dizionario
# depth = livello di profondità della voce 
'''
def generate_tree(dizionario, key, depth, father):
    lista_figli = dizionario.get(key, None)
    node = Node_Tree(key, depth, father)
    
    for child in lista_figli:
        node.content += [generate_tree(dizionario, child, depth + 1, key)]   
    
    return node


'''Funzione che filtra un albero versione Manuel
@ root nodo di partenza
@ x = nodo da filtrare
'''
def tree_filter(root, x):
    if root == None or root.key == x: # trovato l'oggetto
        return root
    
    for child in root.content:
         node=tree_filter(child, x) # la ricorsiva mi tornerà il nodo di filtro
         if node and node.key==x: 
             return node # elemento trovato quindio esco dalla funzione
    
    
    
'''Funzione che elimina un ramo a partire da un nodo
Elimina dalla lista dei figli, il nodo incriminato
@ node = nodo di partenza
@ x = vaklore nodo da eliminare
'''
def elimina_rami(node, x):
    figli = []
    for child in node.content:
        if child.key != x:    # Buono, aggiungo lista figli.
            figli.append(child)
            elimina_rami(child, x)

    node.content = figli         # riassegno la lista aggiornata dei figli.
    return node
            
'''Funzione che restituisce un dizionario di livelli con
i nodi che vi appartengono
@ albero = nodo di partenza
@ depth = livello corrente dell albero.
@ diz_result = dizionario di ritorno.
'''
def estrai_livelli(albero, depth, diz_result):
    if depth in diz_result:       # se gia presente come chiave, aggiungo il nodo fratello alla lista.    
        diz_result[depth].append(albero.key)    # aggiungo al valore i fratelli. (lista)
        diz_result[depth] = sorted(diz_result[depth])
    else:
        diz_result[depth] = [albero.key]         # altrimenti assegno il nodo al livello.
    
    for child in albero.content:
        estrai_livelli(child, depth + 1, diz_result)
    
        
    return diz_result
    
''' Funzione ricorsiva che restituisceun dizionario dove a ogni
elemento associa il numero di antenati di grado y (quelli che hanno y figli)
@ albero = nodo di partenza
@ y = numero figli degli antenati.
@ gradi = accumolatore o lista del numero di figli degli antenati del nodo che sto esaminando.
@ diz_result = dizionario di ritorno.
'''
def antenati(albero, y, gradi, diz_result):
    diz_result[albero.key] = len([x for x in gradi if x == y])   # prendo solo gli elementi che hanno grado y.
                                                                 # ad esempio se ho y == 2 e gradi uguale a [1,2,1]. restituisce un solo antenato di grado due. 
    for child in albero.content:
        antenati(child, y, gradi + [len(albero.content)], diz_result)   # chiamo la ricorsiva passandole la losta dei gradi degli antentati aggiornata.

    return diz_result


'''Leggo il file JSON e ritorna un dizionario
@ filename = file JSON in input
'''
def leggi_albero(filename):
    with open(filename, encoding='utf8') as f:
       dizionario = json.load(f)

    # ricavo la radice!!!
    # seguo il seguente criterio
    # dal dizionario ricavo la lista delle chiavi
    # dal dizionario ricavo la lista di tutti i valori
    # faccio la differenza di questi 2 set e trovo la radice 
    lista_chiavi=list(dizionario)
    lista_singoli_valori = [item for sublist in dizionario.values() for item in sublist]
    radice = (set(lista_chiavi) - set(lista_singoli_valori)).pop()

    return dizionario, radice


'''Scrivo il file JSON da un  dizionario
@ fout = file JSON in output
@ out = dizionario da scrivere
'''
def scrivi_albero(out, fout):
    with open(fout, mode = "w", encoding='utf8') as f:
        json.dump(out, f)


'''Funzione di serializzazione da albero a dizionario
@ node = radice di partenza
'''
def serializza(node):
    if node == None:
       return {}
    dizionario = {}   
    #dizionario[node.key] = sorted([child.key for child in node.content])  # assegno la lista ORDINATA dei suoi figli alla voce del dizionario.
    dizionario[node.key] = [child.key for child in node.content]  # assegno la lista ORDINATA dei suoi figli alla voce del dizionario.
    for child in node.content:
        dizionario.update(serializza(child))
    return dizionario

'''Funzione di stampa labero
@ node = nodo di partenza
@ livello = indentazione
'''
def print_Tree(node, livello=0):
    print('  '*livello + node.key, node.father)
    lista_figli = node.content
    for child in lista_figli:     
        print_Tree(child, livello+1)
    


if __name__ == '__main__':
    #args        = ('Alb10.json','d','tAlb10_1.json')
    #args        = ('Alb100.json','ultras','tAlb100_1.json')
    #args       = ('Alb20000.json','felici','tAlb20000_1.json')
    args       = ('Alb50000.json','anglofobo','tAlb50000_1.json')
    genera_sottoalbero(*args)
    
    
    args = ('Alb10.json','d','tAlb10_2.json')
    #args        = ('Alb100.json','ultras','tAlb100_2.json')
    args       = ('Alb20000.json','felici','tAlb20000_2.json')
    cancella_sottoalbero(*args)

    args        = ('Alb10.json','tAlb10_3.json')
    #args        = ('Alb100.json','tAlb100_3.json')
    args       = ('Alb20000.json','tAlb20000_3.json')
    dizionario_livelli(*args)
    
    args        = ('Alb10.json',2,'tAlb10_4.json')
    #args        = ('Alb100.json',2,'tAlb100_4.json')
    args       = ('Alb20000.json',2,'tAlb20000_4.json')
    dizionario_gradi_antenati(*args)
    