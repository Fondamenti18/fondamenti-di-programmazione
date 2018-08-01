import re
import json

def initialize(file):
    file = open(file,"r")
    l = []
    for line in file:
        l.append(line)
    return l

def clean_list(input):
    test = []
    for var in input:
        if type(var) == list:
            test += var
            test = clean_list(test)
        else:
            test.append(var)
    return test

def pianifica(fcompiti,insi,fout):
     diz = dict()
     list = initialize(fcompiti)
     for i in range(0,len(list)-1):
         if "comp" in list[i]:
             comp = re.search('[0-9]+',list[i]).group(0)
             diz[comp] = []
             if "sub" in list[i+1]:
                 sub = re.search('[0-9]+', list[i+1]).group(0)
                 diz[comp].append(sub)
     for i in diz:
         if diz[i] != []:
             number = diz[i][0]
             if number in diz:
                 if diz[number] != []:
                    val = diz.get(number)
                    diz[i].insert(0,val)
     dict_final = {your_key: diz[your_key] for your_key in insi if diz.get(your_key) != None}
     for i in dict_final:
         dict_final[i] = clean_list(dict_final[i])
     out_file = open(fout, "w")
     out_file.write(json.dumps(dict_final, ensure_ascii=False))
     out_file.close()