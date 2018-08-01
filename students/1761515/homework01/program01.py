'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi  ed un intero 
non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k divisori propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

ad esempio per ls = [121, 4, 37, 441, 7, 16] 
modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine della funzione si avra' che la lista ls=[16]

Per altri  esempi vedere il file grade.txt

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

def modi(ls,k):
    "inserite qui il vostro codice"
    lst = []
   
    '''for num in range(len(ls)):  
        if( all(ls[num] % x !=0 for x in range(2,ls[num]))) : 
            lst.append(ls[num])'''
    

    for num in ls:
      find=False
      find2=False
      if (num%2!=0): 
          if (num%3!=0):
               if (num%5!=0):
                    if (num%7!=0):
                         if (num%11!=0):
                              if (num%13!=0):
                                   if (num%17!=0):
                                        if (num%19!=0):
                                            x=int(num/2)
                                            for y in range(21, x):
                                                find2=True
                                                if (y%2!=0 and y%3!=0 and num%y==0):  
                                                    find=True
                                                    break
      if (find==False and find2==True):
           lst.append(num)

      
    
    for x in lst:
        ls.remove(x)
    
    l2=ls.copy()
    
    
    for x in l2:
        p=0
        c=True
        for num in range(2,int(x/2)+1):
            if(x%num==0):
                p+=1
                
                #print(x,"   ","  %  ",num,"   ",len(l3))
                
            if(p>k):
                c=False
                break
        if(c==False or p!=k):
            ls.remove(x)
    
    '''
    for x in l2:
        l3=[]
        c=True
        for num in range(2,int(x/2)+1):
            if(x%num==0):
                l3.append(num)
                #print(x,"   ","  %  ",num,"   ",len(l3))
                
            if(len(l3)>k):
                c=False
                break
        if(c==False or len(l3)!=k):
            ls.remove(x)'''
    
    
    '''for x in l2:
        lis = trovaDivisori(x,k)
        if len (lis)!= k:
            ls.remove(x)'''
            

    
    return lst


def trovaDivisori(x,k):
    lis = []
    for i in range(2,int(x/2)+1):
        if x % i == 0 :
            lis.append(i)
        if len(lis)>k:
            break
    return lis
