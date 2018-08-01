import json      
def pianifica(fcompiti,insi,fout): 
    ''' Ricevuti un file, un insieme di compiti e un file di output, scrive nel fout un dizionario composto dai compiti che si trovano
    nel file iniziale e una lista per ognuno, composta dai compiti che devono essere svolti prima dello stesso'''
    f = open(fcompiti,mode='r',encoding='utf-8')
    righe=f.readlines()
    f.close()
    dict_id={}
    dict_id=itera_righe(righe,dict_id)          
    risultato={}
    risultato=itera_insi(insi,risultato,dict_id)
    f = open(fout,mode='w',encoding='utf-8') 
    f.write(json.dumps(risultato)) 
    f.close() 

def itera_righe(righe,dict_id):
    for indice,riga in enumerate(righe):
        dict_id=aggiunta_comp(riga,dict_id,righe,indice)
    return dict_id

def aggiunta_comp(riga,dict_id,righe,indice):
    if 'comp' in riga: 
        comp_in_lettura=''
        comp_in_lettura=riga.split('p')
        del comp_in_lettura[0]
        comp_in_lettura=''.join(comp_in_lettura)
        comp_in_lettura=comp_in_lettura.split()   
        comp_in_lettura=''.join(comp_in_lettura)
        dict_id[comp_in_lettura]=''
        dict_id=try_aggiunta(righe,indice,dict_id,comp_in_lettura)
    return dict_id

def try_aggiunta(righe,indice,dict_id,comp_in_lettura):
    try:
        dict_id=aggiunta_sub(righe,indice,dict_id,comp_in_lettura)
    except IndexError:
        pass
    return dict_id

def aggiunta_sub(righe,indice,dict_id,comp_in_lettura):
    if 'sub' in righe[indice+1]:
        sub_in_lettura=''
        sub_in_lettura=righe[indice+1].split('b')
        del sub_in_lettura[0]
        sub_in_lettura=''.join(sub_in_lettura)
        sub_in_lettura=sub_in_lettura.split()            
        sub_in_lettura=''.join(sub_in_lettura)
        dict_id[comp_in_lettura]=sub_in_lettura
    return dict_id

def itera_insi(insi,risultato,dict_id):
    for elemento in insi:
        risultato=aggiunta_elem(elemento,dict_id,risultato)
    return risultato

def aggiunta_elem(elemento,dict_id,risultato):
    if elemento in dict_id.keys():
        risultato[elemento]=[]
        sub=''
        sub=elemento
        risultato=aggiunta_prel(dict_id,sub,risultato,elemento)
    return risultato

def aggiunta_prel(dict_id,sub,risultato,elemento):
    while not dict_id[sub] == '':    
        risultato[elemento].insert(0,dict_id[sub])     
        sub=dict_id[sub]
    return risultato