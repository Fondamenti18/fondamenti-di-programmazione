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
    comp = set()
    comp_sub = {}
    comp, comp_sub = leggi_file(fcompiti)  # restituisce lista comp trovati e le associazioni dirette compiti-sub.
    #print(comp)
    #print(comp_sub)
    final_set_id = insi & comp             # Restituisce elementi comuni all' insieme di input con quello dei comp.
    #print(final_set_id)
    result_output = genera_output(final_set_id, comp_sub)
    write_json(fout, result_output)

"""
questa funzione restituisce il valore finale di output delle associazioni compiti-sottocompiti.
"""
def genera_output(final_set_id, comp_sub):
    result_output = {}
    for numero in final_set_id:
        chiave = numero
        listino = []
        while True:
            valore = comp_sub.get(chiave, -1)
            if valore != -1:
                listino.insert(0, valore)       # aggiungiamo all inzioo ogni valore.
                chiave = valore
            else:                              # ho finito la mia ricerca nelle relazioni.
                #listino.reverse()
                result_output[numero] = listino
                break                          # Ho finito di ispezionare il dizionario delle relazioni (figli finiti)
                
    return result_output    
"""
questa funzione scrive il json della funzione 'pianifica'.
"""        
def write_json(fout, result_output):
    with open(fout, "w") as output:
        #json.dump(result_output, output)  # Serializzo l'oggetto per il formato json.
        #output.write(str(result_output).replace("'", '"'))  # Serializzo l'oggetto per il formato json.
        output.write(json.dumps(result_output))
        #output.write(re.sub("'", '"', str(result_output)))  # Serializzo l'oggetto per il formato json.

        
"""
questa funzione elabora il file e restituisce gli accoppiamenti.
"""
        
def leggi_file(fcompiti):
    comp_sub = {}
    comp = set()
    with open(fcompiti, "r") as dati:
        try:
            for riga in dati: 
                riga = riga.strip()            # Elimino spazi prima e dopo. Trovero: "comp    7" oppure "sub     4".   
                if riga.find("comp") != -1:
                    Id = riga[4:].strip()
                    comp.add(Id) 
                else:                          # sto leggendo la sub.
                    Id_sub = riga[3:].strip()
                    comp_sub[Id] = Id_sub      # sto scrivendo dizionario accoppiamenti.
        except ValueError:
            print( "errorefile")
        
    return comp, comp_sub 
            



     
if __name__ == '__main__':
    args=('file02_10_2.txt', {'2','4','11','1','6','9','10'},'test1.json')
    #ret = pianifica(*args)
    args= ('file02_10000_50.txt',{'10','20','30','40','50','60','70','80'},'test2.json')
    #ret = pianifica(*args)
    args= ('file02_50000_100.txt', 'set([str(i) for i in range(2000,52001)])','test5.json')
    ret = pianifica('file02_50000_100.txt', set([str(i) for i in range(2000,52001)]),'test5.json')