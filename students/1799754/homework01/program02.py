dizionario=[{0:"",1:"cento",2:"duecento",3:"trecento",4:"quattrocento",5:"cinquecento",6:"seicento",7:"settecento",8:"ottocento",9:"novecento"},{0:"",1:"dieci",2:"venti",3:"trenta",4:"quaranta",5:"cinquanta",6:"sessanta",7:"settanta",8:"ottanta",9:"novanta"},{0:"",1:"uno",2:"due",3:"tre",4:"quattro",5:"cinque",6:"sei",7:"sette",8:"otto",9:"nove",10:"dieci",11:"undici",12:"dodici",13:"tredici",14:"quattordici",15:"quindici",16:"sedici",17:"diciassette",18:"diciotto",19:"diciannove"},{0:"miliardi",1:"milioni",2:"mila",3:""},{0:"unmiliardo",1:"unmilione",2:"mille",3:"uno"}]

def conversione_in_lista(numero):
    lista=[]
    i=0
    while i<len(str(numero).zfill(12)):
        lista.append(str(numero).zfill(12)[i:i+3])
        i+=3
    return lista

def conversione_in_lettere(lista):
    lettere=""
    for x,y in enumerate(lista):
        if int(y)!=0:
            lettere+=dizionario[0].get(int(lista[x][0]))
            if int(y)>100 and 79<int(y)%100<90:
                lettere=lettere[0:-1]+"ottanta"
            elif 1<int(y)%100<20:
                lettere+=dizionario[2].get(int(lista[x][1:3]))
                lettere+=dizionario[3].get(x)
                continue
            else:
                lettere+=dizionario[1].get(int(lista[x][1]))
            if int(lista[x][2])==1 and int(y)%100>11:
                lettere=lettere[0:-1]+"uno"
            elif int(y)==1:
                lettere+=dizionario[4].get(x)
                continue
            elif int(lista[x][2])==8 and int(y)%100>11:
                lettere=lettere[0:-1]+"otto"
            else:
                lettere+=dizionario[2].get(int(lista[x][2]))
            lettere+=dizionario[3].get(x)
    return lettere
       
        
def conv(n):
    a=conversione_in_lista(n)
    return conversione_in_lettere(a)
