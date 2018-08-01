import math

def modi(lista,k):
    listaprimi=[]
    nuovalista=[]
    listano=[]
    for numero in lista:
        var1=math.sqrt(numero)
        var1=math.floor(var1+1)
        counter=0
        for i in range(2,var1+1):
            var2=numero%i
            if var2==0:
                counter=counter+1
        if counter==0:
            listaprimi=listaprimi+[numero]
        elif counter==k//2:
            nuovalista=nuovalista+[numero]
        else:
            listano=listano+[numero]
    listano2=listano+listaprimi
    for i in listano2:
        if i in lista:
            lista.remove(i)

    return listaprimi

