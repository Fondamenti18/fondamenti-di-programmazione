import json


def genera_sottoalbero(fnome, x, fout):
    
    with open(fnome) as diz: diz = json.load(diz)
    
    nuovo_diz = {x : diz[x]}
    nuovo_diz = crea_sottoalbero(x, diz, nuovo_diz)
    
    with open(fout, 'w') as file_finale: 
        
        json.dump(nuovo_diz, file_finale)
    
def crea_sottoalbero(x, d, nuovo_diz):
    
    for valore in d[x]:
        
        nuovo_diz[valore] = d[valore]
        nuovo_diz = crea_sottoalbero(valore, d, nuovo_diz)
    
    return nuovo_diz
    

def cancella_sottoalbero(fnome, x, fout):
    
    with open(fnome) as diz: diz = json.load(diz)
    
    lista_nodi = []
    sottoalberi = list(set(trova_sottoalberi(diz, x, lista_nodi)))
    
    for nodo in sottoalberi:
    
        del diz[nodo]
        
    del diz[x]
    passo_finale = elimina_in_antenati(diz, x)
    
    with open(fout, 'w') as file_finale:
        
        json.dump(diz, file_finale)

def elimina_in_antenati(diz, x):
    
    dizionario_antenati = diz_invertito_con_controllo(diz)
    
    for chiave in dizionario_antenati:
        
        if chiave == x:
                
            valore = dizionario_antenati[chiave][0]
            appoggio = diz[valore]
            indice_x = appoggio.index(x)
            del appoggio[indice_x]
            diz[valore] = appoggio

    return diz

def trova_sottoalberi(d, x, lista_nodi):

    for valore in d[x]:

        lista_nodi  += [valore]
        diz_modificato = trova_sottoalberi(d, valore, lista_nodi)
    
    return lista_nodi

def diz_invertito_con_controllo(d):	

    nodo_padre = list(trova_nodo_padre(d))
    diz_antenati = {nodo_padre[0] : 0}
                             
    for chiave in d:
           
        for elemento in d[chiave]:
	      
            diz_antenati[elemento] = [chiave]
    
    return diz_antenati
    

def dizionario_livelli(fnome, fout):

    with open(fnome) as d: d = json.load(d)
    
    i = 1
    chiavi_in_d = list(d.keys())
    nodo_padre = list(trova_nodo_padre(d))
    dizionario_numerato = {"0" : nodo_padre}
    controllo = set(nodo_padre)
    dizionario_numerato = numera_sottoalberi(chiavi_in_d, d, i, dizionario_numerato, nodo_padre, controllo)
    
    with open(fout, 'w') as file_finale: json.dump(dizionario_numerato, file_finale)
    
def numera_sottoalberi(chiavi_in_d, d, i, dizionario_numerato, chiavi, controllo):
    
    valori = []
    
    if len(controllo) != len(chiavi_in_d):
    
        for chiave in chiavi:
            
            for valore in d[chiave]:
                
                if valore not in controllo:
                    
                    valori += [valore]
                
                controllo.add(valore)
        
        valori = sorted(valori)
        dizionario_numerato[str(i)] = valori
        i += 1
        numeramentazione = numera_sottoalberi(chiavi_in_d, d, i, dizionario_numerato, valori, controllo)

    return dizionario_numerato


def dizionario_gradi_antenati(fnome,x,fout):

    with open(fnome) as d: d = json.load(d)
    
    nodo_padre = list(trova_nodo_padre(d))[0]
    diz_antenati = diz_invertito(d)
    nuovo_dizionario = {}
    i = 0
    
    for chiave in d:
       
        i = antenati_con_x_figli(d, x, i, nodo_padre, nuovo_dizionario, diz_antenati, chiave)
        nuovo_dizionario[chiave] = i
        i = 0
    
    with open(fout, 'w') as file_finale: json.dump(nuovo_dizionario, file_finale)
    
def diz_invertito(d):	

    nodo_padre = list(trova_nodo_padre(d))[0]
    diz_antenati = {nodo_padre : 0}
    
    for chiave in d:
        
        for elemento in d[chiave]:
	
            diz_antenati[elemento] = [chiave]
	
    return diz_antenati

def antenati_con_x_figli(d, x, i, nodo_padre, nuovo_dizionario, diz_antenati, chiave):
    
    controllo = str(diz_antenati[chiave]).strip(" ['] ")
    
    if controllo != '0' and controllo != nodo_padre:
        
        if len(d[controllo]) == x:
        
            i += 1
        
        i = antenati_con_x_figli(d, x, i, nodo_padre, nuovo_dizionario, diz_antenati, controllo)
        
    return i


def trova_nodo_padre(d):
	
    chiavi = set(d.keys())
    insieme_valori = set()
	 
    for chiave in d:
		
        for valore in d[chiave]:
	
            insieme_valori.add(valore)
            padre = chiavi - insieme_valori
	
    return padre