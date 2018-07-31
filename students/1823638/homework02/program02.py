import json

def pianifica(fcompiti,insi,fout):
    with open(fcompiti,'r') as t:
        lett=t.readlines()
        listacomp=[]
        listasub=[]
        for r in lett:
            r=r.replace(' ','')
            r=r.replace('\n','')
            poscomp=r.find('comp')
            if poscomp==0:
                r=r.replace('comp','')
                listacomp=listacomp+[r]
                listasub=listasub+['']
            else:
                r=r.replace('sub','')
                listasub=listasub+[r]
                listacomp=listacomp+['']
        
        listasub=listasub+['']

        insil=list(insi)
        diz1={}
        for n in insil:
            if n in listacomp:
                var2=listacomp.index(n)
                var3=listasub[var2+1]
                if var3=='':
                    diz1[n]=[""]
                else:
                    diz1[n]=[var3]
            #else:
                #insil.remove(n)
                
        
        count=0
        def prova1(diz1,count):
            for i in diz1:
                if diz1[i][0] in listacomp:
                    if diz1[i]=='':
                        continue
                    else:
                        var4=listacomp.index(diz1[i][0])
                        var5=listasub[var4+1]
                        if var5=='':
                            continue
                        else:
                            diz1[i]=[var5]+diz1[i]
            count=count+1
            if count<15:
                return prova1(diz1,count)

        prova1(diz1,count)
        
        for i in diz1:
            if diz1[i][0]=='':
                diz1[i]=[]
            
            
        with open(fout, 'w') as f:
            scritt=json.dumps(diz1)
            f.write(scritt)
            f.close()

    
