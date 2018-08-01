def modi(ls,k):
        from math import sqrt
        lista_numeri_primi = []
        lista_numeri = []
        for numero in ls [:]:
                num_divisori = 0
                for x in range (2,int(sqrt(numero)) + 1):
                        if numero % x == 0:
                                num_divisori = num_divisori + 1
                num_divisori = num_divisori * 2
                if num_divisori == 0:
                        lista_numeri_primi.append(numero)
                        ls.remove(numero)
                elif num_divisori != k:
                        ls.remove (numero)
        return lista_numeri_primi
