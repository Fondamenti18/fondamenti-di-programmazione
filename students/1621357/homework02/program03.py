def decod(pfile, codice):
	risultato = set()
	file = open(pfile,'r')
	for line in file:
		if len(line)-1 == len(codice) and len(set(zip(line,codice))) == len(set(line.strip('\n'))) == len(set(codice)):
			risultato.add(line.strip('\n'))
	file.close()
	return risultato
