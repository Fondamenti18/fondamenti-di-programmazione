import json

def estraiNumero(riga):
    '''data una stringa, estraggo il numero in essa contenuto, la dove esista'''
    comp = [car for car in riga if car.isnumeric()]
    comp = ''.join(comp)
    return (comp)

def pulisciIns(insieme, diz):
    '''rimuovo da insieme i valori non presenti nel file'''
    insieme = [el for el in insieme if el in diz]
    return insieme

def creaDiz(diz, insieme):
    '''creo il dizionario contenente tutti i compiti da fare per poter svolgere i comp dell'insieme dato'''
    insieme= pulisciIns(insieme,diz)
    dizN={}
    for el in insieme :
        sub = ' '
        ris = []
        elOR = el
        while sub != '':
            if el in diz:
                sub = diz[el]
                if sub != '': 
                    ris += [sub]
                el = sub       
            else: sub = ''
        ris.reverse()
        dizN[elOR] = ris
    return(dizN)
                         
        
def trovaComp(compiti,diz):
    '''creo un dizionario composto dai compiti richiesti e corrispettivo sub, la dove esista'''
    subG=[]
    compG = ''
    for riga in compiti.readlines():
        if 'comp' in riga:
            compG = ''
            comp = estraiNumero(riga)
            subG = ''
            compG = comp
            diz[compG]=''
        elif compG != '':
            sub = estraiNumero(riga)
            subG = sub
            diz[compG] = subG     
    return (diz) 
            
def pianifica(fcompiti,insi,fout):

    diz2={}
    diz ={}
    
    with open(fcompiti, encoding='utf-8') as compiti:
        diz = trovaComp(compiti, diz )
    
    diz2 = creaDiz(diz, insi)

    with open(fout, mode='w') as file:
        json.dump(diz2, file)
