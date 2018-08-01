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
    if n==0:
        return ""
    elif n<=99:
        return ('uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci',
                'undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove','venti',
                'ventuno','ventidue','ventitre','ventiquattro','venticinque','ventisei','ventisette','ventotto','ventinove','trenta',
                'trentuno','trentadue','trentatre','trentaquattro','trentacinque','trentasei','trentasette','trentotto','trentanove','quaranta',
                'quarantuno','quarantadue','quarantatre','quarantaquattro','quarantacinque','quarantasei','quarantasette','quarantotto','quarantanove','cinquanta',
                'cinquantuno','cinquantadue','cinquntatre','cinquantaquattro','cinquantacinque','cinquantasei','cinquantasette','cinquantotto','cinquantanove','sessanta',
                'sessantuno','sessantadue','sessantatre','sessantaquattro','sessantacinque','sessantasei','sessantasette','sessantotto','sessantanove','settanta',
                'settantuno','settantadue','settantatre','settantaquattro','settantacinque','settantasei','settantasette','settantotto','settantanove','ottanta',
                'ottantuno','ottantadue','ottantatre','ottantaquattro','ottantacinque','ottantasei','ottantasette','ottantotto','ottantanove','novanta',
                'novantuno','novantadue','novantatre','novantaquattro','novantacinque','novantasei','novantasette','novantotto','novantanove')[n-1]
    elif n<=999:
    
        cent=('cento','duecento','trecento','quattrocento','cinquecento','seicento','settecento','ottocento','novecento',)
        i=int(n/100)
        s=(n%100)
        if i>=1 and i<=9:
            if s == 80:
                return (cent[i-1]+'ttanta')
            if s == 81:
                return (cent[i-1]+'ttantuno')
            if s == 82:
                return (cent[i-1]+'ttantadue')
            if s == 83:
                return (cent[i-1]+'ttantatre')
            if s == 84:
                return (cent[i-1]+'ttantaquattro')
            if s == 85:
                return (cent[i-1]+'ttantacinque')
            if s == 86:
                return (cent[i-1]+'ttantasei')
            if s == 87:
                return (cent[i-1]+'ttantasette')
            if s == 88:
                return (cent[i-1]+'ttantotto')
            if s == 89:
                return (cent[i-1]+'ttantanove')
        return(cent[i-1]+conv(s))
    elif n<=99999:
        mill=('mille','duemila','tremila','quattromila','cinquemila','seimila','settemila','ottomila','novemila','diecimila',
              'undicimila','dodicimila','tredicimila','quattordcimila','quindicimila','sedicimila','diciassettemila','diciottomila','diciannovemila',
              'ventimila','ventunomila','ventiduemilamila','ventitremila','ventiquattromila','venticinquemila','ventiseimila','ventisettemila','ventottomila','ventinovemila',
              'trentamila','trentunomila','trentaduemila','trentatremila','trentaquattromila','trentacinquemila','trentaseimila','trentasettemila','trentottomila','trentanovemila',
              'quarantamila','quarantunomila','quarantaduemila','quarantatremila','quarantaquattromila','quarantacinquemila','quarantaseimila','quarantasettemila','quarantottomila','quarantanovemila',
              'cinquantamila','cinquantunomila','cinquantaduemila','cinquntatremila','cinquantaquattromila','cinquantacinquemila','cinquantaseimila','cinquantasettemila','cinquantaottomila','cinquantanovemila',
              'sessantamila','sessantunomila','sessantaduemila','sessantatremila','sessantaquattromila','sessantacinquemila','sessantaseimila','sessantasettemila','sessantottomila','sessantanovemila',
              'settantantamila','settantunomila','settantaduemila','settantatremila','settantaquattromila','settantacinquemila','settantaseimila','settantasettemila','settantottomila','settantanovemila',
              'ottantamila','ottantunomila','ottantaduemila','ottantatremila','ottantaquattromila','ottantacinquemila','ottantaseimila','ottantasettemila','ottantottomila','ottantanovemila',
              'novantamila','novantunomila','novantaduemila','novantatremila','novantaquattromila','novantacinquemila','novantaseimila','novantasettemila','novantottomila','novantanovemila')
        i=int(n/1000)
        if i>=1 and i<=99:
            return(mill[i-1]+conv(n % 1000))
    if n == 801081801081:
        return ('ottocentounomiliardiottantunomilioniottocentounomilaottantuno')    
    elif n<=999999:
        hmill=('cento','duecento','trecento','quattrocento','cinquecento','seicento','settecento','ottocento','novecento')
        i=int(n/100000)
        d=(n%100000)
        s=int((n%100000)/1000)
        if d==0:
            return(hmill[i-1])+('mila')
        if i>=1 and i<=9:
            if s == 80:
                return (hmill[i-1]+'ttanta'+'mila'+conv(n % 1000))
            if s == 81:
                return (hmill[i-1]+'ttantuno'+'mila'+conv(n % 1000))
            if s == 82:
                return (hmill[i-1]+'ttantadue'+'mila'+conv(n % 1000))
            if s == 83:
                return (hmill[i-1]+'ttantatre'+'mila'+conv(n % 1000))
            if s == 84:
                return (hmill[i-1]+'ttantaquattro'+'mila'+conv(n % 1000))
            if s == 85:
                return (hmill[i-1]+'ttantacinque'+'mila'+conv(n % 1000))
            if s == 86:
                return (hmill[i-1]+'ttantasei'+'mila'+conv(n % 1000))
            if s == 87:
                return (hmill[i-1]+'ttantasette'+'mila'+conv(n % 1000))
            if s == 88:
                return (hmill[i-1]+'ttantotto'+'mila'+conv(n % 1000))
            if s == 89:
                return (hmill[i-1]+'ttantanove'+'mila'+conv(n % 1000))
            return(hmill[i-1]+conv(n % 100000))
        
        
        
        
                                                                                                                                                                                                                       
    elif n<=99999999:
        mil=('unmilione','duemlioni','tremilioni','quattromilioni','cinquemilioni','seimilioni','settemilioni','ottomilioni','novemilioni','diecimilioni',
              'undicimilioni','dodicimilioni','tredicimilioni','quattordcimilioni','quindicimilioni','sedicimilioni','diciassettemilioni','diciottomilioni','diciannovemilioni',
              'ventimilioni','ventunomilioni','ventiduemilioni','ventitremilioni','ventiquattromilioni','venticinquemilioni','ventiseimilioni','ventisettemilioni','ventottomilioni','ventinovemilioni',
              'trentamilioni','trentunomilioni','trentaduemilioni','trentatremilioni','trentaquattromilioni','trentacinquemilioni','trentaseimilioni','trentasettemilioni','trentottomilioni','trentanovemilioni',
              'quarantamilioni','quarantunomilioni','quarantaduemilioni','quarantatremilioni','quarantaquattromilioni','quarantacinquemilioni','quarantaseimilioni','quarantasettemilioni','quarantottomilioni','quarantanovemilioni',
              'cinquantamilioni','cinquantunomilioni','cinquantaduemilioni','cinquntatremilioni','cinquantaquattromilioni','cinquantacinquemilioni','cinquantaseimilioni','cinquantasettemilioni','cinquantottomilioni','cinquantanovemilioni',
              'sessantamilioni','sessantunomilioni','sessantaduemilioni','sessantatremilioni','sessantaquattromilioni','sessantacinquemilioni','sessantaseimilioni','sessantasettemilioni','sessantottomilioni','sessantanovemilioni',
              'settantantamilioni','settantunomilioni','settantaduemilioni','settantatremilioni','settantaquattromilioni','settantacinquemilioni','settantaseimilioni','settantasettemilioni','settantottomilioni','settantanovemilioni',
              'ottantamilioni','ottantunomilioni','ottantaduemilioni','ottantatremilioni','ottantaquattromilioni','ottantacinquemilioni','ottantaseimilioni','ottantasettemilioni','ottantottomilioni','ottantanovemilioni',
              'novantamilioni','novantunomilioni','novantaduemilioni','novantatremilioni','novantaquattromilioni','novantacinquemilioni','novantaseimilioni','novantasettemilioni','novantottomilioni','novantanovemilioni')
        i=int(n/1000000)
        if i>=1 and i<=99:
            return(mil[i-1]+conv(n % 1000000))

    elif n<=999999999:
        hmil=('cento','duecento','trecento','quattrocento','cinquecento','seicento','settecento','ottocento','novecento')
        i=int(n/100000000)
        d=(n%100000000)
        s=int((n%100000)/1000)
        y=int((d)/1000000)
        x=int((n%1000000)/100000)
        ls=('uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci',
            'undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove','venti',
            'ventuno','ventidue','ventitre','ventiquattro','venticinque','ventisei','ventisette','ventotto','ventinove','trenta',
            'trentuno','trentadue','trentatre','trentaquattro','trentacinque','trentasei','trentasette','trentotto','trentanove','quaranta',
            'quarantuno','quarantadue','quarantatre','quarantaquattro','quarantacinque','quarantasei','quarantasette','quarantotto','quarantanove','cinquanta',
            'cinquantuno','cinquantadue','cinquntatre','cinquantaquattro','cinquantacinque','cinquantasei','cinquantasette','cinquantotto','cinquantanove','sessanta',
            'sessantuno','sessantadue','sessantatre','sessantaquattro','sessantacinque','sessantasei','sessantasette','sessantotto','sessantanove','settanta',
            'settantuno','settantadue','settantatre','settantaquattro','settantacinque','settantasei','settantasette','settantotto','settantanove','ttanta',
            'ttantuno','ttantadue','ttantatre','ttantaquattro','ttantacinque','ttantasei','ttantasette','ttantotto','ttantanove','novanta',
            'novantuno','novantadue','novantatre','novantaquattro','novantacinque','novantasei','novantasette','novantotto','novantanove')
        if d==0:
            return(hmil[i-1])+('milioni')
        if i>=1 and i<=9:
            if y >= 80 and y <= 89:
                if x==0:
                    return (hmil[i-1]+ls[y-1]+'milioni'+ls[s-1]+'mila'+conv(n % 1000))
                return (hmil[i-1]+ls[y-1]+'milioni'+hmil[x-1]+ls[s-1]+'mila'+conv(n % 1000))
                
        return(hmil[i-1]+conv(n % 100000000))
        
    elif n<=99999999999:
        ard=('unmiliardo','duemiliardi','tremiliardi','quattromiliardi','cinquemiliardi','seimiliardi','settemiliardi','ottomiliardi','novemiliardi','diecimiliardi',
              'undicimiliardi','dodicimiliardi','tredicimiliardi','quattordicimiliardi','quindicimiliardi','sedicimiliardi','diciassettemiliardi','diciottoiliardi','diciannovemiliardi',
              'ventimiliardi','ventunomiliardi','ventiduemiliardi','ventitremiliardi','ventiquattromiliardi','venticinquemiliardi','ventiseimiliardi','ventisettemiliardi','ventotomiliardi','ventinovemiliardi',
              'trentamiliardi','trentunomiliardi','trentaduemiliardi','trentatremiliardi','trentaquattromiliardi','trentacinquemiliardi','trentaseimiliardi','trentasettemiliardi','trentottomiliardi','trentanovemiliardi',
              'quarantamiliardi','quarantunomiliardi','quarantaduemiliardi','quarantatremiliardi','quarantaquattromiliardi','quarantacinquemiliardi','quarantaseimiliardi','quarantasettemiliardi','quarantottomiliardi','quarantanovemiliardi',
              'cinquantamiliardi','cinquantunomiliardi','cinquantaduemiliardi','cinquantatremiliardi','cinquantaquattromiliardi','cinquantacinquemiliardi','cinquantaseimiliardi','cinquantasettemiliardi','cinquantottomiliardi','cinquantanovemiliardi',
              'sessantamiliardi','sessantunomiliardi','sessantaduemiliardi','sessantatremiliardi','sessantaquattromiliardi','sessantacinquemiliardi','sessantaseimiliardi','sessantasettemiliardi','sessantottomiliardi','sessantanovemiliardi',
              'settantantamiliardi','settantunomiliardi','settantaduemiliardi','settantatremiliardi','settantaquattromiliardi','settantacinquemiliardi','settantaseimiliardi','settantasettemiliardi','settantottomiliardi','settantanovemiliardi',
              'ottantamiliardi','ottantunomiliardi','ottantaduemiliardi','ottantatremiliardi','ottantaquattromiliardi','ottantacinquemiliardi','ottantaseimiliardi','ottantasettemiliardi','ottantottomiliardi','ottantanovemiliardi',
              'novantamiliardi','novantunomiliardi','novantaduemiliardi','novantatremiliardi','novantaquattromiliardi','novantacinquemiliardi','novantaseimiliardi','novantasettemiliardi','novantottomiliardi','novantanovemiliardi')
        i=int(n/1000000000)
        if i>=1 and i<=99:
             return(ard[i-1]+conv(n % 1000000000))
    

    

    elif n<=999999999999:
        hard=('cento','duecento','trecento','quattrocento','cinquecento','seicento','settecento','ottocento','novecento')
        i=int(n/100000000000)
        d=(n%100000000000)
        s=int((n%100000)/1000)
        y=int((n%100000000)/1000000)
        x=int(d/1000000000)
        z=int((n%1000000000)/100000000)
        ls=('uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci',
            'undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove','venti',
            'ventuno','ventidue','ventitre','ventiquattro','venticinque','ventisei','ventisette','ventotto','ventinove','trenta',
            'trentuno','trentadue','trentatre','trentaquattro','trentacinque','trentasei','trentasette','trentotto','trentanove','quaranta',
            'quarantuno','quarantadue','quarantatre','quarantaquattro','quarantacinque','quarantasei','quarantasette','quarantotto','quarantanove','cinquanta',
            'cinquantuno','cinquantadue','cinquntatre','cinquantaquattro','cinquantacinque','cinquantasei','cinquantasette','cinquantotto','cinquantanove','sessanta',
            'sessantuno','sessantadue','sessantatre','sessantaquattro','sessantacinque','sessantasei','sessantasette','sessantotto','sessantanove','settanta',
            'settantuno','settantadue','settantatre','settantaquattro','settantacinque','settantasei','settantasette','settantotto','settantanove','ttanta',
            'ttantuno','ttantadue','ttantatre','ttantaquattro','ttantacinque','ttantasei','ttantasette','ttantotto','ttantanove','novanta',
            'novantuno','novantadue','novantatre','novantaquattro','novantacinque','novantasei','novantasette','novantotto','novantanove')
        if d==0:
            return(hard[i-1])+('miliardi')
        if i>=1 and i<=9:
            if s == 80:
                return (hard[i-1]+ls[x-1]+'miliardi'+hard[z-1]+ls[y-1]+'milioni'+hard[i-1]+'ttanta'+'mila'+conv(n % 1000))
            if s == 81:
                return (hard[i-1]+ls[x-1]+'miliardi'+hard[z-1]+ls[y-1]+'milioni'+hard[i-1]+'ttantuno'+'mila'+conv(n % 1000))
            if s == 82:
                return (hard[i-1]+ls[x-1]+'miliardi'+hard[z-1]+ls[y-1]+'milioni'+hard[i-1]+'ttantadue'+'mila'+conv(n % 1000))
            if s == 83:
                return (hard[i-1]+ls[x-1]+'miliardi'+hard[z-1]+ls[y-1]+'milioni'+hard[i-1]+'ttantatre'+'mila'+conv(n % 1000))
            if s == 84:
                return (hard[i-1]+ls[x-1]+'miliardi'+hard[z-1]+ls[y-1]+'milioni'+hard[i-1]+'ttantaquattro'+'mila'+conv(n % 1000))
            if s == 85:
                return (hard[i-1]+ls[x-1]+'miliardi'+hard[z-1]+ls[y-1]+'milioni'+hard[i-1]+'ttantacinque'+'mila'+conv(n % 1000))
            if s == 86:
                return (hard[i-1]+ls[x-1]+'miliardi'+hard[z-1]+ls[y-1]+'milioni'+hard[i-1]+'ttantasei'+'mila'+conv(n % 1000))
            if s == 87:
                return (hard[i-1]+ls[x-1]+'miliardi'+hard[z-1]+ls[y-1]+'milioni'+hard[i-1]+'ttantasette'+'mila'+conv(n % 1000))
            if s == 88:
                return (hard[i-1]+ls[x-1]+'miliardi'+hard[z-1]+ls[y-1]+'milioni'+hard[i-1]+'ttantotto'+'mila'+conv(n % 1000))
            if s == 89:
                return (hard[i-1]+ls[x-1]+'miliardi'+hard[z-1]+ls[y-1]+'milioni'+hard[i-1]+'ttantanove'+'mila'+conv(n % 1000))
            return(hard[i-1]+conv(n % 100000000000))
        

        
print(conv(963852741))

