import logging

ch = logging.StreamHandler()
formatter = logging.Formatter('%(name)s | %(message)s')
ch.setFormatter(formatter)
log = logging.getLogger(__name__)
log.addHandler(ch)
log.propagate = False
log.setLevel(logging.WARNING)

lsunita=['','uno','due','tre','quattro','cinque','sei','sette','otto','nove']
lsdecine=['','dieci','venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
lsdieci=['dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']

def miliardi(n):
    m = n // 10**9
    s=''
    if m >= 10**2:
        s= centinaia(m)+decine(m)+unita(m)
    elif m >= 10:
        s= decine(m)+unita(m)
    elif m != 1:
        s= unita(m)
    else:
        return 'unmiliardo'
    return s+'miliardi'

def milioni(n):
    m = n // 10**6
    s=''
    if m >= 10**2:
        s= centinaia(m)+decine(m)+unita(m)
    elif m >= 10:
        s= decine(m)+unita(m)
    elif m != 1:
        s= unita(m)
    else:
        return 'unmilione'
    return s+'milioni'

def migliaia(n):
    m = n // 1000
    s=''
    if m >= 10**2:
        s= centinaia(m)+decine(m)+unita(m)
    elif m >= 10:
        s= decine(m)+unita(m)
    elif m != 1:
        s= unita(m)
    else:
        return 'mille'
    return s+'mila'


def centinaia(n):
    c = n % 1000 // 100
    d = n % 100 //10
    log.info('n: {0}, c: {1}, d: {2}'.format(n,c,d))
    s=''
    if c == 0:
        return s
    if c > 1:
        s=lsunita[c]+'cento'
    else:
        s='cento'
    if d == 8:
        return s[:-1]
    return s
    
def decine(n):
    if 10 <= (n % 100) <=19:
        return lsdieci[n%10]
    d = n % 100 // 10           # d sono le decine
    u = n % 10                  # u sono le unita'
    log.info('n: {0}, d: {1}, u: {2}'.format(n,d,u))
    if u not in [1,8]:
        return lsdecine[d]
    else:
        return lsdecine[d][:-1]
    
def unita(n):
    if 10 <= (n % 100) <=19:
        return ''
    return lsunita[n % 10]
        
def conv(n):
    log.info('Conversione di n: {0}'.format(n))
    if n >= 10**9:
        return miliardi(n)+milioni(n)+migliaia(n)+centinaia(n)+decine(n)+unita(n)
    if n >= 10**6:
        return milioni(n)+migliaia(n)+centinaia(n)+decine(n)+unita(n)
    elif n >= 10**3:
        return migliaia(n)+centinaia(n)+decine(n)+unita(n)
    elif n >= 10**2:
        return centinaia(n)+decine(n)+unita(n)
    elif n >= 10:
        return decine(n)+unita(n)
    else:
        return unita(n)


if __name__=='__main__':
    for i in [50011101,43332108,64355186,534471125,12331187,7528589,77298,51781,13000,71018]:
        print (conv(i))

