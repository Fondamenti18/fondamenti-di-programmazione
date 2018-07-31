def conv(n):
    dictionario={0:"",1:"uno",2:"due",3:"tre",4:"quattro",5:"cinque",6:"sei",7:"sette",8:"otto",9:"nove",10:"dieci",11:"undici",12:"dodici",13:"tredici",14:"quattordici",15:"quindici",16:"sedici",17:"diciassette",18:"diciotto",19:"diciannove",20:"venti",30:"trenta",40:"quaranta",50:"cinquanta",60:"sessanta",70:"settanta",80:"ottanta",90:"novanta",100:"cento"}
    da_dividere=""
    lista=[1,2,4,5,7,8,10,11]
    if len(str(n)) in lista:
        if len(str(n))==1 or len(str(n))==4 or len(str(n))==7 or len(str(n))==10:
            da_dividere=("0"*2)+str(n)
        else:
            da_dividere=("0"*1)+str(n)
    else:
        da_dividere=str(n)
    blocchi=[da_dividere[x:x+3] for x in range(0,len(da_dividere),3)]
    k=len(blocchi)
    stringa=blocktostring(dictionario,blocchi,k)
    return stringa

def blocktostring(dictionario,blocchi,k):
    stringa=""
    for blocco in blocchi:
        if int(blocco[0])!=0 and int(blocco[1])!=0:
            if int(blocco[0])==1:
                stringa+=dictionario.get(100)
            else:
                stringa+=dictionario.get(int(blocco[0]))+dictionario.get(100)
            if int(blocco[1])==8:
                stringa=stringa[:-1]
                stringa+=dictionario.get(int(blocco[1])*10)
                if int(blocco[2])==1 or int(blocco[2])==8:
                    stringa=stringa[:-1]
                    stringa+=dictionario.get(int(blocco[2]))
                else:
                    stringa+=dictionario.get(int(blocco[2]))
            else:
                try:
                    stringa+=dictionario.get(int(blocco[1:]))
                except:
                    stringa+=dictionario.get(int(blocco[1])*10)
                    if int(blocco[2])==1 or int(blocco[2])==8:
                        stringa=stringa[:-1]
                    stringa+=dictionario.get(int(blocco[2]))
        elif int(blocco[0])==0 and int(blocco[1])==0:
            stringa+=dictionario.get(int(blocco[2]))
        else:
            if int(blocco[0])==0:
                try:
                    stringa+=dictionario.get(int(blocco[1:]))
                except:
                    stringa+=dictionario.get(int(blocco[1])*10)
                    if int(blocco[2])==1 or int(blocco[2])==8:
                        stringa=stringa[:-1]
                    stringa+=dictionario.get(int(blocco[2]))
            elif int(blocco[1])==0:
                if int(blocco[0])==1:
                    stringa+=dictionario.get(100)+dictionario.get(int(blocco[2]))
                else:
                    stringa+=dictionario.get(int(blocco[0]))+dictionario.get(100)+dictionario.get(int(blocco[2]))
        stringa,k=suff(stringa,k)
    return stringa

def suff(stringa,k):
    if k==2:
        if stringa[-8:]=="miliardi" or stringa[-8:]=="miliardo" or stringa[-7:]=="milioni" or stringa[-7:]=="milione":
            k-=1
            pass
        elif stringa[-11:]=="miliardouno" or stringa[-11:]=="miliardiuno" or stringa[-10:]=="milioneuno" or stringa[-10:]=="milioniuno" or stringa=="uno":
            stringa=stringa.replace("uno","mille",1)
            k-=1
        else:
            stringa+="mila"
            k-=1
    elif k==3:
        if stringa[-8:]=="miliardi" or stringa[-8:]=="miliardo":
            k-=1
            pass
        elif stringa[-11:]=="miliardouno" or stringa[-11:]=="miliardiuno" or stringa=="uno":
            stringa=stringa.replace("uno","unmilione",1)
            k-=1
        else:
            stringa+="milioni"
            k-=1
    elif k==4:
        if stringa=="uno":
            stringa=stringa.replace("uno","unmiliardo",1)
            k-=1
        else:
            stringa+="miliardi"
            k-=1
    return stringa,k