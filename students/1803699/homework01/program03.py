def becomekey(x):
	chiave=''
	for i in range(0, len(x)):
		if x[i].islower()==True:
			chiave+=x[i]
	return chiave

def disordinata(k):
	visto = []
	for i in k[::-1]:
		if i not in visto:
			visto.append(i)
	return list(reversed(visto))

def becomedict(y):
	p=becomekey(y)
	m=disordinata(p)
	n=sorted(m)
	encripta={}
	decripta={}
	for i in range(0, len(m)):
		encripta[m[i]]=n[i]
		decripta[n[i]]=m[i]
	return encripta
	return decripta
    
def becomeencripter(y):
	p=becomekey(y)
	m=disordinata(p)
	n=sorted(m)
	encripter={}
	for i in range(0, len(m)):
		encripter[n[i]]=m[i]
	return encripter

def becomedecripter(y):
	p=becomekey(y)
	m=disordinata(p)
	n=sorted(m)
	decripter={}
	for i in range(0, len(m)):
		decripter[m[i]]=n[i]
	return decripter

def codifica(chiave, testo_in_chiaro):
	encripta=becomeencripter(chiave)
	ls=list(testo_in_chiaro)
	for i in range(0, len(ls)):
		if ls[i] in encripta:
			ls[i]=encripta[ls[i]]
		else:
			ls[i]=ls[i]
	testo_crittografato=''.join(ls)
	return testo_crittografato

def decodifica(chiave, testo_crittografato):
	encripta=becomedecripter(chiave)
	ls=list(testo_crittografato)
	for i in range(0, len(ls)):
		if ls[i] in encripta:
			ls[i]=encripta[ls[i]]
		else:
			ls[i]=ls[i]
	testo_in_chiaro=''.join(ls)
	return testo_in_chiaro   
