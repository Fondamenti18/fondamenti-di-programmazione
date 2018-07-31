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


Scrivere una funzione conv(n) che prende in input un intero n, con 0<n<1.000.000.000.000 
e restituisce in output una stringa con il numero espresso in lettere

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''  
def decine(n_s):
  l_0_9=['zero','uno','due','tre','quattro','cinque','sei','sette','otto','nove']
  l_10_19=['dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
  l_20_90=['venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta',]
  s=''
  s_appo=''
  t=n_s[-2:]
  ln=len(t)
  for i in range(0,10):
    if int(t[0])==0 or ln==1: 
      if i==int(t):
        s=l_0_9[i]
    elif int(t[0])==1: 
      if int(t[1])==i:
        s=l_10_19[i]
    elif int(t[0])==i: 
      if int(t[1])==0:
        s=l_20_90[i-2]
      else:           
        for j in range(1,10):
          if int(t[1])==j:
            if j==1 or j==8:
              s_appo=l_20_90[i-2]
              s=s_appo[:-1]+l_0_9[j]
            else:
              s=l_20_90[i-2]+l_0_9[j]
  return s
def centinaia(n_s):
  s_d=''
  s=''  
  ln=len(n_s)
  if int(n_s[0])==0 or ln<=2: 
      s=decine(n_s) 
  elif int(n_s[0])==1:
    if int(n_s[1])!=8:
      s='cento'+decine(n_s)
    else:
      s='cent'+decine(n_s) 
  elif int(n_s[1])!=8:
    s=decine(n_s[0])+'cento'+decine(n_s)   
  elif int(n_s[1])==8:
    s=decine(n_s[0])+'cent'+decine(n_s)
  return s  
def mr_ml_m(t,m):
  s=''
  m_1=''
  m_a=''
  if m==1:
    m_1='mille'
    m_a='mila'
  elif m==2:
    m_1='un milione'
    m_a='milioni'
  elif m==3:  
    m_1='un miliardo'
    m_a='miliardi'
  
  if centinaia(t)=='uno':
    s=m_1    
  else:
    s=centinaia(t)+m_a  
  return s 

def conv(n):
  'Scrivete qui il codice della funzione'
  n_s=str(n)
  ln=len(n_s)
  t=n_s[-3:]
  t_1=n_s[-6:-3]
  t_2=n_s[-9:-6]
  t_3=n_s[-12:-9]
  if ln>=1 and ln<=3:
    s_out=centinaia(t)
  elif ln>=4 and ln<=6 : 
    s_out=mr_ml_m(t_1,1)+centinaia(t)
  elif ln>=7 and ln<=9:
     s_out=mr_ml_m(t_2,2)+mr_ml_m(t_1,1)+centinaia(t)
  elif ln>=10 and ln<=12:
    a=n_s[0:2]
    b=n_s[2:5]
    s_out=mr_ml_m(t_3,3)+mr_ml_m(t_2,2)+mr_ml_m(t_1,1)+centinaia(t)
  return s_out



