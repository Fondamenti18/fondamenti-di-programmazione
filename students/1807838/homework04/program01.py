from json import *

def genera_sottoalbero(fnome,x,fout):
	diz={}
	with open (fnome) as fail:f=load(fail)
	diz[x]=f[x]
	genera(diz,diz[x],f)
	with open(fout,'w')as fail:dump(diz,fail)
def genera(d,li,f):
	for x in li:
		d[x]=f[x]
		genera(d,d[x],f)
def cancella_sottoalbero(fnome,x,fout):
	with open (fnome) as fail:f=load(fail)
	cancella_nodi(f,x)
	for key in f:
		for val in f[key]:
			if val==x:
				f[key].remove(val)
	with open(fout,'w')as fail:dump(f,fail)
def cancella_nodi(f,x):
	for y in f[x]:
		cancella_nodi(f,y)
	del f[x]

###^^^ OK

def dizionario_livelli(fnome,fout):
	with open(fnome) as fail:f=load(fail)
	d={}
	x=trova_radice(f)
	d['0']=x.split()
	livelli(f,x,1,d)
	for x in d:
		d[x]=sorted(d[x])
	with open(fout,'w')as fail:dump(d,fail)

def livelli(f,x,level,d):
	for key in f[x]:
		try:
			d[str(level)].append(key)
		except KeyError:
			d[str(level)]=key.split()
		livelli(f,key,level+1,d)

def dizionario_gradi_antenati(fnome,y,fout):
	with open(fnome) as fail:f=load(fail)
	d={}
	x=trova_radice(f)
	d[x]=0
	antenati(f,x,d,y)
	with open(fout,'w') as fail:dump(d,fail)


def antenati(f,x,d,y,quanti=0):
	grado=len(f[x])
	for key in f[x]:
		if grado==y:antenati(f,key,d,y,quanti+1)
		else:antenati(f,key,d,y,quanti)
	d[x]=quanti


def trova_radice(f):
	nodi={x for x in f}
	figli=set()
	for x in f:
		for y in f[x]:
			figli.add(y)
	diff=nodi.difference(figli)
	return diff.pop()
