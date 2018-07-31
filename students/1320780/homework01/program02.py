def conv(n):
    
    numConvertito = ''
 
    lsMinVenti = ['uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
    lsDecine = [['venti','vent'],['trenta','trent'],['quaranta','quarant'],['cinquanta','cinquant'],['sessanta','sessant'],['settanta','settant'],['ottanta','ottant'],['novanta','novant']]
    lsTerzine = [['miliardi','unmiliardo'],['milioni','unmilione'],['mila','mille'],['','uno']]
    lsCento = ['cento','cent']
 
    terzine = [0,0,0,0]
    toSubtract = 0
    
    if n > 999999999:
        terzine[0] = n // 1000000000
        toSubtract += terzine[0] * 10 ** 9
    if n > 999999:
        terzine[1] = (n - toSubtract) // 1000000
        toSubtract += terzine[1] * 10 ** 6
    if n > 999:
        terzine[2] = (n - toSubtract) // 1000
        toSubtract += terzine[2] * 10 ** 3
    terzine[3] = n - toSubtract
    
    for i in range(4):
        if terzine[i] != 0:
            toSubtract = 0
            cifre = [0,0,0]
            if terzine[i] > 99:
                cifre[0] = terzine[i] // 100
                toSubtract += cifre[0] * 10 ** 2
            if terzine[i] - toSubtract > 19:
                cifre[1] = (terzine[i] - toSubtract) // 10
                toSubtract += cifre[1] * 10
            cifre[2] = terzine[i] - toSubtract
            
            if terzine[i] == 1:
                numConvertito += lsTerzine[i][1]
            else:
                indexCento = 0
                if cifre[1] == 8:
                    indexCento = 1
                if cifre[0] > 1:    
                    numConvertito += lsMinVenti[cifre[0]-1] + lsCento[indexCento]
                elif cifre[0] == 1:
                    numConvertito += lsCento[indexCento]
                if cifre[1] > 1:
                    if lsMinVenti[cifre[2]-1][0] in 'aeiou':
                        numConvertito += lsDecine[cifre[1]-2][1]
                    else:
                        numConvertito += lsDecine[cifre[1]-2][0]
                if cifre[2] != 0:
                    numConvertito += lsMinVenti[cifre[2]-1] 
                numConvertito += lsTerzine[i][0]
    return numConvertito