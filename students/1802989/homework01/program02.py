unita = {'0': 'zero', '1': 'uno', '2': 'due', '3': 'tre', '4': 'quattro', '5': 'cinque', '6': 'sei',
         '7': 'sette', '8': 'otto', '9': 'nove', '10': 'dieci'}
dec = { '10': 'dieci', '20': 'venti', '30': 'trenta', '40': 'quaranta', '50': 'cinquanta',
          '60': 'sessanta', '70': 'settanta', '80': 'ottanta', '90': 'novanta'}
speciali = {'11':'undici', '12':'dodici', '13':'tredici', '14':'quattordici', '15':'quindici',
            '16':'sedici', '17':'diciassette', '18':'diciotto', '19':'diciannove', }

grandezze = [['cento'],['mila'], ['milioni'], ['miliardi'], ['bilioni']]
end = ['mille', 'milione', 'miliardo', 'bilione', 'mila']
scala = [['cento'],['mila'], ['milioni'], ['miliardi'], ['bilioni'], ['mille'], ['milione'], ['miliardo'], ['bilione']]
convers = {'mila': 'mille', 'milioni': 'milione', 'miliardi': 'miliardo', 'bilioni': 'bilione'}
check = {'unocento': 'cento', 'unomille': 'mille', 'unomilione': 'unmilione', 'unomiliardo': 'unmiliardo',
         'unobilione': 'unbilione'}

def conv(num):
    'Converte qualsiasi numero naturale'
    #Caso noto
    if num == 0:
        return 'zero'
    num = list(str(num))
    raccolto_a2 = raccogli_a2(num)
    corretto_a2 = correggi_a2(raccolto_a2)
    corretto_k = prefix_k(corretto_a2)
    fix_k = remove_k(corretto_k)
    last_fix = change_k(fix_k)
    corretto_h = prefix_h(last_fix)
    traduci = converti(corretto_h)
    risultato = final_check(traduci)
    return risultato

def raccogli_a2(num):
    'Funzione usata per raccogliere centinaia-decine'
    ris = []
    while num:
        ris.append(num[-2:])
        del num[-2:]
        ris.append(num[-1:])
        del num[-1:]
    return ris[::-1]

def correggi_a2(num):
    'Usato per rimuovere eventuali elementi vuoti'
    for el in num:
        if not el:
            num.remove(el)
    return num

def prefix_k(n2):
    'Funzione che aggiunge le misure di grandezza K KK KKK KKKK'
    k = 1
    for i in range(len(n2)-1, 0, -1):
            if len(n2[i]) == 1:
                if n2.index(n2[i]) == 1 or int(''.join((n2[i-1]))) + int(''.join((n2[i-2]))) != 0:
                    n2[i:i] += [grandezze[k]]
                k += 1
 
    for index in range(len(n2)):
        if n2[index] in grandezze:
            if n2.index(n2[index]) == 1 and n2[index-1][0] == '1':
                if len(n2[index-1]) == 1:
                #Può diventare mille, unmilione e così via
                    n2[index] = [convers[''.join(n2[index])]]
            elif n2[index-1][0] == '0' and n2[index-2][0] == '0':
                n2[index] = [convers[''.join(n2[index])]]
                
    return n2

def remove_k(num):
    'Usata per controllare eventuali casi errati'
    if len(num) > 6:
        num_c = num[:]
        for i in range(3, len(num_c)):
            if ''.join(num_c[i]) in end:
                if int(''.join((num_c[i-1]))) + int(''.join((num_c[i-2]))) == 0:
                    del num[i]
    else:
        return num
    return num

def change_k(num):
    'Usata per cambiare da mille a mila'
    num_c = num[:]
    for i in range(3, len(num_c)):
        if ''.join(num_c[i]) == end[0]:
            if int(''.join((num_c[i-1]))) + int(''.join((num_c[i-2]))) > 1:
                num[i] = ['mila']
    return num

def prefix_h(lista_numeri):
    'Usata per aggiungere le centinaia'
    for i in range(len(lista_numeri)-1, 0, -1):
        if len(lista_numeri[i]) == 2:
            if lista_numeri[i-1] != ['0']:
                lista_numeri[i:i] = [grandezze[0]]
    return lista_numeri

def converti(lst_n):
    '''Funzione MAIN che distingue i vari casi, e decide se convertire il numero come un decimale
    oppure come un unita'''
    ris = ''
    for i in range(len(lst_n)):
        'Per ogni numero presente'
        if check_special(lst_n[i]) != '':
            ris += check_special(lst_n[i])
        else:
            if len(lst_n[i]) > 1:
                ris += controlli_dec(lst_n[i])
            elif lst_n[i] in scala:
                ris += ''.join(lst_n[i])
            else:
                ris += trad_un(lst_n[i], 0)
    return ris

def check_special(el):
    'Funzione che controlla e assegna i numeri 11-19'
    el = str(''.join(el))
    for k,v in speciali.items():
        if k == el:
            return v
    return ''

def controlli_dec(el):
    'Funzione opera un controllo preventivo prima di tradurre un numero in decimale'
    if int(''.join(el)) == 0:
        return ''
    elif el[0] == '0':
        return trad_un(el, 1)
    elif el[1] == '8' or el[1] == '1':
        return trad_dec(el, 1)
    else:
        return trad_dec(el, 0)
    
def trad_dec(numero, k):
    '''Il caso con k=1 è quello d'elisione,
    il caso con k=0 è quello standard '''
    finale = ''
    un = numero.pop()
    numero = ''.join(numero)+'0'
    if k == 1:
        decim = dec.get(numero)
        decim = decim[:-1]
        finale += decim
    else:
        finale += dec[numero]
    if un != '0':
        finale += unita[un]
    return finale

def trad_un(el, k):
    'Funzione per tradurre le unita'
    risul = ''
    if k == 1:
        el = el[1:]
    el = ''.join(el)
    if el != '0':
        risul += unita.get(str(el))
    return risul

def final_check(numero):
    'Funzione di chiusura, usata per lanciare in risultato finale'
    for k,v in check.items():
        index = numero.find(k)
        if index != -1:
            n = numero[index:index+len(k)]
            numero = numero.replace(n, v)
  #Caso noto, in corrispondenza di questo caso conviene sostituire direttamente il valore
    if 'oottant'in numero:
        numero = numero.replace('oottant', 'ottant')
    return numero