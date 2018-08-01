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

from json import load, dump

def apri_json(fnome):
    '''Restituisce il contenuto del file json sottoforma di dizionario'''   
    with open(fnome) as f1:
        return load(f1)

def genera_sottoalbero(fnome,x,fout):
    '''Produce il  dizionario-albero che rappresenta il sottoalbero  radicato nell'identificativo x che si ottiene dal dizionario-albero d. Il dizionario-albero ottenuto va registrato nel file fout. Se l'identificativo x non e' tra i nodi di d allora  il dizionario-albero prodotto deve essere vuoto.'''
    #si apre il file ricevendo il dizionario diz
    diz=apri_json(fnome) 
    nuovoDiz={}
    
    #si salva il dizionario (generato dalla funzione ricorsiva genera_ricors) nella destinazione richiesta
    with open(fout, 'w') as f1out:
        f1out = dump(genera_ricors(diz, x, nuovoDiz), f1out)
    

def genera_ricors(diz, x, nuovoDiz):
    '''Funzione ricorsiva della funzione genera_sottoalbero:
    A partire da un dizionario diz, restituisce il sotto-dizionario nuovoDiz la cui radice è l'identificativo x attraverso una ricorsione.'''
    
    if x in diz.keys():
        nuovoDiz[x]=diz[x] #crea nel nuovoDiz il nodo corrispondente all'identificativo sottoforma di chiave-attributo del vecchio
        for subNodo in diz[x]: #scorre la lista-attributo del nodo appena aggiunto nel dizionario vecchio e riesegue la procedura con i nuovi identificativi
            genera_ricors(diz, subNodo, nuovoDiz)
        return nuovoDiz
    
    #in caso l'identificativo non sia nel dizionario, significa che si è arrivati alla fine della ricerca
    else:
        return nuovoDiz

'''-------------------------------------------------------------------------'''

def cancella_sottoalbero(fnome,x,fout):
    '''Ricava da d il sottoalbero radicato in x e lo salva nel file fout. Se x non e' presente tra le chiavi di  d allora  il dizionario-albero d non viene modificato.'''
    diz=apri_json(fnome) #si apre il file ricevendo il dizionario diz
    
    nuovoDiz=dict(diz) #si copia il dizionario per lavorarci
    nuovoDiz=cancella_ricors(diz, x, nuovoDiz) #si crea il nuovo dizionario
    
    #poiché nel padre del nodo con identificativo x è contenuto ancora x, si procede all'eliminazione
    '''MIGLIORARE'''
    for lista in nuovoDiz.values():
        for nodo in lista:
            if nodo==x:
                lista.remove(nodo)
    
    #si salva il dizionario (generato dalla funzione ricorsiva cancella_ricors) nella destinazione richiesta
    with open(fout, 'w') as f2out:
        f2out = dump(nuovoDiz, f2out)
    
def cancella_ricors(diz, x, nuovoDiz):
    '''Funzione ricorsiva della cancella_sottoalbero:
    A partire da un dizionario diz, restituisce il sotto-dizionario nuovoDiz dopo aver eliminato la parte la cui radice è l'identificativo x, attraverso una ricorsione.'''
    
    if x in diz.keys():
        del nuovoDiz[x] #elimina l'elemento corrisponde all'identificativo nel nuovoDiz
        for sub_el in diz[x]: #scorre la lista-attributo del nodo eliminato e riesegue la funzione con i nuovi identificativi
            cancella_ricors(diz, sub_el, nuovoDiz)
        return nuovoDiz
    
    #in caso l'identificativo non sia nel dizionario, significa che si è arrivati alla fine della ricerca
    else:
        return nuovoDiz

'''-------------------------------------------------------------------------'''

def dizionario_livelli(fnome,fout):
    '''Costruisce il  dizionario che ha come  chiavi i livelli del dizionario-albero d. L'attributo di una chiave di valore x e' la lista degli identificativi  dei nodi che si trovano a livello x  nell'albero rappresentato da d. La lista e' ordinata lessicograficamente ed in modo crescente. Il dizionario cosi' costruito va registrato nel file fout.'''
    #si apre il file ricevendo il dizionario diz
    diz=apri_json(fnome)
    
    #si dichiara il dizionario richiesto
    dizLivelli={}
    radice=trova_radice(diz)    
    livello=0
    #si crea la prima chiave-lista del livello 1
    dizLivelli[livello]=[radice]
    
    #si esegue la funzione ricorsiva
    dizLivelli=livelli_ricors(diz, dizLivelli, radice, livello)
    
    #per ogni lista-attributo, riordino gli elementi in maniera lessicografica
    for lista in dizLivelli.values():
        lista.sort()
    
    #salvo il dizionario così ottenuto nella destinazione richiesta
    with open(fout, 'w') as f3out:
        f3out = dump(dizLivelli, f3out)
    
