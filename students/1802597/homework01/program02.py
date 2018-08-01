''' In determinate occasioni ci capita di dover scrivere i numeri in lettere, 
ad esempio quando dobbiamo compilare un assegno. 
Puo' capitare che alcuni numeri facciano sorgere in noi qualche dubbio.

Le perplessita' nascono soprattutto nella scrittura dei numeri composti con 1 e 8. 
Tutti i numeri come venti, trenta, quaranta, cinquanta, ecc... elidono la vocale 
finale (la "i" per 20, la "a" per tutti gli altri) fondendola con la vocale iniziale 
del numero successivo; scriveremo quindi ventuno, ventotto, trentotto, 
cinquantuno ecc...

Il numero cento, nella formazione dei numeri composti con uno e otto, non si comporta 
cosi'; il numero "cento" e tutte le centinaia (duecento, trecento, ecc...), 
infatti, non elidono la vocale finale. Dunque non scriveremo centuno,  trecentotto ma centouno, 
trecentootto, ecc...

I numeri composti dalle centinaia e dalla decina "ottanta" invece tornano ad elidere 
la vocale finale; scriveremo quindi centottanta, duecentottanta,  ecc..., 
non centoottanta, duecentoottanta, ...

Il numero "mille" non elide in nessun numero composto la vocale finale; scriveremo 
quindi milleuno,  milleotto, milleottanta, ecc...

Altri esempi sono elencati nel file grade02.txt


Scrivere una funzione conv(n) che prende in input un intero n, con 0<n<1000000000000, 
e restituisce in output una stringa con il numero espresso in lettere

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''


def conv(n):
  lista_numero=[]
  parola=''  
  m = 3  
  b=False
  e =False
  c=0
  n1=''
  n2=''
  n3=''
  n4=''
  parole=[['', 'uno', 'due', 'tre', 'quattro','cinque','sei', 'sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove'], ['venti', 'trenta','quaranta','cinquanta','sessanta','settanta','ottanta', 'novanta'],['cento', 'duecento','trecento','quattrocento','cinquecento','seicento','settecento','ottocento','novecento']]
  parole_1=['vent', 'trent','quarant','cinquant','sessant','settant','ottant', 'novant']
  line=str(n)
  lunghezza = len(line)  
  if(lunghezza%3)== 0:
    lista_numero=[line[i:i+m] for i in range(0, len(line), m)]
  elif lunghezza==2 or lunghezza == 11 :
    line = '0' * (1)+line
    lista_numero=[line[i:i+m] for i in range(0, len(line), m)]
  elif lunghezza == 4:
    line = '0' * (2)+line
    lista_numero=[line[i:i+m] for i in range(0, len(line), m)]
  elif lunghezza == 8:
    line = '0' * (1)+line
    lista_numero=[line[i:i+m] for i in range(0, len(line), m)]
  elif lunghezza%3!=0:
    line = '0' * (lunghezza// 3)+line
    lista_numero=[line[i:i+m] for i in range(0, len(line), m)]  
  for i in lista_numero:
    numero=int(i)
    num=str(i)       
    if 1<=lunghezza<=2:
        parola = decina(numero,num,i,parole,line,parole_1,lista_numero)
    elif lunghezza == 3:
        parola = centinaia(numero,num,i,parole,line,parole_1,lista_numero)
    elif 4<=lunghezza <=5:
        if b == False:
            n1=decina(numero,num,i,parole,line,parole_1,lista_numero) 
            b = True
        elif b == True:
            n2=centinaia(numero,num,i,parole,line,parole_1,lista_numero)
    elif lunghezza ==6:
        if b == False:
            n1=centinaia(numero,num,i,parole,line,parole_1,lista_numero) 
            b = True
        elif b == True:
            n2=centinaia(numero,num,i,parole,line,parole_1,lista_numero) 
    elif 7<=lunghezza<=9:        
        if e==False:            
            n1=decina(numero,num,i,parole,line,parole_1,lista_numero)
            e=True
            c=1
        elif c==1: 
            n2=centinaia(numero,num,i,parole,line,parole_1,lista_numero) 
            c=2
        elif c==2:
            n3=centinaia(numero,num,i,parole,line,parole_1,lista_numero)
    elif 10<=lunghezza<=12:  
        if e==False:            
            n1=decina(numero,num,i,parole,line,parole_1,lista_numero)
            e=True
            c=1
        elif c==1: 
            n2=centinaia(numero,num,i,parole,line,parole_1,lista_numero) 
            c=2
        elif c==2:
            n3=centinaia(numero,num,i,parole,line,parole_1,lista_numero)
            c = 3
        elif c==3:
            n4=centinaia(numero,num,i,parole,line,parole_1,lista_numero)                
  if b==True:
      if int(lista_numero[0]) == 1:
          parola='mille'+n2
      else:
          parola=n1+'mila'+n2
  elif c == 2:
      if int(lista_numero[0]) == 1:
          parola='unmilione'+n2+'mila'+n3
      else:
          parola=n1+'milioni'+n2+'mila'+n3
  elif c ==3:
      if int(lista_numero[0]) == 1:
          parola='unmiliardo'+n2+'milioni'+n3+'mila'+n4
      else:
          parola=n1+'miliardi'+n2+'milioni'+n3+'mila'+n4
  return(parola)   
def decina(numero,num,i,parole,line,parole_1,lista_numero):
    decine=''
    n_str=str(numero)  
    if 0<=numero<20:
        decine=str(parole[0][numero])      
    elif numero==20 or numero == 30 or numero == 40 or numero == 50 or numero == 60 or numero == 70 or numero == 80 or numero == 90:
        decine=str(parole[1][(numero//10)-2])        
    elif 21<=numero<=99:
        if int(n_str[1:2])==1 or int(n_str[1:2])==8:      
            decine=str(parole_1[int(n_str[0:1])-2]) + str(parole[0][int(n_str[1:2])])
        else: 
            decine=str(parole[1][int(n_str[0:1])-2]) + str(parole[0][int(n_str[1:2])])      
    elif numero>99:
        decine =centinaia(numero,num,i,parole,line,parole_1,lista_numero)
    return decine
def centinaia(numero,num,i,parole,line,parole_1,lista_numero):
    centinaia='' 
    mezzo =''
    n_str=str(numero)
    uno=str(lista_numero[0])    
    if numero==100 or numero == 200 or numero == 300 or numero == 400 or numero == 500 or numero == 600 or numero == 700 or numero == 800 or numero == 900:
      centinaia=str(parole[2][(numero//100)-1])      
    elif 101<=numero<=999:
        if int(n_str[1:4]) >19:
            if int(uno[0:1])==1 or int(n_str[0:1]) == 1: 
                mezzo=str(parole_1[int(n_str[1:2])-2])    
                centinaia= "cento" +mezzo + str(parole[0][int(n_str[2:3])])               
            elif int(uno[0:1])==8 and int(n_str[1:4]) < 19:
                mezzo=str(parole_1[int(n_str[1:2])-2])
                centinaia= mezzo + str(parole[0][int(n_str[2:3])])
            elif 80<=int(n_str[1:4]) <=89 :               
                mezzo=str(parole_1[int(n_str[1:2])-2])
                centinaia=str(parole[0][numero//100])+ "cent" +mezzo + str(parole[0][int(n_str[2:3])])        
            elif int(n_str[2:3]) == 8 or int(n_str[2:3]) == 1:
                mezzo=str(parole_1[int(n_str[1:2])-2])
                centinaia=str(parole[0][numero//100])+ "cento" +mezzo + str(parole[0][int(n_str[2:3])])
            elif int(n_str[1:4])<80 or int(n_str[1:4])>89 :
                mezzo=str(parole[1][int(n_str[1:2])-2])
                centinaia=str(parole[0][numero//100])+ "cento" +mezzo + str(parole[0][int(n_str[2:3])])        
        elif int(n_str[1:4]) < 19:            
            mezzo=str(parole[0][int(n_str[1:3])])         
            centinaia=str(parole[0][numero//100])+ "cento" +mezzo         
    elif numero< 100:
      centinaia=decina(numero,num,i,parole,line,parole_1,lista_numero)
    return centinaia



        
    
    
    
    
    
