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



def genera_sottoalbero(fnome,x,fout):
    out={}
    with open(fnome) as ins:
        dic=json.load(ins)
        
    
    out=generasottoalbero(dic,x)
     
    with open(fout, 'w') as fp:
        json.dump(out, fp)
  
           
def cancella_sottoalbero(fnome,x,fout):
    out={}
    OUT={}
    with open(fnome) as ins:
        dic=json.load(ins)
    
    radice=list(dic.keys())[0]
    
    if x in dic:
        del dic[x]
    
    
    out=generasottoalbero(dic,radice)
    
    
    for nodo in out:
        if x in out[nodo]:
            n=[]
            for el in out[nodo]:
                if el != x:
                    n+=[el]
            out[nodo] = n
            
    
    for f in range(len(list(out.keys()))-1,-1,-1):
        OUT[list(out.keys())[f]] = out[list(out.keys())[f]] 
            
    with open(fout, 'w') as fp:
        json.dump(OUT, fp)
            
    

def generasottoalbero(dic,x):
    out={}

    try:
        for foglia in dic[x]:
            
            out.update(generasottoalbero(dic,foglia))
    
        if dic[x] == []:
            out[x] = []
            
        out[x] = dic[x]
    
    except KeyError:
        return out
            
    return out

def dizionario_livelli(fnome,fout):
    out={}
    OUT={}
    n=[]
    i = 0
    with open(fnome) as ins:
        dic=json.load(ins)
        radice = list(dic.keys())[0]
        
        out[0] = [radice]
        
        insi=profondita(dic,radice,i)
        
        
        
        insi=str(insi)
        
        for x in '(),\'':
            insi=insi.replace(x,'')
        
        
        
        
        for i in range(0,(len(insi))):
           
            insieme=''
            t=()
            if insi[i] in '1234567890' and insi[i-1] == ' ':
                if insi[i+1] in '1234567890':
                    x= insi[i]+insi[i+1]
                    for el in range(i+3,(len(insi))):
                        if insi[el] not in '1234567890':
                            nodo=insi[el]
                        else:
                            break
                        insieme+=nodo
                else:
                    x=insi[i]
                    
                    for el in range(i+2,(len(insi))):
                        
                        
                        if (i+2 == len(insi)-1):
                            
                            nodo = insi[-1]
                        
                        elif insi[el] not in '1234567890':
                            nodo=insi[el]
                        else:
                            break
                        
                        insieme+=nodo
            else:
                if i == 0:
                    x = insi[0]
                    for el in range(i+2,len(insi)):
                        if insi[el] not in '1234567890':
                            nodo = insi[el]
                        else:
                            break
                        insieme+=nodo
                        
                      
            if insieme != '':
                t=(x,insieme)
                n+=[t]
            
            

        
        
        for x in range(0,len(n)):
            var = n[x]
            N = int(var[0])
            
            
            
            if var[1] == ' ':
                continue
            if N not in out:
                
                
                lista = crealista(var[1])
                out[N] = lista
                
            else:
                lista = crealista(var[1])
                out[N] = out[N] + lista
    
    
    
    for chiave, valore in sorted(out.items()):
        
        OUT[chiave] = valore
    
    
    
        
    for x in OUT:
        lista=OUT[x]
        lista= ordina(lista)
        OUT[x] = lista
        
    
    
    
    with open(fout, 'w') as fp:
        json.dump(OUT, fp)
        
   
        
def dizionario_gradi_antenati(fnome,y,fout):
    a=[]
    out={}
    c=0
    with open(fnome) as ins:
        dic=json.load(ins)
    with open(fnome) as ins:
        Odic=json.load(ins)
    
    radice=list(Odic.keys())[0]
    
    out[radice] = 0    
       
    for nodo in dic:
            
        out[nodo] = c
        
        
        
    del dic[list(dic.keys())[0]]


    out.update(gradi_antenati(dic,y,out,Odic,radice))
        
    with open(fout, 'w') as fp:
        json.dump(out, fp)    


