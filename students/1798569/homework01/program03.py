
from copy import copy
def codifica(chiave, testo):
    listaChiave,listaChOrd,listaTesto=creaDiz(chiave, testo)
    'creazione accoppiamenti'
    diz={}
    cnt=0
    while cnt<len(listaChiave):
        diz[listaChOrd[cnt]]=listaChiave[cnt]
        cnt+=1
    
    'sostituzione'
    cnt1=0
    listaSost1=list(diz.keys())
    listaSost2=list(diz.values())
    while cnt1<len(listaTesto):
        cnt2=0
        while cnt2<len(listaSost1):
            if listaTesto[cnt1]==listaSost1[cnt2]:
                listaTesto[cnt1]=listaSost2[cnt2]
                cnt2=len(listaSost1)
            cnt2+=1
        cnt1+=1
    testoCod=''.join(listaTesto)    
    return testoCod


def decodifica(chiave, testo):
    listaChiave,listaChOrd,listaTesto=creaDiz(chiave, testo)
    'creazione accoppiamenti'
    diz={}
    cnt=0
    while cnt<len(listaChiave):
        diz[listaChiave[cnt]]=listaChOrd[cnt]
        cnt+=1
    
    'sostituzione'
    cnt1=0
    listaSost1=list(diz.keys())
    listaSost2=list(diz.values())
    while cnt1<len(listaTesto):
        cnt2=0
        while cnt2<len(listaSost1):
            if listaTesto[cnt1]==listaSost1[cnt2]:
                listaTesto[cnt1]=listaSost2[cnt2]
                cnt2=len(listaSost1)
            cnt2+=1
        cnt1+=1
    testoDecod=''.join(listaTesto)    
    return testoDecod


def creaDiz (chiave,testo):
    'pulizia stringa a<stringa<z'
    listaChiave=[]
    for x in chiave:
        if x<='z' and x>='a':
            listaChiave+=[x]
    
    'eliminazione occorrenze'
    cnt1=len(listaChiave)-1
    while cnt1>0:
        cnt2=len(listaChiave)-1
        y=listaChiave[cnt1]
        while cnt2>0:
            if y==listaChiave[cnt2-1] and (cnt2-1)!=cnt1:
                listaChiave[cnt2-1]=''
            cnt2-=1
        cnt1-=1
    while'' in listaChiave:
        listaChiave.remove('')
    
    'creazione lista ordinata'
    listaChOrd=copy(listaChiave)
    listaChOrd.sort()
    
    'conversione testo in lista cartteri'
    listaTesto=[]
    for x in testo:
        listaTesto+=[x]
    return listaChiave,listaChOrd, listaTesto
