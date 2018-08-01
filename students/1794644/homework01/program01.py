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
    import math
    primi=[]
    n_divisori=[]
    a=0
    b=0
    c=0
    e=0
    f=0
    g=0
    h=0
    i=0
    j=0
    l=0
    m=0
    n=0
    o=0
    p=0
    q=0
    for n in ls:
        if all(n%i!=0 for i in range (2, int(math.sqrt(n))+1)):
            primi.append(n)
            
    
    try:
            
        for d in range(2, int(math.sqrt(ls[0]))+1):
            if ls[0]%d==0:
                a+=2
        n_divisori.append(a)
        
        for d in range(2, int(math.sqrt(ls[1]))+1):
            if ls[1]%d==0:
                b+=2
        n_divisori.append(b)
            
        for d in range(2, int(math.sqrt(ls[2]))+1):
            if ls[2]%d==0:
                c+=2
        n_divisori.append(c)
        
        for d in range(2, int(math.sqrt(ls[3]))+1):
            if ls[3]%d==0:
                e+=2
        n_divisori.append(e)
        
        for d in range(2, int(math.sqrt(ls[4]))+1):
            if ls[4]%d==0:
                f+=2
        n_divisori.append(f)
        
        for d in range(2, int(math.sqrt(ls[5]))+1):
            if ls[5]%d==0:
                g+=2
        n_divisori.append(g)
        
        for d in range(2, int(math.sqrt(ls[6]))+1):
            if ls[6]%d==0:
                h+=2
        n_divisori.append(h)
        
        for d in range(2, int(math.sqrt(ls[7]))+1):
            if ls[7]%d==0:
                i+=2
        n_divisori.append(i)
        
        for d in range(2, int(math.sqrt(ls[8]))+1):
            if ls[8]%d==0:
                j+=2
        n_divisori.append(j)
        
        for d in range(2, int(math.sqrt(ls[9]))+1):
            if ls[9]%d==0:
                l+=2
        n_divisori.append(l)
        
        for d in range(2, int(math.sqrt(ls[10]))+1):
            if ls[10]%d==0:
                m+=2
        n_divisori.append(m)
        
        for d in range(2, int(math.sqrt(ls[11]))+1):
            if ls[11]%d==0:
                n+=2
        n_divisori.append(n)
        
        for d in range(2, int(math.sqrt(ls[12]))+1):
            if ls[12]%d==0:
                o+=2
        n_divisori.append(o)
        
        for d in range(2, int(math.sqrt(ls[13]))+1):
            if ls[7]%d==0:
                p+=2
        n_divisori.append(p)
        
        for d in range(2, int(math.sqrt(ls[14]))+1):
            if ls[14]%d==0:
                q+=2
        n_divisori.append(q)
        
    except(IndexError):
        pass
         
    
     
    for value in range(len(ls)-1, -1, -1):
        if n_divisori[value]!=k:
            del ls[value]
            
    return primi    
   
                
                
            
        
     
        
        
            
                    
                
    #return primi   
    
print(modi([42, 27, 39, 17, 32, 5, 7], 4))