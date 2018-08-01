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
    num = str(n)
    lun = len(num)
    a = ''
    base={1:'uno',2:'due',3:'tre',4:'quattro',5:'cinque',6:'sei',
          7:'sette',8:'otto',9:'nove',10:'dieci',11:'undici',
          12:'dodici',13:'tredici',14:'quattordici',15:'quindici',
          16:'sedici',17:'diciassette',18:'diciotto',19:'diciannove',
          20:'venti',21:'ventuno',28:'ventotto',30:'trenta',
          31:'trentuno',38:'trentotto',40:'quaranta',41:'quarantuno',
          48:'quarantotto',50:'cinquanta',51:'cinquantuno',58:'cinquantotto',
          60:'sessanta',61:'sessantuno',68:'sessantotto',70:'settanta',
          71:'settantuno',78:'settantotto',80:'ottanta',81:'ottantuno',
          88:'ottantotto',90:'novanta',91:'novantuno',98:'novantotto',
          100:'cento',1000:'mille',100000:'centomila',1000000:'unmilione',
          10000000: 'diecimilioni',100000000:'centomilioni',1000000000:'unmiliardo',
          10000000000:'diecimiliardi', 100000000000:'centomiliardi'}
    if n in base:
        a = (base[n])
    if lun == 2:
        a = duecifre(num,base)
    if lun == 3:
        a = trecifre(num,base)
    if lun == 4:
        a = quatcifre(num,base)
    if lun == 5:
        a = cincifre(num,base)
    if lun == 6:
        a = seicifre(num,base)
    if lun == 7:
        a = settecifre(num,base)
    if lun == 8:
        a = ottocifre(num,base)
    if lun == 9:
        a = novecifre(num,base)
    if lun == 10:
        a = diecicifre(num,base)
    if lun == 11:
        a = undicicifre(num,base)
    if lun == 12:
        a = dodicicifre(num,base)
    return a
        

def duecifre(num,base):
    numero = ''
    if int(num) in base:
        numero = base[int(num)] 
    if int(num) == '00':
        numero = ''
    if int(num) not in base:
        nume = []
        pc = int(num[0])*10
        sc = int(num[1])
        nume += base[pc]+base[sc]
        numero =''.join(nume)
    return numero

def trecifre(d,base):
    nume = []
    treci = ''
    if int(d) in base:
        nume += base[int(d)]
        treci = ''.join(nume)
    if d[:2] == '00' and d != '000':
        nume += base[int(d[2])]
        treci = nume
    if d[:] == '000':
        treci = ''
    if d[0] == '0' and d[1:3] != '00':
        nume = duecifre(d[1:],base)
        treci = ''.join(nume)
    if d[:2] != '00' and d[0] != '0':
        if d[0] == '1' and int(d) not in base:# casistica dei numeri da 100 a 200
            if d[1] == '0':
                nume += 'cento' + base[int(d[2])]
                treci = ''.join(nume)
            if d[1] == '8':
                if d[1:3] in base:
                    nume += 'cent' + base[int(d[1:3])]
                    treci = ''.join(nume)
                if d[1:3] not in base:
                    nume += 'cent' + duecifre(d[1:3],base)
                    treci = ''.join(nume)
            if int(d[1:]) in base:
                nume += 'cento' + base[int(d[1:3])]
                treci = ''.join(nume)
            if int(d[1:3]) not in base:
                nume += 'cento' + duecifre(d[1:3],base)
                treci = ''.join(nume)
    #casistica con numeri dai duecento in su
        if d[1:] == '00' and int(d) not in base:
            nume += base[int(d[0])] + 'cento'
            treci = ''.join(nume)
        if d[0] != '1':
            if d[1] == '0' and d[2] != '0':
                nume += base[int(d[0])] + 'cento' + base[int(d[2])]
                treci = ''.join(nume)
            if d[1] == '8':
                nume += base[int(d[0])] + 'cent' + duecifre(d[1:],base)
                treci = ''.join(nume)
            if d[1] != '0' and d[2] != '0' and d[0] != '0' and d[1] != '8':
                nume += base[int(d[0])] + 'cento' + duecifre(d[1:3],base)
                treci = ''.join(nume)
    return treci
            
