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
import json
#estrai il primo numero da una stringa
"""def estrai_num(stringa):
    A = len(stringa)
    x = 0
    num = ""
    while x < A:
        B = ord(stringa[x])
        if B >= 48 and B <= 57:
            num += stringa[x]
        x += 1
    return num"""

def estrai_num(stringa):
    num = ""
    y = len(stringa)-1
    for x in range(y): 
        if stringa[x].isdigit():
            num += stringa[x]
    return num

#cerca se il copmito esiste
    #lista+num_compito= indice
def cerca_comp(lista,num,l):
    ris = -1
    i = 0
    
    while i < l:
        if lista[i].find("comp") != -1 and estrai_num(lista[i]) == num:
            ris = i
            i = l
        i += 1
    return ris

#Funzione che cerca se un compito ha un sub e quale
    #lista+indice= num compito
def cerca_sub(lista,num,l):
    ris = "-1";
    i = num
    if i != l-1:
        if lista[i+1].find("sub") != -1:
            ris = estrai_num(lista[i+1])
    return ris


def riordina(lista):
    l = len(lista)
    if l > 1:
        L = l
        i = 0
        f = l-1
        if l % 2 == 0:
            while l/L != 2:
                L-=1
                app = lista[i]
                lista[i] = lista[f]
                lista[f] = app
                i+=1
                f-=1
        else:
            while (l-1)/L != 2:
                L-=1
                app = lista[i]
                lista[i] = lista[f]
                lista[f] = app
                i+=1
                f-=1

#dizionario+valore_stringa
def trova(dizionario,val):
    esiste = False
    dizionario1 = dizionario.copy()
    for x in dizionario1:
        for y in range(len(dizionario1[x])):
            if dizionario1[x][y] == val:
                z = y+1
                esiste = True
                dizionario[val] = []
                while z < len(dizionario1[x][y]):    
                    dizionario[val].append(dizionario[x][z])
                    z += 1
                break
        if esiste == True:
            break
    return esiste
    
def dizio(lista):
    dizionario = {}
    lun = len(lista)
    for x in range(lun):
        if lista[x].find("comp") != -1:
            c = estrai_num(lista[x])
            dizionario[c] = []
        else:
            s = estrai_num(lista[x])
            dizionario[c].append(s)
    return dizionario

def nario(diz):
    i = 0
    c = True
    while c == True:
        c = False
        for x in diz:
            #print(x)
            #print(diz)
            
            if len(diz[x]) > i:
                if len(diz[diz[x][i]]) > 0:
                    c = True
                    diz[x].append(diz[diz[x][i]][0])
            #print(diz)
        i += 1
    return diz
        

def pianifica(fcompiti,insi,fout):
    '''Implementare qui la funzione'''
    f = open(fcompiti)
    F = open(fout,"w")
    lista = f.readlines()
    dizionario = {}
    dizionario = nario(dizio(lista))
    DIZIONARIO = {}
    #insieme = list(insi)
    
    for x in insi:
        if x in dizionario.keys():
            DIZIONARIO[x] = dizionario[x]
    for y in DIZIONARIO:
        riordina(DIZIONARIO[y])
    #print(DIZIONARIO)
    json.dump(DIZIONARIO, F)
    
    
    f.close()
    F.close()

pianifica('file02_10_2.txt', {'2','4','11','1','6','9','10','7'},'test1.json')