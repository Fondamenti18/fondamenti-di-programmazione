'''
Un  file di compiti contiene  informazioni su un insieme  di compiti da eseguire.
Esistono  due tipologie di compiti:
- compiti che possono essere eseguiti indipendentemente dagli altri.
- compiti da svolgere  solo al termine di un compito preliminare.
I compiti del primo tipo sono codificati nel file mediante una linea che contiene
in sequenza le due sottostringhe "comp" ed "N" (senza virgolette) eventualmente inframmezzate,
precedute e/o seguite da  spazi. "N" e' l'ID del compito (un numero positivo).
Compiti del secondo tipo sono codificati nel file mediante due linee di codice.
-- la prima  linea,  contiene in sequenza le due sottostringhe "comp" ed "N"
(senza virgolette) eventualmente inframmezzate,
precedute e/o seguite da  spazi. "N" e' l'ID del compito (un numero positivo).
-- la seconda linea (immediatamente successiva nel file) contiene
in sequenza le due sottostringhe "sub" ed "M" (senza virgolette) eventualmente inframmezzate,
precedute e/o seguite da  spazi. "M" e' l'ID del compito preliminare.

il seguente file di compiti contiene informazioni su 4 compiti (con identificativi 1,3,7 e 9).
I compiti con identificativi 1 e 9 possono essere svolti indipendentemente dagli altri mentre i compiti
con identificativo 3 e 7 hanno entrambi un compito preliminare.

comp 3
 sub 9
        comp1
comp              9
    comp 7
sub3

Scrivere la funzione pianifica(fcompiti,insi,fout) che prende in input:
- il percorso di un file (fcompiti)
- un insieme  di ID di compiti da cercare (insi)
- ed il percorso di un file (fout)
e che salva in formato JSON nel file fout un dizionario (risultato).

Il dizionario (risultato) dovra' contenere come chiavi gli identificativi (ID) dei compiti
presenti in fcompiti e richiesti nell'insieme insi.
Associata ad ogni ID x del dizionario deve esserci una lista contenente  gli identificativi (ID) dei compiti
che bisogna eseguire prima di poter eseguire il compito x richiesto
(ovviamente la lista di un ID di un compito che non richie un compito preliminare risultera' vuota ).
Gli (ID) devono comparire nella lista nell'ordine di esecuzione corretto, dal primo fino a quello precedente a quello richiesto
(ovviamente il primo ID di una lista non vuota corripondera' sempre ad un compito che non richiede un compito preliminare).


Si puo' assumere che:
 - se l' ID di un compito che richieda un compito preliminare e' presente  in fcompiti
    allora anche l'ID di quest'ultimo e' presente in fcompiti
 - la sequenza da associare al compito ID del dizionario esiste sempre
 - non esistono cicli (compiti che richiedono se' stessi anche indirettamente)


Ad esempio per il file di compiti  fcompiti contenente:

comp 3
 sub 9
        comp1
comp              9
    comp 7
sub3

al termine dell'esecuzione di  pianifica(fcompiti,{'7','1','5'}, 'a.json')
il file 'a.json' deve contenere il seguente dizionario
{'7':['9','3'],'1':[]}


Per altri esempi vedere il file grade02.txt

AVVERTENZE:
    non usare caratteri non ASCII, come le lettere accentate;
    non usare moduli che non sono nella libreria standard.
NOTA: l'encoding del file e' 'utf-8'
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero.
'''
def clear(r): #funzione per pulire le righe dai caratteri non alfabetici
    l=[]
    for word in r:
        w=word.strip()
        w=w.split(' ')
        if "\n" in word:
            w=word.replace("\n", "")
            if 'comp' in w:
                w=w.replace('comp', 'comp ')
                w=w.split()
            if 'sub' in w:
                w=w.replace('sub', 'sub ')
                w=w.split()
        l.append(w)
    return(l)

def create_diz(l):
    diz={}
    value=[]
    for i, obj in enumerate(l):
        if 'comp' in l[i]:
            diz[obj[1]]=[]
        elif 'sub' in l[i]:
            value.append(obj[1])

            #if control and 'comp' in obj:
            #if (obj[0]=='comp' and obj[1]==control) in l :
            while True:
                control=obj[1]
                if obj[0]=='comp' in l:
                    if obj[1]==control:
                        value.append(obj[1])
                        control=0
                        print(value)


    #print(diz)

    #adesso devo verificare la presenza di un campo dipendente da comp (ovvero sub)
    #che segue la lista appena analizzata. Dopo avera individuata, analizzo il suo
    #ID, lo aggiungo alla lista dei valori, e vado al campo comp con lo stesso
    #valore di ID, e faccio lo stesso controllo: se il campo successivo è un altro
    #comp, allora la lista dell'elemento precedente non aggiunge nuovi valori

    #Idea: mi creo un flag e scorro le varie liste della lista che abbiano come
    #primo elemento comp e come secondo lo stesso ID del precedente Sub analizzato


    '''
    if i+1<len(l):
        if 'sub' in l[i+1]:
            value.append(obj[1])
    diz[obj[1]]=value
    if (value and 'comp' in obj) in l:
        print(value)



    for lista in l:
        if lista[0]=='comp':
            diz[lista[1]]=value
            if 'sub' in l[lista+1]:
                value.append(lista[1])'''
    return(diz)

def pianifica(fcompiti,insi,fout):
    '''Implementare qui la funzione'''
    riga=[]
    with open(fcompiti, 'r', encoding='utf-8') as fp:
        for line in fp:
            riga.append(line)
    l=[]
    l=clear(riga)
    diz={}
    diz=create_diz(l)

    return()
pianifica('file02_10_2.txt', {'2','4','11','1','6','9','10'},'test1.json')
