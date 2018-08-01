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

spec_num={
    '0' : '',    
    '1' : 'uno',
    '2' : 'due',
    '3' : 'tre',
    '4' : 'quattro',
    '5' : 'cinque',
    '6' : 'sei',
    '7' : 'sette',
    '8' : 'otto',
    '9' : 'nove',
    '10' : 'dieci',
    '11' : 'undici',
    '12' : 'dodici',
    '13' : 'tredici',
    '14' : 'quattordici',
    '15' : 'quindici',
    '16' : 'sedici',
    '17' : 'diciassette',
    '18' : 'diciotto',
    '19' : 'diciannove',
    '20' : 'venti',
    '30' : 'trenta',
    '40' : 'quaranta',
    '50' : 'cinquanta',
    '60' : 'sessanta',
    '70' : 'settanta',
    '80' : 'ottanta',
    '90' : 'novanta',
    '100' : 'cento',
    '1000' : 'mille',
    '1000000' : 'unmilione',
    '1000000000' : 'unmiliardo',

    }

esp = {
       '0' : '',
       '1' : 'mila',
       '2' : 'milioni',
       '3' : 'miliardi',
       }

def assegna_chiave_valore(num_str,esponente_gruppo):
    if num_str=="000": return ''
    if len(num_str)==3: return tre_cifre(num_str,esponente_gruppo)
    elif len(num_str)==2: return due_cifre(num_str,esponente_gruppo)
    else: return una_cifra(num_str,esponente_gruppo)
        
        
        
def una_cifra(num_str,esponente_gruppo):
    u = int(num_str)
    if u!=1: return spec_num[str(u)]+str(esp.get(str(esponente_gruppo),''))
    else: return spec_num[str(u*(10**(3*esponente_gruppo)))]

def tre_cifre(num_str,esponente_gruppo):
    numero=""
    u,d,c = [int(i) for i in num_str]
    if d==1:
        return spec_num.get(str(c*(10**2)),spec_num[str(c)]+"cento")+spec_num[str(d)+str(u)]+str(esp.get(str(esponente_gruppo),''))
    else:
        numero+=spec_num.get(str(c*(10**2)),spec_num[str(c)]+"cento")
        numero=contr_d_otto(d,numero) ###########
        numero+=spec_num.get(str(d*10),"decina non trovata")
        numero=contr_u_uno_otto(u,d,numero) ###########
        numero+=spec_num.get(str(u),"0")
        return numero+str(esp.get(str(esponente_gruppo),''))


def due_cifre(num_str,esponente_gruppo):
    numero=""
    u,d = [int(i) for i in num_str]
    if d==1:
        return spec_num[str(d)+str(u)]+str(esp.get(str(esponente_gruppo),''))
    else:
        numero+=spec_num.get(str(d*10),"decina non trovata")
        numero=contr_u_uno_otto(u,1,numero)
        numero+=spec_num.get(str(u),"0")
        return numero+str(esp.get(str(esponente_gruppo),''))


def contr_d_otto(d,numero):
    if d==8: return numero[:-1]
    return numero
    
def contr_u_uno_otto(u,d,numero):
    if (u==1 or u==8) and d!=0: return numero[:-1]
    return numero

def scomponi(n):
    ##n_str = correggi_format(n)
    rang = range(0,len(n),3)
    n = n[::-1]
    lista = [n[i:i+3] for i in rang]
    return lista

def conv(n):
    if str(n) in spec_num.keys(): return spec_num[str(n)]
    
    return "".join([assegna_chiave_valore(tripla,pos) for pos,tripla in enumerate(scomponi(str(n)))][::-1])

