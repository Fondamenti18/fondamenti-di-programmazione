

def conv(num):
    stringa=""
    erow=str(num)
    controllo=0
    myiter= iter(range(0,len(erow)))
    i=0
    for i in myiter:

        if(len(erow)-i)==12:                               #12 cifre
            if(erow[i]=="0"):
                stringa+=""
            elif(erow[i]=="1"):
                stringa+="cento"
            else:
              if (erow[i]== 8) and (erow[i+1]==1):
                stringa+="ottant"
              else:
                  stringa+=genera(erow[i])
                  if(erow[i+1]=="8"):
                    stringa+="cent"
                  else:
                    stringa+="cento"
                  
                  
        elif(len(erow)-i)==11:                               #11 cifre
            if(erow[i]=="0"):
                stringa+=""
            else:
                if(erow[i]=="1") or (erow[i+1]=="0"):
                  stringa+=genera(erow[i]+erow[i+1])
                  next(myiter, None)
                else:
                   if (erow[i]== 8) and (erow[i+1]==1):
                    stringa+="ottantuno"
                    next(myiter, None)
                   else:
                    stringa+=genera(erow[i]+"0")
            if (erow[i+1]==0):
              stringa+="miliardi"
        
        elif(len(erow)-i)==10:                                 #10cifre
            if(erow[i]=="1") and (erow[i-1]==0):
               stringa+="unmiliardo"
            else:
                stringa+=genera(erow[i])+"miliardi"

        elif(len(erow)-i)==9:                               #9 cifre
            if(erow[i]=="0"):
                stringa+=""
            elif(erow[i]=="1"):
                stringa+="cento"
            else:
                stringa+=genera(erow[i])
                if(erow[i+1]=="8"):
                  stringa+="cent"
                else:
                  stringa+="cento"
    
   


        elif(len(erow)-i)==8:                                 #8cifre
               stringa+=genera(erow[i]+"0")
               if(erow[i+1]=="1") or(erow[i+1]=="8"):#################################################
                    stringa=stringa[:-1]###############################################################



        elif(len(erow)-i)==7:                                 #7cifre
            if(erow[i]=="1"):
              if (erow[i-1]):
                stringa+="unomilioni"
              else:
               stringa+="unmilione"
            else:
                stringa+=genera(erow[i])+"milioni"
               

        elif(len(erow)-i)==6:                               #6 cifre
            if(erow[i]=="0"):
                stringa+=""
            elif(erow[i]=="1"):
                stringa+="cento"
                if(erow[i+1]=="8"):#################################################
                    stringa=stringa[:-1]###############################################################
            else:
                stringa+=genera(erow[i])
                if(erow[i+1]==8):
                  stringa+="cent"
                else:
                  stringa+="cento"
                if(erow[i+1]=="1") or(erow[i+1]=="8"):#################################################
                    stringa=stringa[:-1]###############################################################
                
        
        elif(len(erow)-i)==5:                               #5 cifre
            if(erow[i]=="0"):
                stringa+=""
            else:
                if(erow[i]=="1") or (erow[i+1]=="0"):
                  stringa+=genera(erow[i]+erow[i+1])
                  next(myiter, None)
                else:
                  if(erow[i]=="8") and (erow[i+1]=="8"):
                    stringa+="ottant"
                  else:
                   stringa+=genera(erow[i]+"0")
            if (erow[i+1] == 0):
                  stringa+="mila"
                
              
        elif(len(erow)-i)==4:                                 #4cifre
            if(erow[i]=="1") and (erow[i-1]=="0") and (erow[i-2]=="0"):
               stringa+="mille"
            else:
                 if(i==0):
                  stringa+="mille"
                 else:
                  stringa+=genera(erow[i])+"mila"
        elif(len(erow)-i)==3:                               #3 cifre
            if(erow[i]=="0"):
                stringa+=""
            elif(erow[i]=="1"):
                stringa+="cento"
              
            else:
                stringa+=genera(erow[i])
                if(erow[i+1]=="8"):
                   stringa+="cent"
                else:
                  stringa+="cento"
                
        elif(len(erow)-i)==2:                               #2 cifre
            if(erow[i]=="0"):
                stringa+=""
            elif(erow[i]=="1"):
                stringa+=genera(erow[i]+erow[i+1])
                controllo=1
            else:
                stringa+=genera(erow[i]+"0")
                if(erow[i+1]=="1") or(erow[i+1]=="8"):
                    stringa=stringa[:-1]
                    
                


        elif(((len(erow)-i)==1)and(controllo==0)):                               #1 cifra
            if(erow[i]=="0"):
                stringa+=""
            else:
                stringa+=genera(erow[i])
    
    return stringa    

def genera(num):
    if(num=="1"):
        return "uno"
    elif(num=="2"):
        return "due"
    elif(num=="3"):
        return "tre"
    elif(num=="4"):
        return "quattro"
    elif(num=="5"):
        return "cinque"
    elif(num=="6"):
        return "sei"
    elif(num=="7"):
        return "sette"
    elif(num=="8"):
        return "otto"
    elif(num=="9"):
        return "nove"
    elif(num=="0"):
        return ""

    elif(num=="10"):
        return "dieci"
    elif(num=="11"):
        return "undici"
    elif(num=="12"):
        return "dodici"
    elif(num=="13"):
        return "tredici"
    elif(num=="14"):
        return "quattordici"
    elif(num=="15"):
        return "quindici"
    elif(num=="16"):
        return "sedici"
    elif(num=="17"):
        return "diciassette"
    elif(num=="18"):
        return "diciotto"
    elif(num=="19"):
        return "diciannove"
    elif(num=="20"):
        return "venti"
    elif(num=="30"):
        return "trenta"
    elif(num=="40"):
        return "quaranta"
    elif(num=="50"):
        return "cinquanta"
    elif(num=="60"):
        return "sessanta"
    elif(num=="70"):
        return "settanta"
    elif(num=="80"):
        return "ottanta"
    elif(num=="88"):
      return "ottantotto"
    elif(num=="90"):
        return "novanta"