def pianifica(fcompiti,insi,fout):
    lista_xID=[]  
    import re
    with open(fcompiti,encoding='utf-8') as f:
        for linea in f:
            stringa_caratteri_alfabetici=' '.join(re.findall("[a-zA-Z]+", str(linea)))
            stringa_caratteri_numerici=' '.join(re.findall('[0-9]+',str(linea)))
            lista_coppia=(stringa_caratteri_alfabetici,stringa_caratteri_numerici)
            lista_xID.append(lista_coppia)
    lista_comp_sub=lista_xID
    lista_comp_sub+=[('','')]
    dizionario(insi,fout,lista_comp_sub)

def dizionario(insi,fout,lista_comp_sub):
    dict_ID={}
    i=1
    for c in range(0,len(lista_comp_sub)-1):
        if lista_comp_sub[c][0]=='comp' and lista_comp_sub[c+1][0]=='sub':
            dict_ID[lista_comp_sub[c][1]]=lista_comp_sub[c+1][1]
            i+=1
        elif lista_comp_sub[c][0]=='comp' and lista_comp_sub[c+1][0]=='comp':
            dict_ID[lista_comp_sub[c][1]]=[]
            i+=1
        elif len(lista_comp_sub)-1==i and lista_comp_sub[c][0]=='comp' and lista_comp_sub[c+1][0]=='':
            dict_ID[lista_comp_sub[c][1]]=[]
            break
        elif lista_comp_sub[c][0]=='sub':
            i+=1
    calcolo_insieme(insi,fout,dict_ID)

def calcolo_insieme(insi,fout,dict_ID):
    dict_result={}
    for x in insi:
        y=x
        while x in dict_ID:
            if x in dict_ID and dict_ID[x]==[]:
                dict_result[(x)]=dict_ID[x]
                break
            dict_result[(x)]=[dict_ID[x]]
            break
            y=dict_ID[x]
        while y in dict_ID:
            if y in dict_ID and dict_ID[y]==[]:
                #serve a bloccare il ciclo qualora nel primo ciclo x non aveva alcun sub
                break
            y=str(dict_ID[y])
            if y in dict_ID and dict_ID[y]==[]:
                break
                #serve a bloccare l'ultimo del ciclo
            dict_result[x]+=[dict_ID[y]]
        if x in dict_ID:
            dict_result[x].reverse()
        else:
            pass
    import json
    with open(fout,'w') as f:
        json.dump(dict_result,f)



pianifica('file02_10_2.txt', {'2','4','11','1','6','9','10'},'test1.json')
