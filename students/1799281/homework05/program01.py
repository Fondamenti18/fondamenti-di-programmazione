'''
FUNZIONI:
DECODIFICATORE: OUTPUT E RESET QUANDO CAMBIA CODICE
TENTATIVI: FORNISCE L'OUTPUT. PROVA LE COMBINAZIONI CHE NON SONO NEL DIZIONARIO SBAGLIATO, E SONO NEL DIZIONARIO GIUSTO (SE CREATI)
NON FORNISCE PIù DI UNA VOLTA LO STESSO TENTATIVO
CASI: LA RARA OCCASIONE IN CUI ESCONO DUE COBINAZIONI TIPO (6,1) CONFRONTA 3 STRINGHE PER VEDERE SE TUTTE E TRE HANNO 6 NUMERI DIVERSI POSIZIONI DIVERSE E 1 UGUALE STESSA POSIZIONE, O VICEVERSA
CASIY: DOVE LA RISPOSTA è (5,2)(6,3) PRENDE IL MAGGIORE. SE CI SONO TANTI NUMERI UGUALI UGUALE POSIZIONE QUANTO IL NUMERO MAGGIORE, LI INSERISCE NEL DIZIOANRIO DEI GIUSTI
CASIX: CONTRARIO DI CASIY, CON AGGIUNTA DI COPPIE UGUALI (3,3)(4,4)
LISTE,1,2: FORNISCONO 3-4 LISTE CASUALI AI VARI METODI CASI, LE 3 LISTE VENGONO SALVATE IN UN DIZIONARIO PER FAR Sì CHE NON VENGA PASSATA PIù DI UNA VOLTA LA STESSA COMBINAZIONE, ANCHE IN ORDINE CAMBIATO.

























 for x in range(flag1):
        if x==0:
            continue
        if mas in configurazione[x][1] and configurazione[x][1][0]!=configurazione[x][1][1]:    #<--- importante
            if configurazione[x][0] in gia:
                continue
            else:
                lista=lista+[configurazione[x][0]]
            print("il massimo e' ..........",mas)
            print("la lista e' ------------------",lista)
    for x in lista:
        gia=gia+[x]
    for x in range((len(lista)-1)):
        for j in range(len(lista[0])):
            if lista[x][j]==lista[x+1][j]:
                count+=1                                 #count: numeri uguali al posto giusto
                print("il contatore e'    ",count)
                d[j]=lista[x][j]
                print("dizionario---------------->",d)
    if count==(mas*2):   #(len(lista)-1)
        for x in d.keys():
            if x not in giuste.keys():
                print("!")
                crea1=1
                giuste.setdefault(x,[]).append(d[x])
                print("dizionario giusto ----------->",giuste)
        












ATTENZIONE: NON usate lettere accentate ne' nel codice ne' nei commenti
def decodificatore(configurazione):
    n=configurazione[0]
    x='0123456789'
    risposta=[]
    for _ in range(n):
        y=random.choice(x)
        risposta+=[int(y)]
        x=x.replace(y,'')
    print (risposta,"------",configurazione,"------",len(configurazione))
    return(risposta)

'''

