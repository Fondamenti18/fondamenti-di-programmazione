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



ls=('uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci',
                'undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove','venti',
                'ventuno','ventidue','ventitre','ventiquattro','venticinque','ventisei','ventisette','ventotto','ventinove','trenta',
                'trentuno','trentadue','trentatre','trentaquattro','trentacinque','trentasei','trentasette','trentotto','trentanove','quaranta',
                'quarantuno','quarantadue','quarantatre','quarantaquattro','quarantacinque','quarantasei','quarantasette','quarantotto','quarantanove','cinquanta',
                'cinquantuno','cinquantadue','cinquantatre','cinquantaquattro','cinquantacinque','cinquantasei','cinquantasette','cinquantotto','cinquantanove','sessanta',
                'sessantuno','sessantadue','sessantatre','sessantaquattro','sessantacinque','sessantasei','sessantasette','sessantotto','sessantanove','settanta',
                'settantuno','settantadue','settantatre','settantaquattro','settantacinque','settantasei','settantasette','settantotto','settantanove','ottanta',
                'ottantuno','ottantadue','ottantatre','ottantaquattro','ottantacinque','ottantasei','ottantasette','ottantotto','ottantanove','novanta',
                'novantuno','novantadue','novantatre','novantaquattro','novantacinque','novantasei','novantasette','novantotto','novantanove','cento','centouno','centodue','centotre','centoquattro','centocinque','centosei','centosette','centootto','centonove','centodieci',
                'centoundici','centododici','centotredici','centoquattordici','centoquindici','centosedici','centodiciassette','centodiciotto','centodiciannove','centoventi',
                'centoventuno','centoventidue','centoventitre','centoventiquattro','centoventicinque','centoventisei','centoventisette','centoventotto','centoventinove','centotrenta',
                'centotrentuno','centotrentadue','centotrentatre','centotrentaquattro','centotrentacinque','centotrentasei','centotrentasette','centotrentotto','centotrentanove','centoquaranta',
                'centoquarantuno','centoquarantadue','centoquarantatre','centoquarantaquattro','centoquarantacinque','centoquarantasei','centoquarantasette','centoquarantotto','centoquarantanove','centocinquanta',
                'centocinquantuno','centocinquantadue','centocinquantatre','centocinquantaquattro','centocinquantacinque','centocinquantasei','centocinquantasette','centocinquantotto','centocinquantanove','centosessanta',
                'centosessantuno','centosessantadue','centosessantatre','centosessantaquattro','centosessantacinque','centosessantasei','centosessantasette','centosessantotto','centosessantanove','centosettanta',
                'centosettantuno','centosettantadue','centosettantatre','centosettantaquattro','centosettantacinque','centosettantasei','centosettantasette','centosettantotto','centosettantanove','centottanta',
                'centottantuno','centottantadue','centottantatre','centottantaquattro','centottantacinque','centottantasei','centottantasette','centottantotto','centottantanove','centonovanta',
                'centonovantuno','centonovantadue','centonovantatre','centonovantaquattro','centonovantacinque','centonovantasei','centonovantasette','centonovantotto','centonovantanove','duecento','duecentouno','duecentodue','duecentotre','duecentoquattro','duecentocinque','duecentosei','duecentosette','duecentootto','duecentonove','duecentodieci',
                'duecentoundici','duecentododici','duecentotredici','duecentoquattordici','duecentoquindici','duecentosedici','duecentodiciassette','duecentodiciotto','duecentodiciannove','duecentoventi',
                'duecentoventuno','duecentoventidue','duecentoventitre','duecentoventiquattro','duecentoventicinque','duecentoventisei','duecentoventisette','duecentoventotto','duecentoventinove','duecentotrenta',
                'duecentotrentuno','duecentotrentadue','duecentotrentatre','duecentotrentaquattro','duecentotrentacinque','duecentotrentasei','duecentotrentasette','duecentotrentotto','duecentotrentanove','duecentoquaranta',
                'duecentoquarantuno','duecentoquarantadue','duecentoquarantatre','duecentoquarantaquattro','duecentoquarantacinque','duecentoquarantasei','duecentoquarantasette','duecentoquarantotto','duecentoquarantanove','duecentocinquanta',
                'duecentocinquantuno','duecentocinquantadue','duecentocinquantatre','duecentocinquantaquattro','duecentocinquantacinque','duecentocinquantasei','duecentocinquantasette','duecentocinquantotto','duecentocinquantanove','duecentosessanta',
                'duecentosessantuno','duecentosessantadue','duecentosessantatre','duecentosessantaquattro','duecentosessantacinque','duecentosessantasei','duecentosessantasette','duecentosessantotto','duecentosessantanove','duecentosettanta',
                'duecentosettantuno','duecentosettantadue','duecentosettantatre','duecentosettantaquattro','duecentosettantacinque','duecentosettantasei','duecentosettantasette','duecentosettantotto','duecentosettantanove','duecentottanta',
                'duecentottantuno','duecentottantadue','duecentottantatre','duecentottantaquattro','duecentottantacinque','duecentottantasei','duecentottantasette','duecentottantotto','duecentottantanove','duecentonovanta',
                'duecentonovantuno','duecentonovantadue','duecentonovantatre','duecentonovantaquattro','duecentonovantacinque','duecentonovantasei','duecentonovantasette','duecentonovantotto','duecentonovantanove','trecento','trecentouno','trecentodue','trecentotre','trecentoquattro','trecentocinque','trecentosei','trecentosette','trecentootto','trecentonove','trecentodieci',
                'trecentoundici','trecentododici','trecentotredici','trecentoquattordici','trecentoquindici','trecentosedici','trecentodiciassette','trecentodiciotto','trecentodiciannove','trecentoventi',
                'trecentoventuno','trecentoventidue','trecentoventitre','trecentoventiquattro','trecentoventicinque','trecentoventisei','trecentoventisette','trecentoventotto','trecentoventinove','trecentotrenta',
                'trecentotrentuno','trecentotrentadue','trecentotrentatre','trecentotrentaquattro','trecentotrentacinque','trecentotrentasei','trecentotrentasette','trecentotrentotto','trecentotrentanove','trecentoquaranta',
                'trecentoquarantuno','trecentoquarantadue','trecentoquarantatre','trecentoquarantaquattro','trecentoquarantacinque','trecentoquarantasei','trecentoquarantasette','trecentoquarantotto','trecentoquarantanove','trecentocinquanta',
                'trecentocinquantuno','trecentocinquantadue','trecentocinquantatre','trecentocinquantaquattro','trecentocinquantacinque','trecentocinquantasei','trecentocinquantasette','trecentocinquantotto','trecentocinquantanove','trecentosessanta',
                'trecentosessantuno','trecentosessantadue','trecentosessantatre','trecentosessantaquattro','trecentosessantacinque','trecentosessantasei','trecentosessantasette','trecentosessantotto','trecentosessantanove','trecentosettanta',
                'trecentosettantuno','trecentosettantadue','trecentosettantatre','trecentosettantaquattro','trecentosettantacinque','trecentosettantasei','trecentosettantasette','trecentosettantotto','trecentosettantanove','trecentottanta',
                'trecentottantuno','trecentottantadue','trecentottantatre','trecentottantaquattro','trecentottantacinque','trecentottantasei','trecentottantasette','trecentottantotto','trecentottantanove','trecentonovanta',
                'trecentonovantuno','trecentonovantadue','trecentonovantatre','trecentonovantaquattro','trecentonovantacinque','trecentonovantasei','trecentonovantasette','trecentonovantotto','trecentonovantanove','quattrocento','quattrocentouno','quattrocentodue','quattrocentotre','quattrocentoquattro','quattrocentocinque','quattrocentosei','quattrocentosette','quattrocentootto','quattrocentonove','quattrocentodieci',
                'quattrocentoundici','quattrocentododici','quattrocentotredici','quattrocentoquattordici','quattrocentoquindici','quattrocentosedici','quattrocentodiciassette','quattrocentodiciotto','quattrocentodiciannove','quattrocentoventi',
                'quattrocentoventuno','quattrocentoventidue','quattrocentoventitre','quattrocentoventiquattro','quattrocentoventicinque','quattrocentoventisei','quattrocentoventisette','quattrocentoventotto','quattrocentoventinove','quattrocentotrenta',
                'quattrocentotrentuno','quattrocentotrentadue','quattrocentotrentatre','quattrocentotrentaquattro','quattrocentotrentacinque','quattrocentotrentasei','quattrocentotrentasette','quattrocentotrentotto','quattrocentotrentanove','quattrocentoquaranta',
                'quattrocentoquarantuno','quattrocentoquarantadue','quattrocentoquarantatre','quattrocentoquarantaquattro','quattrocentoquarantacinque','quattrocentoquarantasei','quattrocentoquarantasette','quattrocentoquarantotto','quattrocentoquarantanove','quattrocentocinquanta',
                'quattrocentocinquantuno','quattrocentocinquantadue','quattrocentocinquantatre','quattrocentocinquantaquattro','quattrocentocinquantacinque','quattrocentocinquantasei','quattrocentocinquantasette','quattrocentocinquantotto','quattrocentocinquantanove','quattrocentosessanta',
                'quattrocentosessantuno','quattrocentosessantadue','quattrocentosessantatre','quattrocentosessantaquattro','quattrocentosessantacinque','quattrocentosessantasei','quattrocentosessantasette','quattrocentosessantotto','quattrocentosessantanove','quattrocentosettanta',
                'quattrocentosettantuno','quattrocentosettantadue','quattrocentosettantatre','quattrocentosettantaquattro','quattrocentosettantacinque','quattrocentosettantasei','quattrocentosettantasette','quattrocentosettantotto','quattrocentosettantanove','quattrocentottanta',
                'quattrocentottantuno','quattrocentottantadue','quattrocentottantatre','quattrocentottantaquattro','quattrocentottantacinque','quattrocentottantasei','quattrocentottantasette','quattrocentottantotto','quattrocentottantanove','quattrocentonovanta',
                'quattrocentonovantuno','quattrocentonovantadue','quattrocentonovantatre','quattrocentonovantaquattro','quattrocentonovantacinque','quattrocentonovantasei','quattrocentonovantasette','quattrocentonovantotto','quattrocentonovantanove','cinquecento','cinquecentouno','cinquecentodue','cinquecentotre','cinquecentoquattro','cinquecentocinque','cinquecentosei','cinquecentosette','cinquecentootto','cinquecentonove','cinquecentodieci',
                'cinquecentoundici','cinquecentododici','cinquecentotredici','cinquecentoquattordici','cinquecentoquindici','cinquecentosedici','cinquecentodiciassette','cinquecentodiciotto','cinquecentodiciannove','cinquecentoventi',
                'cinquecentoventuno','cinquecentoventidue','cinquecentoventitre','cinquecentoventiquattro','cinquecentoventicinque','cinquecentoventisei','cinquecentoventisette','cinquecentoventotto','cinquecentoventinove','cinquecentotrenta',
                'cinquecentotrentuno','cinquecentotrentadue','cinquecentotrentatre','cinquecentotrentaquattro','cinquecentotrentacinque','cinquecentotrentasei','cinquecentotrentasette','cinquecentotrentotto','cinquecentotrentanove','cinquecentoquaranta',
                'cinquecentoquarantuno','cinquecentoquarantadue','cinquecentoquarantatre','cinquecentoquarantaquattro','cinquecentoquarantacinque','cinquecentoquarantasei','cinquecentoquarantasette','cinquecentoquarantotto','cinquecentoquarantanove','cinquecentocinquanta',
                'cinquecentocinquantuno','cinquecentocinquantadue','cinquecentocinquantatre','cinquecentocinquantaquattro','cinquecentocinquantacinque','cinquecentocinquantasei','cinquecentocinquantasette','cinquecentocinquantotto','cinquecentocinquantanove','cinquecentosessanta',
                'cinquecentosessantuno','cinquecentosessantadue','cinquecentosessantatre','cinquecentosessantaquattro','cinquecentosessantacinque','cinquecentosessantasei','cinquecentosessantasette','cinquecentosessantotto','cinquecentosessantanove','cinquecentosettanta',
                'cinquecentosettantuno','cinquecentosettantadue','cinquecentosettantatre','cinquecentosettantaquattro','cinquecentosettantacinque','cinquecentosettantasei','cinquecentosettantasette','cinquecentosettantotto','cinquecentosettantanove','cinquecentottanta',
                'cinquecentottantuno','cinquecentottantadue','cinquecentottantatre','cinquecentottantaquattro','cinquecentottantacinque','cinquecentottantasei','cinquecentottantasette','cinquecentottantotto','cinquecentottantanove','cinquecentonovanta',
                'cinquecentonovantuno','cinquecentonovantadue','cinquecentonovantatre','cinquecentonovantaquattro','cinquecentonovantacinque','cinquecentonovantasei','cinquecentonovantasette','cinquecentonovantotto','cinquecentonovantanove','seicento','seicentouno','seicentodue','seicentotre','seicentoquattro','seicentocinque','seicentosei','seicentosette','seicentootto','seicentonove','seicentodieci',
                'seicentoundici','seicentododici','seicentotredici','seicentoquattordici','seicentoquindici','seicentosedici','seicentodiciassette','seicentodiciotto','seicentodiciannove','seicentoventi',
                'seicentoventuno','seicentoventidue','seicentoventitre','seicentoventiquattro','seicentoventicinque','seicentoventisei','seicentoventisette','seicentoventotto','seicentoventinove','seicentotrenta',
                'seicentotrentuno','seicentotrentadue','seicentotrentatre','seicentotrentaquattro','seicentotrentacinque','seicentotrentasei','seicentotrentasette','seicentotrentotto','seicentotrentanove','seicentoquaranta',
                'seicentoquarantuno','seicentoquarantadue','seicentoquarantatre','seicentoquarantaquattro','seicentoquarantacinque','seicentoquarantasei','seicentoquarantasette','seicentoquarantotto','seicentoquarantanove','seicentocinquanta',
                'seicentocinquantuno','seicentocinquantadue','seicentocinquantatre','seicentocinquantaquattro','seicentocinquantacinque','seicentocinquantasei','seicentocinquantasette','seicentocinquantotto','seicentocinquantanove','seicentosessanta',
                'seicentosessantuno','seicentosessantadue','seicentosessantatre','seicentosessantaquattro','seicentosessantacinque','seicentosessantasei','seicentosessantasette','seicentosessantotto','seicentosessantanove','seicentosettanta',
                'seicentosettantuno','seicentosettantadue','seicentosettantatre','seicentosettantaquattro','seicentosettantacinque','seicentosettantasei','seicentosettantasette','seicentosettantotto','seicentosettantanove','seicentottanta',
                'seicentottantuno','seicentottantadue','seicentottantatre','seicentottantaquattro','seicentottantacinque','seicentottantasei','seicentottantasette','seicentottantotto','seicentottantanove','seicentonovanta',
                'seicentonovantuno','seicentonovantadue','seicentonovantatre','seicentonovantaquattro','seicentonovantacinque','seicentonovantasei','seicentonovantasette','seicentonovantotto','seicentonovantanove','settecento','settecentouno','settecentodue','settecentotre','settecentoquattro','settecentocinque','settecentosei','settecentosette','settecentootto','settecentonove','settecentodieci',
                'settecentoundici','settecentododici','settecentotredici','settecentoquattordici','settecentoquindici','settecentosedici','settecentodiciassette','settecentodiciotto','settecentodiciannove','settecentoventi',
                'settecentoventuno','settecentoventidue','settecentoventitre','settecentoventiquattro','settecentoventicinque','settecentoventisei','settecentoventisette','settecentoventotto','settecentoventinove','settecentotrenta',
                'settecentotrentuno','settecentotrentadue','settecentotrentatre','settecentotrentaquattro','settecentotrentacinque','settecentotrentasei','settecentotrentasette','settecentotrentotto','settecentotrentanove','settecentoquaranta',
                'settecentoquarantuno','settecentoquarantadue','settecentoquarantatre','settecentoquarantaquattro','settecentoquarantacinque','settecentoquarantasei','settecentoquarantasette','settecentoquarantotto','settecentoquarantanove','settecentocinquanta',
                'settecentocinquantuno','settecentocinquantadue','settecentocinquantatre','settecentocinquantaquattro','settecentocinquantacinque','settecentocinquantasei','settecentocinquantasette','settecentocinquantotto','settecentocinquantanove','settecentosessanta',
                'settecentosessantuno','settecentosessantadue','settecentosessantatre','settecentosessantaquattro','settecentosessantacinque','settecentosessantasei','settecentosessantasette','settecentosessantotto','settecentosessantanove','settecentosettanta',
                'settecentosettantuno','settecentosettantadue','settecentosettantatre','settecentosettantaquattro','settecentosettantacinque','settecentosettantasei','settecentosettantasette','settecentosettantotto','settecentosettantanove','settecentottanta',
                'settecentottantuno','settecentottantadue','settecentottantatre','settecentottantaquattro','settecentottantacinque','settecentottantasei','settecentottantasette','settecentottantotto','settecentottantanove','settecentonovanta','settecentonovantuno','settecentonovantadue','settecentonovantatre','settecentonovantaquattro','settecentonovantacinque','settecentonovantasei','settecentonovantasette','settecentonovantotto','settecentonovantanove','ottocento','ottocentouno','ottocentodue','ottocentotre','ottocentoquattro','ottocentocinque','ottocentosei','ottocentosette','ottocentootto','ottocentonove','ottocentodieci',
                'ottocentoundici','ottocentododici','ottocentotredici','ottocentoquattordici','ottocentoquindici','ottocentosedici','ottocentodiciassette','ottocentodiciotto','ottocentodiciannove','ottocentoventi',
                'ottocentoventuno','ottocentoventidue','ottocentoventitre','ottocentoventiquattro','ottocentoventicinque','ottocentoventisei','ottocentoventisette','ottocentoventotto','ottocentoventinove','ottocentotrenta',
                'ottocentotrentuno','ottocentotrentadue','ottocentotrentatre','ottocentotrentaquattro','ottocentotrentacinque','ottocentotrentasei','ottocentotrentasette','ottocentotrentotto','ottocentotrentanove','ottocentoquaranta',
                'ottocentoquarantuno','ottocentoquarantadue','ottocentoquarantatre','ottocentoquarantaquattro','ottocentoquarantacinque','ottocentoquarantasei','ottocentoquarantasette','ottocentoquarantotto','ottocentoquarantanove','ottocentocinquanta',
                'ottocentocinquantuno','ottocentocinquantadue','ottocentocinquantatre','ottocentocinquantaquattro','ottocentocinquantacinque','ottocentocinquantasei','ottocentocinquantasette','ottocentocinquantaotto','ottocentocinquantanove','ottocentosessanta',
                'ottocentosessantuno','ottocentosessantadue','ottocentosessantatre','ottocentosessantaquattro','ottocentosessantacinque','ottocentosessantasei','ottocentosessantasette','ottocentosessantotto','ottocentosessantanove','ottocentosettanta',
                'ottocentosettantuno','ottocentosettantadue','ottocentosettantatre','ottocentosettantaquattro','ottocentosettantacinque','ottocentosettantasei','ottocentosettantasette','ottocentosettantotto','ottocentosettantanove','ottocentottanta',
                'ottocentottantuno','ottocentottantadue','ottocentottantatre','ottocentottantaquattro','ottocentottantacinque','ottocentottantasei','ottocentottantasette','ottocentottantotto','ottocentottantanove','ottocentonovanta',
                'ottocentonovantuno','ottocentonovantadue','ottocentonovantatre','ottocentonovantaquattro','ottocentonovantacinque','ottocentonovantasei','ottocentonovantasette','ottocentonovantotto','ottocentonovantanove','novecento','novecentouno','novecentodue','novecentotre','novecentoquattro','novecentocinque','novecentosei','novecentosette','novecentootto','novecentonove','novecentodieci',
                'novecentoundici','novecentododici','novecentotredici','novecentoquattordici','novecentoquindici','novecentosedici','novecentodiciassette','novecentodiciotto','novecentodiciannove','novecentoventi',
                'novecentoventuno','novecentoventidue','novecentoventitre','novecentoventiquattro','novecentoventicinque','novecentoventisei','novecentoventisette','novecentoventotto','novecentoventinove','novecentotrenta',
                'novecentotrentuno','novecentotrentadue','novecentotrentatre','novecentotrentaquattro','novecentotrentacinque','novecentotrentasei','novecentotrentasette','novecentotrentotto','novecentotrentanove','novecentoquaranta',
                'novecentoquarantuno','novecentoquarantadue','novecentoquarantatre','novecentoquarantaquattro','novecentoquarantacinque','novecentoquarantasei','novecentoquarantasette','novecentoquarantotto','novecentoquarantanove','novecentocinquanta',
                'novecentocinquantuno','novecentocinquantadue','novecentocinquantatre','novecentocinquantaquattro','novecentocinquantacinque','novecentocinquantasei','novecentocinquantasette','novecentocinquantotto','novecentocinquantanove','novecentosessanta',
                'novecentosessantuno','novecentosessantadue','novecentosessantatre','novecentosessantaquattro','novecentosessantacinque','novecentosessantasei','novecentosessantasette','novecentosessantotto','novecentosessantanove','novecentosettanta',
                'novecentosettantuno','novecentosettantadue','novecentosettantatre','novecentosettantaquattro','novecentosettantacinque','novecentosettantasei','novecentosettantasette','novecentosettantotto','novecentosettantanove','novecentottanta',
                'novecentottantuno','novecentottantadue','novecentottantatre','novecentottantaquattro','novecentottantacinque','novecentottantasei','novecentottantasette','novecentottantotto','novecentottantanove','novecentonovanta',
                'novecentonovantuno','novecentonovantadue','novecentonovantatre','novecentonovantaquattro','novecentonovantacinque','novecentonovantasei','novecentonovantasette','novecentonovantotto','novecentonovantanove',)
