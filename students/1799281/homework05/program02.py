#programma preso molto dal libro

class _nodo:
    def __init__(self,nome,ad):          #Oggetto di tipo nodo            
        self.nome=nome
        self.ad=set(ad)
class _grafo:                            #Grafo:  NODO:[NODO1,NODO2]   <----- vicini
    def __init__(self):
        self.nodi={}         #<-----------------DIZIONARIO
    
    def add_nodo(self,nome):       
        if nome in self.nodi:
            return
        self.nodi[nome]=_nodo(nome,set())
    def add_arco(self,nome1,nome2):
        if nome1 not in self.nodi:
            return
        if nome2 not in self.nodi:
            return
        self.nodi[nome1].ad.add(nome2)
        self.nodi[nome2].ad.add(nome1)

    def lista_adiacenti(self,nome):
        if nome not in self.nodi:
            return None
        return list(self.nodi[nome].ad)
    def lista_nodi(self):
            return list(self.nodi.keys())
    def lista_archi(self):                   #RITORNA TUTTI I NODI CON TUTTE LE CONNESSIONI
            archi=set()
            for nome, nodo in self.nodi.items():
                for adiacenti in nodo.ad:
                    if (adiacente,nome) in archi:
                        continue
                    archi.add((nome,adiacente))
            return list(archi)

def distanza(grafo, nome):            #GENERA: UN DIZIONARIO CON LA DISTANZA TRA NOME E TUTTI I NODI DOPO
    vedere=set([nome])                #GENERA: UN DIZIONARIO CON IL GRAFO CONVERTITO AD ALBERO SE IL NOME PASSATO E' LA RADICE
    visti=set([nome])
    distanze={nome:0}
    albero={nome:None}
    while vedere:
        nuovo=set()
        while vedere:
            u = vedere.pop()
            for i in grafo.lista_adiacenti(u):
                if i not in visti:
                    visti.add(i)
                    nuovo.add(i)
                    distanze[i]=distanze[u] + 1
               
        vedere=nuovo
    return(distanze)
def genera_albero(grafo,nome):
    global creato
    vedere=set([nome])                #GENERA: UN DIZIONARIO CON IL GRAFO CONVERTITO AD ALBERO SE IL NOME PASSATO E' LA RADICE
    visti=set([nome])
    distanze={nome:0}
    albero={nome:None}
    while vedere:
        nuovo=set()
        while vedere:
            u = vedere.pop()
            #print("u--->",u)
            for i in grafo.lista_adiacenti(u):
                if i not in visti:
                    visti.add(i)
                    nuovo.add(i)
                    albero[i]=u
        vedere=nuovo
    #print(albero)
        creato=1
    return(albero)
    
def cammino(albero,nome):
    global crea1
    global percorso
    radice=None
    for root, gen in albero.items():
        if gen==None:
            print(root,nome)
            radice = root
            break
        print(nome in albero)
    if nome in albero:
        print("soem")
        percorso=[nome]
        while nome!= radice:
            nome=albero[nome]
            percorso.insert(0,nome)  #insert: index,valore
            #print("CREA --->",percorso)
        crea1=1
        return percorso
        #else:
            #print("CREA --->",percorso)
            #crea1=1
            #return []

def genera_grafico(mappa,car):
    global creato
    global pista
    pista=_grafo()
    vicini=[(-1,0),(1,0),(0,-1),(0,1)]
    for y in range(len(mappa)):
        for x in range(len(mappa[0])):
            if mappa[y][x]==" " or  mappa[y][x]=="O" or  mappa[y][x]==car or  (mappa[y][x].isalpha()==True and mappa[y][x].isalpha!=car) :
                pista.add_nodo((x,y))
    for y in range(len(mappa)):
        for x in range(len(mappa[0])):
            if mappa[y][x]==" " or mappa[y][x]=="O" or mappa[y][x]==car or  (mappa[y][x].isalpha()==True and mappa[y][x].isalpha!=car) :
                for k,j in vicini:
                    a=k+x
                    b=j+y
                    if mappa[b][a]==" " or mappa[b][a]=="O" or mappa[b][a]==car or  (mappa[b][a].isalpha()==True and mappa[b][a].isalpha!=car) :
                        pista.add_arco((x,y),(a,b))
    #creato=1
