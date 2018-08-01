
#!/usr/bin/python
unita = {1: 'uno', 2: 'due', 3: 'tre', 4: 'quattro', 5: 'cinque', 6: 'sei', 7: 'sette', 8: 'otto', 9: 'nove', 10: 'dieci', 11: 'undici', 12: 'dodici',
        13: 'tredici', 14: 'quattordici', 15: 'quindici', 16: 'sedici', 17: 'diciassette', 18: 'diciotto',19: 'diciannove'}
def conv(n):
    if n==0:
        return 'zero'

    elif n <= 19:
        return unita[n]

    elif n <= 99:
        decine = ("venti", "trenta", "quaranta","cinquanta", "sessanta","settanta", "ottanta", "novanta")
        l = decine[int(n/10)-2]
        t = n%10
        if t == 1 or t == 8:
            l = l[:-1]
        return l + conv(n%10)

    elif n <= 199:
        return "cento" + conv(n%100)

    elif n <= 999:
        m = n%100
        m = int(m/10)
        l = "cent"
        if m != 8:
            l = l + "o"
        return conv( int(n/100))+ l+ conv(n%100)

    elif n<= 1999 :
        return "mille" + conv(n%1000)

    elif n<= 999999:
        return conv(int(n/1000)) + "mila" + conv(n%1000).lower()

    elif n <= 1999999:
        return "unmilione" + conv(n%1000000)

    elif n <= 999999999:
        return conv(int(n/1000000))+ "milioni" + conv(n%1000000)
    elif n <= 1999999999:
        return "unmiliardo" + conv(n%1000000000)

    else:
        return conv(int(n/1000000000)) + "miliardi" + conv(n%1000000000)
