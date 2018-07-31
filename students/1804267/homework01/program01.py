import math as m
ls = [121, 4, 37, 441, 7, 16]

def findfac(n):
   faclist = []
   for i in range(2, int(m.sqrt(n) + 2)):
       if n%i == 0:
           if i not in faclist:
               faclist.append(i)
               if n/i not in faclist:
                   faclist.append(n/i)
   return faclist

def modi(ls, k):
    lp = []
    for el in ls[:]:
        nfac = len(findfac(el))
        if nfac == 0:
            lp.append(el)
        if nfac != k:
            ls.remove(el)
    return lp

print(modi(ls,3))
print(ls)