# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 17:55:21 2017

@author: Lorenzo
"""

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



def conv(j):
   if j==0:
       return ''
   elif j<=19:
       return ('uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove', 'dieci', 'undici', 'dodici', 'tredici', 'quattordici', 'quindici', 'sedici', 'diciassette', 'diciotto', 'diciannove')[j-1]
   elif j<=99:
       decine=('venti', 'trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta')
       letter=decine[int(j/10)-2]
       z=j%10
       if z==1 or z==8:
           letter=letter[:-1]
       return letter + conv(j%10)
   elif j<=199:
       return 'cento'+conv(j%100)
   elif j<=999:
       m=j%100
       m=int(m/10)
       letter='cent'
       if m!=8:
           letter=letter+'o'
       return conv(int(j/100))+ letter+ conv(j%100)
   elif j<=1999:
       return 'mille'+conv(j%1000)
   elif j<=999999:
       return conv(int(j/1000))+'mila'+conv(j%1000)
   elif j<=1999999:
       return 'unmilione'+conv(int(j%1000000))
   elif j<=999999999:
       return conv(int(j/1000000))+'milioni'+conv(j%1000000)
   elif j<=1999999999:
       return 'unmiliardo'+ conv(j%1000000000)
   else:
       return conv(int(j/1000000000))+'miliardi'+conv(j%1000000000)
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   