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
    'Scrivete qui il codice della funzione'
    dict_unita = { '0': '',
                   '1': 'uno',
                   '2': 'due',
                   '3': 'tre',
                   '4': 'quattro',
                   '5': 'cinque',
                   '6': 'sei',
                   '7': 'sette',
                   '8': 'otto',
                   '9': 'nove'}
    dict_decinetonde = {'20': 'venti',
                        '30': 'trenta',
                        '40': 'quaranta',
                        '50': 'cinquanta',
                        '60': 'sessanta',
                        '70': 'settanta',
                        '80': 'ottanta',
                        '90': 'novanta',}
    dict_decine = {'10': 'dieci',
                   '11': 'undici',
                   '12': 'dodici',
                   '13': 'tredici',
                   '14': 'quattordici',
                   '15': 'quindici',
                   '16': 'sedici',
                   '17': 'diciassette',
                   '18': 'diciotto',
                   '19': 'diciannove'}
    dict_centinaia = {'000': '',
                      '100': 'cento',
                      '200': 'duecento',
                      '300': 'trecento',
                      '400': 'quattrocento',
                      '500': 'cinquecento',
                      '600': 'seicento',
                      '700': 'settecento',
                      '800': 'ottocento',
                      '900': 'novecento'}
    lista = []
    stringa = str(n)
    while len(stringa) != 0: # fino a che la stringa non è vuota
        if len(stringa) <= 3: # se la stringa ha al più tre elementi
            lista.append(stringa)
            stringa = ''
        else: # altrimenti
            valori = stringa[-3:] # prendi i valori più a destra
            stringa = stringa[:-3]
            lista.append(valori)
    lista_numero_scritto = []
    numero_scritto = ''
    for n in lista: # per ogni elemento in lista
        if len(n) == 1: # se è lungo uno vado a prendere la chiave in dict_unita
            numero_scritto = dict_unita.get(n)
            lista_numero_scritto.append(numero_scritto)
        if len(n) == 2: # se è lungo due
            if n[-1] == '0' and n[0] != '1': # se la decina è tonda prendo la chiave in dict_decinetonde
                numero_scritto = dict_decinetonde.get(n)
                lista_numero_scritto.append(numero_scritto)
            if n[0] != '1' and n[-1] != '0': # se n non è né una decina tonda ne una decina allora
                a = n[0] # prendo la decina
                a += '0' # ci attacco 0
                stringa_tmp = dict_decinetonde.get(a) # e prendo la decina tonda
                if a[0] == '8' or n[-1] == '8': # se il primo elemento è otto
                    stringa_tmp = stringa_tmp[0:-1] # recidi la lettera nell'ultima pos
                stringa_tmp += dict_unita.get(n[-1])
                numero_scritto = stringa_tmp
                lista_numero_scritto.append(numero_scritto)
            if n[0] == '1': # se il primo numero è 1 allora vai nel dict_decine
                numero_scritto = dict_decine.get(n)
                lista_numero_scritto.append(numero_scritto)
        if len(n) == 3: # quando n ha lunghezza 3
            if n[0] == '1' and n[-2:] == '00': #controlla se è cento
                numero_scritto += 'cento'
                lista_numero_scritto.append(numero_scritto)
            if n[0] == '1' and n[-2:] != '00': # quando il primo numero è uno
                if n[-2] == '0' and n[-1] != '0': # quando il secondo numero è zero vado in dict_unita
                    numero_scritto += 'cento' + dict_unita.get(n[-1])
                if n[-2] != '0' and n[-2] != '1' and n[-1] == '0': # quando c'è una decina tonda
                    numero_scritto += 'cento'+ dict_decinetonde.get(n[-2])
                if n[-2] == '1' and n[-1] != '0': # quando c'è una decina
                    numero_scritto += 'cento' + dict_decine.get(n[-2]+n[-1])
                if n[-2] != '0' and n[-1] != '0':
                    b = n[0]
                    b += '00'
                    stringa_tmp = dict_centinaia.get(b)
                    if b[1] == '8' or b[2] == '8':
                        stringa_tmp = stringa_tmp[:-1]
                    dec = n[1] + "0"
                    unit = n[2]
                    stringa_tmp += dict_decinetonde.get(dec)
                    if unit == "1" or unit == "8":
                        stringa_tmp = stringa_tmp[:-1]
                    stringa_tmp += dict_unita.get(unit)
                numero_scritto = stringa_tmp
                lista_numero_scritto.append(numero_scritto)
            else:
                c = n[0] + '00'
                centinaia = dict_centinaia.get(c)
                if n[-2] == '0' and n[-1] != '0':
                    centinaia += dict_unita.get(n[-1])
                    numero_scritto = centinaia
                    lista_numero_scritto.append(numero_scritto)
                elif n[-2] == '1':
                    centinaia += dict_decine.get(n[-2]+n[-1])
                    numero_scritto = centinaia
                    lista_numero_scritto.append(numero_scritto)
                else:
                    decina = n[-2]
                    decina += '0'
                    if n[-2] == '8':
                        centinaia = centinaia[:-1]
                    centinaia += dict_decinetonde.get(decina)
                    if n[-1] == '1' or n[-1] == '8':
                        centinaia = centinaia[:-1]
                    centinaia += dict_unita.get(n[-1])
                    numero_scritto = centinaia
                    lista_numero_scritto.append(numero_scritto)
        numero_scritto = ''
    numero_finale = ''
    lista_finale = invertiLista(lista_numero_scritto)
    lista_copia_temp = lista_finale.copy()

    for n in lista_finale:
        if n == 'uno' and len(lista_copia_temp) == 4:
            numero_finale += 'unmiliardo'
        elif n == 'uno' and len(lista_copia_temp) == 3:
            numero_finale += 'unmilione'
        elif n == 'uno' and len(lista_copia_temp) == 2:
            numero_finale += 'mille'
        else:
            if len(lista_copia_temp) == 4:
                numero_finale += n
                numero_finale += 'miliardi'
            elif len(lista_copia_temp) == 3:
                numero_finale += n
                numero_finale += 'milioni'
            elif len(lista_copia_temp) == 2:
                numero_finale += n
                numero_finale += 'mila'
            else:
                numero_finale += n
        lista_copia_temp.remove(n)
    return numero_finale

def invertiLista(l):
    lista = []
    i = len(l)-1
    for e in range(len(l)):
        lista.append(l[i])
        i = i-1
    return lista
