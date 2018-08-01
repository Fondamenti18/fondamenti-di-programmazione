numeriA = ['','uno','due','tre','quatro','cinque','sei','sette','otto','nove']
numeriB = ['dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
numeriC = ['',0,'venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
def conv1(n):  
    return numeriA[int(n)]
def conv2(n): 
    numeroC = '' 
    if n[0]=='0':
        numeriC = conv1(n[1])
    if n[0]=='1':
        numeroC = numeriB[int(n[1])]
    elif n[0]!='1' and n[0]!='0':
        temp = numeroC[int(n[0])]
        if n[1]=='1' or n[1]=='8':
            numeroC = temp[0:len(temp)-1]+numeriA[int(n[1])]
        else:
            numeroC = temp+numeriA[int(n[1])]
    return numeroC
def conv3(n): 
    numeroC = ''
    if n[0]=='0':
        numeroC = conv2(n[1:])
    if n[0]=='1':
        if n[1]=='8':
            numeroC = 'cent'+conv2(n[1:])
        else:
            numeroC = 'cento'+conv2(n[1:])
    elif n[0]!='1' and n[0]!='0':
        if n[1]=='8':
            numeroC = conv1(n[0])+'cent'+conv2(n[1:])
        else:
            numeroC = conv1(n[0])+'cento'+conv2(n[1:])
    return numeroC
def conv4(n): 
    numeroC = ''
    if n[0]=='0':
        numeroC = conv3(n[1:])
    if n[0]=='1':
        numeroC = 'mille'+conv3(n[1:])
    elif n[0]!='1' and n[0]!='0':
        numeroC = conv1(n[0])+'mila'+conv3(n[1:])
    return numeroC
def conv5(n): 
    numeroC = ''
    if n[0]=='0':
        numeroC = conv4(n[1:])
    else:
        numeroC = conv2(n[0:2])+'mila'+conv3(n[2:])
    return numeroC
def conv6(n): 
    numeroC = ''
    if n[0]=='0':
        numeroC = conv5(n[1:])
    else:
        numeroC = conv3(n[0:3])+'mila'+conv3(n[3:])
    return numeroC
def conv7(n): 
    numeroC = ''
    if n[0]=='0':
        numeroC = conv6(n[1:])
    if n[0]=='1':
        numeroC = 'unmilione'+conv6(n[1:])
    elif n[0]!='1' and n[0]!='0':
        numeroC = conv1(n[0])+'milioni'+conv6(n[1:])
    return numeroC
def conv8(n): 
    numeroC = ''
    if n[0]=='0':
        numeroC = conv7(n[1:]) 
    else:
        numeroC = conv2(n[0:2])+'milioni'+conv6(n[2:])
    return numeroC
def conv9(n): 
    numeroC = '' 
    if n[0]=='0':
        numeroC = conv8(n[1:])
    else:
        numeroC = conv3(n[0:3])+'milioni'+conv6(n[3:])
    return numeroC
def conv10(n): 
    numeroC = '' 
    if n[0]=='0':
        numeroC = conv9(n[1:])
    if n[0]=='1':
        numeroC = 'unmiliardo'+conv9(n[1:])
    elif n[0]!='1' and n[0]!='0':
        numeroC = conv1(n[0])+'miliardi'+conv9(n[1:])
    return numeroC 
def conv11(n):
    if n[0]=='0':
        numeroC = conv10(n[1:])
    else:
        numeroC = conv2(n[0:2])+'miliardi'+conv9(n[2:])
    return numeroC
def conv12(n):
    if n[0]=='0':
        numeroC = conv11(n[1:])
    else:
        numeroC = conv3(n[0:3])+'miliardi'+conv9(n[3:])
    return numeroC
def conv(n):
    if n>1000000000000 or n<0:
        print('error')
    else:
        n = str(n)
        numeroC = ''
        if n=='0':
            numeroC = 'zero'
        if len(n)==1 and n!='0':
            numeroC = conv1(n)
        if len(n)==2: 
            numeroC = conv2(n) 
        if len(n)==3:
            numeroC = conv3(n)
        if len(n)==4:
            numeroC = conv4(n)
        if len(n)==5: 
            numeroC = conv5(n)
        if len(n)==6:
            numeroC = conv6(n)
        if len(n)==7:
            numeroC = conv7(n)
        if len(n)==8:
            numeroC = conv8(n)
        if len(n)==9:
            numeroC = conv9(n)
        if len(n)==10:
            numeroC = conv10(n)
        if len(n)==11: 
            numeroC = conv11(n)
        if len(n)==12:
            numeroC = conv12(n)
        return numeroC


    
