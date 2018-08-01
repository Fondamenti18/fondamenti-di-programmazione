from  my_html import HTMLNode, fparse

global ck1
ck1=0
def conta_nodi(fileIn, selettore):
    with open(fileIn) as f:
        lett = f.readlines()
        global cont_fin
        counter=0
        cont_fin=0
        pos_s=0
        tag=['p','a','h']
        
        #conteggio nodi ID
        if selettore.startswith('#'):
            for r in lett:
                if 'id='+'"'+selettore[1:]+'"' in r:
                    counter=counter+1
                    cont_fin=counter
        #conteggio nodi CLASS
        elif selettore.startswith('.'):
            for r in lett:
                if selettore[1:]+'=' in r:
                    counter=counter+1
                    cont_fin=counter
        #conteggio nodi ATTR
        elif selettore.startswith('@'):
            div=selettore.split('>')
            div=selettore.split(' ')
            if len(div)==1:
                for r in lett:
                    if selettore[2:][:-1] in r:
                        counter=counter+1
                        cont_fin=counter
            else:
                pos_s2_in=0
                pos_s2_out=0
                tagname=''
                for r in lett:
                    pos_s=pos_s+1
                    if div[0][2:][:-2] in r:
                        r=r.replace(' ','')
                        pos_s2_in=pos_s
                        tagname=r[:6]
                    if '/'+tagname[1:] in r:
                        pos_s2_out=pos_s
                pos_s=0
                pos_s3_in=[]
                pos_s3_out=[]
                for r in lett[pos_s2_in:pos_s2_out]:
                    pos_s=pos_s+1
                    if '<'+div[2] in r:
                        pos_s3_in=pos_s3_in+[pos_s]
                    if '</'+div[2] in r:
                        pos_s3_out=pos_s3_out+[pos_s]
                val_count=-1
                listval=[]
                for val in pos_s3_in:
                    val_count=val_count+1
                    for r in lett[pos_s2_in+val:pos_s2_out+pos_s3_out[val_count]]:
                        if '<'+div[3] in r:
                            if '<'+div[5] in r:
                                if r not in listval:
                                    listval=listval+[r]
                                else:
                                    pass
                cont_fin=len(listval)
        #conteggio nodo TAG
        elif selettore in tag:
            for r in lett:
                if '<'+selettore in r:
                    counter=counter+1
                    cont_fin=counter
        #conteggio nodo padre->figlio (<tag - <tag>)
        elif len(selettore.split(' '))==3:
            div=selettore.split(' ')
            for r in lett:
                if '<'+div[0] in r:
                    if '<'+div[2]+'>' in r:
                        counter=counter+1
                        cont_fin=counter
        #conteggio nodo discendente (<tag - <tag)
        elif len(selettore.split(' '))==2:
            div=selettore.split(' ')
            for r in lett:
                if '<'+div[0] in r:
                    if '<'+div[1] in r:
                        counter=counter+1
                        cont_fin=counter
        else:
            cont_fin=0
        global ck1
        if ck1==0:
            ck1=ck1+1
            return conta_nodi(fileIn, selettore)
        else:
            return cont_fin

global ck2
ck2=0
def elimina_nodi(fileIn,selettore,fileOut):
    global ck2
    if ck2==0:
        ck2=ck2+1
        elimina_nodi(fileIn,selettore,fileOut)
    else:
        ric_elimina_nodi(fileIn,selettore,fileOut)
    
def ric_elimina_nodi(fileIn,selettore,fileOut):
    var1=fparse(fileIn)
    var2=var1.to_string()
    div=selettore.split(' ')
    
    index=0
    occfound_open=[]
    occfound_close=[]
    if len(div)==2:
        while index<len(var2):
            index=var2.find('<'+div[0],index)
            index2=var2.find('</'+div[0],index)
            if index==-1:
                break
            if index2==-1:
                break
            occfound_close=occfound_close+[index2]
            occfound_open=occfound_open+[index]
            index=index+len('<'+div[0])
        counter=-1
        listafin_open=[]
        listafin_close=[]
        for val in occfound_open:
            counter=counter+1
            if var2.find('<'+div[1],val,occfound_close[counter]) != -1:
                listafin_open=listafin_open+[var2.find('<'+div[1],val,occfound_close[counter])]
            if var2.find('</'+div[1],val,occfound_close[counter]) != -1:
                listafin_close=listafin_close+[var2.find('</'+div[1],val,occfound_close[counter])]
        tog=var2[listafin_open[0]:listafin_close[0]+4]
        var2=var2.replace(tog,'')
        
        with open(fileOut, 'w') as f:
            f.write(var2)
    return elimina_nodi


import io
global ck3
ck3=0
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    global ck3
    if ck3==0:
        ck3=ck3+1
        cambia_attributo(fileIn, selettore, chiave, valore, fileOut)
    else:
        ric_cambia_attr(fileIn, selettore, chiave, valore, fileOut)
    
def ric_cambia_attr(fileIn, selettore, chiave, valore, fileOut):
    var1=fparse(fileIn)
    var2=var1.to_string()
    div=selettore.split(' ')
    if len(div)==2:
        index=0
        occfound_open=[]
        occfound_close=[]
        while index<len(var2):
            index=var2.find('<'+div[0],index)
            index2=var2.find('</'+div[0],index)
            if index==-1:
                break
            if index2==-1:
                break
            occfound_close=occfound_close+[index2]
            occfound_open=occfound_open+[index]
            index=index+len('<'+div[0])
        counter=-1
        listafin_open=[]
        listafin_close=[]
        for val in occfound_open:
            counter=counter+1
            if var2.find('<'+div[1],val,occfound_close[counter]) != -1:
                listafin_open=listafin_open+[var2.find('<'+div[1],val,occfound_close[counter])]
            if var2.find('</'+div[1],val,occfound_close[counter]) != -1:
                listafin_close=listafin_close+[var2.find('</'+div[1],val,occfound_close[counter])]
        counter2=-1
        listafin2_open=[]
        for val2 in listafin_open:
            counter2=counter2+1
            if var2.find('href="',val2,listafin_close[counter2]) != -1:
                listafin2_open=listafin2_open+[var2.find('href="',val2,listafin_close[counter2])+6]
        counter3=-1
        listafin3_open=[]
        for val3 in listafin2_open:
            counter3=counter3+1
            if var2.find('"',val3) != -1:
                listafin3_open=listafin3_open+[var2.find('"',val3)+1]
        counter4=0
        for val4 in listafin3_open:
            val4=val4+(29*counter4)
            counter4=counter4+1
            var2=var2[:val4]+' '+chiave+'="'+valore+'"'+var2[val4:]
            
    with io.open(fileOut, 'w', encoding='utf8') as f:
        f.write(var2)
