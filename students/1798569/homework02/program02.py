import json
def pianifica(fcompiti,insi,fout):
    listID=[]
    listaSub=[]
    listaVal=[]
    diz={}
    'ottenimento ID compiti'
    f=open(fcompiti)
    testo=f.read()
    listaComp= testo.split('comp')
    'Eliminazione spazi e ottenere valori ID'
    for x in range(0,len(listaComp)):
        listaComp[x]=listaComp[x].strip()
        listID+=' '
        for i in listaComp[x]:
            if i.isdigit():
                listID[x]+=i
                listID[x]=listID[x].strip()
            else:
                break
    del(listaComp[0])
    del(listID[0])
    'ottenimento ID sub'
    for x in range (0,len(listaComp)):
        z=''
        d=listaComp[x].split('\n')
        del(d[0])
        if d!=[]:
            y=d[-1]
            y=y.strip()
            z=y[3:]
            z=z.strip()
            listaSub+=[z]
        else:
            listaSub+=' '
    'creazione dizionario'
    for x in range(0,len(listID)):
        if listID[x] in insi:
            end=True
            listaVal=[]
            listaVal+=[listaSub[x]]
            'controllo se sub inserito già in dizionario'
            while end==True:
                for y in diz:
                    if end==True and y==listaVal[-1]:
                        listaVal+=diz[y]
                        end=False
                    if end==True and listaVal[-1] in diz[y]:
                        d=diz[y]
                        lim=diz[y].index(listaVal[-1])
                        if lim != 0:
                            listaVal+=d[lim:]
                        else:
                            listaVal+=d[1:]
                        end=False              
                if end ==True and listaVal[-1]!=' ' and listaSub[listID.index(listaVal[-1])]!=' ':
                    listaVal+=[listaSub[listID.index(listaVal[-1])]]
                else:
                    end=False
            if listaVal != [' ']:
                diz[listID[x]]=listaVal
            else:
                diz[listID[x]]=[]
    'reverse dizionario'
    for x in diz:
        diz[x].reverse() 
        for i in diz[x]:
            if diz[x].count(i) > 1:
                diz[x].remove(i)
    'scrittura su file json'
    with open(fout,'w') as f:
        json.dump(diz, f)
    return 
