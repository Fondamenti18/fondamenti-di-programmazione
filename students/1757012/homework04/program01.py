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



def trovasottoalbero(albero, valore):
    dic={}
    a=0
    try:
        a=albero[valore]
    except:
        pass
    if a==0:
        return {}
    if a==[]:
        return {valore: a}
    else:
        dic[valore]=a
        for w in a:
            valore=w
            z=trovasottoalbero(albero, valore)
            dic.update(z)
        return dic





def genera_sottoalbero(fnome,x,fout):
    b=open(fnome,'r')
    dicout={}
    with b:
        a=json.load(b)
    dicout=trovasottoalbero(a,x)
    w=open(fout,'w')
    with w:
        jeson=json.dumps(dicout)
        w.writelines(jeson)
    
        
    
        
    

def cancella_sottoalbero(fnome,x,fout):
    dictout={}
    b=open(fnome,'r')
    with b:
        a=json.load(b)
    alberodacancellare=trovasottoalbero(a,x)
    dictout=a
    for key in alberodacancellare:
        dictout.pop(key)
    for q in dictout:
        for z in dictout[q]:
            if z==x:
                dictout[q].remove(z)
    w=open(fout,'w')
    with w:
        jeson=json.dumps(dictout)
        w.writelines(jeson)
    
    



def livelliricorsivi(dizionario,radice,dizionarioout,contatore=0):
    radiceswap=radice
    dizionarioout2=dizionarioout
    if contatore in dizionarioout2: 
        dizionarioout2[contatore].append(radiceswap)
    else:
        dizionarioout2[contatore]=[radiceswap]
    if dizionario[radiceswap]==[]:
        return dizionarioout2
    if dizionario[radiceswap]!=0:
        for figli in dizionario[radiceswap]:
            dizionarioout2.update(livelliricorsivi(dizionario,figli,dizionarioout2,contatore=contatore+1))
    return dizionarioout2


def dizionario_livelli(fnome,fout):
    dictout={}
    file=open(fnome,'r')
    with file:
        a=json.load(file)
    for key in a:
        root=key
        break
    dictout=livelliricorsivi(a,root,dictout)
    for key in dictout:
        dictout[key].sort()
    file=open(fout,'w')
    with file:
        jeson=json.dumps(dictout)
        file.writelines(jeson)
    
    
    
    
    
 

def dizionario_gradi_antenati(fnome,y,fout):
    dizout={}
    file=open(fnome,'r')
    with file:
        a=json.load(file)

    for b in a:
        root=b
        break
    funzionelivelli(a,root,dizout,y)
    file=open(fout,'w')
    with file:
        jeson=json.dumps(dizout)
        file.writelines(jeson)
    
    
    
    
def funzionelivelli(dizionario,radice,dizionarioout,grado,livello=0):
    contatore=livello
    dizionarioout.update({radice:contatore})
    listafigli=dizionario[radice]
    if len(listafigli)==grado:
        contatore=contatore+1
    if listafigli!=[]:
        for c in range(0,len(listafigli)):
            funzionelivelli(dizionario,listafigli[c],dizionarioout, grado, livello=contatore)
    if len(listafigli)==[]:
        return dizionarioout
        
        
