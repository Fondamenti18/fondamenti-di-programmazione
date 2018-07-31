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

def open_file(file):
    '''Funzione che legge il file json e ritorna una variabile con il contenuto
    '''
    with open(file) as f:   #apre file
        var = json.load(f)  #inserisce contenuto file nella variabile var
    return var  #ritorna variabile var
 
 
def save_file(file, var):
    '''Funzione per salvare il file json
    '''
    with open(file, 'w') as f:  #apre file in modalità scrittura
        json.dump(var, f)   #scrive nel file json il contenuto della variabile var


def trova_nodo_radice(albero):
    '''Funzione che cerca il nodo radice nel dizionario passato come argomento, controlla ogni chiave del dizionario se compare in uno dei valori delle chiavi, se non compare è il nodo radice.
    '''
    radice = ''     #inizializzazione variabile radice
    count = 0       #inizializzazione contatore
    for chiave in albero.keys():        #scorre chiavi del dizionario albero
        for valore in albero.values():  #scorre i valore del dizionario albero
            if(chiave in valore):       #se la chiave è presente nel valore
                count += 1      #incrementa contatore di 1
                break           #ferma ciclo for valore
        if(count == 0):     #se al termine del ciclo for valore il contatore è uguale a 0
            radice = chiave     #metti la chiave nella variabile radice
            return(radice)     #ritorna la variabile radice 
        count = 0              #reset contatore


def cerca_nodi(albero, sottoalbero, var):
    '''Funzione che costruisce albero a partire da un valore passato come argomento.
    '''
    if(var in albero and var not in sottoalbero):       #se il valore var è presente nel dizionario albero e non nel dizionario sottoalbero
        sottoalbero[var] = albero[var]  #inserisci nel dizionario sottoalbero alla chiave var il valore della chiave var del dizionario albero
        for valore in albero[var]:      #scorri singolarmente i valori della chiave var del dizionario albero
            sottoalbero = cerca_nodi(albero, sottoalbero, valore)   #richiama funzione ricorsiva e passa valore
        return(sottoalbero)     #ritorna il dizionario sottoalbero


def ordina_lista(diz):
    '''Preso come argomento un dizionario scorre i valori e ordina le liste
    '''
    for valore in diz.values():     #scorre valori dizionario
        valore.sort()       #ordina lista
    return(diz) 	#ritorna dizionario
    
    
def cerca_livello(albero, x, livello, diz):
    '''Funzione che ritorna il livello di profondità del nodo dell'albero.
    '''
    if(albero[x] != []):        #se il valore della chiave x del dizionario albero è diverso da lista vuota
        for valore in albero[x]:     #scorri valori del dizionario alla chiave x
            if(str(livello) in diz.keys()):     #se il livello è presente come chiave del dizionario
                if(valore not in diz[str(livello)]):    #se il valore non è nella chiave livello del dizionario
                    diz[str(livello)].append(valore)    #aggiungi alla chiave livello del dizionario il valore
            else:   #altrimenti
                diz[str(livello)] = albero[x]   	#aggiungi chiave livello a dizionario e valore della chiave x del dizionario albero
            diz = cerca_livello(albero, valore, livello+1, diz)     #chiama funzione ricorsiva, passa livello +1
    return(diz)     #ritorna dizionario
    

def calcola_grado_nodi(albero):
    '''Funzione che calcola il grado di ogni nodo.
    '''
    diz_grado = {}    #dizionario
    for chiave, valore in albero.items():   #scorre chiave, valore del dizionario albero
        diz_grado[chiave] = len(valore)     #aggiunge chiave e come valore il numero di figli del nodo    
    return(diz_grado)       #ritorna dizionario

def trova_antenati(albero, nodo, lista):
    '''Funzione che cerca antenati dei nodi
    '''
    for chiave, valore in albero.items():       #scorre chiave, valore del dizionario albero
        if(nodo in valore):     #se il nodo passato come argomento alla funzione è uguale al valore
            lista.append(chiave)        #aggiungi alla lista la chiave
            trova_antenati(albero, chiave, lista)   #chiamata ricorsiva alla funzione, passa come nodo la chiave
    return(lista)       #ritorna la lista
    
