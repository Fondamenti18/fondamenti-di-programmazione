def conv(n):
    '''Viene composta la stringa formata dalle cifre del numero in input in forma letterale. Esse vengono
    costruite attraverso la chiamata di funzioni secondarie (unita, centinaia, migliaia, ecc)'''
    numero=str(n)
    numero='0'*(12-len(numero))+numero
    num_lett=""
    num_lett=unita(numero[0],'!uno')+centinaia(numero[0],numero[1])+decina(numero[1],numero[2])
    num_lett+=unita(numero[2],'!uno',numero[1])+miliardo(numero[2],numero[1],num_lett)+unita(numero[3],'!uno')+centinaia(numero[3],numero[4])+decina(numero[4],numero[5])
    num_lett+=unita(numero[5],'!uno',numero[4])+milione(numero[5],numero[4],numero[3],num_lett)+unita(numero[6],'!uno')+centinaia(numero[6],numero[7])+decina(numero[7],numero[8])
    num_lett+=unita(numero[8],'!uno',numero[7])+migliaia(numero[8],numero[7],numero[6],num_lett)+unita(numero[9],'!uno')+centinaia(numero[9],numero[10])+decina(numero[10],numero[11])
    num_lett+=unita(numero[11],'',numero[10])
    return num_lett       

def unita(cifra, eccezione='',cifra_prec=''):
    risultato=''
    if int(cifra)>1: risultato= unita_1(cifra)
    elif cifra == '1' and eccezione == '!uno': risultato=''
    elif cifra == '1': risultato='uno'
    if cifra_prec=='1':risultato=''
    return risultato

def unita_1(cifra):
    risultato=''
    if int(cifra)>4: risultato= unita_2(cifra)
    elif cifra == '2': risultato='due'
    elif cifra == '3': risultato='tre' 
    elif cifra == '4': risultato='quattro'   
    return risultato

def unita_2(cifra):
    risultato=''
    if cifra == '5': risultato='cinque'
    elif cifra == '6': risultato='sei'
    elif cifra == '7': risultato='sette'
    elif cifra == '8': risultato='otto'
    elif cifra == '9': risultato='nove'
    return risultato


def decina(cifra,cifra_succ):
    risultato=''
    if cifra == '1' and cifra_succ != '0': risultato=mag_dieci(cifra_succ)
    elif cifra == '1': risultato='dieci'
    elif int(cifra) > 1:risultato=decina_1(cifra) 
    if int(cifra)>1 and (cifra_succ == '1' or cifra_succ == '8'): risultato = risultato[:-1]
    return risultato

def decina_1(cifra):
    risultato=''
    if int(cifra)>4:risultato=decina_2(cifra)
    elif cifra == '2': risultato='venti'
    elif cifra == '3': risultato='trenta'
    elif cifra == '4': risultato='quaranta'
    return risultato

def decina_2(cifra):
    risultato=''
    if cifra == '5': risultato='cinquanta'
    elif cifra == '6': risultato='sessanta'
    elif cifra == '7': risultato='settanta'
    elif cifra == '8': risultato='ottanta'
    elif cifra == '9': risultato='novanta'
    return risultato

def mag_dieci(cifra_succ):
    risultato=''
    if int(cifra_succ)>4:risultato=mag_dieci_1(cifra_succ)
    elif cifra_succ == '1': risultato='undici'
    elif cifra_succ == '2': risultato='dodici'
    elif cifra_succ == '3': risultato='tredici'
    elif cifra_succ == '4': risultato='quattordici'
    return risultato

def mag_dieci_1(cifra_succ):
    risultato=''
    if cifra_succ == '5': risultato='quindici'
    elif cifra_succ == '6': risultato='sedici'
    elif cifra_succ == '7': risultato='diciassette'
    elif cifra_succ == '8': risultato='diciotto'
    elif cifra_succ == '9': risultato='diciannove'
    return risultato

def centinaia(cifra,cifra_succ):
    risultato=''
    if not cifra == '0': risultato = 'cento'
    if not cifra =='0' and cifra_succ== '8': risultato = 'cent'
    return risultato

def migliaia(cifra,cifra_prec,sec_cifra_prec,parte_prec):
    risultato=''
    if cifra == '0' and not parte_prec=='':risultato=migliaia_0(cifra_prec,sec_cifra_prec)
    elif cifra == '1':risultato=migliaia_1(cifra_prec,sec_cifra_prec,parte_prec)
    elif cifra_prec=='1':risultato='mila'
    elif not cifra == '0': risultato='mila'
    return risultato

def migliaia_0(cifra_prec,sec_cifra_prec):
    risultato=''
    if cifra_prec == '0' and sec_cifra_prec =='0': risultato=''
    else: risultato='mila'
    return risultato

def migliaia_1(cifra_prec,sec_cifra_prec,parte_prec):
    risultato=''
    if parte_prec == '': risultato='mille'
    elif not parte_prec == '' and cifra_prec == '0' and sec_cifra_prec =='0': risultato='mille'
    elif not parte_prec == '' and cifra_prec=='1': risultato='mila'
    elif not parte_prec == '': risultato='unomila'
    return risultato

def milione(cifra,cifra_prec,sec_cifra_prec,parte_prec):
    risultato='' 
    if cifra == '0' and not parte_prec == '':risultato=milione_0(cifra_prec,sec_cifra_prec)
    elif cifra == '1':risultato=milione_1(cifra_prec,sec_cifra_prec,parte_prec)
    elif cifra_prec=='1':risultato='milioni'
    elif not cifra == '0': risultato='milioni'
    return risultato

def milione_0(cifra_prec,sec_cifra_prec):
    risultato=''
    if cifra_prec == '0' and sec_cifra_prec =='0': risultato=''
    else: risultato='milioni'
    return risultato

def milione_1(cifra_prec,sec_cifra_prec,parte_prec):
    risultato=''
    if parte_prec == '': risultato='unmilione'
    elif not parte_prec == '' and cifra_prec == '0' and sec_cifra_prec =='0': risultato='unmilione'
    elif not parte_prec == '' and cifra_prec=='1': risultato='milioni'
    elif not parte_prec == '': risultato='unomilioni'
    return risultato

def miliardo(cifra,cifra_prec,parte_prec):
    risultato=''
    if cifra == '1': risultato= miliardo_1(cifra_prec,parte_prec)
    elif cifra_prec=='1':risultato='miliardi'
    elif cifra == '0' and not parte_prec == '': risultato='miliardi'
    elif not cifra == '0': risultato='miliardi'
    return risultato

def miliardo_1(cifra_prec,parte_prec):
    risultato=''
    if parte_prec == '': risultato='unmiliardo'
    elif not parte_prec == '' and cifra_prec=='1': risultato='miliardi'
    elif not parte_prec == '': risultato='unomiliardi'
    return risultato