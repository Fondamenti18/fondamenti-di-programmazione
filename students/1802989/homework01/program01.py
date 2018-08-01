def modi(ls, k):
    'Funzione main'
    primi = prime(ls, k)
    return primi

def prime(ls, k):
    'Funzione che restituisce i numeri primi'
    primi = []
    for num in ls[:]:
        divisione_iterata(num, ls, k, primi)
    return primi

def divisione_dispari(num, primi, k, ls, x, totale_exp):
    'Funzione che si occupa di iterare le divisioni da 2 fino alla rad di n'
    for div in range(3, int(num ** 0.5)+1, 2):
        exp = 0
        while x % div == 0:
            x = x // div
            exp += 1
            if x % div != 0:
                exp += 1
                totale_exp *= exp
    check(x, totale_exp, primi, ls, num, k)
    return primi

def divisione_iterata(num, ls, k, primi):
    totale_exp = 1
    x = num
    if x % 2 == 0:
        exp = 0
        while x % 2 == 0:
            x = x // 2
            exp += 1
            if x % 2 != 0:
                exp += 1
                totale_exp *= exp
    divisione_dispari(num, primi, k, ls, x, totale_exp)

def check(x, totale_exp, primi, ls, num, k):
    ''
    if x > 1:
        totale_exp *= 2
    if totale_exp == 2:
        primi.append(num)    
    if totale_exp-2 != k:
        ls.remove(num)
    return