import random                      #un macello di controlli inutili e perditempo, non l'ho ancora ottimizzato
x='0123456789'
flag=0
flag1=0
num=""
controllo=False
sbagliate=[]
sbagliati=[]
dizio={1000000:[]}      #DIZIONARIO dove sono registrate tutte le posizioni dei numeri sbagliati
creato=0
rand=[]
giuste={}
crea1=0
a=0
b=0
c=[]
e=0
mas=0
gia=0
me={10000:[]}
prese=[]
dd=[]
me1={10000:[]}
prese1=[]
gia1=0
me2={10000:[]}
prese2=[]
gia2=0
uu=[]
# ESEMPIO di strategia che tira a caso una combinazione di N valori anche ripetuti
def decodificatore(configurazione):
    global x
    global flag                     
    global num
    global flag1
    global controllo
    global sbagliate
    global dizio
    global creato
    global sbagliati
    global a
    global b
    global c
    global e
    global mas
    global prese
    global me
    global gia
    global giuste
    global c
    global dd
    global uu
    n=configurazione[0]
    if len(configurazione)==1:        #Idea generale: creo un dizionario e come chiavi metto le posizioni, come values i numeri
        flag=0                        #cosi' so in quale posizione quali numeri posso scegliere e quali no
        flag1=0                       #nei dizionari sono segnati i numeri da NON scegliere per quella posizione
        dizio={10000000:[]}
        num=""
        controllo=False              #con soli i numeri sbagliati sicuramente (8,0) (7,0) ecc.. ci mette troppo (30 tentativi).
        sbagliate=[]
        creato=0                     #controllo = True :    quando i numeri di numeri sono = a n
        x='0123456789'
        sbagliati=[]
        giuste={}
        crea1=0
        prese=[]
        me={10000:[]}
        gia=0
        giuste={}
        c=[]
        tempo=0
        me1={10000:[]}
        prese1=[]
        gia1=0
        dd=[]
        me2={10000:[]}
        prese2=[]
        gia2=0
        uu=[]
    if flag>0 :
        sbagliati=sbagliati+[configurazione[flag1][0]]
        if 1 in configurazione[flag1][1] and controllo==False:             #starting
            num=num+str(configurazione[flag1][0][0])
        elif 1 not in configurazione[flag1][1] and controllo==False :      #starting
            flag-=1
        if 0 in configurazione[flag1][1] and controllo==True:              #se la configurazione e' tipo (6,0),(7,0) ecc..
 
            for i in configurazione[flag1][0]:
               
                if creato==1:
                    if i not in dizio[configurazione[flag1][0].index(i)]:
                       # print("aggiungo questo -->",i)
                        dizio.setdefault(configurazione[flag1][0].index(i),[]).append(i)
                else:
                    dizio.setdefault(configurazione[flag1][0].index(i),[]).append(i)   #as always comando utile per mettere chaivi e valori
            creato=1            #<---------- NON CANCELLARLO PIU' PER SBAGLIO
        #if 1 in configurazione[flag1][1] and controllo==True: #[1]
           # sbagliate=sbagliate+[configurazione[flag1][0]]
        if controllo== True:  
           
            a = configurazione[flag1][1][0]
            b = configurazione[flag1][1][1]
            if (a==1 or b==1) and (a!=0 and b!=0):
                uu=uu+[1]
                if uu.count(1)>=4:
                    
                    casi(n,configurazione)
            if a!=1 and b!=1 and a!=0 and b!=0:
                mas=max(a,b)
                e=min(a,b)
                c=c+[mas]
                dd=dd+[e]
               # print("MAS--->---",mas) 
                #if mas in c:
                if c.count(mas)>=3:
                    #    print("C -->",c,"MAS--->",mas)
                        casiy(configurazione)
                if dd.count(e)>=3:
                    minore(configurazione)
                #c=c+[mas]
        #casi(n,configurazione)
        
                
                
            












          
#    if len(sbagliate)==3:
      #  casi(n-1)
   # if len(sbagliate)==2:
        #casix(n-1,len(sbagliate))

    if flag==n:
        controllo=True
       
        risposta=tentativi(n)
        flag1+=1
        return(risposta)    
    y=random.choice(x)
    risposta=[]
    for _ in range(n):
        risposta+=[int(y)]
    x=x.replace(y,'')
   
    flag+=1
    flag1+=1
   
    return(risposta)
def tentativi(n):
    num1=num
    num2=num
    risposta=[]
    risp=""
    temp=0
    if crea1==0:
        for t in range(n):
            num1=num2
            if creato==1:
                for i in dizio[t]:
                    num1=num1.replace(str(i),'')
           # print(num2,"---->",num1)
            if num1=='':
                risposta=tentativi(n)
                for x in sbagliati:
                    #print("XXX",x)
                    if risposta==x:
                        #print("!!!!!!!!")
                        risposta=tentativi(n)
                #print(risposta)
                return(risposta)
            y=random.choice(num1)
            risposta+=[int(y)]
            num2=num2.replace(y,'')
           # print("risposta ---...---..--->",risposta)
        for x in sbagliati:
            #print("UP---------")
            if risposta==x:
              #  print("DIZIO><>>>>>>>",dizio)
                risposta=tentativi(n)
                #return(risposta)
       # if risposta in sbagliati:  #.-------------
         #   print("UP---------")
           # tentativi(n)          #.--------
        return(risposta)
    else:                 #<------------ MODIFICARE QUI
        #num1=num
        for t in range(n):
            if t in giuste.keys() and giuste[t]!=[]:
                risposta=risposta+giuste[t]
                print("àààààààààààà",risposta)
                num1=num1.replace(str(giuste[t][0]),'')
            else:
                if num1=='':
                    risposta=tentativi(n)
                    for t in sbagliati:
            #print("UP---------")
                        if risposta==t:
                            tentativi(n)
                    return(risposta)
                y=random.choice(num1)
                num1=num1.replace(str(y),'')
                if y in dizio[t]:
                    risposta=tentativi(n)
                risposta=risposta+[int(y)]
                
                
    return(risposta)
            


