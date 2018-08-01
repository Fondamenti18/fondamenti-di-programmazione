def post(fposts,insieme):
	with open(fposts, encoding = 'utf-8') as f:
		s = f.read()
	lista = makeList(s)
	return contenuto(lista, insieme)
	

def makeList(stringa):
	ls = stringa.split('<POST>')
	for i in range(len(ls)):
		ls[i] = ls[i].lstrip()
	return ls
	
def contenuto(lista, insieme):
	insieme = list(insieme)
	risultato = set()
	for line in lista:
		if controllo(line, insieme):
			risultato.add(id(line))
	return risultato
			
def controllo(post, parola):
	i = 0
	post = editaStringa(post).lower().split()
	while parola[i].lower() not in post and i < len(parola) - 1:
			i += 1
	return  parola[i].lower() in post
	
def id(line):
	i = 0
	temp = ''
	while line[i].isdigit():
		temp += line[i]
		i += 1
	return temp

def editaStringa(stringa):
	s = ''
	for i in stringa:
		if i.isalpha():
			s += i
		else:
			s += ' '
	return s

