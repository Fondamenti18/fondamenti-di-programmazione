def pianifica(fcompiti,insi,fout):
    diz={}
    temp={} 
    with open(fcompiti, encoding='utf-8-sig') as compiti:
        linee=compiti.readlines()
        lstidcomp=[]
        lstidsub=[]
        for linea in linee:
            lstidsub=[]
            if 'comp' in linea:
                idcomp=''
                for x in linea:
                    if x.isdigit():
                        idcomp+=x
                lstidcomp.append(idcomp)
                temp[idcomp]=[]
            if 'sub' in linea:
                idsub=''
                for y in linea:
                    if y.isdigit():
                        idsub+=y
                lstidsub.append(idsub)
                temp[idcomp]=lstidsub
            diz.update(temp)    
        for w in diz.values():
            for x in w:
                for y, z in diz.items():
                    if x==y:
                        for j in z:
                            if j not in w:
                                w.append(j)
        diz2={}
        for k, v in diz.items():
            diz2[k]=list(reversed(v))
        diz3={}
        for i in insi:
            for c, t in diz2.items():
                if i==c:
                    diz3[c]=t
        import json
        sjson=json.dumps(diz3, sort_keys=True, indent=4)
        out=open(fout, 'w')
        out.write(str(sjson))