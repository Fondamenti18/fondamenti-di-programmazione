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

{'a': 0, 'b': 0, 'c': 1, 'd': 1, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 1, 'l': 2}



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

def ricorsione_sotto(diz,key,outdiz):
    outdiz[key]=diz[key]
    for value in diz[key]:
        if diz[value]==[]:
            outdiz[value]=[]
        else:
            ricorsione_sotto(diz,value,outdiz)
    return outdiz

def genera_sottoalbero(fnome,x,fout):
    filea=open(fnome)
    file=json.load(filea)
    filea.close()
    if x in file:
        appoggio={}
        output=ricorsione_sotto(file,x,appoggio)
    else:
        output={}
    foutput=open(fout,"w")
    json.dump(output,foutput)
    foutput.close
    
def cancella_sottoalbero(fnome,x,fout):
    filea=open(fnome)
    file=json.load(filea)
    filea.close()
    output={}
    if x not in file:
        output=file
    else:
        appoggio1={}
        appoggio=ricorsione_sotto(file,x,appoggio1)
        listacanc=set(appoggio.keys())
        listaout=set(file.keys())
        listaout.difference_update(listacanc)
        for el in listaout:
            app=[]
            for ele in file[el]:
                if ele not in listacanc:
                    app.append(ele)    
            output[el]=app
        
    foutput=open(fout,"w")
    json.dump(output,foutput)
    foutput.close    

def trovaradice(dizi):
    keys=dizi.keys()
    items=dizi.items()
    flag=0
    for key in keys:
        for item in items:
            if key in item[1]:
                break
        else:
            flag=1
        
        if flag==1:
            possiblekey=key
            break
            
    return possiblekey  

def livelli(diz,key,cont,out):
    if cont not in out:
        out[cont]=[key]
    else:
        out[cont].append(key)
        out[cont].sort()
    if diz[key]!=[]:
        for items in diz[key]:
            livelli(diz,items,cont+1,out)
    return out

def dizionario_livelli(fnome,fout):
    filea=open(fnome)
    file=json.load(filea)
    filea.close()
    
    radice=trovaradice(file)
    out={}
    output=livelli(file,radice,0,out)
    
    foutput=open(fout,"w")
    json.dump(output,foutput)
    foutput.close

def antenati(diz,key,antenaticount,out,grado):
    
    out[key]=antenaticount
    
    if figli(diz[key])==grado:
        antenaticount+=1
        
    if diz[key]!=[]:
        for items in diz[key]:
            antenati(diz,items,antenaticount,out,grado)
    else:
        out[key]=antenaticount
    return out

def figli(lista):
    return len(lista)

def dizionario_gradi_antenati(fnome,y,fout):
    filea=open(fnome)
    file=json.load(filea)
    filea.close()
    radice=trovaradice(file)
    appoggio={}
    output=antenati(file,radice,0,appoggio,y)


    foutput=open(fout,"w")
    json.dump(output,foutput)
    foutput.close








