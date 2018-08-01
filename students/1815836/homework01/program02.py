
pos0=['','uno','due','tre','quattro','cinque','sei','sette','otto','nove']
pos1=['','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
pos2=['','venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
def conv(n):
    str_n=str(n)
    lun=len(str_n)
    listn=list(str_n)
    numero=[]
    if (lun==12):
        k=listn[len(listn)-12:len(listn)-9]
        numero+=suddividi(k)+'miliardi'
        lun-=3
    if (lun==11):
        k=listn[len(listn)-11:len(listn)-9]
        numero+=suddividi(k)+'miliardi'
        lun-=2
    if (lun==10):
        k=listn[len(listn)-10:len(listn)-9]
        s=''.join(k)
        s=int(s)
        if(s!=1):
            numero+=suddividi(k)+'miliardi'
        else:
            numero+='unmiliardo'
        lun-=1
    
    
    
    
    if (lun==9):
        k=listn[len(listn)-9:len(listn)-6]
        numero+=suddividi(k)+'milioni'
        lun-=3
    if (lun==8):
        k=listn[len(listn)-8:len(listn)-6]
        numero+=suddividi(k)+'milioni'
        lun-=2
    if (lun==7):
        k=listn[len(listn)-7:len(listn)-6]
        s=''.join(k)
        s=int(s)
        if(s!=1):
            numero+=suddividi(k)+'milioni'
        else:
            numero+='unmilione'
        lun-=1
        
        
        
    if (lun==6):
        k=listn[len(listn)-6:len(listn)-3]
        numero+=suddividi(k)+'mila'
        lun-=3
    if (lun==5):
        k=listn[len(listn)-5:len(listn)-3]
        numero+=suddividi(k)+'mila'
        lun-=2
    if (lun==4):
        k=listn[len(listn)-4:len(listn)-3]
        s=''.join(k)
        s=int(s)
        if(s!=1):
            numero+=suddividi(k)+'mila'
        else:
            numero+='mille'
        lun-=1
    
    
    
    if (lun==3):
        k=listn[len(listn)-3:len(listn)]
        numero+=suddividi(k)
        lun-=3
    if (lun==2):
        k=listn[len(listn)-2:len(listn)]
        numero+=suddividi(k)
        lun-=2
    if (lun==1):
        k=listn[len(listn)-1:len(listn)]
        numero+=suddividi(k)
        lun-=1
        




    ris=''.join(numero)
    return(ris)






def suddividi(k):
    a=[]
    c=len(k)
    if(c==3):
        k3=int(k[-3])
        k2=int(k[-2])
        k1=int(k[-1])
        if(k3==1 and k2==0 and k1==0):
            a+='cento'
        if(k3>1 and k2==0 and k1>0) and (k1!=8 or k1!=1) and (k2!=8 or k2!=1):
            a+=pos0[k3]+'cento'+pos0[k1]
        if(k3>1 and k2==0 and k1>0) and (k1==8 and k1==1)and (k2!=8 or k2!=1):
            a+=pos0[k3]+'cent'+pos0[k1]
        if(k3>=2 and k2>0 and k1>0) and (k1!=8 or k1!=1)and (k2!=8 and k2!=1):
            a+=pos0[k3]+'cento'            
        if(k3>=2 and k2>1 and k1>0) and (k1==8 and k1==1)and (k2!=8 or k2!=1):
            a+=pos0[k3]+'cent'
        if(k3==1 and k2>0 and k1>0) and (k1!=8 or k1!=1)and (k2!=8 or k2!=1):
            a+='cento'
        if(k3>=2 and k2>1 and k1>0) and (k1!=8 or k1!=1)and (k2==8 or k2==1):
            a+=pos0[k3]+'cent'
        if(k3>=2 and k2==1 and k1>0) and (k1==8 or k1==1):
            a+=pos0[k3]+'cento'
        
        if(k2==1):
            a+=pos1[k1+1]
        if(k2>1 and (k1!=1 and k1!=8)):
            a+=pos2[k2-1]+pos0[k1]
        if(k2>1 and (k1==1 or k1==8)):
            a+=pos2[k2-1][0:-1]+pos0[k1]
        if(k3==0 and k2==0 and k1>0):
            a+=pos0[k1] 
    if(c==2):
        k2=int(k[-2])
        k1=int(k[-1])
        if(k2==1):
            a+=pos1[k1+1]
        if(k2>1 and (k1!=1 and k1!=8)):
            a+=pos2[k2-1]+pos0[k1]
        if(k2>1 and (k1==1 or k1==8)):
            a+=pos2[k2-1][0:-1]+pos0[k1]
    if(c==1):
        k1=int(k[-1])
        a+=pos0[k1]    
    r=''.join(a)
    return(r)
    
        