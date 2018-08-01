
import copy
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.dizionario_lvl,self.esitilvl=self.vittorie_livelloxesiti()
    def tipo(self):
        return tipo_gen(self.nome)
    
    def esiti(self):
        return gen_esitixalbero(self.esitilvl,0,0,0,[])
    
    def vittorie_livello(self,giocatore,h):
        d=self.dizionario_lvl
        c=copy.deepcopy(d)
        x=vittorie_lvl(c,h)
        if giocatore=="x":
            return x[1]
        else:
            return x[0]
        
    def vittorie_livelloxesiti(self):
        griglia=self.nome
        dizionario_livelli={}
        tipoo=self.tipo()
        if tipoo=="x":
            dizionario_livelli[0]=[0,1]
            return dizionario_livelli,[(0,0,1)]
        elif tipoo=="o":
            dizionario_livelli[0]=[1,0]
            return dizionario_livelli,[(0,1,0)]
        elif tipoo=="-":
            dizionario_livelli[0]=[0,0]
            return dizionario_livelli,[(1,0,0)]
        elif tipoo=="?":
            dizionario_livelli[0]=[0,0]
        lista_generazione=[griglia]
        lista_temp=[]
        giocatore=""
        vittorie=0
        vittorie_o=0
        vittorie_x=0
        patte=0
        giocatore=turno_giocatore(lista_generazione[0])
        c=1
        lista_lvl=[]
        while lista_generazione!=[]:
            lista=[]
            vittorie_lvlx=0
            vittorie_lvlo=0
            for i in lista_generazione:
                lista_temp,vittorie,pattet=mosse_successive(i,giocatore)
                lista+=lista_temp
                if giocatore=="x":
                    vittorie_x+=vittorie
                    vittorie_lvlx+=vittorie
                elif giocatore=="o":
                    vittorie_o+=vittorie
                    vittorie_lvlo+=vittorie
                patte+=pattet
            lista_lvl.append((patte,vittorie_lvlo,vittorie_lvlx))
            dizionario_livelli[c]=[vittorie_lvlo,vittorie_lvlx]
            giocatore=toggler(giocatore)
            lista_generazione=lista
            c+=1
        self.ultimo_giocatore=toggler(giocatore)
        return dizionario_livelli,lista_lvl
    
    def strategia_vincente(self,giocatore):
        tupla=gen_esitixalbero(self.esitilvl,0,0,0,[])
        if self.ultimo_giocatore=="x" and giocatore=="x" and tupla[2]>0:
            return True
        elif self.ultimo_giocatore=="o" and giocatore=="o" and tupla[1]>0:
            return True
        else:
            return False

        
def toggler(x):
        if x=="x":
            x="o"
        else:
            x="x"
        return x

def mosse_successive(griglia,giocatore):
    lista_possibilita=[]
    griglia_futura=copy.deepcopy(griglia)
    vittorie=0
    patte=0
    tipoo=tipo_gen(griglia_futura)
    for j in range(3):
        for i in range(3):
            if griglia[j][i]=="":
                griglia_futura[j][i]=giocatore
                tipoo=tipo_gen(griglia_futura)
                if tipoo=="x" or tipoo=="o":
                    vittorie+=1
                    griglia_futura=copy.deepcopy(griglia)
                    continue
                elif tipoo=="-":
                    patte+=1
                    griglia_futura=copy.deepcopy(griglia)
                    continue
                lista_possibilita.append(griglia_futura)
                griglia_futura=copy.deepcopy(griglia)
    return lista_possibilita,vittorie,patte

def vittorie_lvl(d,h):
    x=list(d.keys())[0]
    if x==h:
        return d[x]
    else:
        del d[x]
        vittorie_lvl(d,h)
        return d[h]

def gen_esitixalbero(lista,patte,vittorieo,vittoriex,listaout):
	if lista==[]:
		return patte,vittorieo,vittoriex
	else:
		patte+=lista[0][0]
		vittorieo+=lista[0][1]
		vittoriex+=lista[0][2]
		listaout.append((patte,vittorieo,vittoriex))
	gen_esitixalbero(lista[1:],patte,vittorieo,vittoriex,listaout)
	return listaout[-1]
    

def tipo_gen(griglia):
        c=0
        patta=0
        lista_pos=[
            [griglia[0][0],griglia[0][1],griglia[0][2]],
            [griglia[1][0],griglia[1][1],griglia[1][2]],
            [griglia[2][0],griglia[2][1],griglia[2][2]],
            [griglia[0][0],griglia[1][0],griglia[2][0]],
            [griglia[0][1],griglia[1][1],griglia[2][1]],
            [griglia[0][2],griglia[1][2],griglia[2][2]],
            [griglia[0][0],griglia[1][1],griglia[2][2]],
            [griglia[0][2],griglia[1][1],griglia[2][0]]]
        for i in lista_pos:
            if i.count("x")==3:
                return "x"
            elif i.count("o")==3:
                return "o"
            if "" in i:
                patta=1
        if patta==1:
            return "?"
        else:
            return "-"
def gen_tree(griglia):
    griglia=NodoTris(griglia)
    return griglia
def turno_giocatore(griglia):
    verifica=copy.deepcopy(griglia)
    verifica=str(verifica)
    o=verifica.count("o")
    x=verifica.count("x")
    if o==x:
        return "o"
    elif x<o:
        return "x"
    else:
        return "o"


    






        
