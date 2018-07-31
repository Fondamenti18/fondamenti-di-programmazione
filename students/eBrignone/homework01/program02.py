''' In determinate occasioni ci capita di dover scrivere i numeri in lettere, 
ad esempio quando dobbiamo compilare un assegno. 
Puo' capitare che alcuni numeri facciano sorgere in noi qualche dubbio.

Le perplessita' nascono soprattutto nella scrittura dei numeri composti con 1 e 8. 
Tutti i numeri come venti, trenta, quaranta, cinquanta, ecc... elidono la vocale 
finale (la "i" per 20, la "a" per tutti gli altri) fondendola con la vocale iniziale 
del numero successivo; scriveremo quindi ventuno, ventotto, trentotto, 
cinquantuno ecc...

Il numero cento, nella formazione dei numeri composti con uno e otto, non si comporta 
cosi'; il numero "cento" e tutte le centinaia (duecento, trecento, ecc...), 
infatti, non elidono la vocale finale. Dunque non scriveremo centuno,  trecentotto ma centouno, 
trecentootto, ecc...

I numeri composti dalle centinaia e dalla decina "ottanta" invece tornano ad elidere 
la vocale finale; scriveremo quindi centottanta, duecentottanta,  ecc..., 
non centoottanta, duecentoottanta, ...

Il numero "mille" non elide in nessun numero composto la vocale finale; scriveremo 
quindi milleuno,  milleotto, milleottanta, ecc...

Altri esempi sono elencati nel file grade02.txt


Scrivere una funzione conv(n) che prende in input un intero n, con 0<n<1000000000000, 
e restituisce in output una stringa con il numero espresso in lettere

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

dizionario = {
    0: "",
    1 : "uno",2 : "due", 3: "tre", 4: "quattro", 5: "cinque", 6: "sei", 7: "sette", 8:"otto", 9:"nove",
    10 : "dieci", 11 : "undici", 12: "dodici", 13: "tredici",14: "quattordici",15: "quindici", 16: "sedici", 17: "diciassette", 18: "diciotto", 19: "diciannove",
    20 : "venti", 30: "trenta" , 40: "quaranta", 50: "cinquanta", 60: "sessanta", 70: "settanta", 80: "ottanta", 90: "novanta",
    100: "cento",
    1000: "mila",
    1000000: "milioni",
    1000000000: "miliardi",
    1000000000000: "bilioni"
    
}
speciali = {
    1000 : "mille",
    1000000: "milione",
    1000000000: "miliardo"
}

def scomponiDec(numero):
    divisore = 1000000000000
    scomposizione = []
    while numero > 0:
        n = numero/divisore
        if int(n)>0:
            scomposizione += [(int(n),int(divisore))]
            numero -= int(n)*divisore
        divisore /= 10
    return scomposizione
def getValoreByK(scomposizione, k):
    for tupla in scomposizione:
        if tupla[1]==k:
            return tupla[0]
    return 0
def getTupleInRange(scomposizione, low, high):
    ret = []
    for tupla in scomposizione:
        if low<=tupla[1] and tupla[1]<high:
            ret.append(tupla)
        ret.reverse()       
        
    return ret

def raggruppa(scomposizione,kMinore):
    if len(scomposizione)==0:
        return []
    scomposizione.reverse()
    valore = 0
    for tupla in scomposizione:
        valore += (tupla[0]*tupla[1]/kMinore)
    return (int(valore),kMinore)
    
def raggruppaInK(scomposizione):
    k = 1000
    ranges = [(1,1000),(1000,1000000), (1000000,1000000000), (1000000000,1000000000000)]
    raggruppamento = []
    for r in ranges:
        tupleInRange = getTupleInRange(scomposizione,r[0],r[1])
        if len(tupleInRange)>0:
            if r[0]==1:
                raggruppamento.extend(tupleInRange)
            else:
                tupleInRange = raggruppa(tupleInRange,r[0])
                raggruppamento.append(tupleInRange)
        
    return raggruppamento
def stringaByValore(unita,decine,centinaia):
    ret = ""
    if centinaia>0:
        if centinaia==1:
            ret += dizionario[100]
        else:
            ret += dizionario[centinaia] + dizionario[100]
        if decine==8:
            ret = ret[:-1]
    if decine*10+unita>=10 and decine*10+unita<=19:
        ret += dizionario[decine*10+unita]
    else:
        if unita==1 or unita==8:
            ret += dizionario[decine*10][:-1]+str(dizionario[unita])
        else:
            ret += dizionario[decine*10]+str(dizionario[unita])
    
    return ret
def raggruppamentoToString(raggruppamento):
    ret = ""
    ranges = [(1,1000),(1000,1000000), (1000000,1000000000), (1000000000,1000000000000)]
    ranges.reverse()
    for r in ranges:
        if r[0]==1:
            unita = getValoreByK(raggruppamento,1)
            decine = getValoreByK(raggruppamento,10)
            centinaia = getValoreByK(raggruppamento,100)
            ret += stringaByValore(unita,decine,centinaia)
        else:
            lista = getTupleInRange(raggruppamento,r[0],r[1])
            if len(lista)>0:
                tupla = lista[0]
                valore = tupla[0]

                if valore==1:
                    if tupla[1]==1000:
                        ret += speciali[tupla[1]]
                    else:
                        ret += dizionario[valore][:-1] + speciali[tupla[1]]
                else:
                
                    centinaia = int(valore/100)
                    decine = int((valore-centinaia*100)/10)
                    unita = int(valore-centinaia*100-decine*10)
                    ret += stringaByValore(unita,decine,centinaia) + dizionario[tupla[1]]
    return ret
        
def conv(n):
    scomposizione = scomponiDec(n)
    raggruppamento = raggruppaInK(scomposizione)
    raggruppamento.reverse()
    return raggruppamentoToString(raggruppamento)


