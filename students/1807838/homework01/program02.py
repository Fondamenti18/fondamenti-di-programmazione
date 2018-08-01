esp1=[12,11,10]
esp2=[9,8,7]
esp3=[6,5,4]
d1={'0':'','1':'uno','2':'due','3':'tre','4':'quattro','5':'cinque','6':'sei','7':'sette','8':'otto','9':'nove'}
d2={'0':'','2':'venti','3':'trenta','4':'quaranta','5':'cinquanta','6':'sessanta','7':'settanta','8':'ottanta','9':'novanta'}
cento='cento'
d10={'0':'dieci','1':'undici','2':'dodici','3':'tredici','4':'quattordici','5':'quindici','6':'sedici','7':'diciassette','8':'diciotto','9':'diciannove'}
def conv(n):
	n=str(n)
	f=len(n) 
	zero='0'
	lettere=''
	while f!=0:
		if f in esp1:
			gr=str(int(n)//1000000000)
			gr=gr.zfill(3)
			if f%3==2:
				f+=1
			if f%3==1:
				f+=2
		elif f in esp2:
			gr=str((int(n)//1000000)%1000)
			gr=gr.zfill(3)
			if f%3==2:
				f+=1
			if f%3==1:
				f+=2
		elif f in esp3:
			gr=str((int(n)//1000)%1000)
			gr=gr.zfill(3)
			if f%3==2:
				f+=1
			if f%3==1:
				f+=2
		else:
			gr=str(int(n)%1000)
			gr=gr.zfill(3)
			if f%3==2:
				f+=1
			if f%3==1:
				f+=2
		f,ris=gruppo2(f,gr)
		f-=3
		lettere+=ris
	return lettere

def gruppo2(f,gr):
	e=len(gr)
	s=''
	c=0
	uno=False
	while e!=0:
		if e==3:
			s1,e,c=terza(gr,c,e)
			s+=s1
		elif e==2:
			s1,e,c=seconda(gr,c,e)
			s+=s1
		elif e==1:
			s1,e,c,uno=prima(gr,c,e,uno)
			s+=s1
	if gr!='000':
		s+=suffisso(uno,s,f)
	return f,s

def terza(gr,c,e,s=''):
	if gr[c+1]=='8' and gr[c]!='0' and gr[c]!='1':
		s+=d1[gr[c]]+cento[:-1]
	elif gr[c+1]!='8' and gr[c]!='0' and gr[c]!='1':
		s+=d1[gr[c]]+cento
	elif gr[c]=='1':
		s+=cento
	c+=1
	e-=1
	return s,e,c

def seconda(gr,c,e,s=''):
	if gr[c]=='1':
		s+=d10[gr[c+1]]
		c+=2
		e-=2
	elif (gr[c+1]=='8' or gr[c+1]=='1') and gr[c]!='1':
		s+=d2[gr[c]][:-1]
		c+=1
		e-=1
	elif gr[c+1]!='1' and gr[c+1]!='8' and gr[c]!='1':
		s+=d2[gr[c]]
		c+=1
		e-=1
	return s,e,c

def prima(gr,c,e,uno=False,s=''):
	if gr[c]=='1' and gr[c-1]=='0' and gr[c-2]=='0':
		uno=True
	else:
		s+=d1[gr[c]]
	c+=1
	e-=1
	return s,e,c,uno

def suffisso(uno,s,f):
	if uno:
		if f in esp1:
			add='unmiliardo'
		elif f in esp2:
			add='unmilione'
			
		elif f in esp3:
			add='mille'
		else:
			add='uno'
	else:
		if f in esp1:
			add='miliardi'
		elif f in esp2:
			add='milioni'
		elif f in esp3:
			add='mila'
		else:
			add=''
	return add
