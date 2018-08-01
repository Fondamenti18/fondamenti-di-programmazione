def post(fposts,insieme):
    with open(fposts,'r') as f:
        lett=f.readlines()
        #nrighefin = linea in cui si trova ogni <post>
        nrighe=-1
        nrighefin=[]
        #TROVA POST
        lista1=[]
        lista2=[]
        occfound=[]
        for righe in lett:
            righe=righe.replace(' ','')
            nrighe=nrighe+1
            lista1=lista1+[nrighe]
            if righe.find('<POST>') == 0:
                nrighefin=nrighefin+[nrighe]
                lista2=lista2+[lista1]
                occfound=occfound+[righe]
                lista1=[]
        lista2=lista2+[[207,208,209,210,211]]

        var1=[]
        for v in occfound:
            v = v.replace('\n', '') and v.replace('<POST>','')
            var1=var1+[int(v)]
        
        diz1={}
        count=0
        for val in var1:
            count=count+1
            diz1[val]=lista2[count]
        
        def ric_parole():
            riclinee=[]
            nrighe=0
            for w in insieme:
                w=w.lower()
                for righe in lett:
                    righe=righe.lower()
                    nrighe=nrighe+1
                    if righe.find(w) != -1:
                        for car in '?!.,-_<>[]{}':
                            righe=righe.replace(car,'')
                        var2=righe.split()
                        for w2 in var2:
                            if w2 == w:
                                riclinee=riclinee+[nrighe]
                nrighe=0
            
            listafin=[]
            for d,d2 in diz1.items():
                for i in riclinee:
                    if i in d2:
                        listafin=listafin+[str(d)]
            
            listafin=set(listafin)
            return listafin
            
        return ric_parole()

