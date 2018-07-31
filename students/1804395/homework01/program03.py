def generaChiave(chiave):
    key=''
    for i in range (len(chiave)-1,-1,-1):        
        if (chiave[i] >= 'a' and chiave[i] <= 'z') and key.find(chiave[i])== -1:
            key= chiave[i] + key            
    return key

def ordinaStringa (string):
    ordinateKey=list(string)
    ordinateKey.sort()
    ordinateKey=''.join(ordinateKey)
    return ordinateKey
    
def algoritmo (key, testo, i):    
    if i== 0:
        chiaveComplementare=generaChiave(key)
        chiave=ordinaStringa(chiaveComplementare)
    else :
        chiave=generaChiave(key)
        chiaveComplementare=ordinaStringa(chiave)  
    newText=''
    for char in testo:
        if char in chiave:
            for pos, keyChar in enumerate(chiave):
                if char==keyChar:
                    newText+= chiaveComplementare[pos]
        else:
            newText+= char
    return newText

def codifica(chiave, testo):    
    return algoritmo(chiave, testo, 0)
    
def decodifica(chiave, testo):
    return algoritmo(chiave, testo, 1)
   
