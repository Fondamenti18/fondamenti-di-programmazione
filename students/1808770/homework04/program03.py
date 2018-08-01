from  my_html import HTMLNode,fparse

def conta_nodi(fileIn,selettore):
    separated,html,tag=selettore.split(" > "),hparser(fileIn),[]
    for x in separated:
        tag.append(taggami(x))
    if len(tag)==1:
        count,lista=counter(html,tag[0],0,[])
    else:
        count,lista=counter(html,tag,0,[])
    return count

def counter(html,tag,count,lista):
    if type(tag)==str and tag in html:
        count+=1
        return counter(html.replace(tag,"",1),tag,count,lista)
    elif type(tag)==tuple and tag[0] in html:
        for x in [x for x in html.split(tag[0]) if tag[1] in x]:
            count+=1
            lista.append(x[x.index(tag[1]):x.index("</"+tag[1][1:]+">")+len("</"+tag[1][1:]+">")])
            return counter(html.replace(tag[1],"",1),tag,count,lista)
    elif type(tag)==list and tag[0] in html:
        for xx in [x.split(tag[1]) for x in html.split(tag[0]) if tag[1] in x]:
            for x in xx:
                if "<" not in x:
                    count+=1
                    return counter(html.replace(tag[1],"",1),tag,count,lista)
    return count,lista

def elimina_nodi(fileIn,selettore,fileOut):
    separated,html,tag=selettore.split(" > "),hparser(fileIn),[]
    for x in separated:
        tag.append(taggami(x))
    if len(tag)==1:
        count,lista=counter(html,tag[0],0,[])
    else:
        count,lista=counter(html,tag,0,[])
    for x in lista:
        html=html.replace(x,"")
    save(inverti(html),fileOut)

def cambia_attributo(fileIn,selettore,chiave,valore,fileOut):
    separated,html,tag=selettore.split(" > "),hparser(fileIn),[]
    for x in separated:
        tag.append(taggami(x))
    if len(tag)==1:
        count,lista=counter(html,tag[0],0,[])
    else:
        count,lista=counter(html,tag,0,[])
    for x in lista:
        html=html.replace(x,x.replace('" ','" '+chiave+'="'+valore+'" '))
    save(inverti(html),fileOut)


def hparser(html):
    with open(html,encoding='utf8') as f:
        return f.read()
def taggami(separated):
    if len(separated.split(" "))>1:
        s=separated.split(" ")
        tag="<"+s[0],"<"+s[1]
    elif "#" in separated:
        tag='id="%s"'%separated[1:]
    elif "." in separated:
        tag=separated[1:]+"="
    elif "@" in separated:
        tag=separated[2:-1]
    else:
        tag="<"+separated
    return tag
def inverti(html):
    final=[]
    for line in html.split("\n"):
        if "=" in line:
            lista=[x for x in line.split(" ") if "=" in x]
            for s in lista:
                if "<" in s:
                    lista[lista.index(s)]=s.split("<")[0]
                elif ">" in s:
                    lista[lista.index(s)]=s.split(">")[0]
                elif s.endswith('"')==False:
                    lista[lista.index(s)]=html[html.index(s):html.index('">')+1]
            inverti2(html,line,lista,final)
        else:
            if line!="":
                final.append(line)
    return ("\n").join(final)
def inverti2(html,line,lista,final):
    lista2=[]
    if len(lista)!=5:
        slista=sorted(lista)
    else:
        slista=sorted(lista[:2])+sorted(lista[2:5])
    for x in lista:
        line=line.replace(x,slista[0])
        lista2.append(line[:line.index(slista[0])+len(slista[0])])
        line=line[line.index(slista[0])+len(slista[0]):]
        del slista[0]
    if not "/" in line[-5:-1]:
        line=line[:-2]+"/>"
    lista2.append(line)
    final.append(("").join(lista2))
def save(html,out):
    savami=open(out,"w")
    savami.write(html)
    savami.close()