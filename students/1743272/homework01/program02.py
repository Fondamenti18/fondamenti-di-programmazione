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


Scrivere una funzione conv(n) che prende in input un intero n, con 0 < n < 1 000 000 000 000, 
e restituisce in output una stringa con il numero espresso in lettere

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''


def conv(n):
   'Scrivete qui il codice della funzione'

   unita = ['','uno','due','tre','quattro','cinque','sei','sette','otto','nove',
            'dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
   decine = ['','','venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
   cento = ['','cento','duecento','trecento','quattrocento','cinquecento','seicento','settecento','ottocento','novecento']
   scan = str(n)

   def traduzioneCen(scan):
      if (len(scan)==2):
         scan = '0'+scan
      if (len(scan)==1):
         scan = '00'+scan
      cen = int(scan[0:1])
      if(int(scan[1:2])==1):
         dec = 0
         uni = int(scan[1:3])
      else:
         dec = int(scan[1:2])
         uni = int(scan[2:3])
      if((int(scan[2:3])==1 and int(scan[1:2])!=0)):
         elid = decine[dec]
         traduzione = cento[cen]+elid[:-1]+'uno'  
      elif(int(scan[2:3])==8 and int(scan[1:2])!=0):
         elid = decine[dec]
         traduzione = cento[cen]+elid[:-1]+'otto'   
      else:
         traduzione = cento[cen]+decine[dec]+unita[uni]
      return traduzione
   
   def traduzioneM(scan):
      if (len(scan)==5):
         scan = '0'+scan
      if (len(scan)==4):
         scan = '00'+scan
      cen = int(scan[0:1])
      if(int(scan[1:2])==1):
         dec = 0
         uni = int(scan[1:3])
      else:
         dec = int(scan[1:2])
         uni = int(scan[2:3])
      if(int(scan[0:3])==1):
         traduzione = 'mille'
      else:
         traduzione = cento[cen]+decine[dec]+unita[uni]+'mila'
      return traduzione

   def traduzioneMM(scan):
      if (len(scan)==8):
         scan = '0'+scan
      if (len(scan)==7):
         scan = '00'+scan
      cen = int(scan[0:1])
      if(int(scan[1:2])==1):
         dec = 0
         uni = int(scan[1:3])
      else:
         dec = int(scan[1:2])
         uni = int(scan[2:3])
      traduzione = cento[cen]+decine[dec]+unita[uni]+'milioni'
      return traduzione
   


   if (int(scan)<0):
      print('error')
   if(int(scan)==0):
      print('zero')
   out = []  
   if (len(scan)<4): 
      tradC = (traduzioneCen(scan))
      out = tradC
      
   elif (len(scan)<7):
      tradM=traduzioneM(scan)
      if(len(scan)==6): scan = scan[3:6] 
      elif(len(scan)==5): scan = scan[2:5] 
      elif(len(scan)==4): scan = scan[1:4] 
      tradC = (traduzioneCen(scan))
      out = tradM+tradC
      
   elif (len(scan)<10):
      tradMM = traduzioneMM(scan)
      if(len(scan)==9): scan = scan[6:9] 
      elif(len(scan)==8): scan = scan[5:8] 
      elif(len(scan)==7): scan = scan[4:7]
      tradM = traduzioneM(scan)
      if(len(scan)==6): scan = scan[3:6] 
      elif(len(scan)==5): scan = scan[2:5] 
      elif(len(scan)==4): scan = scan[1:4] 
      tradC = (traduzioneCen(scan))
      out = tradMM+tradM+tradC
   return out