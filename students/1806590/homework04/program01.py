import json
from pprint import pprint
dg={}
dc={}
dl={}
da={}
#liv = 0


def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    albero = json.load(open(fnome))
    dg[x]=albero[x]
    for i in dg[x]:
        genera_sottoalbero(fnome, i, fout)
    k=[x for x in dg]
    for x in k:
        if x not in albero:
            dg.pop(x)
    
    diz=open(fout,"w")
    json.dump(dg, diz)
    diz.close()
    
    
    

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    albero = json.load(open(fnome))
    dc[x]=albero[x]
    for i in dc[x]:
        cancella_sottoalbero(fnome, i, fout)
    k=[x for x in dc]
    for x in k:
        if x not in albero:
            dc.pop(x)
    
    for i in dc:
        del(albero[i])
    
    
    for i in albero:
        for x in dc:
            if x in albero[i]:
                albero[i].remove(x)
    
    diz=open(fout,"w")
    json.dump(albero, diz)
    diz.close()
    
    
def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    liv=0
    l=[]
    albero = json.load(open(fnome))
    k=[x for x in albero]
    dl[liv]=[k[liv]]
    for x in range(len(dl[liv])):
        l=albero[dl[liv][x]]
        liv+=1
        dl[liv]=l
        dizionario_livelli(fnome,fout)

    diz=open(fout,"w")
    json.dump(dl, diz)
    diz.close()
            
  
def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    albero = json.load(open(fnome))

    for x in albero:
        for i in albero:
            if x in albero[i]:
                count=0
                count+=1
                da[x]=count
        dizionario_gradi_antenati(fnome,y,fout)   
                
    diz=open(fout,"w")
    json.dump(da, diz)
    diz.close()
            
  


    

