# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 11:47:35 2017

@author: utente
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


def conv_1(n):
    ls=['','uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove', 'dieci','undici', 'dodici', 'tredici', 'quattordici', 'qiuindici', 'sedici', 'diciassette', 'diciotto', 'diciannove']
    if (n<20):
        return ls[n]
    else:
        ls2=['vent', 'trent', 'quarant', 'cinquant', 'sessant', 'settant', 'ottant', 'novant']
        if n%10==1 or n%10==8:
            return (ls2[((n//10)-2)]+ls[(n%10)])
        elif n//10==2:
            return (ls2[(n//10)-2]+'i'+ ls[(n%10)])
        else:
            return (ls2[((n//10)-2)]+'a'+ls[(n%10)])        
        

def conv_2(n):
    if n<100:
        return conv_1(n%100)
    if n%100>79 and n%100<90:
        if n//100==1:
            return 'cent'+conv_1(n%100)
        return conv_1(n//100)+'cent'+conv_1(n%100)
    if n<200:
        return 'cento'+conv_1(n%100)
    return conv_1(n//100)+'cento'+conv_1(n%100)

def conv_3(n):
    if n<1000:
        return conv_2(n%1000)
    if n<2000:
        return 'mille'+conv_2(n%1000)
    return conv_2(n//1000)+'mila'+conv_2(n%1000)

def conv_4(n):
    if n<1000000:
        return conv_3(n%1000000)
    if n<2000000:
        return 'milione'+conv_3(n%1000000)
    return conv_3(n//1000000)+'milioni'+conv_3(n%1000000)

def conv_5(n):
    if n<1000000000:
        return conv_4(n%1000000000)
    if n<2000000000:
        return 'miliardo'+conv_4(n%1000000000)
    return conv_4(n//1000000000)+'miliardi'+conv_4(n%1000000000)
    
def conv(n):
    if n<100:
        return conv_1(n)
    elif n<1000:
        return conv_2(n)
    elif n<1000000:
        return conv_3(n)
    elif n<1000000000:
        return conv_4(n)
    else:
        return conv_5(n)
    