def casi(n,configurazione):   
    global giuste
    global crea1
    global gia2
    global dizio
    sba=0
    temp=0
    lista=[]
    count=0
    d={}
    d1={}
    lista=liste2(configurazione)
    if lista==[]:
        return()

    for j in range(len(lista[0])):
            if lista[0][j]==lista[1][j]==lista[2][j]==lista[3][j]:
                count+=1                                 
                
                d[j]=lista[0][j]
            else:
                d1[j]=lista[0][j]            
    if count==(n-1):
       # print("liste----> ",lista[0],lista[1],lista[2],lista[3])
        for x in d.keys():
            if x not in giuste.keys():
              #  print("!")
                crea1=1
                giuste.setdefault(x,[]).append(d[x])
               # print("dizionario giusto ----------->  casi",giuste)
        for x in d1.keys():
            if x not in dizio.keys():
               # print("!")
                dizio.setdefault(x,[]).append(d1[x])
                #print("dizionario giusto ----------->    casi",giuste)
    if crea1==0:
        casi(n,configurazione)
'''    elif count==1:
        print("liste----> casi",lista[0],lista[1],lista[2],lista[3])
        for x in d1.keys():
            if x not in dizio.keys():
                crea1=1
                dizio.setdefault(x,[]).append(d1[x])
        for x in d.keys():
            if x not in giuste.keys():
                print("!")
                crea1=1
                giuste.setdefault(x,[]).append(d[x])
                print("dizionario giusto ----------->    casi",giuste)
                
    '''        

                

'''def casix(n,l):
    global sbagliate                
    global giuste
    global crea1
    a=sbagliate[0]
    b=sbagliate[1]               
    cont=0                           
    temp=0
    cont1=0
    for i in range(len(a)):
        if a[i]==b[i]:
            cont+=1
        elif a[i]!=b:
            cont1+=1
            temp=i
            if cont1>1:
                sbagliate=sbagliate[:-1]  
                return()
    if cont==n:
        for x in range(n):
            if x != temp1:
                giuste.setdefault(x,[]).append(a[x])
            else:
                giuste.setdefault(x,[])
        crea1=1
    sbagliate=sbagliate[:-1]  '''
            
                   
    
def casiy(configurazione):
    global giuste
    global crea1
    global gia
    lista=[]
    count=0
    count1=0
    d={}
    lista=liste(configurazione)
    if lista==[]:
        return()
    #for x in range((len(lista)-1)):
    for j in range(len(lista[0])):
            if lista[0][j]==lista[1][j]==lista[2][j]:
                count+=1                                 #count: numeri uguali al posto giusto
                #print("il contatore e'    ",count)
                d[j]=lista[0][j]
                #print("dizionario---------------->     casiy",d)
    if count==(mas*2):   #(len(lista)-1)
        for x in d.keys():
            if x not in giuste.keys():
                #print("!")
                crea1=1
                giuste.setdefault(x,[]).append(d[x])
                #print("dizionario giusto ----------->    casiy",giuste)
    if crea1==0:
        casiy(configurazione)
            
def liste(configurazione):                  #questa parte e' decisamente un macello anche se funziona
    global giuste                           #un sacco di operazioni ripetute che non servono
    global gia
    global me
    global prese
    lista=[]                                #dovrebbe dare 3 liste casuali da configurazione, senza ridare 3 volte le stesse liste in ordine diverso
    passo=[]
    a=0

    
    for x in range(flag1+1):
        if x==0:
            continue
        if mas in configurazione[x][1] and configurazione[x][1][0]!=configurazione[x][1][1]:    #<--- importante
            lista=lista+[configurazione[x][0]]

    #print("LISTA --->",lista,"MAS----",mas)
    for x in lista:
        if x not in prese:
            a=1
    if a==0:
        return([])
        
    for x in range(3):
        y=random.choice(lista)
        lista.remove(y)
        passo=passo+[y]
        prese=prese+[y]
    for j in me.keys():
        count=0
        for x in passo:
            if x in me[j]:
                count+=1
            if count==3:
                passo=liste(configurazione)
                return(passo)
    for x in passo:
        me.setdefault(gia,[]).append(x)
    gia+=1
   # print("PRESE ------",prese)
   # print("ME-------->",me)    
   # print("PASSO--------->",passo)
    return(passo)

        
        
            
