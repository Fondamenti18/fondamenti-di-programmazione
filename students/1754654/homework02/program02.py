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

def pianifica(fcompiti,insi,fout):

    with open(fcompiti, encoding = 'utf-8') as f_:
        tasks = f_.read()

    task_list = []
    for line in tasks.splitlines():
        if len(line.split()) != 2:
            line = clean_line(line)
        task_list.append((line.split()))

    dictionary_structure = {}
    for index,comp in enumerate(task_list):
        if comp[0] == 'comp':
            if index + 1 < len(task_list):
                if task_list[index+1][0] == 'sub':
                    dictionary_structure[comp[1]] = task_list[index + 1][1]
                else:
                    dictionary_structure[comp[1]] = []
            else:
                    dictionary_structure[comp[1]] = []
                
        else:
            if index == len(task_list):
                dictionary_structure[comp[1]] = []
                print(index)





    dict_schedule = {}

    for elements in insi:
        if elements in dictionary_structure:
            task_schedule = [] #here we put the schedule of every single process
            task_schedule = search_asubtasks(elements, dictionary_structure)
            dict_schedule[elements] = task_schedule


    with open(fout,'w') as wr_:
        json.dump(dict_schedule,wr_)

    return None

def search_asubtasks(ele , dictionary):
    asubtasks_ = []
    disc_ = dictionary[ele]
    while disc_ != []:
        asubtasks_.append(disc_)
        disc_ = dictionary[disc_]
    asubtasks_.reverse()
    return asubtasks_


def clean_line(dirtyline):
    ID_task = ''
    flag = False
    for _ in dirtyline:
        if _.isnumeric() and flag == False:
            ID_task = ID_task + ' '
            flag = True
        ID_task = ID_task + _
    return ID_task


if __name__ == '__main__':
    pianifica('file02_10_2.txt', {'2','4','11','1','6','9','10'},'testino.json')
