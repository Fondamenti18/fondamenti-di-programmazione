
class NodoTris:
    def __init__(self, griglia):        
        self.nome = griglia
        self.stato="?"
        self.lista_figli = [] #lista dei nodi figli
    p=0
    v_o=0
    v_x=0
    def conta(self):
        for x in self.lista_figli:
            if x.stato=="x":
                NodoTris.v_x+=1
            elif x.stato=="o":
                NodoTris.v_o+=1
            elif x.stato=="-":
                NodoTris.p+=1
            x.conta()	
        return (NodoTris.p,NodoTris.v_o,NodoTris.v_x)
    
    def esiti(self):        
        NodoTris.p=0
        NodoTris.v_o=0
        NodoTris.v_x=0
        l=NodoTris.conta(self)
        ris=self.tipo()
        if ris=="x":
            return (l[0],l[1],l[2]+1)
        elif ris=="o":
            return (l[0],l[1]+1,l[2])
        elif ris=="-":
            return (l[0]+1,l[1],l[2])
        return l
    
    def tipo(self):
	    n_o=0
	    for x in range(3):
		    n_o=n_o+self.nome[x].count("o")
		    c= self.nome[0][x]+self.nome[1][x]+self.nome[2][x]
		    if self.nome[x].count("x")>2:			    
			    return "x"
		    elif self.nome[x].count("o")>2:
			    return "o"
		    elif c=="xxx":
			    return "x"
		    elif c=="ooo":
			    return "o"
	    obl1=self.nome[0][0]+self.nome[1][1]+self.nome[2][2]
	    obl2=self.nome[0][2]+self.nome[1][1]+self.nome[2][0]
	    if obl1=="xxx" or obl2=="xxx":
		    return "x"
	    elif obl2=="ooo" or obl1=="ooo":
		    return "o"
	    elif n_o==5:
		    return "-"
	    else:
		    return"?"



    def vittorie_livello(self, giocatore, h):
        count=0
        if h==0:
            if self.stato==giocatore:
                return 1
        for x in self.lista_figli:
            count=count+x.vittorie_livello(giocatore,h-1)
        return count					

    def strategia_vincente(self,giocatore):
        if self.tipo()==giocatore:
            return True
        elif self.tipo()=="?":
            pass
        else:
            return False
        n_x=0
        n_o=0
        for x in self.nome:
            n_x=n_x+x.count("x")
            n_o=n_o+x.count("o")
        if giocatore=="o" and n_o==n_x:
            return self.strategia(giocatore,giocatore)
        elif giocatore=="x" and n_o==n_x:
            return self.strategia(giocatore,"ciao")
        elif giocatore=="x" and n_o>n_x:
            return self.strategia(giocatore,"ciao")
        elif giocatore=="o" and n_o>n_x:
            return self.strategia(giocatore,giocatore)  
              
    
    def vittoria(self,giocatore):
        c=False
        for x in self.lista_figli:            
            if x.tipo()==giocatore:
                return True
            c=x.vittoria(giocatore)
            if c:
                return True
        return False

    
    def strategia(self,giocatore,mossa):
        r=0
        #print("ciclio")
        if mossa==giocatore:
            #print("muove il giocatore")
            for x in self.lista_figli:
                #print("controllo l'elemento ",x.nome)
                if giocatore==x.tipo():
                    #print("trovata una combianazione vincente ",x.nome)
                    return True
                if x.vittoria(giocatore):
                    #print("possibile vittoria per ",x.nome)
                    r=x.strategia(giocatore,"coso")
                    #print(" r del giocatore vale ",r)
                    if r:
                        return True            
        else:
            #print("muovo l'avversario ")
            for x in self.lista_figli:
                if not x.vittoria(giocatore):
                    #print("beccato uno che blocca la strada  ", x.nome)
                    return False
            for x in self.lista_figli:
                #print("controllo dopo l'avversario ")
                r=x.strategia(giocatore,giocatore)
                #print("tutti questi non fermano il giocatore   ",x.nome,"    r",r) 
                if r:
                    return True
        return False

ciclo=range(3)
		
def gen_tree(griglia):
	#print(griglia)
	g2= [x[:] for x in griglia]
	elemento1=NodoTris(g2)
	n_x=0
	n_o=0
	switch=False

	for x in g2:
		n_x=n_x+x.count("x")
		n_o=n_o+x.count("o")

	if n_o>2:
		chk=elemento1.tipo()
		#print("ck ",chk)
		if chk=="x":
			elemento1.stato="x"
			return elemento1
		elif chk=="o":
			elemento1.stato="o"
			return elemento1
		elif chk=="-":
			elemento1.stato="-"
			return elemento1
	if n_o>n_x:
		switch=True


	for x in ciclo:
		for y in ciclo:
			if g2[x][y]=="" and switch:
				g2[x][y]="x"
				elemento1.lista_figli.append(gen_tree(g2))
				g2[x][y]=""
			elif g2[x][y]=="":
				g2[x][y]="o"
				elemento1.lista_figli.append(gen_tree(g2))
				g2[x][y]=""
	return elemento1

    
    

