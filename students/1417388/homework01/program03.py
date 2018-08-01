def codifica(chiave, testo):
 
    chiave=chiave.replace(' ', '');
    
    for i in range(0,len(chiave)):
        if (ord(chiave[i])< ord('a') or ord(chiave[i])> ord('z') ):
            chiave = chiave[:i] + chiave[i+1:]
       
    while i >= 0:
        j=0
        while(j<i):
            if(chiave[j]==chiave[i]):
                 chiave = chiave[:j] + chiave[j+1:]
                 i=i-1
            j=j+1
        i=i-1
        
    chiave_ord=sorted(chiave)
    dizionario={}
    
    for i in range(0,len(chiave)):
        dizionario[chiave_ord[i]]=chiave[i]
      
    for i in range(0, len(testo)):
        trovato=False
        for key, value in dizionario.items():
            if(testo[i]==key and trovato==False):
                testo=testo[:i] + value + testo[i+1:]
                trovato=True
              
    return testo
    
        
def decodifica(chiave, testo):
    chiave=chiave.replace(' ', '');
    
    for i in range(0,len(chiave)):
        if (ord(chiave[i])< ord('a') or ord(chiave[i])> ord('z') ):
            chiave = chiave[:i] + chiave[i+1:]
       
    while i >= 0:
        j=0
        while(j<i):
            if(chiave[j]==chiave[i]):
                 chiave = chiave[:j] + chiave[j+1:]
                 i=i-1
            j=j+1
        i=i-1
        
    chiave_ord=sorted(chiave)
    dizionario={}
    
    for i in range(0,len(chiave)):
        dizionario[chiave[i]]=chiave_ord[i]
      
    for i in range(0, len(testo)):
        trovato=False
        for key, value in dizionario.items():
            if(testo[i]==key and trovato==False):
                testo=testo[:i] + value + testo[i+1:]
                trovato=True
    return testo