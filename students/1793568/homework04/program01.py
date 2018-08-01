import json

def scroll_sub_tree(k,d,r):
	if d[k] == []:
		r[k] = []
	else:
		r[k] = d[k]
		l = d[k]
		for e in l:
			scroll_sub_tree(e,d,r)

def del_sub_tree(k,d):
	#print(k)
	if d[k] == []:
		del d[k]
	else:
		l = d[k]
		#print(l)
		#del d[k]
		for n in d[k]:
			#print(n)
			del_sub_tree(n,d)
		del d[k]

def calculate_h(n,d,c):
	for k,v in d.items():
		if n in v:
			c[0] += 1
			calculate_h(k,d,c)

def calculate_older(n,d,c,y):
	for k,v in d.items():
		if n in v:
			if len(v) == y:
				c[0] += 1
			calculate_older(k,d,c,y)

def del_elem_values(v,x):
    for i in range(len(v[:])):
        if v[i] == x:
            del v[i]

def check_compatibility(x,i,m):
	s = ""
	if m == 0:
		for c in i:
			s += c
			if s == x:
				return True
	if m == 1:
		for st in i:
			s = ""
			for c in st:
				s += c
				if s == x:
					return True
	return False

def genera_sottoalbero(fnome,x,fout):
	res = {}
	with open(fnome) as f:
		d = json.load(f)
		for k,v in d.items():
			if k == x:
				scroll_sub_tree(k,d,res)
	with open(fout,"w") as f:
		json.dump(res,f)
	
def cancella_sottoalbero(fnome,x,fout):
	res = {}
	with open(fnome) as f:
		d = json.load(f)

		for k,v in d.items():
			if check_compatibility(x,v,1):
				del_elem_values(v,x)
			if check_compatibility(x,k,0):
				if k in d.keys():
					del_sub_tree(k,d)
	res = d

	with open(fout,"w") as f:
		json.dump(res,f)


def dizionario_livelli(fnome,fout):
    res = {}
    lista = [0]
    with open(fnome) as f:
        d = json.load(f)
        for k,v in d.items():
            lista[0] = 0
            calculate_h(k,d,lista)
            if lista[0] not in res.keys():
                res[lista[0]] = [k]
            else:
                res[lista[0]] += [k]
                set2 = set(res[lista[0]])
                res[lista[0]] = sorted(set2)
                
    with open(fout,"w") as f:
        json.dump(res,f)


def dizionario_gradi_antenati(fnome,y,fout):
    res = {}
    lista = [0]
    with open(fnome) as f:
        d = json.load(f)
        for k,v in d.items():
            lista[0] = 0
            calculate_older(k,d,lista,y)
            res[k] = lista[0]
    with open(fout,"w") as f:
        json.dump(res,f)