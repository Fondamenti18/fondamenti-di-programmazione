def leggi(fword):
	f = open(fword, "r")
	res = f.read()
	f.close()
	return res

def sublist(lista, lencod):
	res = []
	for i, x in enumerate(lista):
		if len(x) == lencod:
			res += [x]
	return res

def formatta(lista):
	res = []
	for x in lista:
		res.append(formattacod(x))
	return res

def formattacod(cod):
    tab = []
    res = ""
    for c in cod:
        if c in tab:
            res += str(tab.index(c)+1)
        else:
            res += str(len(tab)+1)
            tab.append(c)
    return res

def decod(pfile, codice):
	lista = leggi(pfile).split()
	s3 = sublist(lista, len(codice))
	codici = formatta(s3)
	cod = formattacod(codice)
	res = set()
	for i,x in enumerate(codici):
		if x == cod:
			res.add(s3[i])
	return res

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

"""
import timeit
wrapped = wrapper(decod, 'all.txt','99223475')
print(timeit.timeit(wrapped, number=1)*1000, "ms")

wrapped = wrapper(decod, 'file03.txt','3533939339')
print(timeit.timeit(wrapped, number=1)*1000, "ms")
wrapped = wrapper(decod, 'file03.txt','138831')
print(timeit.timeit(wrapped, number=1)*1000, "ms")
wrapped = wrapper(decod, 'file03.txt','609155')
print(timeit.timeit(wrapped, number=1)*1000, "ms")
wrapped = wrapper(decod, 'all.txt','2091555')
print(timeit.timeit(wrapped, number=1)*1000, "ms")
wrapped = wrapper(decod, 'file03.txt', '121')
print(timeit.timeit(wrapped, number=1)*1000, "ms")
"""
