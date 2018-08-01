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

#la funzione conv chiama la funzione zero_to_999, passandole le cifre del numero n 3 alla volta (da 0 a 999)
#la funzione zero_to_999 costruisce un numero da 1 a 99 e lo passa ad hundreds, che in caso 
#il numero sia maggiore di 99 attacca il suffisso corretto per le centinaia. il nome poi torna a conv
#che valuta la posizione delle tre cifre all' interno del numero n, e aggiunge alla stringa i suffissi adeguati

def conv(n):
    i=0
    k=0
    words=[]
    w=''
    unit=['','uno','due','tre','quattro','cinque','sei','sette','otto','nove']
    exp=['','mila','milioni','miliardi']
    onexp=['','mille','unmilione','unmiliardo',]
	# scompatta il numero in una lista, e la gira, per comodita' dei cicli successivi
    ls=[int(x) for x in reversed(str(n))]
	# aggiunge gli 0 che mancano per poter passare le cifre a zero_to_999 sempre a 3 a 3
    while len(ls)%3!=0: ls+=[0]   
    triples= len(ls)//3
	# ciclo una volta per ogi 3 cifre di n, ogni passo eccetto il primo appende il suffisso adeguato, pescato dalle liste exp o onexp    
    while i<triples:
        w=zero_to_999(ls[k+2],ls[k+1],ls[k],unit)
        if w=='uno'and i!=0: words.append(onexp[i])
        elif w=='':pass
        else: words.append(w+exp[i])
        i+=1
        k+=3
	# il numero e' pronto, ma e' formato al contrario, lo rigira e lo compatta in una stringa, poi ritorna           
    w=''.join(reversed(words))    
    return w


#unit e' una lista con i nomi delle cifre 0-9, definita in conv, poiche' serve ad entrambe le funzioni, e passata a zero_to_999
def zero_to_999(c,d,u,unit):
    st=''
    num=d*10+u
    teens=['','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
    dec=['','dieci','vent','trent','quarant','cinquant','sessant','settant','ottant','novant']
    
	# controlla che le decine non siano in range "scomodo", in quel caso prende valori direttamente dalla lista 10-19 o da quella 1-9
    if num <20:st+=teens[d and u+1]+unit[-(d-1)*u]
        # altrimenti c' un controllo "eufonico" per l'elisione delle vocali
    elif u==1 or u==8: st+=dec[d]+unit[u]
        # se il numero non e' tra quelli, allora controlla che non sia tra 20 e 30, poi chiama le posizioni relative alle giuste stringhe   
    else:
        if d==2:st+='venti'+unit[u] 
        else: st+=dec[d]+'a'+unit[u]    
	 # se le centinaia sono 0 ritorna la stringa col numero nel range 0-99
    if c==0:
        return st
    else:
        return hundreds(st,c,d,unit)
	
    
def hundreds(st,c,d,unit):    
        # se c e' 1 per comodita' lo poniamo 0, per pescare da unit la stringa vuota
    if c==1:c=0
	# controllo eufonico come prima, ma solo sugli 80, poi si compongono le centinaia col resto fatto in precedenza, e si ritorna st
    if d==8:
        st=unit[c]+'cent'+st
    else:
        st=unit[c]+'cento'+st
    return st


