from math import sqrt
def modi(ls,k):
    listadiv=[]
    numeriprimi=[]
    '''Primo for per scorrere gli elementi ls'''
    for el in ls:
        k1=0
        '''Secondo for dei possibili divisori'''
        for x in range(2,int(sqrt(el)+1)):
            if el%x==0:
                    if el//x==x:
                        k1+=1
                    if el//x!=x:
                        k1+=2
                    if k1>k:
                        break
        if k1==k:
            listadiv+=[el]
                    
            
        '''Se il n di div.  0 el  primo,'''     
        if k1==0:
            if el>1:
                numeriprimi+=[el]
    '''Aggiorno ls con i numeri con divisori pari alla variabile k'''            
    ls.clear()
    ls+=listadiv
    del listadiv    	
    return numeriprimi