def minore(configurazione):
    global giuste
    global crea1
    lista=[]
    count=0
    count1=0
    d={}
    lista=liste1(configurazione)
    if lista==[]:
        return()
    #for x in range((len(lista)-1)):
    for j in range(len(lista[0])):
            if lista[0][j]==lista[1][j]==lista[2][j]:
                count+=1                                 #count: numeri uguali al posto giusto
                #print("il contatore e'    ",count)
                d[j]=lista[0][j]
               # print("dizionario---------------->     minore",d)
    if count==(e*2):   #(len(lista)-1)
        for x in d.keys():
            if x not in giuste.keys():
               # print("!")
                crea1=1
                giuste.setdefault(x,[]).append(d[x])
               # print("dizionario giusto ----------->     minore",giuste)
    if crea1==0:
        minore(configurazione)
              
                
            
            
def liste1(configurazione):                  #questa parte e' decisamente un macello anche se funziona
    global giuste                           #un sacco di operazioni ripetute che non servono
    global prese1
    global me1
    global gia1
    lista=[]                                # dovrebbe dare 3 liste casuali da configurazione, senza ridare 3 volte le stesse liste in ordine diverso
    passo=[]
    a=0

    
    for x in range(flag1+1):
        if x==0:
            continue
        if e in configurazione[x][1] and configurazione[x][1][0]!=0 and configurazione[x][1][1]!=0 :    #<--- importante
            lista=lista+[configurazione[x][0]]

  #  print("LISTA --->",lista,"MAS----",mas)
    for x in lista:
        if x not in prese1:
            a=1
    if a==0:
       # print("lllllllllllll")
        return([])
        
    for x in range(3):
        y=random.choice(lista)
        lista.remove(y)
        passo=passo+[y]
        prese1=prese1+[y]
    for j in me1.keys():
        count=0
        for x in passo:
            #print("X ....",x,"----->",me1[j])
            if x in me1[j]:
               # print("RIMUOVO")
                count+=1
            if count==3:
                passo=liste1(configurazione)
               # print("PASSO----------->",passo)
                return(passo)
    for x in passo:
        me1.setdefault(gia1,[]).append(x)
    gia1+=1
   # print("PRESE ------",prese)
   # print("ME-------->",me)    
   # print("PASSO--------->",passo)
    return(passo)
    
    
def liste2(configurazione):                  #questa parte e' decisamente un macello anche se funziona
    global giuste                           #un sacco di operazioni ripetute che non servono
    global prese2
    global me2
    global gia2
    lista=[]                                # dovrebbe dare 3 liste casuali da configurazione, senza ridare 3 volte le stesse liste in ordine diverso
    passo=[]
    a=0

    
    for x in range(flag1+1):
        if x==0:
            continue
        if 1 in configurazione[x][1] and configurazione[x][1][0]!=0 and configurazione[x][1][1]!=0 :    #<--- importante
            lista=lista+[configurazione[x][0]]

  #  print("LISTA --->",lista,"MAS----",mas)
    for x in lista:
        if x not in prese2:
            a=1
    if a==0:
       # print("lllllllllllll")
        return([])
        
    for x in range(4):
        y=random.choice(lista)
        lista.remove(y)
        passo=passo+[y]
        prese2=prese2+[y]
    for j in me2.keys():
        count=0
        for x in passo:
            #print("X ....",x,"----->",me1[j])
            if x in me2[j]:
               # print("RIMUOVO")
                count+=1
            if count==3:
                passo=liste2(configurazione)
               # print("PASSO----------->",passo)
                return(passo)
    for x in passo:
        me2.setdefault(gia2,[]).append(x)
    gia2+=1
   # print("PRESE ------",prese)
   # print("ME-------->",me)    
   # print("PASSO--------->",passo)
    return(passo)
                    