def ia2(prossimo,vx,vy,x,y,mappa):
    global distanze
    global albero
    lista=[]
    if mappa[prossimo[1]][prossimo[0]]=="O" or (mappa[prossimo[1]][prossimo[0]].isalpha==True and mappa[prossimo[1]][prossimo[0]].isalpha!= car) or (mappa[y][x]=='|'):
        if vx!=0:
            #if mappa[prossimo[1]+1][prossimo[0]]!="O" or (mappa[prossimo[1]+1][prossimo[0]].isalpha==True and mappa[prossimo[1]+1][prossimo[0]].isalpha!= car):
                if mappa[prossimo[1]+1][prossimo[0]]==" " or (mappa[y][x]=='|'):            #se è libera la casella adiacente
                     prossimo=(prossimo[0],prossimo[1]+1)
                     #distanze,albero=distanza(
                elif mappa[prossimo[1]-1][prossimo[0]]==" " or (mappa[y][x]=='|'):
                    prossimo=(prossimo[0],prossimo[1]-1)
        elif vy!=0:
            #if mappa[prossimo[1]][prossimo[0]+1]=="O" or (mappa[prossimo[1]][prossimo[0]+1].isalpha==True and mappa[prossimo[1]][prossimo[0]+1].isalpha!= car):
                if mappa[prossimo[1]][prossimo[0]+1]==" " or (mappa[y][x]=='|'):
                    prossimo=(prossimo[0]+1,prossimo[1])
                elif mappa[prossimo[1]][prossimo[0]-1]==" " or (mappa[y][x]=='|'):
                    prossimo=(prossimo[0]-1,prossimo[1])
    return(prossimo)
       # if prossimo[0]>x:
def velocita(mappa,car,prossimo,pista):
    global dis
    global temp
    global dis2
    temp=[]
    cont=0
    dis=0
    dis2=0
    for x,y in percorso:
        if mappa[y][x]=='O' or (mappa[y][x].isalpha==True and mappa[y][x]!=car) :   #vede il primo ostacolo   or (mappa[y][x]=='|')
            temp.insert(0,x)
            temp.insert(1,y)
            break
        cont+=1
    dis=cont-1
    dis=dis//3
    dis2=dis
    
    
def non_au(prossimo,x,y,vx,vy):  #così rimane costante
        vi=[]
        if prossimo[0]>x:
            if vx==1:
                vi.append(0)
            else:
                vi.append(1)
        elif prossimo[0]==x:
            if vx==0:
                vi.append(0)
            elif vx==1:
                vi.append(-1)
            else:
                vi.append(1)
        elif prossimo[0]<x:
            if vx==-1:
                vi.append(0)
            else:
                vi.append(-1)
        if prossimo[1]>y:
            if vy==1:
                vi.append(0)
            else:
                vi.append(1)
        elif prossimo[1]==y:
            if vy==0:
                vi.append(0)
            elif vy==1:
                vi.append(-1)
            else:
                vi.append(1)
        elif prossimo[1]<y:
            if vy==-1:
                vi.append(0)
            else:
                vi.append(-1)
                                        
            
        return vi                



def decelera(vx,vy,prossimo,x,y):
        vi=[]
        if prossimo[0]>x:
            if vx==1:
                vi.append(0)
            elif vx>1:
                vi.append(-1)
        elif prossimo[0]==x:
            if vx==0:
                vi.append(0)
            elif vx==1:
                vi.append(-1)
            else:
                vi.append(1)
        elif prossimo[0]<x:
            if vx==-1:
                vi.append(0)
            elif vx<-1:
                vi.append(1)
            else:
                vi.append(-1)
        if prossimo[1]>y:
            if vy==1:
                vi.append(0)
            elif vy>1:
                vi.append(-1)
            else:
                vi.append(1)
        elif prossimo[1]==y:
            if vy==0:
                vi.append(0)
            elif vy==1:
                vi.append(-1)
            else:
                vi.append(1)
        elif prossimo[1]<y:
            if vy==-1:
                vi.append(0)
            elif vy<-1:
                vi.append(1)
            else:
                vi.append(-1)
                                        
            
        return vi      


