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



    
#Dizionari per unita
#da 1 a 10
dic1={'0': '','1':'uno', '2':'due', '3':'tre', '4':'quattro', '5':'cinque', '6':'sei', '7':'sette',
           '8':'otto', '9':'nove', '10':'dieci'}

#da 11 a 20
dic2={'0':'dieci', '1':'undici','2':'dodici', '3':'tredici', '4':'quattordici', '5':'quindici', '6':'sedici', '7':'diciasette',
              '8':'diciotto', '9':'dicianove'}
#decine
dic3={'0': '', '2': 'venti', '3': 'trenta', '4': 'quaranta', '5': 'cinquanta', '6': 'sessanta', '7': 'settanta',
        '8': 'ottanta', '9': 'novanta'}

#centinaia
dic4={'0': '', '1': 'cento', '2': 'duecento', '3':'trecento', '4': 'quattrocento', '5': 'cinquecento', '6': 'seicento',
             '7': 'settecento', '8': 'ottocento', '9': 'novecento'}

#migliaia, contiamo il numero delle cifre dalla fine
dic5={'0': '', '3':'mila', '6':'milioni', '9':'miliardi'}

#introduciamo le variabili
word=''
numero_1=numero#per avere il numero originale
count_position=len(numero)
change_position=3#per contare il numero di cifre dalla fine e sostituire rispettivamente con 'mille', 'milione' o 'miliardo'
cambio=3
#Se l'elemento inserito non e il numero
if int(numero)<=0 or int(numero)>=1000000000000:
    print("numero non incluso nell'intervallo")
while not numero.isdigit():
    print("Inserire solo i numeri")
def conv(numero):
    count_position=len(numero)
    word=''
    numero_1=numero#per avere il numero originale
    change_position=3
    cambio=3
    while count_position>0:
        if numero=='0':
            word='zero'
            break
        if numero_1[count_position-2]=='1':
        #prende il valore di key words per testare l'ultima cifra
            for x in dic2:
                if numero_1[count_position-1]==x:
                    word=dic2[x]+word
        else:
            for x1 in dic1:
                if numero_1[count_position-1]==x1:
                    word=dic1[x1]+word
        #per verificare se la parte 'migliaia' non e uguale ad 1, altrimenti facciamo la procedura standard
        #verifica se count_position non e uguale ad 1, verifica da destra a sinistra
        #se count_position=1 non c'e la decina
            if count_position > 1:#testare le decine
                for x2 in dic3:
                    if numero_1[count_position-2]==x2:
                        word = dic3[x2] + word
    #verifica di centinaia, non e uguale a 1 o 2
        if count_position>2:
            for x3 in dic4:
                if numero_1[count_position-3]==x3:
                    word=dic4[x3]+word
    #verifica per mila
        if count_position>3:
          word=dic5[str(cambio)]  + word
        cambio=cambio+3
        count_position=count_position-3
        return word
if "ventiuno" in word:
    word=word.replace("ventiuno", "ventuno")
if "ventiotto" in word:
    word=word.replace("ventiotto", "ventotto")
if "trentauno" in word:
    word=word.replace("trentauno", "trentuno")
if "trentaotto" in word:
    word=word.replace("trentaotto", "trentotto")
if "quarantaotto" in word:
    word=word.replace("quarantaotto", "quarantotto")
if "quarantauno" in word:
    word=word.replace("quarantauno", "quarantuno")
if "cinquantauno" in word:
    word=word.replace("cinquantauno", "cinquantuno")
if "cinquantaotto" in word:
    word=word.replace("cinquantaotto", "cinquantotto")
if "sessantauno" in word:
    word=word.replace("sessantauno", "sessantuno")
if "sessantaotto" in word:
    word=word.replace("sessantaotto", "sessantotto")
if "settantaotto" in word:
    word=word.replace("settantaotto", "settantotto")
if "settantauno" in word:
    word=word.replace("settantauno", "settantuno")
if "ottantauno" in word:
    word=word.replace("ottantauno", "ottantuno")
if "ottantaotto" in word:
    word=word.replace("ottantaotto", "ottantotto")
if "novantaotto" in word:
    word=word.replace("novantaotto", "novantotto")
if "novantauno" in word:
    word=word.replace("novantauno", "novantuno")
#eccezione per mille
if "unomila" in word:
    word=word.replace("unomila", "mille")
#eccezione per un milione
if "unomilioni" in word:
    word=word.replace("unomilioni", "un milione")
#eccezione per un miliardo
if "unomiliardi" in word:
    word=word.replace("unomiliardi", "un miliardo")
if "milionimila" in word:
    word=word.replace("milionimila", "milioni")
if "milionimila" in word:
    word=word.replace("milionimila", "milioni")
if "miliardimila" in word:
    word=word.replace("miliardimila", "miliardi")
if "miliardomila" in word:
    word=word.replace("miliardomila", "miliardi")
if "milionemila" in word:
    word=word.replace("milionemila", "milione")
if "miliardimilioni" in word:
    word=word.replace("miliardimilioni", "miliardi")
if "miliardomilioni" in word:
    word=word.replace("miliardomilioni", "miliardo")
if "centoott" in word:
    word=word.replace("centoott", "centott")
print(word)

























