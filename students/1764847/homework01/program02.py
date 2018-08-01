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
    '''prende in input un intero n, con 0<n<1000000000000,
    e restituisce una stringa con il numero espresso in lettere'''
    listaM = ['','', 'mila', 'milioni', 'miliardi']
    listaMP = ['', '', 'mille', 'unmilione', 'unmiliardo']
    num = str(n)                                                            #Converte il numero in una stringa
    lstParti = dividiInParti(num)                                           #Crea una lista dove ogni elemento contiene esattamente 3 caratteri della stringa num
    risultato = ''                                                          #Stringa da restituire
    length = len(lstParti)                                                  #Contiene la lunghezza della lista
    for i in range(len(lstParti)):                                          #Per ogni i, per tutta la lunghezza della stringa
        if len(lstParti[i]) > 1 and lstParti[i] == '001':                   #Se la lunghezza dell'elemento i della lista è > 1 e l'indice i della lista contiene la stringa '001'
            risultato += convertiNumero(lstParti[i]) + listaMP[length]      #Chiama la funzione convertiNumero e concatena alla stringa l'elemento della listaMP che si trova
                                                                            #in posizione dell'indice pari alla lunghezza della stringa
            risultato = risultato[3:]                                       #Elimina dalla stringa gli zeri iniziali
        else:                                                               #Alrimenti fa lo stesso procedimento ma con la listaM
            risultato += convertiNumero(lstParti[i]) + listaM[length]
        length -= 1                                                         #Decrementa la variabile che contiene la lunghezza della lista
    return risultato                                                        #Restituisce il numero convertito in lettere


def dividiInParti(s):
    '''Prende in input una stringa e restituisce una lista
    dove ogni posizione contiene esattamente 3 caratteri della stringa'''
    length = len(s)                                                         #Calcola la lunghezza della stringa
    while length%3 != 0:                                                    #Finche la lunghezza della stringa modulo 3 e diverso da 0
        s = '0' + s                                                         #Aggiune uno zero in testa alla stringa
        length = len(s)                                                     #Calcola di nuovo la lunghezza
    p=0
    result=[]                                                               #Lista da restituire
    while p<len(s):                                                         #finche la variabile p < della lunghezza di s
        result.append(s[p:p+3])                                             #aggiunge alla lista gli elementi che vanno da p a p+3
        p+=3                                                                #incrementa p di 3
    return result                                                           #Restituisce la lista


def convertiNumero(s):
    '''Prende in input una stringa contenente il numero espresso in cifre 0<s<999
    e restituisce la traduzione del numero espresso in lettere'''
    risultato = ''                                                          #Contiene il numero espresso in lettere
    unita = ['', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove',
             'dieci', 'undici', 'dodici', 'tredici', 'quattordici', 'quindici', 
             'sedici', 'diciassette', 'diciotto','diciannove']
    decine = ['', '', 'venti', 'trenta', 'quaranta', 'cinqunta', 'sessanta', 
              'settanta', 'ottanta', 'novanta', 'cento']
    decineV = ['', '', 'vent', 'trent', 'quarant', 'cinquant', 'sessant', 'settant', 'ottant', 'novant', 'cent']
    if s[0] == '1':                                                         #Se il primo carattere di s e uguae a '1'
        if s[1] == '8':                                                         #Se il secondo carattere di s e uguale a '8'
            risultato += decineV[10]                                                #Aggiunge al risultato l elemeto 10 della lista decineV
        else:                                                                   #Altrimenti
            risultato += decine[10]                                                 #Aggiunge al risultato l elemento 10 della lista decine
    elif s[0] != '0' and s[0] != '1':                                       #Altrimenti se il primo carattere e != '1' e != '1'
        if s[1] == '8':                                                         #Se il secondo elemento di s e ugale a '8'
            risultato += unita[int(s[0])] + decineV[10]                             #Aggiunge al risultato l'elemento avente lo stesso indice del numero in prima posizione di s
                                                                                    #e l elemenro 10 della lista decineV
        else:                                                                   #Altrimenti
            risultato += unita[int(s[0])] + decine[10]                              #Stesso procedimento appena descritto ma l elemento 10 viene preso dalla lista decine
    if int(s[1:]) <= 19:                                                    #Se i caratteri che vanno dalla seconda posizione fino alla fine della stringa convertiti in intero < 19
        risultato += unita[int(s[1:])]                                          #Aggiunge al risultato l elemento contenuto nella lista decine in posizione s[1:] convertita in intero
    else:                                                                   #Altrimenti
        if s[-1] == '1' or s[-1] == '8':                                        #se l'ultimo carattere della stringa e == '1' oppure == '8'
            risultato += decineV[int(s[1])] + unita[int(s[2])]                      #aggiunge al risultato l elemento s[1] convertito in intero nella lista decineV
                                                                                    #e concatena l elemento s[2] convertito in intero  contenuto nella lista unita
        else:                                                                   #Altrimenti
            risultato += decine[int(s[1])] + unita[int(s[2])]                       #Fa lo stesso procedimento ma prende gli elementi dalla lista decine e unita
    return risultato                                                        #Restituisce la stringa convertita