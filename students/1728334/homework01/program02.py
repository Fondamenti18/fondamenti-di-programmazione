def elisioni(t): #le uniche elisioni da fare sono queste.
	return(t
		.replace("oo", "o")
		.replace("ao", "o")
		.replace("io", "o")
		.replace("au", "u")
	)
	
#def zero_nop(d):
    #return "" if d[-4:] is "zero" else d

cardinali = ['', 'uno', 'due', 'tre', 'quattro',
             'cinque', 'sei', 'sette', 'otto',
             'nove', 'dieci', 'undici', 'dodici', 
             'tredici', 'quattordici', 'quindici',
             'sedici', 'diciassette', 'diciotto', 
             'diciannove']

decine = ['venti', 'trenta', 'quaranta', 'cinquanta',
          'sessanta', 'settanta', 'ottanta', 'novanta']

def get_divisione(n, p):
    return n // p

def get_resto(n, p):
    return n % p

def first_case(n=0):
    return cardinali[n]

def second_case(n=0):
    #decina = n // q(1) # numero intero della divisione
    #unita = n % q(1) # resto
    #text_decina = decine[get_divisione(n, q(1)) - 2]
    x = decine[get_divisione(n, 10) - 2]
    t = get_resto(n, 10)
    if t == 1 or t == 8:
        x = x[:-1]
    return x + conv(t)

def third_case(n=0):
    t = get_divisione(n, q(2))
    x = get_resto(n, q(2))
    if t == 1:
        return "cento" + conv(x)
    y = get_divisione(x, 10)
    l = "cent"
    if y != 8:
        l = l + "o"
    return conv(t) + l + conv(x)
    
def fourth_case(n=0):
    migliaia = get_divisione(n, q(3))
    centinaia = get_resto(n, q(3))
    return conv(migliaia) + "mila" + conv(centinaia) if migliaia is not 1 else "mille" + conv(centinaia)

def fifth_case(n=0):
    migliaia = get_divisione(n, q(6))
    centinaia = get_resto(n, q(6))
    return conv(migliaia) + "milioni"  + conv(centinaia) if migliaia is not 1 else "unmilione" + conv(centinaia)

def sixth_case(n=0):
    migliaia = get_divisione(n, q(9))
    centinaia = get_resto(n, q(9))
    return conv(migliaia) + "miliardi"  + conv(centinaia) if migliaia is not 1 else "unmiliardo" + conv(centinaia)


def q(n):
    return 10**n
 
CASI = {19 : first_case, q(2) : second_case, q(3) : third_case, q(6) : fourth_case, q(9) : fifth_case, q(12) : sixth_case, q(15) : '1'}

def stop_conv(n):
    if n < 0 or n > q(12):
        return "Inserisci un numero compreso tra 0 e " + str(q(12)) + "."
    

def conv(n):
    stop_conv(n)
    for x, v in CASI.items():
        if n < x:
            return CASI[x](n)
    
    