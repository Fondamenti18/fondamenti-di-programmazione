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
        
plan_dict = {}


def pianifica(fcompiti,insi,fout):
    '''Implementare qui la funzione'''
    global plan_dict
    
    
    result = {}
    with open(fcompiti, 'r', encoding='utf-8') as f:
        
        f_lines = f.readlines()
        compito_to_line_dict = generate_compito_to_line_index(f_lines)
        
        for compito_id in insi:
            if(compito_id not in compito_to_line_dict):
                continue
            line_index = compito_to_line_dict[compito_id]
            result[compito_id] = plan(line_index, f_lines, plan_dict, compito_to_line_dict)[::-1]
            
    with open(fout, 'w') as output:
        json.dump(result, output)
    
    plan_dict = {}




def plan(compito_line_index, fcompiti_text, plan_dict, compito_to_line_dict):
    
    compito = fcompiti_text[compito_line_index]
    compito_id = get_id(compito)
    sub_list = []
    
    if(compito_id in plan_dict):
        return plan_dict[compito_id]
    
    if(compito_line_index == len(fcompiti_text)-1):
        plan_dict[compito_id] = []
        return plan_dict[compito_id]
    
    
    if( is_sub(fcompiti_text[compito_line_index+1]) == False):
        plan_dict[compito_id] = []
        
    else:
        sub = fcompiti_text[compito_line_index+1]
        sub_id = get_id(sub)
        sub_list += [sub_id]
        
        sub_sub_list = plan(compito_to_line_dict[sub_id], fcompiti_text, plan_dict, compito_to_line_dict)
        
        for el in sub_sub_list:
            sub_list += [el]
        
        plan_dict[compito_id] = sub_list
    
    return plan_dict[compito_id]
        
    

def generate_compito_to_line_index(fcompiti_text):
    compito_to_line = {}
    for line_index in range(len(fcompiti_text)):
        compito = fcompiti_text[line_index]
        if("comp" in compito):
            compito_id = get_id(compito)
            compito_to_line[compito_id] = line_index
    return compito_to_line
            

def is_sub(compito):
    compito = "".join(compito.split())
    if(compito[0:3] == "sub"):
        return True
    else:
        return False

def get_id(compito):
    compito = "".join(compito.split())
    if(compito[0:3] == "sub"):
        return compito[3:]
    else:
        return compito[4:]