temp=[]
dis=0
crea1=0  
pista=_grafo()
distanze={}
albero={}
creato=0
percorso=[]
controllo=0
dis2=0
def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty, laps):
    global pista
    global creato
    global albero
    global distanze
    global percorso
    global dis
    global controllo
    global dis2
    supremo=1     #supremo: velocita costante di 1
    vi=[]
   # print("VELOCITA ATTUALE",vx,vy)
   # print(creato)
    if laps== 0 and vx==0 and vy==0:
        genera_grafico(griglia_corrente,car)
       # print(pista.lista_nodi())
        percorso=[]
        albero={}
      #  print("funziona",vx,vy,laps,x,y)
        if verso==1:
           # print("almno qui")
            return(1,0)
        else:
           # print("almeno qua")
            return(-1,0)
    if creato==0:
      #  print("EJHRNSJKFNHJ")
        if verso==1:
            albero=genera_albero(pista,(x+3,y))
            #print("QUA")

            percorso=cammino(albero,(startx-2,starty))
            percorso=percorso[:-1]
        else:
           # print(x-1,y,"---",pista)
            albero=genera_albero(pista,(x-3,y))
           # print("QUI")
            percorso=cammino(albero,(startx+2,starty))
            percorso=percorso[:-1]
            #print(creato,crea1,percorso,".........")
    if crea1==1 and len(percorso)>0:
       #print("ENTRA QUIIIII")
       prossimo=percorso.pop(0)
       if prossimo==(x,y):
           prossimo=percorso.pop(0)
          # print("PROSSIMO------>",prossimo)
       prossimo=ia2(prossimo, vx,vy,x,y,griglia_corrente)
      # print("MODIFICATO---->",prossimo)
       albero=genera_albero(pista,(x,y))
            #albero=genera_albero(pista,(x,y))
       velocita(griglia_corrente,car,prossimo,pista)
    if dis!=0 and supremo!=1:       #accelera
        
       # cont=dis
        if prossimo[0]>x:
            if vx==1:
                vi.append(1)
            else:
                vi.append(1)
        elif prossimo[0]==x:
            if vx==0:
                vi.append(0)
            elif vx==1:
                vi.append(-1)
            else:
                vi.append(1)
        elif prossimo[0]<x:
            if vx==-1:
                vi.append(-1)
            else:
                vi.append(-1)
        if prossimo[1]>y:
            if vy==1:
                vi.append(1)
            else:
                vi.append(1)
        elif prossimo[1]==y:
            if vy==0:
                vi.append(0)
            elif vy==1:
                vi.append(-1)
            else:
                vi.append(1)
        elif prossimo[1]<y:
            if vy==-1:
                vi.append(-1)
            else:
                vi.append(-1)
        #print("DIS1 ----->",dis)
        dis-=1
    elif dis==0 and dis2!=0 and supremo!=1:
        vi=decelera(vx,vy,prossimo,x,y)
        dis2-=1
        #print("DIS2--->",dis2)
        return(vi[0],vi[1])
    if len(percorso)<=0:
        if verso==1:
            return -1,0
        else:
            return 1,0
    
    elif crea1==1 and supremo==1 and laps!=1:
        vi=non_au(prossimo,x,y,vx,vy)
        #print("NON AUMENTA!!")
    if laps==1:
        if verso==1 and vx!=0:
           # print("!|!!!!!!!!!!!!")
            return -1,0
        elif verso==-1 and vx!=0:
           # print("??????????????")
            return 1,0
    return(vi[0],vi[1])
        
        
            
            
                             
                             
                             
                             
            
        




def frena(x,y,vx,vy,mappa):
    for x,y in percorso:
        if mappa[y][x]=='|':
            if verso==1:
                return 1,0
            else:
                return -1,0
        else:
            if verso==1:
                return -1,0
            else:
                return 1,0

























                    
