"""
Created on Thu Nov  2 21:53:51 2017

@author: NICO
"""


def contalettere(parola):
    lista=[]
    conta=0
    for i in parola:
        if(i in lista):
            conta=conta+0
        else:
            lista+=[i]
            conta=conta+1
    return conta

def accettabile(parola,struttura):
    if(len(struttura)>len(parola))or(contalettere(parola)!=contalettere(struttura)):
       return False

    
    d={}
    
    h=0
    if(len(parola)!=len(struttura)):
        return False
    else:
        for i in range(0,len(parola)):
            if(parola[i] not in d):
                if(struttura[i] not in d.values()):
                    d[parola[h]]=struttura[i]
            h=h+1
        h=0
    for lettera in parola:
        if (lettera in d):
            if(d[lettera]!=struttura[h]):
                return False
            h=h+1
    return(True)

def decod(pfile, codice):
    f=open(pfile,"r")
    lista=[]
    
    for linea in f:
        line=linea.replace("\n","")
        if(accettabile(line,codice)==True):
            lista+=[line]
    ris=set(lista)
    return ris



