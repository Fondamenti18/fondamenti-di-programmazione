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
def crea_lista(fcompiti):
    f=open(fcompiti, 'r', encoding='utf-8')
    t=f.read()
    f.close()
    ls=t.split('comp')
    c=len(ls)-1
    while c>=0:
        ls[c]=ls[c].split()
        if len(ls[c])==2:
            l=list(ls[c][1])
            s1=''.join(l[:3])
            s2=''.join(l[3:])
            del ls[c][1]
            ls[c]+=[s1]
            ls[c]+=[s2]
        if ls[c]==[]:
            del ls[c]
        ls[c][0]=int(ls[c][0])
        c-=1
    ls.sort()
    c=0
    if ls[c][0]>1:
        for x in range(0,ls[c][0]-1):
           ls[x:x]=[['-']]
           c+=1
    while c<=len(ls)-2:
        a=ls[c+1][0]-ls[c][0]
        if a>1:
            for x in range(ls[c][0],ls[c+1][0]-1):
                ls[x:x]=[['-']]
            c+=a
        else:
            c+=1
    c=len(ls)-1
    while c>=0:
        if type(ls[c][0])==int:
            ls[c][0]=str(ls[c][0])
        c-=1
    return ls

def crea_diz(insi,ls):
    diz={}
    for x in insi:
        x=int(x)
        if x<=len(ls):
            x=str(x)
            diz[x]=[]
    for x in diz:
        x=int(x)
        y=x-1
        x=str(x)
        t=True
        while t:
            if len(ls[y])==1:
                t=False
            if len(ls[y])==3:
                diz[x]=[ls[y][2]]+diz[x]
                a=int(ls[y][2])
                y=a-1
    return diz
def carica_file(diz,fout):
    from json import dump
    f=open(fout,'w',encoding='utf-8')
    dump(diz,f)
    f.close()
       
def pianifica(fcompiti,insi,fout):
    '''Implementare qui la funzione'''
    ls=crea_lista(fcompiti)
    diz=crea_diz(insi,ls)
    carica_file(diz,fout)
                    
        
