import json

def create_nd(d,strx,nd):  #rec funz create
    #for x in strx:
        #print('  '*len(strx),x)
    for child in strx:
        val=d.get(child,False)
        if val!=False:

            nd[child]=val
            strx=list()
            for child1 in val:
                #print(child1)
                strx.append(child1)

            #print(strx)
            #print('nd=',nd,'\n')
            create_nd(d,strx,nd)
        else: d={}
    return nd

def genera_sottoalbero(fnome,x,fout):
    f=open(fnome,'U')
    t=f.read()
    f.close()
    diz_a=json.loads(t)
    nd=dict()
    strx=[x]
    nd=create_nd(diz_a,strx,nd)
    #print('Scrivo diz-alb\n',nd)
    f=open(fout,'w')
    f.write(json.dumps(nd))
    f.close()



def delete_d(d,strx):  #rec func delete
    #print(strx)
    for child in strx:  #itero su strx
        val=d.get(child,False)#restituisce il valore della chiave altrimenti se non presente False
        if val!=False:
            del d[child]    #eliminiamo la chiave child
            strx=list()
            for child1 in val:
                #print(child1)
                strx.append(child1)
            #print(strx)
            #print('d=',d,'\n')
            delete_d(d,strx)
        else: d={}
    return d

def cancella_sottoalbero(fnome,x,fout):
    f=open(fnome,'U')
    t=f.read()
    f.close()
    diz_a=json.loads(t)
    strx=[x]
    d=delete_d(diz_a,strx)
    for k in d:
        if x in d.get(k):
            d.get(k).remove(x)
            #print('yes')
    #print(d)
    f=open(fout,'w')
    f.write(json.dumps(d))
    f.close()



def lev(d,c,nd,l):
    #print('entro con lista-> ',l)
    #print('ln',l)
    if d!={}:
        #print(l)
        for k in l:

            if nd.get(c,False)!=False:    #se ci sono elementi ass a chiave c
                #---print('\ngia presente-> ',nd.get(c))
                app=nd.get(c)      #crea lista di elementi
                if type(app)==str:

                    #---print('app',type(app),app)
                    list_app=[app]
                    #---print('provalista app->',list_app)

                    list_app.append(k)            #agg alla lista l elemento k
                    #---print('list_app',list_app)
                    return
                #return
                #print('sortata',app,'->',app.sort(),type(app))
                #print('metto',c,'ass',app,type(app))
                #print('sortata',app,'->',sorted(app),type(app))
                    nd[c]=sorted(list_app)
                else:
                    #---print('else')
                    app=nd.get(c)
                    app.append(k)
                    nd[c]=sorted(app)

                #print('sortata',sorted(app))
                #return
                l=d.get(k)     #l diventa una lista di valori di k
                #print('listarenew',l)
                #return

            else:             #se non ci sono elementi ass a chiave c
                #print('2metto',c,'ass',k,'\n')
                #---print('metto',c,'ass',k)
                nd[c]=[k]    #ass (k->list) alla chiave c
                #---print(nd)
                #print('quauqa',k)
                #--print(type(nd),nd)
                #--print('qua k',k)
                l=list()
                l=d.get(k)       #l diventa una lista di valori di k
                #print('lista nuova',l)
                #print('cancello',k)
                #--print('elimino',k)
                del d[k]    #eliminiamo la chiave k dal dizionario
                #return
                #print('nuovo',d)
                #lev(d,c+1,nd,l)
            lev(d,c+1,nd,l)
        return nd
    else:
        return nd


def dizionario_livelli(fnome,fout):
    f=open(fnome,'U')
    t=f.read()
    f.close()
    d=json.loads(t)
    #next(iter(d)))
    nd=dict()
    #lista_k=list()
    #lista_k=list(d.keys())
    #l=[next(iter(d))]
    #print(l)
    insk=set()
    insv=set()
    for k,v in d.items():
         insk.add(k)
         for elemento in v:
             insv.add(elemento)
    rad=insk-insv
    #print(rad)
    #a=rad[0]
    #print('radstr',a)






    nd=lev(d,0,nd,rad)
    #---print(nd)
    f=open(fout,'w')
    f.write(json.dumps(nd))
    f.close()

def calc_g_ant(d,nd,c,gr,l):
    for k in l:
        nd[k]=gr
        if d.get(k,False)!=False:
            l=d.get(k)
            if len(d.get(k))==c:
                calc_g_ant(d,nd,c,gr+1,l)
            else:
                calc_g_ant(d,nd,c,gr,l)
    return nd








def dizionario_gradi_antenati(fnome,y,fout):
    f=open(fnome,'U')
    t=f.read()
    f.close()
    d=json.loads(t)
    nd=dict()
    #l=[next(iter(d))]
    insk=set()
    insv=set()
    for k,v in d.items():
         insk.add(k)
         for elemento in v:
             insv.add(elemento)
    rad=insk-insv
    #print(rad)
    nd=calc_g_ant(d,nd,y,0,rad)
    #print('diz->',nd)
    f=open(fout,'w')
    f.write(json.dumps(nd))
    f.close()


#genera_sottoalbero('Alb100.json','ultras','prova.json')
#cancella_sottoalbero('Alb10.json','d','prova.json')
dizionario_livelli('Alb10.json','prova.json')

#dizionario_livelli('Alb100.json','prova.json')
#dizionario_gradi_antenati('Alb100.json',2,'prova.json')
#dizionario_gradi_antenati('Alb100.json',2,'prova.json')
