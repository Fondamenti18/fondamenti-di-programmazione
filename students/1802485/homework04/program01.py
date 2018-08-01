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



#PRIMA FUNZIONE
def genera_sottoalbero(fnome,x,fout):
    albero=json.load(open(fnome))
    dizionario=sottoalbero(albero,x,dizionario={})
    f=open(fout,'w')
    json.dump(dizionario, f)
    f.close()
    

      
def sottoalbero(albero,x,dizionario={}):
   if x not in albero: return {}
   else:
        dizionario[x]=albero[x]
        for i in albero[x]:
            if i in albero:
                dizionario[i]=albero[i]
                dizionario[i]=sorted(dizionario[i])
                dizionario=sottoalbero(albero,i,dizionario)
   return dizionario

 
    
#SECONDA FUNZIONE
def cancella_sottoalbero(fnome,x,fout):
    albero=json.load(open(fnome))
    dizionario=sottoalbero2(albero,x,dizionario={})
    albero=funzione_ricorsiva_a_parte(albero,x,dizionario)
    f=open(fout,'w')
    json.dump(albero, f)
    f.close()
    

      
def sottoalbero2(albero,x,dizionario={}):
    if x not in albero: return {}
    else:
         dizionario[x]=albero[x]
         for i in albero[x]:
             if i in albero:
                 dizionario[i]=albero[i]
                 dizionario[i]=sorted(dizionario[i])
                 dizionario=sottoalbero2(albero,i,dizionario)
    
    return dizionario



def funzione_ricorsiva_a_parte(albero,x,dizionario):
    if x not in albero and x not in dizionario: return albero
    if x in albero and x in dizionario:
        albero.pop(x)
    if x in dizionario and x not in albero:
        for i in dizionario[x]:
            if i in albero and i in dizionario:
                albero.pop(i)
                albero=funzione_ricorsiva_a_parte(albero,i,dizionario)
    for j in albero:
        for n in albero[j]:
            if n==x:
                albero[j].remove(n)
    return albero


#TERZA FUNZIONE
def dizionario_livelli(fnome,fout):
    a=json.load(open(fnome))
    livelli=riccy(a,nodo_radice(a,lista_chiavi=[],lista_valori=[],dizionario={}),{},0)
    f=open(fout,'w')
    json.dump(livelli, f)
    f.close()


def nodo_radice(a,lista_chiavi=[],lista_valori=[],dizionario={}):
    for chiave in a:
        lista_chiavi+=[chiave]
        for valori in a[chiave]:
            lista_valori+=[valori]
            if chiave in lista_chiavi and chiave not in lista_valori:
                return chiave
   


def riccy(a, nodo, dizionario, n=0):
    if n in dizionario.keys():
        dizionario[n].append(nodo)
    else:
        dizionario[n]=[nodo]
    if a[nodo]==[]: return dizionario
    else:
        for i in a[nodo]:
            dizionario=riccy(a,i,dizionario,n+1)
            dizionario[n]=sorted(dizionario[n])
            dizionario[n+1]=sorted(dizionario[n+1])
    return dizionario



#QUARTA FUNZIONE
def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
