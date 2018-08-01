chiave="sim sala Bim!"
testo='il mare sa di sale'

def minuscole(chiave):
    chiave=list(chiave) #converto la stringa in lista
    for c in chiave[:]: #lavoro sulla copia della lista appena creata
        if not 'a'<=c<='z':
            chiave.remove(c) #se fosse stata una stringa avrei messo chiave.replace(c,'')
    return ''.join(chiave) #cosi scrive tutto attaccato

def occorrenze(chiave):
    chiave_finale=''.join((minuscole(chiave)))
    for c in chiave_finale:
        if chiave_finale.count(c)>1:
           chiave_finale=chiave_finale.replace(c,'',chiave_finale.count(c)-1) #con -1 obbligo il programma a fermarsi
    return chiave_finale

def codifica(chiave,testo):
    chiave_disordinata=occorrenze(chiave)
    chiave_ordinata=sorted(chiave_disordinata) #sorted ritorna sempre una lista
    l_testo=[]
    for t in testo:
        controllo=True
        for i,c in enumerate(chiave_ordinata): #for i in range(len(chiave_disordinata)): #ottengo indice indice=chiave[i]
            if c==t:
                controllo=False
                l_testo.append(chiave_disordinata[i])
        if controllo:
            l_testo.append(t)
    return ''.join(l_testo)

testo2=codifica(chiave,testo)
        
def decodifica(chiave,testo):
    chiave_disordinata=occorrenze(chiave)
    chiave_ordinata=sorted(chiave_disordinata)
    l_testo=[]
    for t in testo:
        controllo=True
        for i,c in enumerate(chiave_disordinata):
            if c==t:
                controllo=False
                l_testo.append(chiave_ordinata[i])
        if controllo:
            l_testo.append(t)
    return ''.join(l_testo)