def gradi_antenati(dic,y,out,Odic,radice):
    Ndic={}
    
    if len(dic) == 0:
        return out
    
    work = list(dic.keys())[0]
    
    for nodo in list(dic.keys())[1:]:
        Ndic[nodo] = dic[nodo]
    
    dicCont={}
    
    dicCont=genera_albero_percorso(work,Odic,radice,dicCont)
    
    for check in dicCont:
        if len(dicCont[check]) == y:
            out[work]= (out[work]+1)
    
    
    
    
    out.update(gradi_antenati(Ndic,y,out,Odic,radice))
    
    
    
    return out

        
def genera_albero_percorso(work,Odic,radice,dicCont):
    
    if work == radice:
        return dicCont
    
    for elemento in Odic:
        n=[]
        if work in Odic[elemento]:
            dicCont[elemento] = Odic[elemento]
            work=elemento
        
    dicCont.update(genera_albero_percorso(work,Odic,radice,dicCont))           
    return dicCont           
        

    
def ordina(lista):
    return sorted(lista)

def profondita(dic,nodo,i):
    out=[]
    regi=set()
    n=[]
    i+=1
    for foglia in dic[nodo]:
        regi.add(profondita(dic,foglia,i))
        n+=[foglia]
     
    n = tuple(n)
    a = (i,n)
    regi.add(a)
    regi=tuple(regi)
    
    return regi

def crealista(stringa):
    lista=[]
    elemento=''
    
    if len(stringa) == 1:
        lista=[stringa]
        return lista
    for c,i in enumerate(stringa):
        
        
        
        if i == ' ':
            
            if elemento not in lista:
                lista+=[elemento]
                elemento=''
            
        else:
            elemento += i
            
            if c == (len(stringa)-1):
                if elemento not in lista:
                    lista+=[elemento]
    
    if len(elemento) == len(stringa):
        if elemento not in lista:
            lista+=[elemento]
            return lista
    
    
    return lista
            
def dizionariolivelli(fnome):
    out={}
    OUT={}
    n=[]
    i = 0
    with open(fnome) as ins:
        dic=json.load(ins)
        radice = list(dic.keys())[0]
        
        out[0] = [radice]
        
        insi=profondita(dic,radice,i)
        
        
        
        insi=str(insi)
        
        for x in '(),\'':
            insi=insi.replace(x,'')
        
        
        
        
        for i in range(0,(len(insi))):
           
            insieme=''
            t=()
            if insi[i] in '1234567890' and insi[i-1] == ' ':
                if insi[i+1] in '1234567890':
                    x= insi[i]+insi[i+1]
                    for el in range(i+3,(len(insi))):
                        if insi[el] not in '1234567890':
                            nodo=insi[el]
                        else:
                            break
                        insieme+=nodo
                else:
                    x=insi[i]
                    
                    for el in range(i+2,(len(insi))):
                        
                        
                        if (i+2 == len(insi)-1):
                            
                            nodo = insi[-1]
                        
                        elif insi[el] not in '1234567890':
                            nodo=insi[el]
                        else:
                            break
                        
                        insieme+=nodo
            else:
                if i == 0:
                    x = insi[0]
                    for el in range(i+2,len(insi)):
                        if insi[el] not in '1234567890':
                            nodo = insi[el]
                        else:
                            break
                        insieme+=nodo
                        
                      
            if insieme != '':
                t=(x,insieme)
                n+=[t]
            
            

        
        
        for x in range(0,len(n)):
            var = n[x]
            N = int(var[0])
            
            if var[1] == ' ':
                continue
            if N not in out:
                
                
                
                lista = crealista(var[1])
                out[N] = lista
                
            else:
                lista = crealista(var[1])
                out[N] = out[N] + lista
    

    for chiave, valore in sorted(out.items()):
        
        OUT[chiave] = valore
    
    

        
    for x in OUT:
        lista=OUT[x]
        lista= ordina(lista)
        OUT[x] = lista
        
    
    return OUT