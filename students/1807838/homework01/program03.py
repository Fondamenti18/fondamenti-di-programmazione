def codifica(chiave, testo):
	chiave=list(chiave)
	d=[]
	testo=list(testo)
	for x in range (len(chiave)-1,-1,-1):
		if chiave[x]>'z' or chiave[x]<'a' or chiave[x] in d:
			chiave.remove(chiave[x])
		else:
			d+=chiave[x]
	d=sorted(d)
	chiave={d[x]:chiave[x] for x in range (0,len(d))}
	testo=code(testo,chiave)
	return testo
	
def code(testo,chiave):
	testo2=''
	for x in range(len(testo)-1,-1,-1):
		if testo[x] in chiave:
			testo2+=chiave[testo[x]]
		else:
			testo2+=testo[x]
	testo2=testo2[::-1]
	return testo2
	
def decodifica(chiave, testo):
	chiave=list(chiave)
	d=[]
	testo=list(testo)
	for x in range (len(chiave)-1,-1,-1):
		if chiave[x]>'z' or chiave[x]<'a' or chiave.count(chiave[x])>1 :
			chiave.remove(chiave[x])
		else:
			d+=chiave[x]
		d=sorted(d)
	chiave={chiave[x]:d[x] for x in range (0,len(d))}
	testo=code(testo,chiave)
	return testo
