def conv(n):
   centinaia = n % 1000
   n = n // 1000
   migliaia = n % 1000
   n= n // 1000
   milione = n % 1000
   n= n // 1000
   miliardo = n % 1000
   n = n // 1000
   bilione = n % 1000
   n= n // 1000
   trilione = n % 1000
   n= n // 1000
   risultato = ''
   if trilione>1:
       risultato += scomponi(trilione) + 'trilioni'
   elif trilione==1:
       risultato += 'untrilione' 
   if bilione>1:
       risultato += scomponi(bilione) + 'bilioni'
   elif bilione==1:
       risultato += 'unbilione' 
   if miliardo>1:
       risultato += scomponi(miliardo) + 'miliardi'
   elif miliardo==1:
      risultato += 'unmiliardo'
   if milione>1:
       risultato += scomponi(milione) + 'milioni'
   elif milione==1:
       risultato += 'unmilione' 
   if migliaia>1:
       risultato += scomponi(migliaia) + 'mila'
   elif migliaia==1:
       risultato += 'mille' 
   if centinaia:
       risultato += scomponi(centinaia)  
   return risultato

def scomponi (n):
   numero = n % 100
   numero2 = n // 10
   n_unita=['zero','uno','due','tre','quattro','cinque','sei','sette','otto','nove']
   n_decimali=['zero','dieci','venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
   n_centinaia=['zero','cento','duecento','trecento','quattrocento','cinquecento','seicento','settecento','ottocento','novecento']
   n_numeri={11:'undici',12:'dodici',13:'tredici',14:'quattordici',15:'quindici',16:'sedici',17:'diciassette',18:'diciotto',19:'dicianove',
   21:'ventuno',31:'trentuno',41:'quarantuno',51:'cinquantuno',61:'sessantuno',71:'settantuno',81:'ottantuno',91:'novantuno',
   28:'ventotto',38:'trentotto',48:'quarantotto',58:'cinquantotto',68:'sessantotto',78:'settantotto',88:'ottantotto',98:'novantotto'} 
   n_numeri2={18:'cent',28:'duecent',38:'trecent',48:'quattrocent',58:'cinquecent',68:'seicent',78:'settecent',88:'ottocent',98:'novecent'}
   unita = n % 10
   n = n // 10
   decine = n % 10
   n = n // 10
   centinaia = n % 1000
   n = n // 1000
   risultato=''
   if numero2 in n_numeri2.keys():
       risultato += n_numeri2[numero2]
   else:
       if centinaia>1:
           risultato += n_centinaia[centinaia]
       elif centinaia==1:
           risultato += 'cento'
   if numero in n_numeri.keys():
       risultato += n_numeri[numero] 
   else:
       if decine:
           risultato += n_decimali[decine]
       if unita:
           risultato += n_unita[unita]   
   return risultato