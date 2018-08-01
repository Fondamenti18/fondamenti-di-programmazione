from  my_html import HTMLNode, fparse
def conta_nodi(fileIn, selettore):
	f=fparse(fileIn)
	sel=selettore.split()
	insi=finder(f,sel,set())
	return len(insi)
def finder(nodo,sel,nodi={}):
	flag=False
	if sel[0]=='>':
		flag=True
		sel=sel[1:]
	lun=len(sel)
	trovato=False
	if not nodo.istext():
		if sel[0].isalnum():
			if nodo.tag==sel[0]:
				trovato=True
		if sel[0].startswith('.'):
			if 'class' in nodo.attr:
				if sel[0][1:] in nodo.attr['class']:
					trovato=True
		if sel[0].startswith('#'):
			if 'id' in nodo.attr:
				if nodo.attr['id']==sel[0][1:]:
					trovato=True
		if sel[0].startswith('@'):
			attri,sep,val=sel[0].partition('=')
			attri=attri[2:]
			if attri in nodo.attr:
				val=val[1:-2]
				if nodo.attr[attri]==val:
					trovato=True
		if trovato:
			if lun>1:
				for child in nodo.content:nodi=nodi.union(finder(child,sel[1:],nodi))
			else:
				nodi.add(nodo)
				return nodi
		else:
			if flag:
				return nodi
			else:
				for child in nodo.content:nodi=nodi.union(finder(child,sel,nodi))
	return nodi
def elimina_nodi(fileIn, selettore, fileOut):
	f=fparse(fileIn)
	sel=selettore.split()
	insi=finder(f,sel,set())
	delete(f,insi)#funzione ricorsiva che scorre i self.content e se sono in insi li elimina 
	doc=f.to_string()
	with open(fileOut,'w',encoding='utf-8') as fail:fail.write(doc)
def delete(nodo,insi):
	if not nodo.istext():
		for child in nodo.content:
			if child in insi:nodo.content.remove(child)
			delete(child,insi)
	return
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
	f=fparse(fileIn)
	sel=selettore.split()
	insi=finder(f,sel,set())
	changer(f,insi,chiave,valore)#funzione ricorsiva che scorre i self.content e se sono in insi li elimina 
	doc=f.to_string()
	with open(fileOut,'w',encoding='utf-8') as fail:fail.write(doc)
def changer(nodo,insi,key,val):
	if not nodo.istext():
		if nodo in insi:nodo.attr[key]=val
		for child in nodo.content:changer(child,insi,key,val)
	return
