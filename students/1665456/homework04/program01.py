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
                                  |
                                 'i'


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
La lista è ordinata lessicograficamente ed in modo crescente. 
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

def estrainodi(nodi,father,son):
    if type(nodi)!=list:
        nodi=[nodi] 
    for nodo in nodi:
        if nodo in father.keys():
            son[nodo] = father[nodo]
            if len(son[nodo])!=0:
                estrainodi(son[nodo], father, son)
        else:
            son[nodo] = []

def crealivelli(Dizio,Livelli):
	#Purtroppo essendo il dizionario un tipo mappato e non ordinato,
	#Per il corretto funzionamento del programma, e' richiesta l'importazione
        #di un modulo esterno, che definisce una speciale classe dizionario che preserva
        #l'ordine del dizionario di origine (tale dizionario non si auto-ordina, quindi
        # perde informazioni inerente all'ordine di inserimento di dati nel dizionario)
        #https://docs.python.org/3/library/collections.html#collections.OrderedDict

        #Una volta importato il modulo, i dizionari passati come argomento alla seguente funzione
        #Dovranno prima essere dichiarati come OrderedDict, ed inizializzati secondo le regole
        #dettate dal costruttore della suddetta classe
        
    it = iter(Dizio) #python3
    i=0
    Livelli[i] = [next(it)] #python3
    #La riga immediatamente sovrastante "Livelli[i] = [next(it)]"
    #Serve ad identificare la radice dell'albero
    #(nel caso in cui il dizionario non si auto-ordini, quindi mantenga l'ordine originale)
    #Facendo cio (vedi sotto "for key in Livelli[i-1]"),
    #e' possibile l'analisi dell'intero albero spostandosi da padre a figlio

    while 1:
        i=i+1
        if Livelli.has_key(i-1) and Livelli[i-1] != []:
            Livelli[i-1].sort()
            Livelli[i] = []
            for key in Livelli[i-1]:
                if key in Dizio.keys():
                    #print(D[Livelli[i-1]])
                    for val in Dizio[key]:
                        Livelli[i].append(val)   
        else:
            break
    Livelli.pop(len(Livelli)-1)
                
def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    
    f=open(fnome,'r')
    t=f.read()
    D=json.loads(t)
    SottoD={}
    estrainodi(x, D, SottoD) 
    with open(fout, 'w') as f:
        json.dump(SottoD, f, ensure_ascii=False)
    #print("this is the final Genera", SottoD)
        

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    f=open(fnome,'r')
    t=f.read()
    D=json.loads(t)
    SottoD={}
    estrainodi(x, D, SottoD)
    DeletedTree = {k:v for k,v in D.items() if k not in SottoD}
    #print("this is the deleted alb", DeletedTree) 
    #print(D.items())
    #print(SottoD.items())
    #print(SottoD.keys())
    
    for x in DeletedTree:
        Lista = [] 
        if len(DeletedTree[x]) >= 1:
            for v in DeletedTree[x]:
                if v not in SottoD.keys():
                    Lista.append(v)
            DeletedTree[x] = Lista
        #print("lista",Lista)
    with open(fout, 'w') as f:
        json.dump(DeletedTree, f, ensure_ascii=False)
    #print(DeletedTree)

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    f=open(fnome,'r')
    t=f.read()
    D=json.loads(t)
    Livelli = {}
    
    crealivelli(D,Livelli)
    with open(fout, 'w') as f:
        json.dump(Livelli, f, ensure_ascii=False)
    #print(Livelli)
 

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    f=open(fnome,'r')
    t=f.read()
    D=json.loads(t)
    Livelli = {}
    Antenati = {}
    flg = 0

    crealivelli(D,Livelli)
    
    for x in D.keys():
        #print("this is x ",x)
        flg=0
        for values in Livelli.values():
            if flg==1:
                break
            #print("This is values =",values)
            if type(values)==list:
                for value in values:
                    #print(value)
                    #print("passing")
                    if value == x:
                        index = Livelli.values().index(values)
                        #print("This is index = ",index)
                        #print("\n")
                        LivIndex = index-y
                        if LivIndex>=0:
                            Antenati[x]=len(Livelli[LivIndex])
                        else:
                            Antenati[x]=0
                        flg=1
                        break
    
    with open(fout, 'w') as f:
        json.dump(Antenati, f, ensure_ascii=False)
    #print(Antenati)
    #In caso di risultato errato vedere la spiegazione
    #nella definizione di "crealivelli(Dizio,Livelli)"
        
    
#genera_sottoalbero('Alb10.json','d','tAlb10_1.json')
#cancella_sottoalbero('Alb10.json','d','tAlb10_2.json')
#dizionario_livelli('Alb10.json','tAlb10_1.json')
#genera_sottoalbero('Alb100.json','ultras','tAlb100_1.json')
#cancella_sottoalbero('Alb100.json','ultras','tAlb100_2.json')
#genera_sottoalbero('Alb20000.json','felici','tAlb20000_1.json')
#cancella_sottoalbero('Alb20000.json','felici','tAlb20000_2.json')
#dizionario_gradi_antenati('Alb10.json',2,'tAlb10_4.json')
#dizionario_gradi_antenati('Alb100.json',2,'risAlb100_4.json')
#dizionario_livelli('Alb100.json','tAlb100_1.json')
