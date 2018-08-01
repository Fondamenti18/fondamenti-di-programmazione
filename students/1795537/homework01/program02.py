diz = {0:'',1:'uno',2:'due',3:'tre',4:'quattro',5:'cinque',6:'sei',7:'sette',8:'otto',9:'nove',10:'dieci',
           11:'undici',12:'dodici',13:'tredici',14:'quattordici',15:'quindici',16:'sedici',17:'diciassette',18:'diciotto',19:'diciannove',20:'venti',
           30:'trenta',40:'quaranta',50:'cinquanta',60:'sessanta',70:'settanta',80:'ottanta',90:'novanta'}
diz2 = {0:'miliardi',1:'milioni',2:'mila',3:'',4:'unmiliardo',5:'unmilione',6:'mille'} 

def aggiusta_parola(parola):
    return (parola[:-1])

def magg_99(n, p1, parola):
    if n > 99:
            p1 = n// 100
            n = n%100
            if(p1 != 1):
                parola = diz[p1]
            parola = parola + 'cento'
    return(parola, n)
    
def contr_ultimo(n,p2,parola):
    if (n == 1 or n == 8) and p2 != 0:
            parola = aggiusta_parola(parola)
    return (parola)
            
def controllo(n,pos):
    parola=''
    p1 = p2 = 0
    if n == 1:
        parola = parola + diz2[pos+4]
    else :
        parola ,n=  magg_99(n,p1,parola)
        if n not in diz:
            p2 = n // 10
            n = n % 10     
        if p2 == 8:
            parola = aggiusta_parola(parola)
        parola = parola + diz[p2*10]
        parola = contr_ultimo(n,p2,parola)
        
        parola = parola + diz[n] + diz2[pos]
    return (parola)

def scomponi(n):
    lista = []
    a=0
    for s in range(3,13,3):
        a = n % 10**s
        n = n-a
        a = a // 10**(s-3)
        lista += [a]
    lista.reverse()
    return (lista)
         
def inviaVal(lista):
    parola = ''
    for pos,num in enumerate(lista):
        if num >0:
            parola = parola + controllo(num,pos)
    return (parola)

def conv(n):
    n = scomponi(n)
    p = inviaVal(n)
    return (p)