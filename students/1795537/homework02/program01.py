def preleva_n(stringa,n):
    '''controllo le singole righe. Se trovo POST, allora prelevo il numero del post'''
    if '<POST>' in stringa :
            n = [num for num in stringa if num not in '<POST> \n']
            n = ''.join(n)
    return(n)
    
def scomponiInsieme(insieme):
    '''creo una lista con i vari elementi dell'insieme'''
    ins = []
    for el in insieme:
        ins += [el.lower()]
    return (ins)

def sistemaRiga(riga):
    '''ogni volta che nella riga trovo un carattere speciale lo sostituisco con uno space'''
    line = ''
    for car in riga:
        if car in ',.;:!"?{}[]-_':
            car = ' '
        line += car
    line = line.split()
    return (line)

def controlloPost(file, insieme):
    '''controllo se dentro ogni singola riga è presente la stringa cercata'''
    posts = []
    n_post=0
    insieme = scomponiInsieme(insieme)
    for riga in file.readlines():
        n_post = preleva_n(riga,n_post)
        riga = riga.lower()
        riga = sistemaRiga(riga)
        for el in riga:
            if   el in insieme:
                posts += [n_post]
    return(posts)

def post(fposts,insieme):
    with open(fposts, encoding = 'utf-8') as file:
        post = controlloPost(file, insieme)
    return (set(post))
