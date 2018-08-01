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
unita = ["uno","due","tre","quattro","cinque","sei","sette","otto","nove","dieci",
         "undici","dodici","tredici","quattordici","quindici","sedici","diciassette","diciotto","diciannove"];
decine = ["dieci","venti","trenta","quaranta","cinquanta","sessanta","settanta","ottanta","novanta"];
decine1 = ["cosa","vent","trent","quarant","cinquant","sessant","settant","ottant","novant"];
altro = ["cento","cent"];
altro1 = ["","mila","milioni","miliardi"];
altro2 = ["","mille","unmilione","unmiliardo"];

def triplettaggio(x):
    numero = [];
    while x >= 1:
        numero.append(str(int((x/1000-x//1000)*1000+0.1)));
        x = x//1000;
    
    return numero;

def conv(n):
    stringa = "";
    triplette = [];
    numero = triplettaggio(n);
    i = 0;
    while i < len(numero):
        
        '''se la tripletta è composta da 3 cifre'''
        if len(numero[i]) == 3:
            
            '''controllo sul primo valore'''
            if numero[i][1] == '8':
                stringa += unita[int(numero[i][0])-1];
                stringa += altro[1];
            elif numero[i][0] == '1':
                stringa += altro[0];
            else:
                stringa += unita[int(numero[i][0])-1];
                stringa += altro[0];
                
            '''controllo gli ultimi 2'''
            if numero[i][1] == '0' and numero[i][2] == '0':
                i += 1;
            elif numero[i][1] == '0':
                stringa += unita[int(numero[i][2])-1];
                i += 1;
            elif numero[i][1] == '1':
                stringa += unita[int(numero[i][2])+9];
                i += 1;
            elif numero[i][2] == '0':
                stringa += decine[int(numero[i][1])-1];
                i += 1;
            elif numero[i][2] == '1' or numero[i][2] == '8':
                stringa += decine1[int(numero[i][1])-1] + unita[int(numero[i][2])-1];
                i += 1;
            else:
                stringa += decine[int(numero[i][1])-1] + unita[int(numero[i][2])-1];
                i += 1;
                
            triplette.append(stringa);
            stringa = "";
            
            '''se la tripletta ha 2 valori'''
        elif len(numero[i]) == 2:
            
            if numero[i][0] == '1':
                stringa += unita[int(numero[i][1])+9];
                i += 1;
            elif numero[i][1] == '0':
                stringa += decine[int(numero[i][0])-1];
                i += 1;
            elif numero[i][1] == '1' or numero[i][1] == '8':
                stringa += decine1[int(numero[i][0])-1] + unita[int(numero[i][1])-1];
                i += 1;
            else:
                stringa += decine[int(numero[i][0])-1] + unita[int(numero[i][1])-1];
                i += 1;
                
            triplette.append(stringa);
            stringa = "";
            
            '''se la tripletta ha 1 valore'''
        elif len(numero[i]) == 1:
            stringa += unita[int(numero[i][0])-1];
            triplette.append(stringa);
            stringa = "";
            i += 1;
            
    i = len(triplette);
    while i > 0:
        if triplette[i-1] != 'uno':
            stringa += triplette[i-1] + altro1[i-1];
        else:
            stringa += altro2[i-1];

        i -= 1;
        
    return stringa;

print(conv(1234567))