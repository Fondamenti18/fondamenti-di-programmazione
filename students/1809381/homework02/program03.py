import re
def decod(pfile, codice):
        bu=open(pfile,"r" )
  
        cod=len(set(codice))
  
        ripetizioni=[]
        count=0
        for i in cod:
                ripetizioni[count]=codice.count(i)
                count+=1
  
                parole=[]			
		for x in f.readlines():
                        X=set(x)
			if len(X)-1==cod:
                                for i in X:
                                        if x.count(i) in ripetizioni:
                                                parole+=x
    
    
    
        return set(parole)
