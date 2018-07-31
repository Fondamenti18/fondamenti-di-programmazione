import json

def pianifica(fcompiti,insi,fout):
    with open(fcompiti,"r") as file:
        file=file.read()
        file=file.replace(" ","")
        file=file.splitlines()
        file.append("x")
    file=dizionario_sub(file)
    output=insieme_compiti(insi,file)
    with open(fout,"w") as j:
        json.dump(output,j)

def insieme_compiti(insieme,dizionario):
    dizionario_output={}
    for i in insieme:
        if i in dizionario:
            dizionario_output[i]=trova_percorso(i,dizionario)
        else:
            continue
    return dizionario_output
            
        
    
def dizionario_sub(file):
    i=0
    dizionario={}
    while i<len(file)-1:
        if file[i].startswith("comp"):
            compito=file[i][4:]
            if file[i+1].startswith("sub"):
                sub=file[i+1][3:]
                dizionario[compito]=sub
                i=i+2
            else:
                dizionario[compito]=""
                i=i+1
    return dizionario


def trova_percorso(n,dizionario):
    lista=[]
    while 1:
        sub=dizionario[n]
        if sub=="":
            break
        lista.insert(0,sub)
        n=sub
    return lista


        
        
        
                    
                
    
            
