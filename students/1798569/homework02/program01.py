
def post(fposts,insieme):
    listID=[]
    listaIns=[]
    insRet=set()
    insieme2=set()
    'trasformazione elementi insieme in minuscolo'
    while insieme!=set():
        x=insieme.pop()
        x=x.lower()
        insieme2.add(x)
    'Split file in base al POST'
    f=open(fposts)
    testo=f.read()
    listaPost= testo.split('<POST>')
    'Eliminazione spazi e ottenere valori ID'
    for x in range(0,len(listaPost)):
        listaPost[x]=listaPost[x].strip()
        listID+=' '
        listaIns+=' '
        for i in listaPost[x]:
            if i.isdigit():
                listID[x]+=i
                listID[x]=listID[x].strip()
            else:
                break
    del(listID[0])
    'creazione lista insiemi'
    for x in range (0,len(listaPost)):
        d=listaPost[x].split()
        'rimozione caratteri non letterali e trasformazione in minuscolo'
        for y in range(0,len(d)):
            while d[y]!='' and d[y][-1].isalpha()==False and d[y]!='':
                d[y]=d[y][:-1]        
            d[y]=d[y].lower()
        listaIns[x]=set(d)
    del(listaIns[0])
    'confronto insiemi'
    for x in range(0,len(listaIns)):
        if listaIns[x].intersection(insieme2)!=set():
            insRet.add(listID[x])
    return insRet
