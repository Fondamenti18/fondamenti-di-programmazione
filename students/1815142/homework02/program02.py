'''('file02_200000.txt', '{1,3,..79} | {199998-80,199998-78,...199998}','test6.json')'''

import json

def pianifica(fcompiti,insi,fout):
    t=open(fcompiti)
    t=t.readlines()
    for i in range(len(t)):
        t[i]=t[i].replace(" ",'').replace("\n",' ')
    t.append('')
    d={}
    for i in insi:
        c=0
        s=i
        a=[]
        while c==0:
            c=1
            try:
                indice=t.index('comp'+s+' ')
                controllo=1
                if t[indice+1].find('sub')!=-1:
                    c=0
                    s=t[indice+1].replace('sub','').replace(' ','')
                    a.insert(0,s)
            except ValueError:
                controllo=0
        if controllo==1:
            d[i]=a
    file=json.dumps(d)
    p=open(fout,'w')
    p.write(file)
                    
