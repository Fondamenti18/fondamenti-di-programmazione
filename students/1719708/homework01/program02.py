def conv(n):
    return nome(make_list(n))	

def make_list(n):
	lista = list(str(n))
	lista.reverse()
	add = 3 - len(lista)%3
	while len(lista)%3:
		lista += ['0']*add
	return lista
    
def nome(lista):
	s = ''
	suffissi = [['', ''], ['mille', 'mila'], ['unmilione', 'milioni'], ['unmiliardo', 'miliardi'], ['unbilione', 'bilioni']]
	i = len(lista) - 1
	while i > 0:
		s += algoritmo(lista, i)
		if s == 'uno':
			s = suffissi[int(i/3)][0]
		elif s:
			s += suffissi[int(i/3)][1]
		i += -3
	return s

def algoritmo(lista, i):
	s = ''
	primi = {0 : '', 1 : 'uno', 2 : 'due', 3 : 'tre', 4 : 'quattro', 5 : 'cinque', 6 : 'sei', 7 : 'sette', 8 : 'otto', 9 : 'nove', 10 : 'dieci', 11 : 'undici', 12 : 'dodici', 13 : 'tredici', 14 : 'quattordici', 15 : 'quindici', 16 : 'sedici', 17 : 'diciassette',
				18 : 'diciotto', 19 : 'diciannove'}
	dec = {2 : 'venti', 3 : 'trenta', 4 : 'quaranta', 5 : 'cinquanta', 6 : 'sessanta', 7 : 'settanta', 8 : 'ottanta', 9 : 'novanta'}
	s1 = decine(lista, i, dec, primi)
	s2 = centinaia(lista, i, primi)
	if lista[i-1] == '8':
		s = s2[:-1] + s1
	else:
		s = s2 + s1
	return s
	
def centinaia(lista, i, primi):
	s = ''
	if lista[i] == '1':
		s = 'cento'
	elif lista[i] != '0':
		s = primi[int(lista[i])] + 'cento'
	return s

def decine(lista, i, dec, primi):
	s = ''
	if int(lista[i-1]) <= 1:
		s = primi[int(lista[i-1] + lista[i-2])]
	else:
		s = elisioni(lista, i, dec, primi)
	return s

def elisioni(lista, i, dec, primi):
	s = ''
	if int(lista[i-1]) > 1:
		s = dec[int(lista[i-1])]
	
	if lista[i-2] == '1' or lista[i-2] == '8':
		s = s[:-1] + primi[int(lista[i-2])]
	else:
		s = s + primi[int(lista[i-2])]
	return s