

def divpropri(num):          #determina il numero di divisori propri di un numero
    conta=0
    for i in range(2,num):
        if(num%i==0):
            conta=conta+1
    return conta

 
def primo(num):              #determina se un numero è primo o no
    for i in range(2, num):
        if(num%i == 0):
            return False
    return True


                 


def modi(ls, k):             #lista con i numeri primi
    ls1=[]
    for i in ls:
        if(primo(i)==True):
            ls1+=[i]
    
    i=len (ls)-1             #lista contentente solo i numeri con k divisori e senza i numeri primi
    while i>=0:
        if divpropri (ls [i])!=k:
                del ls [i]
        i-=1
    return ls1
  
    
    
  