def genera_albero_antenati(albero, y):
    '''Funzione che cerca gli antenati di grado y di ogni nodo.
    '''
    diz_antenati = {}       #dizionario
    lst_antenati = [] 	#lista
    for chiave in albero.keys():        #scorre chiavi del dizionario albero
        lst_antenati = trova_antenati(albero, chiave, lst_antenati) #richiama funzione trova_antenati
        diz_antenati[chiave] = lst_antenati       #aggiunge al dizionario alla chiave 'chiave' il contenuto della lista
        lst_antenati = []   #reset lista
    return(diz_antenati)    #ritorna dizionario
    
        
def genera_sottoalbero(fnome,x,fout):  
    diz_sottoalbero = {}        #inizializza dizionario sottoalbero
    diz_alb = open_file(fnome)  #richiama funzione open_file e salva il contenuto nel dizionario albero
    diz_sottoalbero = cerca_nodi(diz_alb, diz_sottoalbero, x)   #richiama funzione ricorsiva cerca_nodi
    save_file(fout, diz_sottoalbero)    #richiama funzione save_file
    
    
def cancella_sottoalbero(fnome,x,fout):
    diz_del = {}        #inizializza dizionario del
    diz_alb = open_file(fnome)  #richiama funzione open_file e salva il contenuto nel dizionario albero
    diz_del = cerca_nodi(diz_alb, diz_del, x)   #richiama funzione ricorsiva cerca_nodi
    for chiave_del in diz_del:      #scorre chiavi del dizionario del
        if(chiave_del in diz_alb):  #se la chiave è presente nel dizionario albero
            del diz_alb[chiave_del] #elimina dal dizionario albero la chiave
    for chiave_del in diz_del:  #scorre chiave del dizionario del
        for chiave, valore in diz_alb.items():  #scorre chiave, valore del dizionario albero
            if(chiave_del in valore):   #se la chiave del è presente nei valori del dizionario albero
                valore.remove(chiave_del)       #elimina valore uguale a chiave del
    save_file(fout, diz_alb)        #richiama funzione save_file
    
    
def dizionario_livelli(fnome,fout):
    controllo = False   #inizializza variabile controllo su False
    livello = 0     #inizializza variabile livello su 0
    diz_liv = {}    #inizializza dizionario livelli
    diz_alb = open_file(fnome)      #richiama funzione open_file e salva il contenuto nel dizionario albero
    radice = trova_nodo_radice(diz_alb) 	#richiama funzione trova_nodo_radice e salva il contenuto nella variabile radice
    diz_liv[str(livello)] = [radice]        #aggiunge chiave livello e valore radice al dizionario livelli
    diz = cerca_livello(diz_alb, radice, livello+1, diz_liv)    #richiama funzione cerca_livello
    diz = ordina_lista(diz) 	#richiama funzione ordina_lista
    save_file(fout, diz)    #richiama funzione save_file


def dizionario_gradi_antenati(fnome,y,fout):
    diz = {}    #inizializzazione dizionario
    diz_antenati = {}   #inizializzazione dizionario antenati
    diz_alb = open_file(fnome)      #richiama funzione open_file
    radice = trova_nodo_radice(diz_alb)     #richiama funzione trova_nodo_radice
    diz = cerca_nodi(diz_alb, diz, radice)  #richiama funzione cerca_nodi
    diz_gradi = calcola_grado_nodi(diz)     #richiama funzione calcola_grado_nodi
    diz = genera_albero_antenati(diz, y)    #richiama funzione genera_albero_antenati
    count = 0   #inizializzazione contatore
    for chiave, valore in diz.items():  #scorre chiave, valore del dizionario
        for i in valore:    #scorre singolarmente valori
            if(diz_gradi[i] == y):  #se il valore della chiave i del dizionario gradi è uguale a y
                count += 1  #incrementa contatore di 1
        diz_antenati[chiave] = count        #aggiungi chiave 'chiave' e come valore il contatore
        count = 0   #reset contatore
    save_file(fout, diz_antenati)   #richiama funzione save_file
   
    
    
        
    
if __name__ == '__main__':
    #genera_sottoalbero('Alb10.json','d','tAlb10_1.json')
    #cancella_sottoalbero('Alb10.json','d','tAlb10_2.json')
    #dizionario_livelli('Alb10.json', 'tAlb10_3.json')
    dizionario_gradi_antenati('Alb10.json', 2, 'tAlb10_4.json')