def quatcifre(b,base):
    nume = []
    if b[0] == '1':
        nume += 'mille'+ trecifre(b[1:4],base)
        quatci = ''.join(nume)
    else:
        nume += base[int(b[0])]+'mila'+ trecifre(b[1:4],base)
        quatci = ''.join(nume)
    return quatci

def cincifre(b,base):
    nume = []
    if int(b[0:2]) in base:
        nume += base[int(b[0:2])]+'mila' + trecifre(b[2:],base)
        cincif = ''.join(nume)
    else:
        nume += duecifre(b[0:2],base)+'mila'+trecifre(b[2:5],base)
        cincif = ''.join(nume)
    return cincif

def seicifre(n,base):
    seicif =''
    nume = []
    if int(n) in base:
        seicif = base[int(n)]
    if n == '000000':
        seicif = ''
    else:
        if n[:3] == '000':
            nume += '' + trecifre(n[3:],base)
            seicif = ''.join(nume)
        if n[3:] == '000':
            nume += trecifre(n[:3],base) + 'mila'
            seicif = ''.join(nume)
        if n[3] == '0' and n[4] != '0' and n[5] != '0':
            nume += trecifre(n[:3],base) + 'mila' + duecifre(n[4:],base)
            seicif = ''.join(nume)
        if n[:3] !='000' and n[3:] != '000':
            nume += trecifre(n[:3],base) + 'mila' + trecifre(n[3:],base)
            seicif = ''.join(nume)
    return seicif

def settecifre(n,base):
    nume = []
    if int(n) in base:
        settecif = base[int(n)]
    if n == '0000000':
        settecif = ''
    else:
        if n[0] == '1':
            nume += 'unmilione' + seicifre(n[1:],base)
            settecif = ''.join(nume)
        if n[0] != '1':
            nume += base[int(n[0])] + 'milioni' + seicifre(n[1:],base)
            settecif = ''.join(nume)
    return settecif

def ottocifre(n,base):
    nume = []
    if int(n) in base:
        ottocif = base[int(n)]
    if n[:] == '00000000':
        ottocif = ''
    else:
        if int(n[:2]) in base:
            nume = base[int(n[:2])] + 'milioni' + seicifre(n[2:],base)
            ottocif = ''.join(nume)
        if int(n[:2]) not in base:
            nume = duecifre(n[:2],base) + 'milioni' + seicifre(n[2:],base)
            ottocif = ''.join(nume)    
    return ottocif  

def novecifre(n,base):
    nume = []
    if int(n) in base:
        novecif = base[int(n)]
    if n[:] == '000000000':
        novecif = ''
    if n[0:3] == '000':
        nume += seicifre(n[3:],base)
        novecif = ''.join(nume)
    if n[0:3] != '000':
        nume += trecifre(n[:3],base) + 'milioni' + seicifre(n[3:],base)
        novecif = ''.join(nume) 
    return novecif

def diecicifre(n,base):
    nume = []
    if int(n) in base:
        diecicif = base[int(n)]
    if n[:] == '0000000000':
        diecicif = ''
    else:
        nume += base[int(n[0])] + 'miliardi' + novecifre(n[1:],base)
        diecicif = ''.join(nume) 
    return diecicif

def undicicifre(n,base):
    nume = []
    if int(n) in base:
        undicicif = base[int(n)]
    if n[:] == '00000000000':
        undicicif = ''
    else:
        nume += base[int(n[:2])] + 'miliardi' + novecifre(n[2:],base)
        undicicif = ''.join(nume) 
    return undicicif
     
def dodicicifre(n,base):
    nume = []
    if int(n) in base:
        dodicicif = base[int(n)]
    if n[:] == '000000000000':
        dodicicif = ''
    else:
        nume += trecifre(n[:3],base) + 'miliardi' + novecifre(n[2:],base)
        dodicicif = ''.join(nume) 
    return dodicicif
a = conv(981)
print(a)