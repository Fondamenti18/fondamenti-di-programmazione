def conv(n):
    diz={
         0:'',
         1:'uno',
         2:'due',
         3:'tre',  
         4:'quattro',
         5:'cinque',
         6:'sei',
         7:'sette',
         8:'otto',
         9:'nove',
         10:'dieci',
         11:'undici',
         12:'dodici',
         13:'tredici',
         14:'quattordici',
         15:'quindici',
         16:'sedici',
         17:'diciassette',
         18:'diciotto',
         19:'diciannove',
         20:'venti',
         30:'trenta',
         40:'quaranta',
         50:'cinquanta',
         60:'sessanta',
         70:'settanta',
         80:'ottanta',
         90:'novanta'
        }
    if n<=20:
        s=ventina(n,diz)
    elif n<100:
        s=centina(n,diz)
    elif n<1000:
        s=millina(n,diz)
    elif n<1000000:
        s=milionina(n,diz)
    elif n<1000000000:
        s=miliardina(n,diz)
    else:
        s=bilionina(n,diz)          
    return s 

      
def ventina(x,diz):
    s1=diz[x]
    return s1

def centina(x,diz):
    if x%10!=1 and x%10!=8:
        s1=diz[x//10*10]+diz[x%10]
    else:
        s1=diz[x//10*10][:-1]+diz[x%10]

    return s1

def millina(x,diz):
    if (x//10)%10!=8 and x%100>20:
        s1=diz[x//100]+'cento'+centina(x%100,diz)
    elif (x//10)%10!=8 and x%100<=20:
        s1=diz[x//100]+'cento'+ventina(x%100,diz)
    else:
        s1=diz[x//100]+'cent'+centina(x%100,diz)
    if s1[0:3]=='uno':
        s1=s1[3:]
    if x//100==0 and s1[6]=='t':
        s1=s1[4:]
    elif x//100==0 and s1[6]!='t':
        s1=s1[5:]
            
    return s1

def milionina(x,diz):
    if x//1000==1:
        s1='mille'+millina(x%1000,diz)
    elif x//1000<=20:
        s1=ventina(x//1000,diz)+'mila'+millina(x%1000,diz) 
    elif x//1000<100:
        s1=centina(x//1000,diz)+'mila'+millina(x%1000,diz)
    else:
        s1=millina(x//1000,diz)+'mila'+millina(x%1000,diz)
 
    return s1  

def miliardina(x,diz):
    if x//1000000==1:
        s1='unmilione'+milionina(x%1000000,diz)
    elif x//1000000<=20:
        s1=ventina(x//1000000,diz)+'milioni'+milionina(x%1000000,diz) 
    elif x//1000000<100:
        s1=centina(x//1000000,diz)+'milioni'+milionina(x%1000000,diz)
    else:
        s1=millina(x//1000000,diz)+'milioni'+milionina(x%1000000,diz)

    return s1  

def bilionina (x,diz):
    if x//100000000==1:
        s1='unmiliardo'+milionina(x%1000000000,diz)
    elif x//1000000000<=20:
        s1=ventina(x//1000000000,diz)+'miliardi'+miliardina(x%1000000000,diz) 
    elif x//1000000000<100:
        s1=centina(x//1000000000,diz)+'miliardi'+miliardina(x%1000000000,diz)
    else:
        s1=millina(x//1000000000,diz)+'miliardi'+miliardina(x%1000000000,diz)
    return s1 