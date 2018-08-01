import json
#-----------------------LETTURA_JSON--------------------------------------------
def open_read(fnome):
	with open(fnome, 'r', encoding='UTF-8') as f:
		d=json.load(f)
	return d
	
def open_write(fout,d):
	with open(fout, 'w', encoding='UTF-8') as f:
		json.dump(d, f)

#----------------------GENERA_SOTTOALBERO---------------------------------------------
def pop_subtree(x , d, lista, c):
	if c<len(lista):
		x=lista[c]
		lista+=d.get(x)
		c+=1
		return pop_subtree(x , d, lista, c)
	else:
		return {k:v for (k,v) in d.items() if k in lista}
		
def genera_sottoalbero(fnome,x,fout):
	d=open_read(fnome)
	if x in d: d=pop_subtree(x , d, [x], 0)
	open_write(fout,d)
	
#------------------------CANCELLA_SOTTOALBERO-------------------------------------------
def pop_tree(x , d, lista, c):
	if c<len(lista):
		x=lista[c]
		lista+=d.get(x)
		c+=1
		return pop_tree(x , d, lista, c)
	else:
		d={k:v for (k,v) in d.items() if k not in lista}
		key=list(d.keys())
		val=list(d.values())
		i=0
		while i<len(val):
			val[i]=[x for x in val[i] if x not in lista]
			i+=1
		return dict(zip(key,val))

def cancella_sottoalbero(fnome,x,fout):
	d=open_read(fnome)
	if x in d: d=pop_tree(x , d, [x], 0)
	open_write(fout,d)
	
#--------------------------CONTA_LIVELLI-----------------------------------------
def trovaradice(d, key):
	val=list(d.values())
	v=set()
	for i in range(len(val)):
		for j in range(len(val[i])):
			v.add(val[i][j])
	key.difference_update(v)
	return list(key)
		
def conta_livelli(d, k, controllo, lvl, lista, ind):
	if controllo==False:
		key=set(d.keys())
		rad=trovaradice(d,key)
		return conta_livelli(d,	[[rad[0]]], True, lvl, rad, ind)
	if lista!=[]:
		app=[]
		for i in lista:
			app+=d.get(i)
		if app!=[]:
			app=sorted(app)
			k+=[app]
			ind+=1
			lvl+=[ind]
			lista[:]=app[:]
			return conta_livelli(d,	k, True, lvl, lista, ind)
		else:
			lista[:]=app[:]
			return conta_livelli(d,	k, True, lvl, lista, ind)
	else:
		return dict(zip(lvl,k))
			
def dizionario_livelli(fnome,fout):
	d=open_read(fnome)
	d=conta_livelli(d, [], False, [0], [], 0)
	open_write(fout, d)

#----------------------GRADI_ANTENATI---------------------------------------------
def gradi_antenati(d, controllo, rad):
	if controllo==False:
		key=set(d.keys())
		rad=trovaradice(d,key)
		return gradi_antenati(d, True, rad)

def dizionario_gradi_antenati(fnome,y,fout):
	d=open_read(fnome)
	d=gradi_antenati(d, False, [])
	open_write(fout, d)
