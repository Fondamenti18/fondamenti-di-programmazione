def conv(n):
    if n==0:
        return ''
    elif n<=19:
        a=['uno','due','tre','quattro','cinque','sei','sette','otto',
                'nove','dieci','undici','dodici','tredici',
                'quattordici','quindici','sedici','diciassette','diciotto','diciannove']
        return a[n-1]
    elif n<=99:
        dec=['venti','trenta','quaranta','cinquanta','sessanta',
             'settanta','ottanta','novanta']
        dec1=dec[int(n/10)-2]                           
        u=n%10                                          
        if u==1 or u==8:
            dec1=dec1[:-1]                              
        return dec1+conv(n%10)
    elif n<=199:
        c=n%100
        c=int(c/10)
        cen='cent'
        if c!=8:
            cen=cen+'o'
        return cen+conv(n%100)
    elif n<=999:
        c=n%100
        c=int(c/10)
        cen='cent'
        if c!=8:
            cen=cen+'o'
        return conv(int(n/100))+cen+conv(n%100)
    elif n<=1999:
        return 'mille'+conv(n%1000)
    elif n<=999999:
        return conv(int(n/1000))+'mila'+conv(n%1000)
    elif n<=1999999:
        return 'unmilione'+conv(n%1000000)
    elif n<=999999999:
        return conv(int(n/1000000))+'milioni'+conv(n%1000000)
    elif n<=1999999999:
        return 'unmiliardo'+conv(n%1000000000)
    elif n<=999999999999:
        return conv(int(n/1000000000))+'miliardi'+conv(n%1000000000)
    
                    
    
        
    

    
    
    
    
            
        
        
