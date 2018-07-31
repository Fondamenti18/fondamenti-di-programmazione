import string
def post(fpost,insieme):
    f=open(fpost)
    f1=((f.read()).replace('\n',' ')).split()
    f2=(' '.join(f1)).split('<POST>')
    ls_fin=[]
    ls_sp=[]
    lista_conf=[]
    ins_confr=list(insieme)
    for y in f2:
        if y=='':
            f2.remove(y)
            
    for t in f2:
        ls_sp=t.split()
        for w in ls_sp:

            for k in ins_confr:
                if (w).lower()==k.lower():
                    ls_fin.append(ls_sp[0])
    return set(ls_fin)
    f.close


    
