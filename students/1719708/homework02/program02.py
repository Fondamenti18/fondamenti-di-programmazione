from json import dump
        
def pianifica(fcompiti,insi,fout):
	with open(fcompiti, encoding = 'utf-8') as f_c:
		contenuto = f_c.read()
	d_base = makeDict(contenuto)
	d_avanzato = improveDict(d_base, insi)
	scriviFile(d_avanzato, fout)
	
def makeDict(stringa):
	lista = stringa.replace(' ', '').split()
	i = 0
	d = {}
	while i < len(lista):
		if i+1 < len(lista) and 'sub' in lista[i+1]:
			d[estraiNumeri(lista[i])] = [estraiNumeri(lista[i+1])]
			i += 2
		else:
			d[estraiNumeri(lista[i])] = []
			i += 1
	return d

def estraiNumeri(stringa):
	s = ''
	i = len(stringa) - 1
	while stringa[i].isdigit():
		s = stringa[i] + s
		i += -1
	return s

def improveDict(d, insieme):
	n_d = {}
	for i in insieme:
		n_d = tempDict(n_d, d, i)
	return n_d

def scriviFile(dizionario, file):
	with open(file, 'w', encoding = 'utf-8') as f:
		dump(dizionario, f)
	
def tempDict(n_d, d, i):
	if i in d and d[i] != []:
		n_d = loopDict(n_d, d, i)
	elif i in d:
		n_d[i] = d[i]
	return n_d
	
def loopDict(n_d, d, i):
	n_d[i] = d[i]
	while d[n_d[i][0]] != []:
		n_d[i] = d[n_d[i][0]] + n_d[i]
	return n_d