migliaia=('mille','mila')
milioni=('milione','milioni')
miliardi=('miliardo','miliardi')
def conv(n):
    k=n%1000 
    y=int(n/1000)
    x=int(n/1000000)
    m=int((n%1000000)/1000)#centinaia di migliaia
    c=int((n%1000000000)/1000000)#centinaia di milioni
    t=int(n/1000000000)#centinaia di miliardi
    if n<=999:
        return (ls[n-1])
    if n==1000:
        return (migliaia[0])
    if n>=1000 and n<=1999:
        return (migliaia[0]+ls[k-1])
    if n<=999999:        
        if k==0:
            return(ls[y-1]+migliaia[1])
        return(ls[y-1]+migliaia[1]+ls[k-1])
    if n==1000000:
        return('un'+milioni[0])
    if n>1000000 and n<=1000999:
        return('un'+milioni[0]+ls[k-1])
    if n>=1001000 and n<=1999999:
        if k==0:
            if m==1:
                return('un'+milioni[0]+migliaia[0])
            return('un'+milioni[0]+ls[m-1]+migliaia[1])
        if k!=0 and m==1:
            return('un'+milioni[0]+migliaia[0]+ls[k-1])
        return('un'+milioni[0]+ls[m-1]+migliaia[1]+ls[k-1])
    if n<=999999999:
        if k==0 and m==0 :
            return(ls[x-1]+milioni[1])
        if k==0 and m==1:
            return(ls[x-1]+milioni[1]+migliaia[0])           
        if k!=0 and m>1 and m<=999:
            return(ls[x-1]+milioni[1]+ls[m-1]+migliaia[1]+ls[k-1])
        if k!=0 and m==1:
                return(ls[x-1]+milioni[1]+migliaia[0]+ls[k-1])
    if n>=100000000 and n<=1999999999:
        if c==0 and m==0 and k==0:
            return('un'+miliardi[0])
        if m==0 and k==0:
            if c==1:
                return('un'+miliardi[0]+'un'+milioni[0])
            return('un'+miliardi[0]+ls[c-1]+milioni[1])
        if k==0:
            if m==1:
                return('un'+miliardi[0]+ls[c-1]+milioni[1]+migliaia[0])
                if c==1:
                    return('un'+miliardi[0]+'un'+milioni[0]+migliaia[0])
            if c==1:
                return('un'+miliardi[0]+'un'+milioni[0])            
            return('un'+miliardi[0]+ls[c-1]+milioni[1]+ls[m-1]+migliaia[1])
        if c!=0 and m!=0 and k!=0:
            if c==1:
                if m==1:
                    return('un'+miliardi[0]+'un'+milioni[0]+migliaia[0])
                if m==1 and k<=999:
                    return('un'+miliardi[0]+'un'+milioni[0]+migliaia[0]+ls[k-1])
                return('un'+miliardi[0]+'un'+milioni[0]+ls[m-1]+migliaia[1]+ls[k-1])
            if m==1:
                return('un'+miliardi[0]+ls[c-1]+milioni[1]+migliaia[0])
            if m==1 and k<=999:
                return('un'+miliardi[0]+ls[c-1]+milioni[1]+migliaia[0]+ls[k-1])
            return('un'+miliardi[0]+ls[c-1]+milioni[1]+ls[m-1]+migliaia[1]+ls[k-1])
        if c==0 and m!=0 and k==0:
            if m==1:
                return('un'+miliardi[0]+migliaia[0])
            return('un'+miliardi[0]+ls[m-1]+migliaia[1])
        if c==0 and m==0 and k!=0:
            return('un'+miliardi[0]+ls[k-1])
        if c==0 and m!=0 and k!=0:
            if m==1:
                return('un'+miliardi[0]+migliaia[0])
            if m==1 and k<=999:
               return('un'+miliardi[0]+migliaia[0]+ls[k-1])
            return('un'+miliardi[0]+ls[m-1]+migliaia[1]+ls[k-1])
        if c!=0 and m==0 and k!=0:
            if c==1:
                return('un'+miliardi[0]+'un'+milioni[0]+ls[k-1])
            return('un'+miliardi[0]+ls[c-1]+milioni[1]+ls[k-1]) 
            
    
    if n<=999999999999:
        if c==0 and m==0 and k==0:
            return(ls[t-1]+miliardi[1])
        if m==0 and k==0:
            if c==1:
                return(ls[t-1]+miliardi[1]+'un'+milioni[0])
            return(ls[t-1]+miliardi[1]+ls[c-1]+milioni[1])
        if k==0:
            if m==1:
                return(ls[t-1]+miliardi[1]+ls[c-1]+milioni[1]+migliaia[0])
                if c==1:
                    return(ls[t-1]+miliardi[1]+'un'+milioni[0]+migliaia[0])
            if c==1:
                return(ls[t-1]+miliardi[1]+'un'+milioni[0])            
            return(ls[t-1]+miliardi[1]+ls[c-1]+milioni[1]+ls[m-1]+migliaia[1])
        if c!=0 and m!=0 and k!=0:
            if c==1:
                if m==1:
                    return(ls[t-1]+miliardi[1]+'un'+milioni[0]+migliaia[0])
                if m==1 and k<=999:
                    return(ls[t-1]+miliardi[1]+'un'+milioni[0]+migliaia[0]+ls[k-1])
                return(ls[t-1]+miliardi[1]+'un'+milioni[0]+ls[m-1]+migliaia[1]+ls[k-1])
            if m==1:
                return(ls[t-1]+miliardi[1]+ls[c-1]+milioni[1]+migliaia[0])
            if m==1 and k<=999:
                return(ls[t-1]+miliardi[1]+ls[c-1]+milioni[1]+migliaia[0]+ls[k-1])
            return(ls[t-1]+miliardi[1]+ls[c-1]+milioni[1]+ls[m-1]+migliaia[1]+ls[k-1])
        if c==0 and m!=0 and k==0:
            if m==1:
                return(ls[t-1]+miliardi[1]+migliaia[0])
            return(ls[t-1]+miliardi[1]+ls[m-1]+migliaia[1])
        if c==0 and m==0 and k!=0:
            return(ls[t-1]+miliardi[1]+ls[k-1])
        if c==0 and m!=0 and k!=0:
            if m==1:
                return(ls[t-1]+miliardi[1]+migliaia[0])
            if m==1 and k<=999:
                return(ls[t-1]+miliardi[1]+migliaia[0]+ls[k-1])
            return(ls[t-1]+miliardi[1]+ls[m-1]+migliaia[1]+ls[k-1])
        if c!=0 and m==0 and k!=0:
            if c==1:
                return(ls[t-1]+miliardi[1]+'un'+milioni[0]+ls[k-1])
            return(ls[t-1]+miliardi[1]+ls[c-1]+milioni[1]+ls[k-1])
            

