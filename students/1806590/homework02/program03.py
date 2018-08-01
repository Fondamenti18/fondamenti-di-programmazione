
def decod(pfile, codice):
    '''inserire qui il codice'''
    ris=[]
    ris1=[]
    ris2=[]
    f = open(pfile,'r')
    parole=f.readlines()
    parole[:]=[x.strip('\n') for x in parole]
    parole[:]=[x for x in parole if len(x)==len(codice) and len(set(x))==len(set(codice))]
        
    for p1 in parole:
        for i in range (len(codice)-1):
            if codice[i]==codice[i+1] and p1[i]==p1[i+1]:
                ris2+=[p1]
            
    for p in ris2:
        for h in range(len(codice)):
            if codice.count(codice[h])!= p.count(p[h]):
               ris1+=[p]

    ris[:]= [x for x in ris2 if x not in set(ris1)] 

    return set(ris)


    

    
                


    
                     
                     

                
            
            
           
        
            
   





