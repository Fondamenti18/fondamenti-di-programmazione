from  my_html import HTMLNode, fparse
def conta_nodi(fileIn, selettore):
	albero = fparse(fileIn)
	selettore = selettore.split(' ')
	l = len(selettore)
	ins = conta(albero, selettore)
	return len(ins)
	
def conta(radice, selettore):
	x = selettore[0][0]
	if x.isalpha():
		i = tag(radice, selettore[0], set())
		i = passi(i, selettore[1:])
		return i
	if x == '.':
		i = punto(radice, selettore[0][1:], 'class', set())
		i = passi(i, selettore[1:])
		return i
	if x == '#':
		i = punto(radice, selettore[0][1:], 'id', set())
		i = passi(i, selettore[1:])
		return i
	parole = selettore[0][2:-1].split('=')
	i = punto(radice, parole[1][1:-1], parole[0], set())
	i = passi(i, selettore[1:])
	return i
	
def passi(lista, selettore):
	if not selettore:
		return lista
	l = len(selettore)
	s = selettore[0]
	new = set()
	if s == '>':
		for rad in lista:
			new.update(contasing(rad, selettore[1:]))
		return new
	for rad in lista:
		new.update(conta(rad, selettore))
	return new
	
def contasing(radice, selettore):
	x = selettore[0][0]
	if x.isalpha():
		i = tagsing(radice, selettore[0], set())
		i = passi(i, selettore[1:])
		return i
	if x == '.':
		i = puntosing(radice, selettore[0][1:], 'class', set())
		i = passi(i, selettore[1:])
		return i
	if x == '#':
		i = puntosing(radice, selettore[0][1:], 'id', set())
		i = passi(i, selettore[1:])
		return i
	parole = selettore[0][2:-1].split('=')
	i = puntosing(radice, parole[1][1:-1], parole[0], set())
	i = passi(i, selettore[1:])
	return i

def tagsing(radice, sel, insieme):
	l = len(radice.content)
	if l == 0 or (l == 1 and radice.content[0].istext()):
		return insieme
	for i in radice.content:
		if not i.istext() and i.tag == sel:
			insieme.add(i)
	return insieme
	
def puntosing(radice, sel, at, insieme):
	l = len(radice.content)
	if l == 0 or (l == 1 and radice.content[0].istext()):
		return insieme
	for i in radice.content:
		if not i.istext() and (at in radice.attr.keys() and sel in radice.attr[at]):
			insieme.add(i)
	return insieme
	
def tag(radice, sel, insieme):
	if radice.tag == sel:
		insieme.add(radice)
	l = len(radice.content)
	if l == 0 or (l == 1 and radice.content[0].istext()):
		return insieme
	for i in radice.content:
		if not i.istext():
			insieme.update(tag(i, sel, insieme))
	return insieme
		
def punto(radice, sel, at, insieme):
	if at in radice.attr.keys() and sel in radice.attr[at]:
		insieme.add(radice)
	l = len(radice.content)
	if l == 0 or (l == 1 and radice.content[0].istext()):
		return insieme
	for i in radice.content:
		if not i.istext():
			insieme.update(punto(i, sel, at, insieme))
	return insieme
		
def elimina_nodi(fileIn, selettore, fileOut):
	albero = fparse(fileIn)
	selettore = selettore.split(' ')
	l = len(selettore)
	ins = conta(albero, selettore)
	cancella(albero, ins)
	stampa(albero, fileOut)

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
	albero = fparse(fileIn)
	selettore = selettore.split(' ')
	l = len(selettore)
	ins = conta(albero, selettore)
	cambio(ins, chiave, valore)
	stampa(albero, fileOut)

def cambio(insieme, chiave, valore):
	for i in insieme:
		i.attr[chiave] = valore
	
def stampa(radice, out):
	f = open(out, 'w')
	f.write(radice.to_string())
	f.close()
	
def cancella(radice, insieme):
	if not radice.istext():
		for i, rad  in enumerate(radice.content):
			controllo(rad, i, insieme, radice)
	
			
def controllo(rad, i, insieme, radice):
	if rad in insieme:
		del radice.content[i]
		insieme.remove(rad)
	else:
		cancella(rad, insieme)
		