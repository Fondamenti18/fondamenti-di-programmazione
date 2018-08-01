def decod(pfile, codice):
	parole = []
	with open(pfile, encoding = 'utf-8') as f:
		for line in f:
			if len(line) - 1 == len(codice):
				parole += [line.strip()]
	return make_set(parole, codice)

def make_set(parole, codice):
	set_parole = set()
	for parola in parole:
		set_parole.add(controllo_parola(parola, codice))
	set_parole.remove(None)
	return set_parole

def controllo_parola(stringa, codice):
	d = make_dict(stringa, codice)
	s = generate_keyword(d, codice)
	if s == stringa:
		return stringa

def make_dict(stringa, codice):
	d = {}
	for c in range(len(codice)):
		if codice[c] not in d and stringa[c] not in d.values():
			d[codice[c]] = stringa[c]
	return d
	
def generate_keyword(d, codice):
	s = ''
	for c in codice:
		if c in d:
			s += d[c]
	return s

