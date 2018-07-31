def decod(pfile, codice):
	file = open(pfile, 'r', encoding='utf-8')
	ris = set()
	for parola in file:
		if uguali(parola.strip(),codice):
			ris.add(parola.strip())
	file.close()
	return ris
		
def uguali(parola,codice):
	try:
		m = max([len(parola),len(codice)])
		for indice in range(m):
			if trovaProssimo(parola,indice) != trovaProssimo(codice,indice):
				return False
		return True
	except Exception as eccezione:
		return False
		
def trovaProssimo(stringa,indice):
	return stringa.find(stringa[indice],indice+1)