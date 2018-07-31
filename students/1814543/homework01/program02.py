def conv(number):
    resto = number
    risultato = ""
    suffissi = {0: "", 1: "mila", 2 : "milioni", 3: "miliardi", 4: "mila"}
    suffisso1 = {0: "", 1: "mille", 2 : "unmilione", 3: "unmiliardo", 4: "mille"}
    iSuffix = 0
    while(resto > 0):
        
        if resto / 1000 >= 1:
            mCentinaia = resto % 1000
            strMCentinaia = getStrCentinaia(mCentinaia)
            if(mCentinaia !=0):
                if mCentinaia == 1:
                    risultato = suffisso1[iSuffix]  + risultato
                else:
                    risultato = strMCentinaia + suffissi[iSuffix]  + risultato
            iSuffix = iSuffix + 1
            resto = int ( resto / 1000)
        else:
            mStrCentinaia = getStrCentinaia(resto) + suffissi[iSuffix]
            if resto == 1:
                risultato = suffisso1[iSuffix]  + risultato
            else:
                risultato = mStrCentinaia + "" +  risultato
            resto = 0
    return risultato

def getStrCentinaia(number):
    strCento = "cento"
    strDecine = getStrDecine(number % 100)
    centinaia = int(number / 100)
    decina = number % 100
    decina = int(decina /10)
    
    if centinaia > 1:
        strCentinaia = getStrUnita(centinaia) + strCento
        if decina == 8:
            strCentinaia = strCentinaia[:-1]            
    elif centinaia<1:
        strCentinaia=""
    else:
        strCentinaia = strCento
    ris = strCentinaia + strDecine
    return str(ris)
    
        
def getStrUnita(number):
      
    da_0_a_9 = {0:"zero",1:"uno", 2:"due", 3:"tre",4:"quattro", 5: "cinque",6:"sei", 7:"sette", 8:"otto", 9:"nove"}
    return da_0_a_9[number]
        
def getStrDecine(number):
    ris = str
    da_10_a_99={0: "", 1:"dieci",2:"venti",3:"trenta",4:"quaranta",5:"cinquanta",6:"sessanta",7:"settanta",8:"ottanta",9:"novanta"}
    decine = int(number / 10)
    unita = number % 10
    if decine == 1 and unita > 0:        
        da_11_a_19 = {11: "undici", 12: "dodici", 13: "tredici", 14: "quattordici", 15: "quindici", 16: "sedici", 17: "diciassette", 18: "diciotto", 19: "diciannove"}
        ris = da_11_a_19[number]
    else:
        strUnita = getStrUnita(unita)
        strDecine = da_10_a_99[decine]
        if unita == 0:
            ris = strDecine
        elif unita == 1 or unita == 8:
            ris = strDecine[:-1] + strUnita
        else:
            ris = strDecine + strUnita 
    return str(ris)