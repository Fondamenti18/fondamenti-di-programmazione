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
 if n < 0 or n >= 1000000000000:
  pass #inserire msg di errore
 
 s = ""
 if n >= 1000000000:
  m = n // 1000000000 % 1000
  if m == 1:
   s += "unmiliardo"
  else:
   s += conv(m) + "miliardi"
 
 if n >= 1000000:
  m = n // 1000000 % 1000
  if m == 1:
   s += "unmilione"
  else:
   s += conv(m) + "milioni"
 
 if n >= 1000:
  m = n // 1000 % 1000
  if m == 1:
   s += "mille"
  else:
   s += conv(m) + "mila"
 
 if n >= 100:
  c = n // 100 % 10
  if c == 1:
   s += "cento"
  elif c > 1:
   s += conv(c) + "cento"
  d = n // 10 % 10
  if c!=0 and d == 8:
   s = s[:-1]
 
 if n >= 10:
  d = ("", ("dieci", "undici", "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette", "diciotto", "diciannove", "venti"), "venti", "trenta", "quaranta", "cinquanta", "sessanta", "settanta", "ottanta", "novanta")
  i = n // 10 % 10
  u = n % 10
  if i == 1:
   return s + d[i][u]
  s += d[i]
  if (u == 8 or u == 1) and i > 0:
   s = s[:-1]
 
 u = ("", "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove")
 s += "zero" if n == 0 else u[n%10]
 
 return s