def trova_radice(diz):
    '''Dato un dizionario-albero in input, ritorna la sua radice sottoforma di stringa.'''
    
    insiemeNodi=set()
    for listAtt in diz.values():
        for el in listAtt:
            insiemeNodi.add(el)
    radice = set(diz.keys()) - insiemeNodi
    
    return ''.join(radice)
    
def livelli_ricors(diz, dizLivelli, chiave, livello):
    '''Funzione ricorsiva della dizionario_livelli:
    Dato il dizionario diz, costruisce il dizLivelli che ha come chiavi i livelli dell'albero e come attributi i nodi di quel livello. #chiave alla prima esecuzione è uguale a chiave0, alle successive ricorsioni sarà i nodi scorsi con il for. '''
    
    livello+=1 #si incrementa il livello ad ogni ricorsione (quelle parallele non si confondono)
    
    for nodo in diz[chiave]: #per ogni nodo corrispondente alla chiave
        #verifico se per quel livello ho già creato una chiave uguale al nodo
        if livello in dizLivelli.keys(): #se il livello c'è già, bisogna aggiungere il nuovo nodo alla lista-attributo corrispondente
            dizLivelli[livello].append(nodo)
        else: #significa che la chiave con il livello corrispondente va creata, così come la lista-attributo corrispondente
            dizLivelli[livello]=[nodo]
        
        #si procede alla ricorsione
        livelli_ricors(diz, dizLivelli, nodo, livello)
            
    return dizLivelli

'''-------------------------------------------------------------------------'''

def dizionario_gradi_antenati(fnome,y,fout):
    '''Costruisce  il dizionario che ha come chiavi gli identificativi dei nodi dell'albero rappresentato dal dizionario-albero d, Attributo di una chiave di valore x e' il numero di antenati di grado y che ha il nodo con identificativo x nell'albero. Registra il dizionario costruito nel file fout.'''
    #Si apre il file ricevendo il dizionario diz
    diz=apri_json(fnome)
    
    #Si crea un insieme in cui sono presenti i nodi che hanno grado y (ovvero y figli)
    nodiGradoY = set()
    for nodo in diz.keys():
        if len(diz[nodo]) == y:
            nodiGradoY.add(nodo)
    #Si crea il dizionario inverso: invece che {padre: [figli]}, per ogni figlio {figlio : padre}
    reverseDiz = inverti_diz(diz)
    
    #Si scorrono tutti i nodi del dizionario in input e si aggiunge ognuno nel dizFinale, con attributo uguale al numero di antenati di grado y che la funzione antenati_ricors restituisce.
    dizFinale = {trova_radice(diz) : 0}
    for chiave in reverseDiz.keys():
        dizFinale[chiave] = antenati_ricors(chiave, reverseDiz, dizFinale, nodiGradoY, 0)
    
    #Salvo il dizionario così ottenuto nella destinazione richiesta
    with open(fout, 'w') as f4out:
        f4out = dump(dizFinale, f4out)

def inverti_diz(diz):
    '''Restituisce il dizionario inverito (ovvero scambiando chiavi e valori) del diz dato in input. Ovvero, ciascun figlio diventa chiave di suo padre.'''
    reverseDiz = dict()
    for key, value in diz.items():
        for padre in value:
            reverseDiz.setdefault(padre, key)
    return reverseDiz

def antenati_ricors(chiave, revDiz, dizFinale, nodiGradoY, numAntenati):
    '''Funzione ricorsiva della dizionario_gradi_antenati che calcola il numero di antenati di grado y della chiave data in input alla prima chiamata.'''
#   Per ogni chiave del dizionario INVERTITO (con il ciclo for di dizionario_gradi_antenati), si controlla se il suo attributo (ovvero suo padre) si trova nell'insieme di nodi con grado y; se è così, si incrementa il contatore da returnare.
#   Dopodiché si riesegue il controllo su ogni chiave, dove ogni nuova chiave è ottenuta prendendo il padre di quella precedente. In aggiunta, si controlla se la nuova chiave (il nuovo padre) è già presente in dizFinale. Nel caso, inutile ripetere i calcoli e si restituisce il numero di antenati più l'attributo di dizFinale.
    if chiave not in revDiz:
        return numAntenati
    elif revDiz[chiave] in nodiGradoY:
        numAntenati +=1
        
    nextChiave = revDiz[chiave]
    if nextChiave in dizFinale:
        return numAntenati + dizFinale[nextChiave]
    
    #chiamata ricorsiva
    antenati_ricors(nextChiave, revDiz, dizFinale, nodiGradoY, numAntenati)
    return numAntenati


if __name__=='__main__':
    dizionario_gradi_antenati('Alb10.json',2,'tAlb10_4.json')