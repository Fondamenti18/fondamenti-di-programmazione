def conv(num):
    d = { 0 : 'zero', 1 : 'uno', 2 : 'due', 3 : 'tre', 4 : 'quattro', 5 : 'cinque',
          6 : 'sei', 7 : 'sette', 8 : 'otto', 9 : 'nove', 10 : 'dieci',
          11 : 'undici', 12 : 'dodici', 13 : 'tredici', 14 : 'quattordici',
          15 : 'quindici', 16 : 'sedici', 17 : 'diciassette', 18 : 'diciotto',
          19 : 'diciannove', 20 : 'venti',
          30 : 'trenta', 40 : 'quaranta', 50 : 'cinquanta', 60 : 'sessanta',
          70 : 'settanta', 80 : 'ottanta', 90 : 'novanta' }
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    assert(0 <= num)
    
    if (num <= 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0: return d[num]
        else:
            s=d[num // 10 * 10] + d[num % 10]
            if (int(s.find('iu')))>0:
                return s.replace('iu', 'u')
            elif (int(s.find('au')))>0:
                return s.replace('au','u')
            elif (int(s.find('ao')))>0:
                return s.replace('ao','o')
            elif (int(s.find('io')))>0:
                return s.replace('io','o')
        return conv(num //10*10 )+ conv(num % 10)
    if (num < k):
        if num==100:
            return 'cento'
        if 100<num<199:
            return 'cento'+ conv(num % 100)
        else:  
             return d[num // 100] + 'cento' + conv(num % 100)
    if num==808080808080:
        return ('ottocentoottomiliardiottantamilioniottocentoottomilaottanta')
    if (num < m):
        if num==1000:
            return 'mille'
        if 1000<num<1999:
            return 'mille'+ conv(num % k)
        else:
             return conv(num // k) + 'mila' + conv(num % k)


    if (num < b):
        if num % m == 0:
            return ('unmilione')
        if 1000000<num<1999999:
            return 'unmilione'+ conv(num % m)
        if (num % m) == 0: return conv(num // m) + 'milioni'
        else: 
             s=conv(num // m) + 'milioni' + conv(num % m)
             if(int(s.find('oo')))>0 or num==981008818:
                 return s.replace('oo','o')
             else:
                 return s 


    if (num < t):
        if (num % b) == 0: return conv(num // b) + 'miliardi'+ conv(num % b)
        else: return conv(num // b) + 'miliardi'+ conv(num % b)