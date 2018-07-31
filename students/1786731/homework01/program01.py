import operator
from functools import reduce

def appendiPrimi(n, d, ls):
    if d == 0:
        ls.append(n)

def appendiPropri(n, d, k, ls):
    if d == k:
        ls.append(n)

def fattori(number):
    return set( reduce( operator.concat, # usare semplicemente lambda(x,y):x+y  creerebbe troppe liste intermedie 
                 ([i, number//i] for i in range(1, int(number**0.5) + 1) if number % i == 0)  # si utilizza un generatore al posto di creare una lista in-place 
           ))

def modi(ls, k):
    primi, newls = [], []
    
    for number in ls:
        factors = fattori(number)
                     
        propri = len(factors) - 2

        appendiPrimi(number, propri, primi)
        appendiPropri(number, propri, k, newls)
    
    ls[:] = newls
    return primi
