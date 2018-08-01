def decod(pfile, codice):
	''' Preso un file di parole e un codice numerico, ritorna un insieme composto 
	dalle parole del file che seguono la struttura del codice numerico '''
	f = open(pfile, mode='r', encoding='utf-8')
	righe = f.readlines()
	f.close()
	risultato=set()
	parole=[]
	parole=controlla_lung(righe,codice,parole)
	for parola in parole:
		dict_let={}
		corrisp=True
		corrisp=trova_errori(corrisp,codice,dict_let,parola)
		if corrisp:
			risultato.add(parola)
	return risultato

def controlla_lung(righe,codice,parole):
	for parola in righe:
		parola=''.join(parola.split())
		if len(parola) is len(codice):
			parole.append(parola)
	return parole

def itera_codice(codice,dict_let,parola,corrisp):
	for indice,numero in enumerate(codice):
		dict_let=aggiunta_let(numero,dict_let,parola,indice)
		if not parola[indice] is dict_let[numero]:
			corrisp=False
			break
	return corrisp

def aggiunta_let(numero,dict_let,parola,indice):
	if not numero in dict_let.keys() and not parola[indice] in dict_let.values():
		dict_let[numero]=parola[indice]
	return dict_let

def trova_errori(corrisp,codice,dict_let,parola):
	try:
		corrisp=itera_codice(codice,dict_let,parola,corrisp)
	except KeyError:
		corrisp=False
	return corrisp