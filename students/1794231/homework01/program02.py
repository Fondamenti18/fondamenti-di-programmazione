# -*- coding: utf-8 -*-

def conv(n):
    if n<1000:
        risp=centinaia(n)
    elif n<1000000:
        if n//1000==1:
            risp='mille'+centinaia(n-1000)
        else:
            risp=centinaia(n//1000)+'mila'+centinaia(n%1000)
    elif n<1000000000:
        if (n%1000000)//1000==1:
            risp='mille'+centinaia(n%1000000-1000)
        else:
            risp=centinaia((n%1000000)//1000)+'mila'+centinaia(n%1000)
        if n//1000000==1:
            risp='unmilione'+risp
        else:
            risp=centinaia(n//1000000)+'milioni'+risp
    elif n<1000000000000:
        if (n%1000000)//1000==1:
            risp='mille'+centinaia(n%1000000-1000)
        else:
            risp=centinaia((n%1000000)//1000)+'mila'+centinaia(n%1000)
        if (n%1000000000)//1000000==1:
            risp='unmilione'+risp
        else:
            risp=centinaia((n%1000000000)//1000000)+'milioni'+risp
        if n//1000000000==1:
            risp='unmiliardo'+risp
        else:
            risp= centinaia(n//1000000000)+'miliardi'+risp
    return risp

def centinaia (n):
    lista = ['', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove', 'dieci', 'undici', 'dodici', 'tredici',
              'quattordici', 'quindici', 'sedici', 'diciassette', 'diciotto', 'dicianove', 'venti', 'trenta', 'quaranta', 'cinquanta',
              'sessanta', 'settanta', 'ottanta', 'novanta', 'cento', 'vent', 'trent', 'quarant', 'cinquant',
              'sessant', 'settant', 'ottant', 'novant']
    un=n%10
    ce=n//100
    de=(n%100-un)//10
    if de==1:
        stringa=lista[10+un]
    else:
        stringa= lista[un]
        if de!=0:
            if un!=8 and un!=1:
                stringa=lista[18+de]+stringa
            else:
                stringa=lista[27+de]+stringa
    if n>99:
        if de==8:
            stringa='cent'+stringa
        else:
            stringa='cento'+stringa
        if ce!=1:
            stringa=lista[ce]+stringa
    return stringa