dizionario=[{0:"miliardi",3:"milioni",6:"mila",9:"",12:""},{0:"",1:"uno",2:"due",3:"tre",4:"quattro",5:"cinque",6:"sei",7:"sette",8:"otto",9:"nove",10:"dieci",11:"undici",12:"dodici",13:"tredici",14:"quattordici",15:"quindici",16:"sedici",17:"diciassette",18:"diciotto",19:"diciannove",80:"ottanta"},{0:"",1:"",2:"venti",3:"trenta",4:"quaranta",5:"cinquanta",6:"sessanta",7:"settanta",8:"ottanta",9:"novanta"},{0:"unmiliardo",3:"unmilione",6:"mille",9:"",12:""}]

def conversione_in_stringa(numero):
    stringa=str(numero)
    return stringa.zfill(12)

def cdecine(ns,lettere):
    decine=int(ns[1:3])
    if 19<decine<80 or decine>89:
        lettere+=dizionario[2].get(int(ns[1]))
    if 79<decine<90:
        if int(ns)<100:
            lettere+="ottanta"
        else:
            lettere=lettere[0:-1]+"ottanta"
    return (ns,lettere,decine)

def centinaia(ns):
    lettere=""
    c=int(ns[0])
    if c>1:
        lettere=dizionario[1].get(int(ns[0]))+"cento"
    elif c==1:
        lettere+="cento"
    return (ns,lettere)

def unita(ns,lettere,decine):
    if decine<20:
        lettere+=dizionario[1].get(decine)
        return lettere
    unita=int(ns[2])
    if unita==1 or unita==8:
        lettere=lettere[:-1]+dizionario[1].get(unita)
    else:
        lettere+=dizionario[1].get(unita)
    return lettere
    
def convogni3(n):
    x,y=centinaia(n)
    x,y,z=cdecine(x,y)
    return(unita(x,y,z))

def conv(n):
    stringa=conversione_in_stringa(n)
    i=0
    lettere=""
    valore=0
    for i in range(0,11,3):
        valore=int(stringa[i:i+3])
        lettere+=convogni3(stringa[i:i+3])
        if valore>1:
            lettere+=dizionario[0].get(i)
        elif valore==1:
            lettere=lettere[0:-3]+dizionario[3].get(i)
    return lettere
        
    
    
    








        
    
    
    
    
    
    
    




    
    
    
    
        
        
        
        
        

                
                
                


                                  






        
    
        

    
        
        
        
        
            
            
        




    
    
    
