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

def conv(n):
    numero=''
    lista20=['','uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
    listadec=['','','venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
    listacent=['','cento','duecento','trecento','quattrocento','cinquecento','seicento','settecento','ottocento','novecento']
    cmr=n//100000000000
    dmr=n%100000000000
    mr=n%10000000000
    cml=mr%1000000000
    dml=cml%100000000
    ml=dml%10000000
    cm=ml%1000000
    dm=cm%100000
    m=dm%10000
    c=m%1000
    d=c%100
    u=d%10
    dmr=dmr//10000000000
    mr=mr//1000000000
    cml=cml//100000000
    dml=dml//10000000
    ml=ml//1000000
    cm=cm//100000
    dm=dm//10000
    m=m//1000
    c=c//100
    d=d//10
    listamr=[cmr,dmr,mr]
    listaml=[cml,dml,ml]
    listam=[cm,dm,m]
    listau=[c,d,u]
    listanum=[listamr,listaml,listam,listau]
    print(listanum)
    listamila=['miliardi','milioni','mila','','']
    listamille=['unmiliardo','unmilione','mille','','']
    c=0
    for el in listanum:
        numero+=listacent[el[0]]
        '''Se la cifra delle decine+unità è minore di 20'''
        if el[1]==1:
            el[2]=el[1]*10+el[2]
        '''elisione dell'80'''
        if el[1]==8:
            if el[0]>=1:
                numero=numero[:-1]
                numero+=listadec[8]
            else:
                numero+=listadec[el[1]]
        else:
            numero+=listadec[el[1]]
        '''Elisione dell'unità 8 e 1'''
        if el[2]==1 or el[2]==8:
            if el[1]>0:
                numero=numero[:-1]
                numero+=lista20[el[2]]
            else:
                numero+=lista20[el[2]]   
        else:
            numero+=lista20[el[2]]
        '''Controllo se la terzina non è valorizzata''' 
        if el[0]*100+el[1]*10+el[2]>1:
            numero+=listamila[c]
        '''Controllo se insierire mille/mila,milione/milioni,miliardo/miliardi'''
        if el[0]==0 and el[1]==0 and el[2]==1:
            numero=listamille[c]
        c+=1
        if c==4:
            break
    return numero
