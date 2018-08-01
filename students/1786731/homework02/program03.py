def rejectFromLength(line, codice):
	if len(line) != len(codice):
		return True
	
	return False

def rejectFromEquality(t1, t2):
	codedict = { }

	for i in range(0, len(t2)):
		t = t2[i]

		if t not in codedict:
			codedict[t] = t1[i]
			continue

		if codedict[t] != t1[i]:
			return True

	return False

		
def decod(pfile, codice):
	risultato = set()

	f = open(pfile)
	
	for line in f:

		strippedline = line.strip()

		if rejectFromLength(strippedline, codice): 
			continue

		if rejectFromEquality(strippedline, codice) | rejectFromEquality(codice, strippedline):
			continue

		risultato.add(strippedline)

	f.close()
	return risultato