import json, re

def num(x):
    return re.search(r'\d+',x).group(0)

def cont(content):
    dict = {}
    for x in content:
        if "comp" in x:
            comp = num(x)
            dict[comp] = []
        elif "sub" in x:
            sub = num(x)
            dict[comp] = sub
    return dict

def pianifica(fcompiti,insi,fout):
    with open(fcompiti) as f: content = f.readlines()
    dict2 = {}
    dict = cont(content)
    for y in insi:
        l = []
        if y in dict:
            b = dict[y]
            while b != []:
                l = [b] + l
                b = dict[b]
            dict2[y] = l
    with open(fout, "w") as f: json.dump(dict2,f)
        
        
        
        
        
        
        
    