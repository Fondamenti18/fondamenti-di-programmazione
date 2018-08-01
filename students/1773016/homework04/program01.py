import json
import time
#----------------------------------------------------------------------------------------------------------------------------
value = 0
#---------------------------------------------------------------------------------------------------------------------------- 
def nodoOrigine(diz):    
    valori = diz.values()
    diz2 = {}
    for value in valori:
        for elem in value:  
            diz2[elem] = ''             
    key = ''
    try:
        for chiave in diz: 
            key = chiave
            diz2[chiave]
    except(KeyError):
        return key
    return 0
def formaAlbero(alb,chiave,dizOut):             #Forma un diz albero a partire dal nodo specificato in chiave
    if chiave in alb.keys():
        if alb[chiave] != []:
            dizOut[chiave] = alb[chiave]
            for value in alb[chiave]:
                formaAlbero(alb,value,dizOut)
        else:
            dizOut[chiave] = []
def eliminaValue(alb,value):                   #Elimina il nodo principale dell'albero che si è in procinto di eliminare
    for chiave in alb.keys():                  #dall'albero di partenza
        if value in alb[chiave]:
            alb[chiave].remove(value)
def cancellaAlbero(alb,chiave,dizOut):
    alberoCanc = {}
    formaAlbero(alb,chiave,alberoCanc)
    eliminaValue(alb,chiave)    
    for chiave in alb:
        if chiave not in alberoCanc:
            dizOut[chiave] = alb[chiave]
def trovaLivelli(alb,tempNodo,dizOut,livAttuale):
    if str(livAttuale) not in dizOut:
        dizOut[str(livAttuale)] = [tempNodo]
    else:
        dizOut[str(livAttuale)].append(tempNodo)    
    if alb[tempNodo] != []:
        for chiave in alb[tempNodo]:
            trovaLivelli(alb,chiave,dizOut,livAttuale+1)
def ordinaDiz(diz):
    for chiave in diz:
        diz[chiave].sort()  
def antenati(alb,diz,tempChiave,tempAnt,numAnt):    
    if alb[tempChiave] != []:     
        if len(alb[tempChiave]) == numAnt:
            tempAnt+=1
        for elem in alb[tempChiave]:
            diz[elem] = tempAnt 
            antenati(alb,diz,elem,tempAnt,numAnt)


#---------------------------------------------------------------------------------------------------------------------------#    
def genera_sottoalbero(fnome,x,fout):           #Funziona 
    fin = open(fnome,'r',encoding = 'UTF-8')
    fileOut = open(fout,'w',encoding = 'UTF-8')
    dizAlb = json.load(fin)
    diz = {}
    formaAlbero(dizAlb,x,diz)
    print(json.dumps(diz),file = fileOut)
    fin.close()
    fileOut.close()
    return diz

def cancella_sottoalbero(fnome,x,fout):     #Funziona
    fin = open(fnome,'r',encoding = 'UTF-8')
    fileOut = open(fout,'w',encoding = 'UTF-8')
    dizAlb = json.load(fin)
    diz = {}
    cancellaAlbero(dizAlb,x,diz)
    print(json.dumps(diz),file = fileOut)
    fin.close()
    fileOut.close()
    return diz

def dizionario_livelli(fnome,fout):               #Funziona
    fin = open(fnome,'r',encoding = 'UTF-8')
    fileOut = open(fout,'w',encoding = 'UTF-8')
    dizAlb = json.load(fin)
    diz = {}               
    origine = nodoOrigine(dizAlb)  
    trovaLivelli(dizAlb,origine,diz,0)
    ordinaDiz(diz) 
    print(json.dumps(diz),file = fileOut)
    fin.close()
    fileOut.close()
    return diz       

def dizionario_gradi_antenati(fnome,y,fout):       #Probabilmente da ottimizzare
    fin = open(fnome,'r',encoding = 'UTF-8')
    fileOut = open(fout,'w',encoding = 'UTF-8')
    dizAlb = json.load(fin)
    orig = nodoOrigine(dizAlb)
    dizOut = {orig:0}  
    antenati(dizAlb,dizOut,orig,0,y) 
    print(json.dumps(dizOut),file = fileOut)
    fin.close()
    fileOut.close()
    return dizOut
