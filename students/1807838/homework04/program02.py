class NodoTris:
	def __init__(self, griglia):
		self.nome = griglia
		self.lista_figli = []
		self.stato=self.tipo()
		if self.stato=='o':self.val=100
		elif self.stato=='x':self.val=-100
		elif self.stato=='-':self.val=0
	
	def tipo(self):
		or1=set(self.nome[0])
		if len(or1)==1 and or1!={''}:return or1.pop()
		or2=set(self.nome[1])
		if len(or2)==1 and or2!={''}:return or2.pop()
		or3=set(self.nome[2])
		if len(or3)==1 and or3!={''}:return or3.pop()
		
		ver1={self.nome[0][0],self.nome[1][0],self.nome[2][0]}
		if len(ver1)==1 and ver1!={''}:return ver1.pop()
		ver2={self.nome[0][1],self.nome[1][1],self.nome[2][1]}
		if len(ver2)==1 and ver2!={''}:return ver2.pop()
		ver3={self.nome[0][2],self.nome[1][2],self.nome[2][2]}
		if len(ver3)==1 and ver3!={''}:return ver3.pop()
		
		d1={self.nome[0][0],self.nome[1][1],self.nome[2][2]}
		if len(d1)==1 and d1!={''}:return d1.pop()
		d2={self.nome[0][2],self.nome[1][1],self.nome[2][0]}
		if len(d2)==1 and d2!={''}:return d2.pop()
		
		join=or1.union(or2,or3,ver1,ver2,ver3,d1,d2)
		if '' in join:return '?'
		else:return'-'
	
	def esiti(self): # (patte,win per 'o', win per 'x')
		ret=[0,0,0]
		ret=tuple(self.check_esiti(ret))
		return ret
	
	def check_esiti(self,ret):#      OK
		if self.stato=='-':ret[0]+=1
		if self.stato=='o':ret[1]+=1
		if self.stato=='x':ret[2]+=1
		for child in self.lista_figli:ret=child.check_esiti(ret)
		return ret
	
	def vittorie_livello(self, giocatore, h,livello=0,count=0):
		if self.stato == giocatore and livello==h:
			count+=1
		for child in self.lista_figli:count=child.vittorie_livello(giocatore,h,livello+1,count)
		return count
	
	def strategia_vincente(self,giocatore):#					NO
		val=self.check_win()
		if val>0:win='o'
		else:win='x'
		if win == giocatore:return True
		else: return False
	
	def check_win(self):
		if self.lista_figli==[]:return self.val
		if not check_step(self.nome):
			self.val=1000
			for child in self.lista_figli:
				self.val=min(self.val,child.check_win())
		else:
			self.val=-1000
			for child in self.lista_figli:
				self.val=max(self.val,child.check_win())
		return self.val

def gen_tree(nodo,step=True,c=0):
	if c==0:nodo=NodoTris(nodo)
	if c==0:step=check_step(nodo.nome)
	c+=1
	if nodo.stato=='?':
		copia=[x[:] for x in nodo.nome]
		for row in range(3):
			for col in range(3):
				if nodo.nome[row][col]=='':
					if step:copia[row][col]='o'
					else:copia[row][col]='x'
					appendi=NodoTris(copia)
					nodo.lista_figli.append(appendi)
					gen_tree(appendi,not step,c)
					copia[row][col]=''
	return nodo

def check_step(griglia):
	o=0
	x=0
	for row in griglia:
		o+=row.count('o')
		x+=row.count('x')
	if o>x:return False
	else:return True

'''
g0=[['', '', ''], ['', '', ''], ['', '', '']]
g1=[['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
g2=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'o']]
g3=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', '', 'x']]
g4=[['o', 'x', 'x'], ['x', 'o', 'o'], ['o', 'o', 'x']]

g5=[['', 'x', ''], ['', 'o', ''], ['', '', '']]
g6=[['', 'o', ''], ['', 'x', ''], ['', '', '']]
g7=[['', 'x', 'o'], ['', '', ''], ['', '', '']]
g8=[['', 'o', 'x'], ['', '', ''], ['', '', '']]

fai=[g5,g6,g7,g8]
####						TESTS
import time
start=time.time()
rad=gen_tree(g5)
print(rad.strategia_vincente('o'))
print(time.time()-start)
'''
