def conv(n):
    if n<=9:
        if n==0:
            return ''
        lista_num=[x for x in range(1,10)]
        lista_lett=["uno", "due", "tre", "quattro", "cinque", 
                "sei", "sette", "otto", "nove"]
        for x in lista_num:
            if x==n:
                return lista_lett[x-1]
    elif n>9 and n<=19:
        lista_num1=[x for x in range(10,20)]
        lista_lett1=["dieci", 
                "undici", "dodici", "tredici", 
                "quattordici", "quindici", "sedici", 
                "diciassette", "diciotto", "diciannove"]
        i=0
        while i<=9:
            if lista_num1[i]==n:
                return lista_lett1[i]
            else:
                i+=1
    elif n<=99:
        primi=["venti", "trenta", "quaranta",
                  "cinquanta", "sessanta", 
                  "settanta", "ottanta", "novanta"]
        lettera=primi[int(n/10)-2]
        resto=n%10
        if resto==1 or resto==8:
            lettera=lettera[:-1]
        return lettera+conv(n%10)
    elif n<=199:
        if n==100:
            return 'cento'
        else:
            return 'cento'+conv(n%100)   
    elif n<=999:
         s1=str(n)
         y=int(s1[1:2])
         if y==8:
             z=int (s1[0:1])
             return conv(z)+'cent'+conv(n%100)
         else:
             y=int (s1[0:1])
             return conv(y)+'cento'+conv(n%100)            
    elif n<2000:
        if n==1000:
            return 'mille'
        else:
            return 'mille'+conv(n%1000)
    elif n<=99999:   
        s1=str(n)
        if n<10000:
            y=int(s1[0:1])
            for x in range(2,10):
                if y==x:
                    return conv(x)+'mila'+conv(n%1000)
        else:
            if n>10000:
                z=int(s1[0:2])
                for x in range(10,100):
                    if z==x:
                        return conv(x)+'mila'+conv(n%1000)
    elif n<=999999:
        s1=str(n)
        y=int(s1[0:3])
        return conv(y)+'mila'+conv(n%1000)
    elif n<=99999999:
        s1=str(n)
        if n<2000000:
            if n==1000000:
                return 'unmilione'
            else:
                return 'unmilione'+ conv(n%1000000)
        if n<10000000:
            y=int(s1[0:1])
            for x in range(2,10):
                if y==x:      
                    return conv(x)+'milioni'+conv(n%1000000)
        else:
            if n>10000000 and n<100000000:
                z=int(s1[0:2])
                for x in range(10,100):
                    if z==x:
                        return conv(x)+'milioni'+conv(n%1000000)
    elif  n<=999999999:    
        s2=str(n)
        y=int(s2[0:3])
        return conv(y)+'milioni'+conv(n%1000000)
    elif n<=99999999999:
        s1=str(n)
        if n<2000000000:
            if n==1000000000:
                return 'unmiliardo'
            else:
                return 'unmiliardo'+ conv(n%1000000)
        if n<10000000000:
            y=int(s1[0:1])
            for x in range(2,10):
                if y==x:
                    return conv(x)+'miliardi'+conv(n%1000000000)
        else:
            if n>10000000000 and n<100000000000:
                z=int(s1[0:2])
                for x in range(10,100):
                    if z==x:
                        return conv(x)+'miliardi'+conv(n%1000000000)
    elif  n<=999999999999:   
        s2=str(n)
        y=int(s2[0:3])
        return conv(y)+'miliardi'+conv(n%1000000000)
    
            
        
        
        
                
            
            
        
                
        
                
                
                
                
