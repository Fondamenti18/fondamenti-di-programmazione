import json

def genera_sottoalbero_ricorsivo(albero_dizionario,chiave_corrente,chiave_da_cercare,nuovo_albero,trovato) :
    if(chiave_corrente == chiave_da_cercare):
        trovato = True
    for figlio in albero_dizionario[chiave_corrente]:
        if genera_sottoalbero_ricorsivo(albero_dizionario,figlio,chiave_da_cercare,nuovo_albero,trovato):
            if (not trovato):
                return True
            trovato = True
    if trovato:
        nuovo_albero.update({chiave_corrente:albero_dizionario[chiave_corrente]})
    return trovato

def genera_sottoalbero(fnome,x,fout,):
    
    albero_file= open(fnome,'r')
    albero_stringa = albero_file.readline()
    albero_iniziale = json.loads(albero_stringa) 
    trovato = False
    nuovo_albero = {}
    genera_sottoalbero_ricorsivo(albero_iniziale,list(albero_iniziale.keys())[0],x,nuovo_albero,trovato)
    with open(fout, 'w', encoding='utf8') as f:
        json.dump(nuovo_albero, f)

def cancella_sottoalbero_ricorsivo(albero_dizionario,chiave_corrente,chiave_da_cercare,nuovo_albero) :
    
    figli = albero_dizionario[chiave_corrente]
    lista_figli_buoni = []
    for figlio in figli:
        if (figlio != chiave_da_cercare):
            cancella_sottoalbero_ricorsivo(albero_dizionario,figlio,chiave_da_cercare,nuovo_albero)
            lista_figli_buoni.append(figlio)
    nuovo_albero.update({chiave_corrente:lista_figli_buoni})
       
    return 

def cancella_sottoalbero(fnome,x,fout):
    
    albero_file = open(fnome,'r')
    albero_stringa = albero_file.readline()
    albero_iniziale = json.loads(albero_stringa) 
    nuovo_albero = {}
    cancella_sottoalbero_ricorsivo(albero_iniziale,list(albero_iniziale.keys())[0],x,nuovo_albero)
    with open(fout, 'w', encoding='utf8') as f:
        json.dump(nuovo_albero, f)



def dizionario_livelli_ricorsivo (albero_dizionario,chiave_corrente,nuovo_albero,contatore):
    if contatore in nuovo_albero:
        lista_siblings = nuovo_albero[contatore]
        lista_siblings .append( chiave_corrente)
        lista_siblings = sorted(lista_siblings)
        nuovo_albero.update({contatore:lista_siblings})
    else:
        lista_stringhe = []
        lista_stringhe.append( chiave_corrente)
        nuovo_albero.update({contatore:(lista_stringhe)})
    figli = albero_dizionario[chiave_corrente]
    for figlio in figli:
        dizionario_livelli_ricorsivo(albero_dizionario,figlio,nuovo_albero,contatore +1)
    return 

def dizionario_livelli(fnome,fout):
    
    
    albero_file = open(fnome,'r')
    albero_stringa = albero_file.readline()
    albero_iniziale = json.loads(albero_stringa) 
    nuovo_albero = {}
    contatore = 0
    dizionario_livelli_ricorsivo(albero_iniziale,list(albero_iniziale.keys())[0],nuovo_albero,contatore)
    with open(fout, 'w', encoding='utf8') as f:
        json.dump(nuovo_albero, f)
    

def dizionario_gradi_antenati_ricorsivo (albero_dizionario,chiave_corrente,nuovo_albero,contatore):

    nuovo_albero.update({chiave_corrente:contatore})
    figli = albero_dizionario[chiave_corrente]
    num_figli = len(figli)
    if num_figli == 2:
        contatore= contatore+1
    for figlio in figli:
        dizionario_gradi_antenati_ricorsivo(albero_dizionario,figlio,nuovo_albero,contatore)
    return 
     
    
def dizionario_gradi_antenati(fnome,y,fout):
    
    albero_file = open(fnome,'r')
    albero_stringa = albero_file.readline()
    albero_iniziale = json.loads(albero_stringa) 
    nuovo_albero = {}
    contatore = 0
    dizionario_gradi_antenati_ricorsivo(albero_iniziale,list(albero_iniziale.keys())[0],nuovo_albero,contatore)
    with open(fout, 'w', encoding='utf8') as f:
        json.dump(nuovo_albero, f)
  