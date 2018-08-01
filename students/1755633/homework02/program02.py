import json

def scrivi(d,namew):     #funzione per scriviere sul file
    with open(namew,'w') as f:
        f.write(json.dumps(d))  #doppie apici

def retID(linea):  #funzione per trovare il numero che compare nella riga attuale
    sID=''
    for c in linea:
        if c in '0123456789':
            sID+=c
    return sID             #restituiamo solo il numero

def pianifica(name,ins,namew):    #funzione principale
    d=dict()
    f=open(name,'U')             
    for l in f:                    #creazione dizioinario iniziale--------------
            
        if 'comp' in l:           
            n=retID(l)            
            d[n]=0
            
        else:
            n1=retID(l)
            d[n]=n1
                                   #-----------------------------------------
    d1=dict()
    for elem in ins:               #scorro l insieme input
        ines=False
        a1=elem
        lista=[]
        while True:         
            val=d.get(elem, 'never')           #cerco se esiste chiave e mi restituisce il valore
            if val=='never':
                 ines=True
                 #print('skip')
                 break
                 
            elif val==0:    
                 break  
            else:
                lista.append(val)
                elem=val
        if ines==False:
            
            lista.reverse()    
            d1[a1]=lista                        #creazione nuova chiave con valore(lista al contrario)
        
        
    #print('dizf:',d1) 
    scrivi(d1,namew)                             #chiamat funzione per scrivere sul file

#prova('file02.txt',{'10','20','5','8','2'},'json.txt')
