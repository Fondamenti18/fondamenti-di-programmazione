''' while (cifre>0):
blocchi=blocchi+[n%1000]
n=n//1000
cifre-=3
for parte in blocchi:             stringa =[corrispondenza[1][temp]]    #controllare qui
                stringa=stringa[:-1]
                parola = parola + [stringa]'''
def conv(n):
    num=str(n)            #CONVERTE STRINGA IN NUMERO
    prima=['','uno','due','tre','quattro','cinque','sei','sette','otto','nove']
    sec=['dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
    parola=[]
    cifre=len(num)
    blocco=[]
    mille=["mille","mila"]
    milione=["unmilione","milioni"]
    miliardo=["unmiliardo","miliardi"]
    nu={1:sec,2:"venti",3:"trenta",4:"quaranta",5:"cinquanta",6:"sessanta",7:"settanta",8:"ottanta",9:"novanta"}
    corrispondenza={1:prima,2:nu,3:"cento",4:mille,5:mille,6:mille,7:milione,8:milione,9:milione,10:miliardo,11:miliardo,12:miliardo,13:'nulla'}
    blocchi=[]
    while (cifre>0):
        blocchi=blocchi+[n%1000]
        n=n//1000
        cifre-=3
    cifre1=len(num)
    finale = []
    blocchi.reverse()
    for parte in blocchi:
        print(parte)
        finale = finale + singolo(parte,cifre1)
        cifre1=cifre1-1
        while True:
            if(cifre1%3==0):
                break
            else:
                cifre1=cifre1-1
    finale = ''.join(finale)
    return (finale)
def singolo(blocchi,cifre):
    mille=["mille","mila"]
    milione=["unmilione","milioni"]
    miliardo=["unmiliardo","miliardi"]
    sec=['dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
    prima=['','uno','due','tre','quattro','cinque','sei','sette','otto','nove']
    nu={1:sec,2:"venti",3:"trenta",4:"quaranta",5:"cinquanta",6:"sessanta",7:"settanta",8:"ottanta",9:"novanta"}
    corrispondenza={1:prima,2:nu,3:"cento",4:mille,5:mille,6:mille,7:milione,8:milione,9:milione,10:miliardo,11:miliardo,12:miliardo,13:'nulla'}
    #print("hello")
    cifre1=0
    parola = []
    num=str(blocchi)  #stringa
    num1=len(num)
    if num1==1:         #convertitore signola cifra
        temp=int(num[0])
        #print(temp)
        parola = parola + [corrispondenza[1][temp]]
        #print(parola)
        cifre1=1
        #return(parola)
    if num1==2:               #converte due cifre e da 20 a 90
        cifre1=2
        if (num[0]!='1'):
            temp=int(num[0])  
                                    #20,30,40
            if num[1]=='1' or num[1]=='8':
                stringa = corrispondenza[2][temp]#se 8 è la decimale
                stringa=stringa[:-1]   #modificare
                parola = parola + [stringa]
            else:
                parola = parola + [corrispondenza[2][temp]] #altrimenti
            temp=int(num[1])
            parola = parola + [corrispondenza[1][temp]]
            #return(parola)
        else:                #converte due cifre da 10 a 19
            temp=int(num[1])               
            parola = parola + [corrispondenza[2][1][temp]]
            #return(parola)
            #parola = parola + [corrispondenza[          #it work!
    if num1==3:
        cifre1=3
        if num[0]!='1':            #es: duecento
            temp=int(num[0])
            parola = parola + [corrispondenza[1][temp]]#2
            parola = parola + [corrispondenza[3]]         #cento
        else:                                           #ok!!!!
            #print("heeello")
            parola = parola + [corrispondenza[3]]         #solo cento
        if num[1]!='8':          #diverso da 80
            if num[1]=='1':
                temp=int(num[2])
                parola = parola + [corrispondenza[2][1][temp]]  #10 a 19  ok non testato
               # print(parola)
                #return(parola)
                
            elif num[1]!='0':
                temp=int(num[1])
                #ok??
                #print(parola)
                if num[2]!='8' and num[2]!='1':                  #se le decine diverse da 8 o 1 U WAT
                    parola = parola + [corrispondenza[2][temp]]
                    print("ci siamo")
                    temp=int(num[2])
                    parola = parola + [corrispondenza[1][temp]]
                    #return(parola)
                else:                              #se 8 o 1
                    stringa = corrispondenza[2][temp]
                    stringa = stringa[:-1]
                    parola = parola + [stringa]      #toglie ultima cifra
                    print(parola)
                    temp=int(num[2])
                    parola  =parola + [corrispondenza[1][temp]]
                    #return(parola)
            else:                    #se cifra centrale è 0
                parola = parola + [corrispondenza[1][0]]
                temp=int(num[2])
                parola = parola + [corrispondenza[1][temp]]
        else:                   #con 80!!!!
               #ttanta!!!!
            if num[2]!='8' and num[2]!='1':                  #se le decine diverse da 8 o 1
                stringa=corrispondenza[2][8]
                stringa=stringa[1:]
                parola = parola + [stringa] 
                temp=int(num[2])
                parola = parola + [corrispondenza[1][temp]]
                #return(parola)
            else:                              #se 8 o 1
                stringa=corrispondenza[2][8]
                stringa=stringa[1:-1]
                parola = parola + [stringa] 
                temp=int(num[2])
                parola = parola + [corrispondenza[1][temp]]
                print(parola)
                #return(parola)
    print(cifre,cifre1)
    if cifre==4 or cifre==5 or cifre==6:
        if cifre1==1 and parola[0]=='uno':
            print("saveme")
            parola[0] = ""
            parola = parola + [corrispondenza[4][0]]
        else:
            parola = parola + [corrispondenza[4][1]]
    elif cifre==7 or cifre==8 or cifre==9:
        if cifre1==1:
            parola = parola + [corrispondenza[8][0]]
        else:
            parola = parola + [corrispondenza[8][1]]
    elif cifre>10:
        if cifre1==1:
            parola = parola + [corrispondenza[10][0]]
        else:
            parola =  parola + [corrispondenza[10][1]]
    
    return(parola)
                               
        
        
        
            
                    
                                   











            
                              
                               
