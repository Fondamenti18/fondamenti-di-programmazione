#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 18:33:32 2017

@author: patriziogermani
"""
def conv(n):
    if n <= 19:
         return ("", "uno", "due", "tre", "quattro", "cinque",
                "sei", "sette", "otto", "nove", "dieci", 
                "undici", "dodici", "tredici", 
                "quattordici", "quindici", "sedici", 
                "diciassette", "diciotto", "diciannove")[n]
    if n <= 99:
        decine = ("venti", "trenta", "quaranta",
                  "cinquanta", "sessanta", 
                  "settanta", "ottanta", "novanta")
        lettera = decine[int(n/10)-2]
        voc= n%10
        if voc== 1 or voc== 8:
            lettera=lettera[:-1]
        return lettera + conv(n%10)
    if n <= 199:
        return "cento" + conv(n%100)
    if n <= 999:
        mil = n%100
        mil= int(mil/10)
        lettera= "cent"
        if mil != 8:
            lettera=lettera + "o"
        return conv( int(n/100)) + \
               lettera + \
               conv(n%100)
    if n<= 1999 :
         return "mille" + conv(n%1000)
    if n<= 999999:
         return conv(int(n/1000)) + \
               "mila" + \
               conv(n%1000)
    if n <= 1999999:
         return "unmilione" + conv(n%1000000)
    if n <= 999999999:
         return conv(int(n/1000000))+ \
               "milioni" + \
               conv(n%1000000)
    if n <= 1999999999:
         return "unmiliardo" + conv(n%1000000000)
    else:
         return conv(int(n/1000000000)) + \
               "miliardi" + \
               conv(n%1000000000)
               
