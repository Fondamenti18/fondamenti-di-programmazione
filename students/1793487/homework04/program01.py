import json

def ricorsiva_genera_sottoalbero(diz, x, nuovo_diz):
    nuovo_diz[x] = diz[x]
    for e in diz[x]:
        ricorsiva_genera_sottoalbero(diz, e, nuovo_diz)
    return nuovo_diz

def genera_sottoalbero(fnome,x,fout):
    nuovo_diz = {}
    ricorsiva_genera_sottoalbero(json.load(open(fnome)), x, nuovo_diz)
    json.dump(nuovo_diz, open(fout, 'w'))
'''
def ricorsiva_cancella_sottoalbero(diz, x, nuovo_diz):
    nuovo_diz[x] = diz[x]
    print(nuovo_diz[x])
    for e in diz[x]:
        ricorsiva_genera_sottoalbero(diz, e, nuovo_diz)
    return nuovo_diz
print(ricorsiva_cancella_sottoalbero({"a": ["b"], "b": ["c", "d"], "c": ["i"], "d": ["e", "l"], "e": ["f", "g", "h"],
"f": [], "g": [], "h": [], "i": [], "l": []}, 'd', 0})

def p(d):
    e = []
    cont = 0
    for el in d:
        cont += 1
        e.append(el)
        if el not in d[el]:
            print(el)
    return e, cont
print(p({"a": ["b"], "b": ["c", "d"], "c": ["i"], "d": ["e", "l"]}))

def cancella_sottoalbero(fnome,x,fout):
    nuovo_diz = {}
    #ricorsiva_genera_sottoalbero(diz, x, nuovo_diz)
    for el in fnome:
        print(el)
        if el in nuovo_diz:
            #print(el)
            del diz[el]
    return diz

print(cancella_sottoalbero(diz, 'd', 0))
#
#
#     #print(len(diz))#=10
#
#     def dizionario_livelli(fnome,fout):
#         dic={}
#         cont=-1
#         for chiave in diz:
#             #print(chiave)
#             if len(diz[chiave])>0:
#                 #print(diz[chiave])
#                 cont+=1
#                 dic[cont]='ciao'
#         return dic#return dic
#     #print(dizionario_livelli(diz,0))
#
#
     def dizionario_gradi_antenati(fnome,y,fout):
         dic={}
         cont=0
         for chiave in diz:
             #print(chiave)
             for el in diz[chiave]:
                 #print(el)
                 if len(diz[chiave])==y:
                     #print(len(diz[chiave]))
                     cont+=1
                     print(cont)
                     #dizionario_gradi_antenati(diz[chiave],chiave)
             #print(chiave)
                     #dic[chiave]=cont
         #return dic
     #print(dizionario_gradi_antenati(diz,2,0))
#
# with open('Alb10.json','r') as d:
#         for dizionario in d.readlines():
#             for chiave,valore in dizionario.items():
#                 print(chiave,valore)
#         return chiave,valore
#
'''
