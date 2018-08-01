#calcolo dei divisori tramite moltiplicazione degli esponenti (+1)
import math
def modi(ls,k):
    print(int(math.sqrt(9)))
    primi=[]
    finale=[]
    for x in ls:
        fattori=[]  #lista di fattori
        final=[]    
        cont=2      #primo contatore
        primo=0     #segno per numero primo
        x1=x        
        cont2=0     #secondo contatore
        eccesso=[]
        esponente=0
        elenco=[]
        i=0
        troppo=0
        divisori=1
        c=k+2
        temp=0
        if(prim(x,k)=='primo'):
           primi = primi + [x]
           continue
        elif(prim(x,k)=='troppo'):
             continue
        #cont=int(math.sqrt(x))
        while(x1>1 and cont!=x and cont!=1):                #funzione per trovare i fattori
            if(x1%cont==0):
                fattori=fattori + [cont]
                x1=x1/cont
                cont=2
            else:
                cont=cont+1
        cont=0
        #print(fattori)
        #if(bool(fattori)==False):
            #primi= primi + [x]
            #continue
        fattorif=list(set(fattori)) #elenco dei fattori non ripetuti
        #print(fattorif)
        for i in fattorif:
            elenco= elenco + [0]   #elenco degli esponenti dei fattori (lista di 0)
        #print(elenco)
        #print(fattori)
        i=0
        #elenco[0]=2
        while (i!=len(fattorif)):  #calcolo degli esponenti
            b=fattorif[i]
            #posizione=i
            #print(b)
            esponente=0
            for j in fattori:
                #print("ciao")
                if(b==j):
                    esponente=esponente+1
                    elenco[i]=esponente
                    
                    
                    
            i=i+1
           # print(i)
        #print(elenco)
        i=0                           #se c'è un solo numero con esponente tra i fattori, esso sarà il solo divisore primo
        while(i!=len(elenco)):        #a ogni esponente viene sommato 1
           # print("lento")
            elenco[i]=elenco[i]+1
            i=i+1
        i=0
        #print(elenco)
        for i in elenco:
           # print("lentissimo")#opgni esponente viene moltiplicato
            divisori=divisori*i
           # print(k)
            #print(divisori)
            #print(c)
            if divisori>c:
                print(divisori)
                troppo=1
                break
        if(troppo==1):
            #print("ciao")
            continue
           # print(divisori)
        divisori=divisori-2
        #print(divisori)
        #print(k)
        if(divisori==k):
            #print("ciao")
            finale=finale+[x]
    ls[:]=list(finale)
    #print(ls)
    return(primi)
def prim(x,k):
    cont2=math.sqrt(x)
    temp=int(math.sqrt(x))
    if cont2==temp:
        return('ok')
    i=0
    temp=0
    cont2=int(math.sqrt(x))
    while cont2 != 1:
        #print("entro")
        if x%cont2==0:
            temp=temp+1
            i=i+1
            return('ok')
            break
        else:
            i=i+1
            cont2=cont2-1
    if temp>k:
        return('troppo')
    elif temp==0:
        return('primo')
    
        
            
